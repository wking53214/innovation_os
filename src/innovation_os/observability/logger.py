from .events import IntelligenceEvent


class IntelligenceLogger:

    def __init__(self):

        self.events = []


    def emit(
        self,
        event_type,
        payload,
    ):

        event = IntelligenceEvent(
            event_type=event_type,
            payload=payload,
        )

        self.events.append(
            event
        )

        return event


    def history(self):

        return list(
            self.events
        )
