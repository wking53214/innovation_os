from innovation_os.problem.alignment import (
    ProblemAlignmentEngine,
)


def test_alignment_score():

    engine = ProblemAlignmentEngine()

    result = engine.evaluate(
        idea_id="IDEA-0001",
        problem_id="PROBLEM-0001",
        score=90,
        reasons=[
            "Directly reduces workflow friction",
        ],
    )

    assert result.aligned is True
    assert result.score == 90


def test_alignment_failure():

    engine = ProblemAlignmentEngine()

    result = engine.evaluate(
        idea_id="IDEA-0002",
        problem_id="PROBLEM-0001",
        score=40,
        reasons=[
            "Interesting but unrelated",
        ],
    )

    assert result.aligned is False


def test_alignment_lookup():

    engine = ProblemAlignmentEngine()

    engine.evaluate(
        idea_id="IDEA-0003",
        problem_id="PROBLEM-0002",
        score=80,
        reasons=[],
    )

    result = engine.get_result(
        "IDEA-0003"
    )

    assert result is not None
