import tempfile
from pathlib import Path

from src.innovation_os.reconstruction.archive_engine import (
    ArchiveReconstructionEngine,
)


def test_archive_scan():

    with tempfile.TemporaryDirectory() as directory:

        path = Path(directory)

        (path / "idea.md").write_text(
            "innovation idea"
        )

        (path / "engine.py").write_text(
            "class Engine:"
        )


        engine = ArchiveReconstructionEngine()

        results = engine.scan(
            directory
        )


        assert len(results) == 2

        types = [
            item.artifact_type
            for item in results
        ]

        assert "DOCUMENT" in types
        assert "CODE" in types
