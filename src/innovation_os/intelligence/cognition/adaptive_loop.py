from dataclasses import dataclass


@dataclass
class AdaptiveLoop:
    """
    Repeated cognitive improvement loop.
    """

    cycle: object


    def run(
        self,
        signals
    ):

        results = []

        for signal in signals:

            results.append(
                self.cycle.execute(
                    signal
                )
            )

        return results
