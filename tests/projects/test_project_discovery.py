import tempfile
from pathlib import Path

from innovation_os.projects.project_discovery import (
    ProjectDiscovery,
)



def test_project_discovery():

    with tempfile.TemporaryDirectory() as directory:

        root = Path(directory)

        (root / "README.md").write_text(
            "project"
        )

        (root / "engine.py").write_text(
            "print('test')"
        )


        result = ProjectDiscovery().analyze(
            directory
        )


        assert result.files == 2
        assert "Python" in result.languages
        assert "README.md" in result.markers
