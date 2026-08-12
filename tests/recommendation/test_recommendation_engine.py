from innovation_os.recommendation.recommendation_engine import (
    RecommendationEngine,
)



def test_high_value_recommendation():

    engine = RecommendationEngine()


    result = engine.recommend(
        "PROJECT-SENTINEL",
        score=95,
        relationships=5,
        duplicates=0,
    )


    assert result.action == "Continue Development"
    assert result.priority == "HIGH"



def test_duplicate_recommendation():

    engine = RecommendationEngine()


    result = engine.recommend(
        "PROJECT-OLD",
        score=90,
        relationships=2,
        duplicates=1,
    )


    assert result.action == "Review Existing Work"
