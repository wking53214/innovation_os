from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class TimelineEvent:

    event_id: str
    artifact_id: str
    event_type: str
    timestamp: datetime
    description: str



class TimelineEngine:


    def __init__(self):

        self.events: List[TimelineEvent] = []


    def add_event(
        self,
        event_id: str,
        artifact_id: str,
        event_type: str,
        timestamp: datetime,
        description: str,
    ):

        event = TimelineEvent(
            event_id,
            artifact_id,
            event_type,
            timestamp,
            description,
        )

        self.events.append(event)

        return event



    def history(
        self,
        artifact_id: str,
    ):

        results = [
            event
            for event in self.events
            if event.artifact_id == artifact_id
        ]

        return sorted(
            results,
            key=lambda item: item.timestamp,
        )
