from dataclasses import dataclass


@dataclass
class TelemetryEngine:

    collector: object

    metrics: object



    def observe(
        self,
        event
    ):

        self.collector.record(
            event
        )

        self.metrics.increment(
            event.event_type
        )

        return event
