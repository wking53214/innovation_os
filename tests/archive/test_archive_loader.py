import tempfile
from pathlib import Path

from src.innovation_os.archive.archive_loader import (
    ArchiveLoader,
)



def test_archive_loader():

    with tempfile.TemporaryDirectory() as directory:

        file = Path(directory) / "sentinel.py"

        file.write_text(
            "class Sentinel:"
        )


        loader = ArchiveLoader()

        manifest = loader.load(
            directory
        )


        assert manifest.name
        assert manifest.source == directory
        assert len(manifest.artifacts) == 1
