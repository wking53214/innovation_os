from innovation_os.ideation.engine import (
    IdeationEngine,
)


def test_generate_idea():

    engine = IdeationEngine()

    idea = engine.generate_idea(
        idea_id="IDEA-0001",
        problem_id="PROBLEM-0001",
        title="Adaptive hospital workflow",
        description="Use predictive scheduling concepts",
        sources=[
            "Healthcare",
            "Manufacturing",
        ],
        confidence=0.85,
        tags=[
            "efficiency",
            "automation",
        ],
    )

    assert idea.idea_id == "IDEA-0001"
    assert idea.confidence == 0.85


def test_get_idea():

    engine = IdeationEngine()

    engine.generate_idea(
        idea_id="IDEA-0002",
        problem_id="PROBLEM-0002",
        title="Test idea",
        description="Test",
        sources=[],
        confidence=0.5,
    )

    idea = engine.get_idea(
        "IDEA-0002"
    )

    assert idea.idea_id == "IDEA-0002"
    assert idea.problem_id == "PROBLEM-0002"
    assert idea.title == "Test idea"


def test_find_by_problem():

    engine = IdeationEngine()

    engine.generate_idea(
        idea_id="IDEA-0003",
        problem_id="PROBLEM-0003",
        title="Idea A",
        description="A",
        sources=[],
        confidence=0.7,
    )

    results = engine.find_by_problem(
        "PROBLEM-0003"
    )

    assert len(results) == 1
