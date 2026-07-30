from pathlib import Path
from typing import List

from src.innovation_os.archive.models import ArchiveArtifact


class ArchiveReconstructionEngine:


    def __init__(self):

        self.artifacts: List[ArchiveArtifact] = []


    def scan(
        self,
        directory: str,
    ):

        root = Path(directory)

        results = []


        for file in root.rglob("*"):

            if file.is_file():

                artifact_type = self._classify(
                    file
                )

                artifact = ArchiveArtifact(
                    str(file),
                    artifact_type,
                    file.stat().st_size,
                )

                self.artifacts.append(
                    artifact
                )

                results.append(
                    artifact
                )


        return results


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


        if suffix in [
            ".json",
            ".yaml",
        ]:

            return "DATA"


        return "UNKNOWN"
