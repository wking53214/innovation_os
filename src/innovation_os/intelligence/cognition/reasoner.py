from dataclasses import dataclass


@dataclass
class Reasoner:
    """
    Performs reasoning over perceptions.
    """

    def reason(
        self,
        perception
    ):

        return {
            "type": "inference",
            "input": perception,
        }
