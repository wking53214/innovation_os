from .base_adapter import IntelligenceAdapter

from innovation_os.intelligence.contracts import (
    IntelligenceArtifact,
)


class PatternAdapter(IntelligenceAdapter):

    name = "pattern"

    def __init__(self, engine=None):
        self.engine = engine

    def translate(self, data):

        if self.engine and hasattr(
            self.engine,
            "process"
        ):
            result = self.engine.process(data)
        else:
            result = data

        return IntelligenceArtifact(
            intelligence_type="pattern",
            source_system="pattern_engine",
            observation={
                "result": result
            },
            confidence=0.5,
        )
