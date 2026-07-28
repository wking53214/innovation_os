from dataclasses import dataclass, field
from typing import Any, List

from innovation_os.intelligence.contracts import (
    IntelligenceArtifact,
)


@dataclass
class IntelligencePipeline:
    """
    Base pipeline coordinator.

    Executes ordered intelligence stages while preserving
    independent engine boundaries.
    """

    stages: List[Any] = field(default_factory=list)

    def add_stage(self, stage):
        self.stages.append(stage)

    def execute(self, payload):

        current = payload

        for stage in self.stages:

            if hasattr(stage, "process"):
                current = stage.process(current)

            elif callable(stage):
                current = stage(current)

            else:
                raise TypeError(
                    f"Invalid pipeline stage: {stage}"
                )

        return current

    def create_artifact(
        self,
        intelligence_type: str,
        source_system: str,
        observation: dict,
        confidence: float = 0.0,
    ):

        return IntelligenceArtifact(
            intelligence_type=intelligence_type,
            source_system=source_system,
            observation=observation,
            confidence=confidence,
        )
