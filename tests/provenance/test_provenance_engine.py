from src.innovation_os.provenance.engine import (
    ProvenanceEngine,
)


def test_provenance_registration():

    engine = ProvenanceEngine()

    record = engine.register(
        "IDEA-001",
        "conversation_001",
        {
            "topic": "AI governance"
        },
    )


    assert record.artifact_id == "IDEA-001"
    assert record.source == "conversation_001"
    assert record.metadata["topic"] == "AI governance"


def test_provenance_history():

    engine = ProvenanceEngine()

    engine.register(
        "PROJECT-001",
        "archive",
    )


    engine.add_history(
        "PROJECT-001",
        "Converted from idea to project",
    )


    record = engine.get(
        "PROJECT-001"
    )


    assert len(record.history) == 1
