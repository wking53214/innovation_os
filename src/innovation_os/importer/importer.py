import os
from pathlib import Path
from typing import List

from src.innovation_os.importer.models import (
    ImportedArtifact,
)


SUPPORTED = {
    ".md": "Markdown",
    ".py": "Python",
    ".txt": "Text",
}


class InnovationImporter:

    def __init__(self):
        self.artifacts = []


    def import_directory(
        self,
        directory: str,
    ) -> List[ImportedArtifact]:

        counter = 1

        for root, _, files in os.walk(directory):

            for filename in files:

                extension = Path(filename).suffix

                if extension not in SUPPORTED:
                    continue

                path = os.path.join(
                    root,
                    filename,
                )

                try:
                    with open(
                        path,
                        "r",
                        errors="ignore",
                    ) as file:

                        content = file.read()

                except Exception:
                    continue


                artifact = ImportedArtifact(
                    artifact_id=f"IMPORT-{counter:04d}",
                    source_path=path,
                    artifact_type=SUPPORTED[extension],
                    title=filename,
                    preview=content[:200],
                )

                self.artifacts.append(
                    artifact
                )

                counter += 1


        return self.artifacts
