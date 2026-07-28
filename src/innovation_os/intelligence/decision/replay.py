from dataclasses import dataclass, field


@dataclass
class DecisionReplay:
    """
    Stores historical decisions.
    """

    history: list = field(
        default_factory=list
    )


    def record(
        self,
        decision
    ):

        self.history.append(
            decision
        )

        return decision


    def count(self):

        return len(
            self.history
        )
