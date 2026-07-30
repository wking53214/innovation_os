from dataclasses import dataclass
from pathlib import Path
from typing import List
import hashlib


@dataclass
class ArchiveImportRecord:

    artifact_id: str
    source_path: str
    artifact_type: str
    size: int



class ArchiveImporter:


    def __init__(self):

        self.artifacts = []


    def import_directory(
        self,
        directory: str,
    ) -> List[ArchiveImportRecord]:

        results = []

        root = Path(directory)


        for file in root.rglob("*"):

            if file.is_file():

                artifact = ArchiveImportRecord(
                    self._create_id(file),
                    str(file),
                    self._classify(file),
                    file.stat().st_size,
                )

                self.artifacts.append(
                    artifact
                )

                results.append(
                    artifact
                )


        return results


    def _create_id(
        self,
        file: Path,
    ):

        value = str(file).encode()

        return (
            "ARTIFACT-"
            +
            hashlib.sha256(value)
            .hexdigest()[:12]
        )


    def _classify(
        self,
        file: Path,
    ):

        suffix = file.suffix.lower()


        if suffix in [".py", ".js", ".ts"]:
            return "CODE"

        if suffix in [".md", ".txt"]:
            return "DOCUMENT"

        if suffix in [".json"]:
            return "DATA"

        return "UNKNOWN"
