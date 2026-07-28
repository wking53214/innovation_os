from dataclasses import dataclass


@dataclass
class Observer:
    """
    Converts incoming signals into observations.
    """

    def observe(
        self,
        signal
    ):

        return {
            "type": "observation",
            "source": signal,
        }
