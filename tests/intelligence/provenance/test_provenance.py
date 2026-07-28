from innovation_os.intelligence.provenance import (
    IntelligenceLineage,
    EvidenceTracker,
    DecisionTrace,
)


def test_provenance():

    lineage = IntelligenceLineage()

    lineage.record(
        "artifact",
        "runtime"
    )

    evidence = EvidenceTracker()

    evidence.add(
        "signal"
    )

    trace = DecisionTrace()

    trace.add(
        "reason"
    )

    assert lineage.history()
    assert evidence.all()
    assert trace.replay()
