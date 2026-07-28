from dataclasses import dataclass, field
from typing import List, Dict, Any
from datetime import datetime, timezone


@dataclass
class TelemetryEngine:
    """
    Intelligence execution telemetry collector.
    """

    events: List[Dict[str, Any]] = field(
        default_factory=list
    )


    def record(
        self,
        event_type: str,
        payload: Dict[str, Any]
    ):

        event = {
            "type": event_type,
            "payload": payload,
            "timestamp": datetime.now(
                timezone.utc
            ),
        }

        self.events.append(
            event
        )

        return event


    def query(
        self,
        event_type=None
    ):

        if event_type is None:
            return self.events

        return [
            event
            for event in self.events
            if event["type"] == event_type
        ]
