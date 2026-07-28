from .base_adapter import IntelligenceAdapter

from innovation_os.intelligence.contracts import (
    IntelligenceArtifact,
)


class DuplicateAdapter(IntelligenceAdapter):

    name = "duplicate"

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
            intelligence_type="duplicate_detection",
            source_system="duplicate_engine",
            observation={
                "result": result
            },
            confidence=0.5,
        )
