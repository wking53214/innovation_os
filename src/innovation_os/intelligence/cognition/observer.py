from dataclasses import dataclass


@dataclass
class Observer:
    """
    Observes raw signals and passes them to the perception stage.
    """

    def observe(self, signal):
        return signal
