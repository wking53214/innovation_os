from innovation_os.intelligence.telemetry import (
    TelemetryEngine,
)


def test_telemetry():

    telemetry = TelemetryEngine()

    telemetry.record(
        "execution",
        {
            "status": "success"
        }
    )

    assert len(
        telemetry.events
    ) == 1
