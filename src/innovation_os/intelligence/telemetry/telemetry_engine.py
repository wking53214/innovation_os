from dataclasses import dataclass
from innovation_os.intelligence.telemetry.event import (
    IntelligenceTelemetryEvent,
)


@dataclass
class TelemetryEngine:

    collector: object

    metrics: object



    def observe(
        self,
        event
    ):

        if not hasattr(
            event,
            "event_type"
        ):

            event = IntelligenceTelemetryEvent(
                event_type="intelligence_execution",
                source="runtime",
                payload={
                    "result": event
                },
            )


        self.collector.record(
            event
        )


        self.metrics.increment(
            event.event_type
        )


        return event
