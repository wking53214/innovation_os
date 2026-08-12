from typing import List, Optional

from innovation_os.code_registry.models import (
    CodeArtifact,
)


class CodeRegistryEngine:

    def __init__(self):
        self.artifacts: List[CodeArtifact] = []

    def register_artifact(
        self,
        artifact_id: str,
        file_name: str,
        path: str,
        idea_id: str,
        problem_id: str,
        language: str,
        purpose: str,
        tags: List[str] = None,
    ) -> CodeArtifact:

        artifact = CodeArtifact(
            artifact_id=artifact_id,
            file_name=file_name,
            path=path,
            idea_id=idea_id,
            problem_id=problem_id,
            language=language,
            purpose=purpose,
            tags=tags or [],
        )

        self.artifacts.append(artifact)

        return artifact

    def get_artifact(
        self,
        artifact_id: str,
    ) -> Optional[CodeArtifact]:

        for artifact in self.artifacts:
            if artifact.artifact_id == artifact_id:
                return artifact

        return None

    def find_by_idea(
        self,
        idea_id: str,
    ) -> List[CodeArtifact]:

        return [
            artifact
            for artifact in self.artifacts
            if artifact.idea_id == idea_id
        ]

    def find_by_problem(
        self,
        problem_id: str,
    ) -> List[CodeArtifact]:

        return [
            artifact
            for artifact in self.artifacts
            if artifact.problem_id == problem_id
        ]
