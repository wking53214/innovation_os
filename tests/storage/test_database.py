from innovation_os.storage.database import (
    InnovationDatabase,
)


def test_database_persistence():

    database = InnovationDatabase(
        ":memory:"
    )

    database.add_node(
        "IDEA-001",
        "IDEA",
        "Governed AI Platform",
    )

    result = database.get_node(
        "IDEA-001"
    )

    assert result[0] == "IDEA-001"
    assert result[2] == "Governed AI Platform"


def test_relationship_storage():

    database = InnovationDatabase(
        ":memory:"
    )

    database.add_relationship(
        "PROBLEM-001",
        "IDEA-001",
        "GENERATES",
    )

    results = database.get_relationships(
        "PROBLEM-001"
    )

    assert len(results) == 1
    assert results[0][3] == "GENERATES"
