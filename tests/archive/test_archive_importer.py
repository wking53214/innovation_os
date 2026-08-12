import tempfile
from pathlib import Path

from innovation_os.archive.importer import (
    ArchiveImporter,
)


def test_archive_import():

    with tempfile.TemporaryDirectory() as directory:

        path = Path(directory)

        (path / "idea.md").write_text(
            "innovation"
        )

        (path / "engine.py").write_text(
            "class Engine:"
        )


        importer = ArchiveImporter()

        results = importer.import_directory(
            directory
        )


        assert len(results) == 2

        ids = [
            item.artifact_id
            for item in results
        ]

        assert all(
            item.startswith("ARTIFACT-")
            for item in ids
        )
