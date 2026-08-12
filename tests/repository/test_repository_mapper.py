import tempfile
from pathlib import Path

from innovation_os.repository.mapper import (
    RepositoryMapper,
)


def test_repository_mapping():

    with tempfile.TemporaryDirectory() as directory:

        root = Path(directory)

        (root / "engine.py").write_text(
            "class Engine:"
        )

        (root / "README.md").write_text(
            "Project documentation"
        )


        mapper = RepositoryMapper()

        results = mapper.map_repository(
            directory
        )


        assert len(results) == 2

        types = [
            item.artifact_type
            for item in results
        ]

        assert "CODE" in types
        assert "DOCUMENT" in types


def test_repository_identity():

    with tempfile.TemporaryDirectory() as directory:

        mapper = RepositoryMapper()

        results = mapper.map_repository(
            directory
        )


        assert results == []
