from innovation_os.registry.artifact_registry import (
    Artifact,
    ArtifactRegistry,
)



def test_artifact_registration():

    registry = ArtifactRegistry()


    registry.register(
        Artifact(
            "ART-001",
            "CODE",
            "gateway.py",
            "Sentinel Repository",
            "PROJECT-SENTINEL",
        )
    )


    result = registry.get(
        "ART-001"
    )


    assert result.name == "gateway.py"



def test_project_search():

    registry = ArtifactRegistry()


    registry.register(
        Artifact(
            "ART-002",
            "DOCUMENT",
            "architecture.md",
            "Docs",
            "PROJECT-SENTINEL",
        )
    )


    results = registry.search_by_project(
        "PROJECT-SENTINEL"
    )


    assert len(results) == 1
