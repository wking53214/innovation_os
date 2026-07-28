from dataclasses import dataclass
from datetime import datetime


@dataclass
class IntelligenceTelemetryEvent:

    event_type: str

    source: str

    payload: dict

    timestamp: datetime = None


    def __post_init__(self):

        if self.timestamp is None:
            self.timestamp = datetime.utcnow()
