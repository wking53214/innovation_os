from src.innovation_os.decisions.intelligence import (
    DecisionIntelligenceEngine,
)


def test_decision_creation():

    engine = DecisionIntelligenceEngine()

    decision = engine.create(
        "DECISION-001",
        "Need AI governance",
        [
            "No controls",
            "Human approval",
            "Automated policy",
        ],
        "Human approval",
        "Reduce unsafe execution risk",
        "Governance layer created",
    )


    assert decision.selected == "Human approval"
    assert decision.problem == "Need AI governance"


def test_decision_replay():

    engine = DecisionIntelligenceEngine()

    engine.create(
        "DECISION-002",
        "Security concern",
        [
            "Ignore",
            "Validate",
        ],
        "Validate",
        "Improve reliability",
    )


    replay = engine.replay(
        "DECISION-002"
    )


    assert replay["selected"] == "Validate"
    assert replay["reasoning"] == "Improve reliability"
