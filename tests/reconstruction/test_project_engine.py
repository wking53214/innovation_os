from src.innovation_os.reconstruction.project_engine import (
    ProjectReconstructionEngine,
)


def test_project_reconstruction():

    engine = ProjectReconstructionEngine()

    project = engine.reconstruct(
        "Sentinel OS",
        [
            "conversation about governance",
            "code implementation",
            "decision record",
        ],
    )


    assert project.name == "Sentinel OS"
    assert len(project.evidence) == 3
    assert project.confidence > 50


def test_empty_project():

    engine = ProjectReconstructionEngine()

    project = engine.reconstruct(
        "Unknown",
        [
            "random text",
        ],
    )

    assert project.confidence == 0
