from innovation_os.intelligence.pattern_engine import (
    PatternDetectionEngine,
)



def test_pattern_detection():

    engine = PatternDetectionEngine()


    engine.add(
        "PROJECT-SENTINEL",
        [
            "AI",
            "governance",
            "security",
        ],
    )


    engine.add(
        "PROJECT-GSA",
        [
            "AI",
            "governance",
            "approval",
        ],
    )


    results = engine.detect(
        "PROJECT-SENTINEL"
    )


    assert len(results) == 1
    assert results[0].target_id == "PROJECT-GSA"
    assert "ai" in results[0].shared_terms
