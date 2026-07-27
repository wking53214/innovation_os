from src.innovation_os.scoring.innovation_score import (
    InnovationScoringEngine,
)



def test_innovation_score():

    engine = InnovationScoringEngine()


    result = engine.calculate(
        "PROJECT-SENTINEL",
        artifacts=15,
        concepts=8,
        decisions=12,
        connections=20,
    )


    assert result.score == 100
    assert result.classification == "HIGH POTENTIAL"
