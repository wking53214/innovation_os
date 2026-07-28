from innovation_os.intelligence.decision import (
    DecisionContext,
    DecisionAlternative,
    RiskEngine,
    DecisionScorer,
    DecisionReplay,
    DecisionIntelligenceEngine,
)


def test_context():

    context = DecisionContext(
        "choose platform"
    )

    assert context.objective == "choose platform"



def test_risk_engine():

    engine = RiskEngine()

    option = DecisionAlternative(
        "A",
        risk=0.4
    )

    assert engine.score(option) == 0.4



def test_decision_scoring():

    scorer = DecisionScorer()

    option = DecisionAlternative(
        "A",
        expected_value=10,
        risk=2,
    )

    assert scorer.score(option) == 8



def test_decision_engine():

    scorer = DecisionScorer()

    replay = DecisionReplay()

    engine = DecisionIntelligenceEngine(
        scorer,
        replay,
    )

    winner = engine.evaluate(
        [
            DecisionAlternative(
                "low",
                expected_value=5,
                risk=2,
            ),
            DecisionAlternative(
                "high",
                expected_value=10,
                risk=3,
            ),
        ]
    )

    assert winner.name == "high"
    assert replay.count() == 1
