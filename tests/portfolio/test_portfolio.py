from src.innovation_os.portfolio.engine import (
    InnovationPortfolioEngine,
)


def test_portfolio_add():

    engine = InnovationPortfolioEngine()

    item = engine.add(
        "PROJECT-001",
        "Sentinel OS",
        "AI Governance",
        "HIGH",
        "IMPLEMENTED",
    )


    assert item.name == "Sentinel OS"
    assert item.priority == "HIGH"


def test_active_projects():

    engine = InnovationPortfolioEngine()

    engine.add(
        "PROJECT-001",
        "Active Project",
        "AI",
        "HIGH",
        "IMPLEMENTED",
    )

    engine.add(
        "PROJECT-002",
        "Old Project",
        "Research",
        "LOW",
        "ARCHIVED",
    )


    active = engine.list_active()


    assert len(active) == 1
    assert active[0].artifact_id == "PROJECT-001"


def test_priority_filter():

    engine = InnovationPortfolioEngine()

    engine.add(
        "PROJECT-001",
        "Critical Project",
        "AI",
        "HIGH",
        "IDEA",
    )


    results = engine.by_priority(
        "HIGH"
    )


    assert len(results) == 1
