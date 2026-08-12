"""
Article II guarantees.

Two things must hold:
  1. An artifact cannot be registered under a category outside the ratified six.
  2. A status change is recorded as a transition, not a silent overwrite.
"""

import pytest

from innovation_os.provenance import (
    ProvenanceEngine,
    ProvenanceStatus,
)


def test_taxonomy_is_exactly_the_ratified_six():

    assert {m.name for m in ProvenanceStatus} == {
        "USER_ESTABLISHED",
        "USER_ACCEPTED",
        "ASSISTANT_PROPOSED",
        "UNRESOLVED",
        "REJECTED",
        "PROVENANCE_UNCERTAIN",
    }


def test_cannot_register_with_undefined_category():

    engine = ProvenanceEngine()

    #
    # A freeform locator is exactly what the old `source: str` field accepted.
    # It is not a provenance category and must be refused.
    #
    with pytest.raises(ValueError):
        engine.register(
            "IDEA-002",
            "github://sentinel_os",
        )

    #
    # A plausible-sounding but unratified category is also refused. No
    # inventing categories at the call site.
    #
    with pytest.raises(ValueError):
        engine.register(
            "IDEA-003",
            "USER_INFERRED",
        )

    assert engine.get("IDEA-002") is None

    assert engine.get("IDEA-003") is None


def test_cannot_register_without_a_category():

    engine = ProvenanceEngine()

    #
    # No default. Silence is not a determination.
    #
    with pytest.raises(TypeError):
        engine.register(
            "IDEA-004",
        )


def test_status_accepts_article_ii_labels():

    engine = ProvenanceEngine()

    record = engine.register(
        "IDEA-005",
        "ASSISTANT-PROPOSED",
    )

    assert record.status is ProvenanceStatus.ASSISTANT_PROPOSED


def test_adoption_is_recorded_as_a_transition_not_an_overwrite():

    engine = ProvenanceEngine()

    engine.register(
        "DEC-001",
        ProvenanceStatus.ASSISTANT_PROPOSED,
        source="conversation_014",
    )

    transition = engine.set_status(
        "DEC-001",
        ProvenanceStatus.USER_ACCEPTED,
        reason="Human explicitly adopted in review",
    )

    record = engine.get(
        "DEC-001"
    )

    #
    # Current status advanced.
    #
    assert record.status is ProvenanceStatus.USER_ACCEPTED

    #
    # The prior status survived the change. This is the whole point: the
    # record still shows the machine proposed it first.
    #
    assert len(record.transitions) == 1

    assert transition.from_status is ProvenanceStatus.ASSISTANT_PROPOSED

    assert transition.to_status is ProvenanceStatus.USER_ACCEPTED

    assert transition.reason == "Human explicitly adopted in review"

    assert record.initial_status is ProvenanceStatus.ASSISTANT_PROPOSED


def test_transition_chain_preserves_every_prior_status():

    engine = ProvenanceEngine()

    engine.register(
        "DEC-002",
        ProvenanceStatus.ASSISTANT_PROPOSED,
    )

    engine.set_status(
        "DEC-002",
        ProvenanceStatus.UNRESOLVED,
    )

    engine.set_status(
        "DEC-002",
        ProvenanceStatus.REJECTED,
    )

    record = engine.get(
        "DEC-002"
    )

    chain = [
        t.to_status for t in record.transitions
    ]

    assert chain == [
        ProvenanceStatus.UNRESOLVED,
        ProvenanceStatus.REJECTED,
    ]

    assert record.initial_status is ProvenanceStatus.ASSISTANT_PROPOSED

    assert record.status is ProvenanceStatus.REJECTED


def test_transition_to_undefined_category_is_refused():

    engine = ProvenanceEngine()

    engine.register(
        "DEC-003",
        ProvenanceStatus.UNRESOLVED,
    )

    with pytest.raises(ValueError):
        engine.set_status(
            "DEC-003",
            "PROVENANCE EXTERNAL TO CURRENT RECORD",
        )

    record = engine.get(
        "DEC-003"
    )

    assert record.status is ProvenanceStatus.UNRESOLVED

    assert record.transitions == []
