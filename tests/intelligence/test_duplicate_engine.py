from src.innovation_os.intelligence.duplicate_engine import (
    DuplicateConceptEngine,
)



def test_duplicate_detection():

    engine = DuplicateConceptEngine()


    engine.add(
        "PROJECT-A",
        [
            "AI",
            "governance",
            "security",
        ],
    )


    engine.add(
        "PROJECT-B",
        [
            "AI",
            "governance",
            "approval",
        ],
    )


    results = engine.compare(
        threshold=30
    )


    assert len(results) == 1
    assert results[0].source_id == "PROJECT-A"
    assert results[0].match_id == "PROJECT-B"
    assert "ai" in results[0].shared_terms
