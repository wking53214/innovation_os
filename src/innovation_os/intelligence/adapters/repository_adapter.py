from .base_adapter import IntelligenceAdapter

from innovation_os.intelligence.contracts import (
    IntelligenceArtifact,
)


class RepositoryAdapter(IntelligenceAdapter):

    name = "repository"

    def __init__(self, engine=None):
        self.engine = engine

    def translate(self, data):

        result = data

        if self.engine and hasattr(
            self.engine,
            "process"
        ):
            result = self.engine.process(data)

        return IntelligenceArtifact(
            intelligence_type="repository_analysis",
            source_system="repository_intelligence",
            observation={
                "result": result
            },
            confidence=0.5,
        )
