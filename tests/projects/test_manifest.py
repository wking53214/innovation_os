from src.innovation_os.projects.manifest import (
    ProjectManifest,
    ProjectRegistry,
)


def test_project_registration():

    registry = ProjectRegistry()


    project = ProjectManifest(
        "PROJECT-SENTINEL",
        "Sentinel OS",
        "AI governance platform",
        [
            "sentinel_os"
        ],
        [
            "AI",
            "governance",
        ],
    )


    registry.register(
        project
    )


    result = registry.get(
        "PROJECT-SENTINEL"
    )


    assert result.name == "Sentinel OS"
    assert "AI" in result.tags



def test_project_listing():

    registry = ProjectRegistry()

    registry.register(
        ProjectManifest(
            "PROJECT-001",
            "Test",
            "Example",
            [],
            [],
        )
    )


    assert len(
        registry.list_projects()
    ) == 1
