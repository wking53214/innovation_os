import os
from typing import List

from innovation_os.code_scanner.models import (
    ScannedArtifact,
)


LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".go": "Go",
    ".rs": "Rust",
    ".cpp": "C++",
}


class CodeScanner:

    def __init__(self):
        self.results: List[ScannedArtifact] = []

    def scan_directory(
        self,
        directory: str,
    ) -> List[ScannedArtifact]:

        counter = 1

        for root, _, files in os.walk(directory):

            for file in files:

                extension = os.path.splitext(file)[1]

                if extension in LANGUAGE_MAP:

                    path = os.path.join(
                        root,
                        file,
                    )

                    artifact = ScannedArtifact(
                        artifact_id=f"SCAN-{counter:04d}",
                        file_name=file,
                        path=path,
                        language=LANGUAGE_MAP[extension],
                        size_bytes=os.path.getsize(path),
                        detected_terms=self._extract_terms(path),
                    )

                    self.results.append(
                        artifact
                    )

                    counter += 1

        return self.results


    def _extract_terms(
        self,
        path: str,
    ) -> List[str]:

        terms = []

        try:
            with open(
                path,
                "r",
                errors="ignore",
            ) as file:

                content = file.read().lower()

                keywords = [
                    "ai",
                    "model",
                    "governance",
                    "security",
                    "pipeline",
                    "engine",
                    "innovation",
                    "data",
                ]

                for keyword in keywords:
                    if keyword in content:
                        terms.append(keyword)

        except Exception:
            pass

        return terms
