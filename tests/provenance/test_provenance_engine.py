"""
Rewritten from the former tests against provenance/engine.py, which defined
a second ProvenanceEngine under a colliding name. Same intent (metadata on
registration, free-text history events), now against the canonical store.
"""

from innovation_os.provenance import (
    ProvenanceEngine,
    ProvenanceStatus,
)


def test_provenance_registration():

    engine = ProvenanceEngine()

    record = engine.register(
        "IDEA-001",
        ProvenanceStatus.USER_ESTABLISHED,
        source="conversation_001",
        metadata={
            "topic": "AI governance"
        },
    )

    assert record.artifact_id == "IDEA-001"

    #
    # The locator survives the retrofit. It answers "where from", not "who
    # originated", and is no longer carrying an authority claim it could not
    # support.
    #
    assert record.source == "conversation_001"

    assert record.status is ProvenanceStatus.USER_ESTABLISHED

    assert record.metadata["topic"] == "AI governance"


def test_provenance_history():

    engine = ProvenanceEngine()

    engine.register(
        "PROJECT-001",
        ProvenanceStatus.USER_ESTABLISHED,
        source="archive",
    )

    engine.add_history(
        "PROJECT-001",
        "Converted from idea to project",
    )

    record = engine.get(
        "PROJECT-001"
    )

    assert len(record.history) == 1

    #
    # A history event is an audit note, not a provenance determination. It
    # must not move the Article II category.
    #
    assert record.status is ProvenanceStatus.USER_ESTABLISHED

    assert record.transitions == []
