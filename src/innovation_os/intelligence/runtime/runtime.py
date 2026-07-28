from dataclasses import dataclass, field

from innovation_os.intelligence.contracts import (
    Signal,
    IntelligenceArtifact,
)

from .execution_context import ExecutionContext
from .intelligence_session import IntelligenceSession


@dataclass
class IntelligenceRuntime:
    """
    Execution boundary for the intelligence subsystem.

    Coordinates:
    input -> engines -> artifact
    """

    kernel: object

    session: IntelligenceSession = field(
        default_factory=IntelligenceSession
    )


    def execute(self, payload, source="runtime"):

        context = ExecutionContext(
            input_data=payload
        )


        signal = Signal(
            source=source,
            signal_type="runtime_input",
            payload=payload,
        )


        observation = self.kernel.execute(
            "observation",
            signal
        )

        perception = self.kernel.execute(
            "perception",
            observation
        )

        context_result = self.kernel.execute(
            "context",
            perception
        )

        knowledge = self.kernel.execute(
            "knowledge",
            context_result
        )

        evidence = self.kernel.execute(
            "evidence",
            knowledge
        )

        confidence = self.kernel.execute(
            "confidence",
            evidence
        )

        hypothesis = self.kernel.execute(
            "hypothesis",
            evidence
        )

        inference = self.kernel.execute(
            "inference",
            hypothesis
        )


        artifact = IntelligenceArtifact(
            intelligence_type="inference",
            source_system="intelligence_runtime",
            observation={
                "input": payload,
                "inference": inference,
            },
            confidence=confidence.score,
            provenance={
                "execution_id": context.execution_id
            },
        )


        self.session.add_artifact(
            artifact
        )

        return artifact
