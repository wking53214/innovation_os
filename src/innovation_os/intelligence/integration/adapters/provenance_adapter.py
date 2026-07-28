from dataclasses import dataclass


@dataclass
class ProvenanceAdapter:
    """
    Traceability integration boundary.
    """

    tracker=None


    def record(
        self,
        event
    ):

        if self.tracker and hasattr(
            self.tracker,
            "record"
        ):
            return self.tracker.record(
                event
            )

        return event
