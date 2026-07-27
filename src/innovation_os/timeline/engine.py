from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class TimelineEvent:

    event_id: str
    project_id: str
    event_type: str
    timestamp: datetime
    description: str = ""


    @property
    def artifact_id(self):
        """
        Backward compatibility
        with artifact timeline model.
        """
        return self.event_id



class TimelineEngine:


    def __init__(self):

        self.events: List[TimelineEvent] = []



    def add_event(
        self,
        event_id: str,
        project_id: str,
        event_type: str,
        timestamp: datetime,
        description: str = "",
    ):

        event = TimelineEvent(
            event_id,
            project_id,
            event_type,
            timestamp,
            description,
        )


        self.events.append(event)

        return event



    def generate(self):

        return sorted(
            self.events,
            key=lambda item: item.timestamp,
        )



    def history(
        self,
        project_id: str,
    ):

        return [
            event
            for event in self.generate()
            if event.project_id == project_id
        ]
