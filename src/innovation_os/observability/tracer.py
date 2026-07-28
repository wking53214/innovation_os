from datetime import datetime, timezone


class TraceRecord:


    def __init__(
        self,
        operation
    ):

        self.operation = operation

        self.started = datetime.now(
            timezone.utc
        )

        self.completed = None


    def complete(
        self
    ):

        self.completed = datetime.now(
            timezone.utc
        )

        return self
        

class Tracer:


    def __init__(self):

        self.traces = []


    def start(
        self,
        operation
    ):

        trace = TraceRecord(
            operation
        )

        self.traces.append(
            trace
        )

        return trace
