from innovation_os.scoring.engine import (
    InnovationScoringEngine,
)


def test_score_calculation():

    engine = InnovationScoringEngine()

    result = engine.calculate(
        "PROJECT-001",
        90,
        90,
        80,
        100,
        20,
    )


    assert result.artifact_id == "PROJECT-001"
    assert result.score == 85.0



def test_ranking():

    engine = InnovationScoringEngine()


    low = engine.calculate(
        "PROJECT-LOW",
        40,
        40,
        40,
        40,
        20,
    )


    high = engine.calculate(
        "PROJECT-HIGH",
        90,
        90,
        90,
        90,
        10,
    )


    ranked = engine.rank(
        [
            low,
            high,
        ]
    )


    assert ranked[0].artifact_id == "PROJECT-HIGH"
