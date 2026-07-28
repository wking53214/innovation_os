from innovation_os.intelligence.telemetry import (
    IntelligenceTelemetryEvent,
    TelemetryCollector,
    IntelligenceMetrics,
    TelemetryEngine,
)


def test_telemetry():

    engine = TelemetryEngine(
        TelemetryCollector(),
        IntelligenceMetrics(),
    )


    event = IntelligenceTelemetryEvent(
        "inference",
        "engine",
        {
            "confidence": .9
        }
    )


    engine.observe(
        event
    )


    assert engine.collector.count() == 1
    assert engine.metrics.get(
        "inference"
    ) == 1
