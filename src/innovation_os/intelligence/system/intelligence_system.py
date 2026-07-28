from dataclasses import dataclass, field


from innovation_os.intelligence.runtime import (
    IntelligenceRuntime,
)

from innovation_os.intelligence.memory import (
    IntelligenceMemory,
)

from innovation_os.intelligence.learning import (
    FeedbackEngine,
    AdaptationEngine,
)

from innovation_os.intelligence.metrics import (
    IntelligenceMetrics,
)

from innovation_os.intelligence.telemetry import (
    TelemetryEngine,
)

from innovation_os.intelligence.discovery import (
    DiscoveryEngine,
)


@dataclass
class IntelligenceSystem:
    """
    Complete intelligence subsystem boundary.

    Coordinates:
    perception
    reasoning
    memory
    learning
    observability
    discovery
    """

    runtime: IntelligenceRuntime

    memory: IntelligenceMemory = field(
        default_factory=IntelligenceMemory
    )

    feedback: FeedbackEngine = field(
        default_factory=FeedbackEngine
    )

    adaptation: AdaptationEngine = field(
        default_factory=AdaptationEngine
    )

    metrics: IntelligenceMetrics = field(
        default_factory=IntelligenceMetrics
    )

    telemetry: TelemetryEngine = field(
        default_factory=TelemetryEngine
    )

    discovery: DiscoveryEngine = field(
        default_factory=DiscoveryEngine
    )


    def process(
        self,
        input_data
    ):

        self.metrics.increment(
            "executions"
        )


        self.telemetry.record(
            "execution_started",
            {
                "input": input_data
            }
        )


        artifact = self.runtime.execute(
            input_data
        )


        self.memory.remember(
            artifact
        )


        self.discovery.discover(
            artifact
        )


        self.telemetry.record(
            "execution_completed",
            {
                "artifact_id":
                    artifact.artifact_id
            }
        )


        return artifact
