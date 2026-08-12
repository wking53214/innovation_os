from pathlib import Path

from innovation_os.repository.importer import (
    RepositoryImporter,
)


def test_repository_scan(tmp_path):

    repo = Path(tmp_path)

    (repo / "engine.py").write_text(
        "print('test')"
    )

    (repo / "README.md").write_text(
        "# Project"
    )


    importer = RepositoryImporter()


    artifacts = importer.scan(
        str(repo)
    )


    types = [
        item.artifact_type
        for item in artifacts
    ]


    assert "CODE" in types
    assert "DOCUMENTATION" in types
