from src.innovation_os.opportunity.engine import (
    OpportunityDetectionEngine,
)


def test_opportunity_detection():

    engine = OpportunityDetectionEngine()

    engine.add(
        "PROJECT-SENTINEL",
        [
            "AI",
            "governance",
            "security",
        ],
    )


    results = engine.discover(
        "PROJECT-NEW",
        [
            "AI",
            "governance",
            "research",
        ],
    )


    assert len(results) == 1
    assert results[0].target_id == "PROJECT-SENTINEL"
    assert "ai" in results[0].shared_terms


def test_no_opportunity():

    engine = OpportunityDetectionEngine()

    engine.add(
        "PROJECT-001",
        [
            "biology",
            "plants",
        ],
    )


    results = engine.discover(
        "PROJECT-002",
        [
            "software",
            "cloud",
        ],
    )


    assert len(results) == 0
