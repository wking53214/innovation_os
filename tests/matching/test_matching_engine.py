from src.innovation_os.matching.engine import (
    IdeaMatchingEngine,
)


def test_matching_engine():

    engine = IdeaMatchingEngine()

    results = engine.match(
        artifact_id="SCAN-0001",

        detected_terms=[
            "governance",
            "pipeline",
        ],

        ideas={
            "IDEA-GSA-001": [
                "governance",
                "pipeline",
                "security",
            ]
        },
    )

    assert len(results) == 1
    assert results[0].idea_id == "IDEA-GSA-001"
    assert results[0].confidence > 50


def test_no_match():

    engine = IdeaMatchingEngine()

    results = engine.match(
        artifact_id="SCAN-0002",

        detected_terms=[
            "database",
        ],

        ideas={
            "IDEA-001": [
                "biology",
                "nature",
            ]
        },
    )

    assert len(results) == 0
