import tempfile
from pathlib import Path

from innovation_os.archive.connector import (
    ArchiveConnector,
)


def test_archive_scan():

    with tempfile.TemporaryDirectory() as directory:

        Path(
            directory,
            "engine.py",
        ).write_text(
            "print('test')"
        )

        Path(
            directory,
            "notes.md",
        ).write_text(
            "# idea"
        )


        connector = ArchiveConnector()

        results = connector.scan(
            directory
        )


        assert len(results) == 2

        types = [
            item.artifact_type
            for item in results
        ]

        assert "CODE" in types
        assert "DOCUMENT" in types
