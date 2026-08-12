from innovation_os.solution.engine import (
    SolutionEngine,
)


def test_create_solution():

    engine = SolutionEngine()

    solution = engine.create_solution(
        solution_id="SOLUTION-0001",
        problem_id="PROBLEM-0001",
        idea_id="IDEA-0001",
        title="Adaptive workflow platform",
        description="Improves operational efficiency",
        supporting_artifacts=[
            "CODE-0001",
        ],
        risks=[
            "Adoption risk",
        ],
    )

    assert solution.solution_id == "SOLUTION-0001"
    assert solution.status == "PROPOSED"


def test_get_solution():

    engine = SolutionEngine()

    engine.create_solution(
        solution_id="SOLUTION-0002",
        problem_id="PROBLEM-0002",
        idea_id="IDEA-0002",
        title="Test solution",
        description="Test",
        supporting_artifacts=[],
        risks=[],
    )

    solution = engine.get_solution(
        "SOLUTION-0002"
    )

    assert solution.solution_id == "SOLUTION-0002"
    assert solution.problem_id == "PROBLEM-0002"
    assert solution.title == "Test solution"


def test_update_solution_status():

    engine = SolutionEngine()

    engine.create_solution(
        solution_id="SOLUTION-0003",
        problem_id="PROBLEM-0003",
        idea_id="IDEA-0003",
        title="Pilot",
        description="Pilot solution",
        supporting_artifacts=[],
        risks=[],
    )

    solution = engine.update_status(
        "SOLUTION-0003",
        "TESTING",
    )

    assert solution.status == "TESTING"
