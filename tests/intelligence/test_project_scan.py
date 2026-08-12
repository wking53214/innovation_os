import tempfile
from pathlib import Path


from innovation_os.intelligence.project_scan import (
    ProjectScanner,
)



def test_project_scan():

    with tempfile.TemporaryDirectory() as directory:

        root = Path(directory)

        (root / "engine.py").write_text(
            "class Engine: pass"
        )

        (root / "README.md").write_text(
            "documentation"
        )


        result = ProjectScanner().scan(
            directory
        )


        assert result.artifacts == 2
        assert result.code_files == 1
        assert result.documents == 1
