from innovation_os.intelligence.provenance import (
    IntelligenceLineage,
    EvidenceTracker,
    DecisionTrace,
)
from innovation_os.provenance import ProvenanceStatus


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

    history = lineage.history()
    assert history == [
        {
            "artifact_id": "artifact",
            "source": "runtime",
            "status": ProvenanceStatus.PROVENANCE_UNCERTAIN,
        }
    ]

    assert evidence.all() == ["signal"]
    assert trace.replay() == ["reason"]
