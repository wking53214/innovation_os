from dataclasses import dataclass, field
from pathlib import Path
from typing import List



@dataclass
class HistoricalArtifact:

    path: str
    artifact_type: str
    content_length: int
    keywords: List[str] = field(
        default_factory=list
    )



class InnovationHistoryImporter:


    SUPPORTED = (
        ".md",
        ".txt",
        ".py",
        ".json",
    )


    def import_file(
        self,
        file_path: str,
    ):

        path = Path(file_path)

        content = path.read_text(
            errors="ignore"
        )


        keywords = []

        terms = [
            "sentinel",
            "gsa",
            "synapsis",
            "governance",
            "ai",
        ]


        lowered = content.lower()


        for term in terms:

            if term in lowered:

                keywords.append(
                    term
                )


        artifact_type = (
            "CODE"
            if path.suffix == ".py"
            else "DOCUMENT"
        )


        return HistoricalArtifact(
            path=str(path),
            artifact_type=artifact_type,
            content_length=len(content),
            keywords=keywords,
        )



    def import_directory(
        self,
        directory: str,
    ):

        root = Path(directory)


        results = []


        for file in root.rglob("*"):

            if (
                file.is_file()
                and file.suffix in self.SUPPORTED
            ):

                results.append(
                    self.import_file(
                        str(file)
                    )
                )


        return results
