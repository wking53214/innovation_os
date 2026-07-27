from src.innovation_os.similarity.engine import (
    SimilarityEngine,
)


def test_similarity_detection():

    engine = SimilarityEngine()

    engine.add(
        "PROJECT-SENTINEL",
        [
            "AI",
            "governance",
            "approval",
        ],
    )


    results = engine.compare(
        "NEW-IDEA",
        [
            "AI",
            "governance",
            "security",
        ],
    )


    assert len(results) == 1
    assert results[0].target_id == "PROJECT-SENTINEL"
    assert "ai" in results[0].shared_terms


def test_no_similarity():

    engine = SimilarityEngine()

    engine.add(
        "PROJECT-001",
        [
            "biology",
            "reef",
        ],
    )


    results = engine.compare(
        "NEW",
        [
            "database",
        ],
    )


    assert len(results) == 0
