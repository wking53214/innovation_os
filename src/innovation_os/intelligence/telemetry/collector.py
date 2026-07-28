class TelemetryCollector:


    def __init__(self):

        self.events = []



    def record(
        self,
        event
    ):

        self.events.append(
            event
        )

        return event



    def count(self):

        return len(
            self.events
        )
