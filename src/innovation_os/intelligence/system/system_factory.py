from innovation_os.intelligence.runtime import (
    IntelligenceRuntime,
)

from innovation_os.intelligence.memory import (
    IntelligenceMemory,
)

from innovation_os.intelligence.telemetry import (
    TelemetryCollector,
    IntelligenceMetrics,
    TelemetryEngine,
)

from .intelligence_system import IntelligenceSystem



def create_intelligence_system(
    pipeline
):

    memory = IntelligenceMemory()

    runtime = IntelligenceRuntime(
        pipeline,
        memory,
    )


    telemetry = TelemetryEngine(
        TelemetryCollector(),
        IntelligenceMetrics(),
    )


    return IntelligenceSystem(
        runtime=runtime,
        memory=memory,
        telemetry=telemetry,
    )
