from src.innovation_os.recommendation.engine import (
    RecommendationEngine,
)


def test_recommendation_generation():

    engine = RecommendationEngine()

    engine.add_rule(
        "governance",
        "Create governance audit framework",
    )


    results = engine.recommend(
        "PROJECT-001",
        [
            "AI",
            "governance",
        ],
    )


    assert len(results) == 1
    assert (
        results[0].recommendation
        ==
        "Create governance audit framework"
    )
    assert results[0].confidence == 80.0


def test_no_recommendation():

    engine = RecommendationEngine()

    engine.add_rule(
        "biology",
        "Explore biological models",
    )


    results = engine.recommend(
        "PROJECT-001",
        [
            "software",
        ],
    )


    assert len(results) == 0
