from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class TimelineEvent:

    event_id: str
    artifact_id: str
    event_type: str
    description: str
    timestamp: str



class TimelineEngine:


    def __init__(self):

        self.events: List[TimelineEvent] = []


    def record(
        self,
        event_id: str,
        artifact_id: str,
        event_type: str,
        description: str,
    ):

        event = TimelineEvent(
            event_id=event_id,
            artifact_id=artifact_id,
            event_type=event_type,
            description=description,
            timestamp=datetime.utcnow().isoformat(),
        )

        self.events.append(event)

        return event


    def history(
        self,
        artifact_id: str,
    ):

        return [
            event
            for event in self.events
            if event.artifact_id == artifact_id
        ]
