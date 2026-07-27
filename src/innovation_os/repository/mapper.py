from dataclasses import dataclass
from pathlib import Path
from typing import List
import hashlib


@dataclass
class RepositoryArtifact:

    repository_id: str
    path: str
    artifact_type: str



class RepositoryMapper:


    def __init__(self):

        self.artifacts = []


    def map_repository(
        self,
        directory: str,
    ) -> List[RepositoryArtifact]:

        root = Path(directory)

        results = []


        for file in root.rglob("*"):

            if file.is_file():

                artifact = RepositoryArtifact(
                    self._repository_id(root),
                    str(file),
                    self._classify(file),
                )

                self.artifacts.append(
                    artifact
                )

                results.append(
                    artifact
                )


        return results



    def _repository_id(
        self,
        root: Path,
    ):

        digest = hashlib.sha256(
            str(root).encode()
        ).hexdigest()[:12]

        return (
            "REPO-"
            + digest
        )


    def _classify(
        self,
        file: Path,
    ):

        suffix = file.suffix.lower()


        if suffix in [
            ".py",
            ".js",
            ".ts",
        ]:

            return "CODE"


        if suffix in [
            ".md",
            ".txt",
        ]:

            return "DOCUMENT"


        return "OTHER"
