from pathlib import Path
from typing import List

from src.innovation_os.archive.models import ArchiveArtifact


class ArchiveConnector:


    SUPPORTED = {

        ".py": "CODE",
        ".md": "DOCUMENT",
        ".txt": "CONVERSATION",
        ".json": "DATA",
    }


    def scan(
        self,
        directory: str,
    ) -> List[ArchiveArtifact]:

        artifacts = []

        root = Path(directory)

        for file in root.rglob("*"):

            if not file.is_file():
                continue


            artifact_type = (
                self.SUPPORTED.get(
                    file.suffix.lower(),
                    "UNKNOWN",
                )
            )


            artifacts.append(
                ArchiveArtifact(
                    path=str(file),
                    artifact_type=artifact_type,
                    name=file.name,
                )
            )


        return artifacts
