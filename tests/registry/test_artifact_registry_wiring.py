"""
ArtifactRegistry wiring into provenance (Article II) and context envelope
(Article XV.A). See artifact_registry.py class docstring for why
provenance registration is conditional on an explicit status and context
envelope registration is not.
"""

from innovation_os.registry.artifact_registry import Artifact, ArtifactRegistry
from innovation_os.provenance import ProvenanceEngine, ProvenanceStatus
from innovation_os.context_envelope import ContextEnvelopeStore


def test_registry_with_no_engines_attached_is_unaffected():
    """Existing callers, ArtifactRegistry() with no arguments, must be unaffected."""

    registry = ArtifactRegistry()

    artifact = registry.register(
        Artifact("ART-100", "CODE", "a.py", "src", "PROJECT-X")
    )

    assert artifact.artifact_id == "ART-100"


def test_context_envelope_created_unconditionally_when_attached():

    envelope_store = ContextEnvelopeStore()
    registry = ArtifactRegistry(context_envelope_store=envelope_store)

    registry.register(
        Artifact("ART-101", "CODE", "a.py", "src", "PROJECT-X")
    )

    # Does not raise -- the envelope exists.
    envelope_store.get("ART-101")


def test_provenance_not_registered_without_explicit_status():
    """
    No provenance_status kwarg means no provenance record -- an honest
    absence, not a guessed one.
    """

    engine = ProvenanceEngine()
    registry = ArtifactRegistry(provenance_engine=engine)

    registry.register(
        Artifact("ART-102", "CODE", "a.py", "src", "PROJECT-X")
    )

    assert engine.get("ART-102") is None


def test_provenance_registered_when_status_provided():

    engine = ProvenanceEngine()
    registry = ArtifactRegistry(provenance_engine=engine)

    registry.register(
        Artifact("ART-103", "CODE", "a.py", "src", "PROJECT-X"),
        provenance_status=ProvenanceStatus.USER_ESTABLISHED,
    )

    record = engine.get("ART-103")

    assert record is not None
    assert record.status is ProvenanceStatus.USER_ESTABLISHED
    assert record.source == "src"


def test_legacy_three_arg_registration_still_works_with_engines_attached():
    """
    The legacy (filename, path, language) call path carries no status
    information at all -- it must not silently invent one.
    """

    engine = ProvenanceEngine()
    envelope_store = ContextEnvelopeStore()
    registry = ArtifactRegistry(
        provenance_engine=engine,
        context_envelope_store=envelope_store,
    )

    artifact = registry.register("gateway.py", "/src/gateway.py", "python")

    assert artifact.artifact_id == "CODE-00001"
    assert engine.get(artifact.artifact_id) is None
    envelope_store.get(artifact.artifact_id)  # does not raise
