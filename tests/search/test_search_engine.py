from innovation_os.search.engine import (
    SearchEngine,
)


def test_search_finds_matching_nodes():

    engine = SearchEngine()

    engine.index(
        "IDEA-001",
        "IDEA",
        "Governance AI Platform",
    )

    engine.index(
        "CODE-001",
        "CODE",
        "Database Engine",
    )

    results = engine.search(
        "Governance"
    )

    assert len(results) == 1
    assert results[0].node_id == "IDEA-001"


def test_search_no_match():

    engine = SearchEngine()

    engine.index(
        "IDEA-002",
        "IDEA",
        "Biological Optimization",
    )

    results = engine.search(
        "Satellite"
    )

    assert len(results) == 0
