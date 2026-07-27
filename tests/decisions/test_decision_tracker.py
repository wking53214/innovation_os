from src.innovation_os.decisions.decision_tracker import (
    DecisionTracker,
)



def test_decision_tracking():

    tracker = DecisionTracker()


    result = tracker.record(
        "DECISION-001",
        "Adopt governance layer",
        "Need controlled AI execution",
        alternatives=[
            "No governance",
            "Manual review",
        ],
        outcome="Implemented GSA",
    )


    assert (
        result.decision_id
        ==
        "DECISION-001"
    )


    assert (
        result.outcome
        ==
        "Implemented GSA"
    )


    assert len(
        result.alternatives
    ) == 2
