from src.innovation_os.core.pipeline import (
    InnovationPipeline,
)


def run_demo():

    pipeline = InnovationPipeline()

    result = pipeline.run(
        problem_id="PROBLEM-CORAL-0001",

        ideas=[
            "Adaptive reef restoration zones",
            "Distributed monitoring networks",
            "Resilience-based ecosystem management",
        ],

        alignment_score=88,

        review_complete=True,

        nature_patterns=[
            "Coral stress adaptation",
            "Distributed ecosystem recovery",
            "Symbiotic resilience mechanisms",
        ],

        solution_id="SOLUTION-REEF-0001",

        approved=True,
    )

    print("=" * 60)
    print("INNOVATION OS DEMONSTRATION")
    print("=" * 60)

    print()
    print("Problem:")
    print(result.problem_id)

    print()
    print("Generated Ideas:")
    for idea in result.ideas:
        print("-", idea)

    print()
    print("Nature Parallels:")
    for pattern in result.nature_patterns:
        print("-", pattern)

    print()
    print("Solution:")
    print(result.solution_id)

    print()
    print("Alignment:")
    print(result.aligned)

    print()
    print("Review Complete:")
    print(result.reviewed)

    print()
    print("Human Approved:")
    print(result.approved)

    print()
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
