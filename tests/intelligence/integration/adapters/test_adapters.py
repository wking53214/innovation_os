from innovation_os.intelligence.integration.adapters import (
    IntelligenceMemoryAdapter,
    KnowledgeAdapter,
    DecisionAdapter,
    ProvenanceAdapter,
    AuditAdapter,
)


def test_adapters():

    assert IntelligenceMemoryAdapter().store(
        "data"
    ) == "data"

    assert KnowledgeAdapter().add_relationship(
        "A",
        "B"
    ) == ("A", "B")

    assert DecisionAdapter().evaluate(
        "decision"
    ) == "decision"

    assert ProvenanceAdapter().record(
        "event"
    ) == "event"

    assert AuditAdapter().log(
        "event"
    ) == "event"
