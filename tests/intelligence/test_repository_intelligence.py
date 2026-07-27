from src.innovation_os.intelligence.repository_intelligence import (
    RepositoryIntelligenceEngine,
)

from src.innovation_os.registry.artifact_registry import (
    Artifact,
)



def test_repository_intelligence():

    artifacts = [

        Artifact(
            artifact_id="CODE-00001",
            artifact_type="CODE",
            name="engine.py",
            source="engine.py",
            project_id="sentinel_os",
        ),

        Artifact(
            artifact_id="DOC-00001",
            artifact_type="DOCUMENT",
            name="README.md",
            source="README.md",
            project_id="sentinel_os",
        ),

    ]


    result = RepositoryIntelligenceEngine().analyze(
        artifacts
    )


    assert result.name == "sentinel_os"

    assert result.artifacts == 2

    assert result.code_files == 1

    assert result.documents == 1

    assert "engine.py" in result.modules
