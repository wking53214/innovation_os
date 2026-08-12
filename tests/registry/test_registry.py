from innovation_os.registry.artifact_registry import (
    ArtifactRegistry,
)


def test_register_code():

    registry = ArtifactRegistry()

    artifact = registry.register(
        "engine.py",
        "/code/engine.py",
        "Python",
    )

    assert artifact.artifact_id == "CODE-00001"


def test_link_idea():

    registry = ArtifactRegistry()

    artifact = registry.register(
        "model.py",
        "/code/model.py",
        "Python",
    )

    registry.link_idea(
        artifact.artifact_id,
        "IDEA-001",
    )

    result = registry.get(
        artifact.artifact_id
    )

    assert result.idea_id == "IDEA-001"
