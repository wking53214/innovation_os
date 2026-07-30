from src.innovation_os.models import (
    Problem,
    Question,
    Concept,
    Decision,
    ArtifactRecord,
    Relationship,
)


def test_problem_creation():
    problem = Problem(
        id="PROB-0001",
        title="Disconnected ideas and code",
        description="Ideas and artifacts are difficult to trace."
    )

    assert problem.id == "PROB-0001"
    assert problem.title == "Disconnected ideas and code"


def test_relationship_creation():
    relationship = Relationship(
        source_id="PROB-0001",
        target_id="CON-0001",
        relationship_type="creates"
    )

    assert relationship.source_id == "PROB-0001"
    assert relationship.target_id == "CON-0001"