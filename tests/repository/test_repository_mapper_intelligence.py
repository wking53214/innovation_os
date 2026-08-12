import tempfile
from pathlib import Path

from innovation_os.repository.mapper import (
    RepositoryMapper,
)



def test_repository_mapping():

    with tempfile.TemporaryDirectory() as directory:

        root = Path(directory)


        (root / "engine.py").write_text(
            "class Engine: pass"
        )

        docs = root / "docs"

        docs.mkdir()

        (docs / "readme.md").write_text(
            "documentation"
        )


        result = RepositoryMapper().map(
            directory
        )


        assert len(result.files) == 2
        assert "engine.py" in result.modules
