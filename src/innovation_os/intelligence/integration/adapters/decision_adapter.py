from dataclasses import dataclass


@dataclass
class DecisionAdapter:
    """
    Decision engine integration boundary.
    """

    engine=None


    def evaluate(
        self,
        decision
    ):

        if self.engine and hasattr(
            self.engine,
            "evaluate"
        ):
            return self.engine.evaluate(
                decision
            )

        return decision
