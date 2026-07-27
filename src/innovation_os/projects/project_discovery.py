from dataclasses import dataclass, field
from pathlib import Path
from typing import List



@dataclass
class ProjectProfile:

    name: str
    path: str
    files: int
    languages: List[str] = field(
        default_factory=list
    )
    markers: List[str] = field(
        default_factory=list
    )



class ProjectDiscovery:


    def analyze(
        self,
        directory: str,
    ):

        root = Path(directory)

        files = [
            f
            for f in root.rglob("*")
            if f.is_file()
        ]


        languages = set()

        for file in files:

            if file.suffix == ".py":
                languages.add("Python")

            elif file.suffix in [
                ".js",
                ".ts",
            ]:
                languages.add("JavaScript")



        markers = []

        for marker in [
            "README.md",
            "requirements.txt",
            "pyproject.toml",
            "package.json",
            ".git",
        ]:

            if (root / marker).exists():
                markers.append(marker)



        return ProjectProfile(
            name=root.name,
            path=str(root),
            files=len(files),
            languages=sorted(
                languages
            ),
            markers=markers,
        )
