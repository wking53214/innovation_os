from .event import TelemetryEvent


class TelemetryCollector:


    def __init__(self):

        self.events = []


    def emit(
        self,
        event_type,
        payload
    ):

        event = TelemetryEvent(
            event_type=event_type,
            payload=payload
        )

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
            if event.event_type == event_type
        ]
