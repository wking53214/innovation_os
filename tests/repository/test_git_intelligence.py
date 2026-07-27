import subprocess
import tempfile
from pathlib import Path


from src.innovation_os.repository.git_intelligence import (
    GitIntelligence,
)



def test_git_commit_intelligence():

    with tempfile.TemporaryDirectory() as directory:

        root = Path(directory)


        subprocess.run(
            [
                "git",
                "init",
            ],
            cwd=directory,
            capture_output=True,
        )


        file = root / "engine.py"

        file.write_text(
            "class Engine:"
        )


        subprocess.run(
            [
                "git",
                "add",
                ".",
            ],
            cwd=directory,
        )


        subprocess.run(
            [
                "git",
                "-c",
                "user.name=test",
                "-c",
                "user.email=test@test.com",
                "commit",
                "-m",
                "Add engine",
            ],
            cwd=directory,
            capture_output=True,
        )


        result = GitIntelligence().commits(
            directory
        )


        assert len(result) == 1

        assert (
            "engine.py"
            in result[0].files
        )
