from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class RepositoryArtifact:

    path: str
    artifact_type: str



class RepositoryImporter:


    def scan(
        self,
        repository_path: str,
    ) -> List[RepositoryArtifact]:

        results = []

        root = Path(repository_path)


        for file in root.rglob("*"):

            if file.is_file():

                artifact_type = (
                    self.classify(file)
                )

                results.append(
                    RepositoryArtifact(
                        str(file),
                        artifact_type,
                    )
                )

        return results



    def classify(
        self,
        file: Path,
    ):

        suffix = file.suffix.lower()


        if suffix == ".py":

            return "CODE"


        if suffix in [
            ".md",
            ".txt",
        ]:

            return "DOCUMENTATION"


        if suffix in [
            ".yaml",
            ".yml",
            ".json",
        ]:

            return "CONFIGURATION"


        return "UNKNOWN"
