"""
Article XV.A (context envelope) mechanism tests.

Not ratified -- see envelope.py docstring. These tests check the
mechanism works, not that it is constitutional law.
"""

import pytest

from innovation_os.context_envelope import (
    CompressionConstraint,
    ContextEnvelopeStore,
    ContextOrigin,
    CONDITIONS,
    SPEAKER,
)
from innovation_os.provenance import ProvenanceEngine, ProvenanceStatus


def test_register_creates_an_empty_envelope():

    store = ContextEnvelopeStore()

    envelope = store.register("IDEA-1")

    assert envelope.artifact_id == "IDEA-1"
    assert envelope.recoverable == {}
    assert envelope.inferred == {}


def test_register_is_idempotent():

    store = ContextEnvelopeStore()

    first = store.register("IDEA-1")
    second = store.register("IDEA-1")

    assert first is second


def test_get_unknown_artifact_raises():

    store = ContextEnvelopeStore()

    with pytest.raises(ValueError):
        store.get("IDEA-404")


def test_recoverable_context_is_retrievable():

    store = ContextEnvelopeStore()
    store.register("IDEA-1")

    store.set_recoverable("IDEA-1", SPEAKER, "William")

    envelope = store.get("IDEA-1")

    assert envelope.get(SPEAKER) == "William"
    assert envelope.origin_of(SPEAKER) is ContextOrigin.RECORD_RECOVERABLE


def test_inferred_context_is_retrievable_and_marked_as_such():

    store = ContextEnvelopeStore()
    store.register("IDEA-1")

    store.set_inferred("IDEA-1", CONDITIONS, "assumed active during Q3")

    envelope = store.get("IDEA-1")

    assert envelope.get(CONDITIONS) == "assumed active during Q3"
    assert envelope.origin_of(CONDITIONS) is ContextOrigin.ANALYTICALLY_INFERRED


def test_missing_key_has_no_origin():

    store = ContextEnvelopeStore()
    store.register("IDEA-1")

    envelope = store.get("IDEA-1")

    assert envelope.get(SPEAKER) is None
    assert envelope.origin_of(SPEAKER) is None


def test_recoverable_takes_precedence_over_inferred_for_same_key():
    """
    Record-recoverable is always the stronger claim -- if a key
    somehow ends up in both buckets, recoverable wins.
    """

    store = ContextEnvelopeStore()
    store.register("IDEA-1")

    store.set_inferred("IDEA-1", SPEAKER, "guessed speaker")
    store.set_recoverable("IDEA-1", SPEAKER, "William")

    envelope = store.get("IDEA-1")

    assert envelope.get(SPEAKER) == "William"
    assert envelope.origin_of(SPEAKER) is ContextOrigin.RECORD_RECOVERABLE


def test_provenance_of_without_engine_returns_none():

    store = ContextEnvelopeStore()
    store.register("IDEA-1")

    assert store.provenance_of("IDEA-1") is None


def test_lineage_of_without_engine_returns_empty_list():

    store = ContextEnvelopeStore()
    store.register("IDEA-1")

    assert store.lineage_of("IDEA-1") == []


def test_provenance_of_reads_live_from_attached_engine():
    """
    Article XV.A's Provenance field must not be a second copy of Article
    II data -- it reads the ProvenanceEngine directly, so a status change
    made after the envelope is created is still visible.
    """

    engine = ProvenanceEngine()
    engine.register("IDEA-1", ProvenanceStatus.ASSISTANT_PROPOSED)

    store = ContextEnvelopeStore(provenance_engine=engine)
    store.register("IDEA-1")

    assert store.provenance_of("IDEA-1").status is ProvenanceStatus.ASSISTANT_PROPOSED

    engine.set_status("IDEA-1", ProvenanceStatus.USER_ACCEPTED)

    assert store.provenance_of("IDEA-1").status is ProvenanceStatus.USER_ACCEPTED


def test_lineage_of_reads_live_from_attached_engine():

    engine = ProvenanceEngine()
    engine.register("IDEA-2", ProvenanceStatus.ASSISTANT_PROPOSED)

    store = ContextEnvelopeStore(provenance_engine=engine)
    store.register("IDEA-2")

    assert store.lineage_of("IDEA-2") == []

    engine.derive("IDEA-1", "IDEA-2")

    edges = store.lineage_of("IDEA-2")

    assert len(edges) == 1
    assert edges[0].from_artifact_id == "IDEA-1"


def test_compression_constraint_default_is_unescalated():

    original = CompressionConstraint()
    compressed = CompressionConstraint()

    assert compressed.escalates_beyond(original) is False


def test_compression_constraint_detects_escalation_on_any_axis():

    original = CompressionConstraint()

    assert CompressionConstraint(certainty=True).escalates_beyond(original) is True
    assert CompressionConstraint(scope=True).escalates_beyond(original) is True
    assert CompressionConstraint(permanence=True).escalates_beyond(original) is True
    assert CompressionConstraint(significance=True).escalates_beyond(original) is True


def test_compression_constraint_allows_narrowing():
    """
    Going from True -> False on an axis is fine -- the rule only forbids
    the record getting MORE certain/permanent/global/significant than it
    started, not less.
    """

    original = CompressionConstraint(certainty=True, scope=True)
    compressed = CompressionConstraint()

    assert compressed.escalates_beyond(original) is False
