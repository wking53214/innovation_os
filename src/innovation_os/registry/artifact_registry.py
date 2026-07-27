from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass
class CodeArtifact:
    artifact_id: str
    filename: str
    path: str
    language: str
    idea_id: str = ""
    project_id: str = ""
    created_at: datetime = field(
        default_factory=datetime.now
    )


class ArtifactRegistry:

    def __init__(self):
        self.artifacts: Dict[str, CodeArtifact] = {}
        self.counter = 1


    def register(
        self,
        filename,
        path,
        language,
    ):

        artifact_id = (
            f"CODE-{self.counter:05d}"
        )

        artifact = CodeArtifact(
            artifact_id=artifact_id,
            filename=filename,
            path=path,
            language=language,
        )

        self.artifacts[artifact_id] = artifact

        self.counter += 1

        return artifact


    def link_idea(
        self,
        artifact_id,
        idea_id,
    ):

        artifact = self.artifacts[
            artifact_id
        ]

        artifact.idea_id = idea_id

        return artifact


    def get(
        self,
        artifact_id,
    ):

        return self.artifacts.get(
            artifact_id
        )


    def all(self) -> List[CodeArtifact]:

        return list(
            self.artifacts.values()
        )
