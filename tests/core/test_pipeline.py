from innovation_os.core.pipeline import (
    InnovationPipeline,
)


def test_complete_pipeline():

    pipeline = InnovationPipeline()

    result = pipeline.run(
        problem_id="PROBLEM-0001",
        ideas=[
            "Adaptive scheduling",
        ],
        alignment_score=90,
        review_complete=True,
        nature_patterns=[
            "Adaptive recovery",
        ],
        solution_id="SOLUTION-0001",
        approved=True,
    )

    assert result.aligned is True
    assert result.reviewed is True
    assert result.approved is True


def test_pipeline_lookup():

    pipeline = InnovationPipeline()

    pipeline.run(
        problem_id="PROBLEM-0002",
        ideas=[],
        alignment_score=80,
        review_complete=False,
        nature_patterns=[],
        solution_id="SOLUTION-0002",
        approved=False,
    )

    result = pipeline.get(
        "PROBLEM-0002"
    )

    assert result is not None
