from dataclasses import dataclass, field

from .artifact_store import ArtifactStore


@dataclass
class IntelligenceMemory:
    """
    Long-term intelligence artifact memory.
    """

    store: ArtifactStore = field(
        default_factory=ArtifactStore
    )


    def remember(self, artifact):

        return self.store.save(
            artifact
        )


    def recall(self, artifact_id):

        return self.store.get(
            artifact_id
        )


    def history(self):

        return self.store.all()
