from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class ArtifactStore:
    """
    Storage boundary for intelligence artifacts.
    """

    artifacts: Dict[str, Any] = field(
        default_factory=dict
    )


    def save(self, artifact):

        self.artifacts[
            artifact.artifact_id
        ] = artifact

        return artifact


    def get(self, artifact_id):

        return self.artifacts.get(
            artifact_id
        )


    def all(self):

        return list(
            self.artifacts.values()
        )
