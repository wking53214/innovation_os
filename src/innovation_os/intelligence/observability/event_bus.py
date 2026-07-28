from dataclasses import dataclass, field


@dataclass
class IntelligenceEventBus:
    """
    Intelligence internal event stream.
    """

    events: list = field(
        default_factory=list
    )


    def publish(
        self,
        event
    ):

        self.events.append(
            event
        )

        return event


    def latest(self):

        if not self.events:
            return None

        return self.events[-1]
