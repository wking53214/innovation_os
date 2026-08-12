from innovation_os.relationship_engine.discovery import (
    RelationshipDiscoveryEngine,
)


def test_relationship_discovery():

    engine = RelationshipDiscoveryEngine()

    results = engine.discover(
        source_id="CODE-00001",

        source_terms=[
            "governance",
            "security",
        ],

        targets={
            "IDEA-GSA-001": [
                "governance",
                "security",
                "AI",
            ]
        },
    )


    assert len(results) == 1
    assert results[0].target_id == "IDEA-GSA-001"
    assert results[0].relationship == "POSSIBLY_SUPPORTS"
    assert results[0].confidence > 50


def test_no_relationship():

    engine = RelationshipDiscoveryEngine()

    results = engine.discover(
        source_id="CODE-00002",

        source_terms=[
            "database",
        ],

        targets={
            "IDEA-001": [
                "biology",
            ]
        },
    )

    assert len(results) == 0
