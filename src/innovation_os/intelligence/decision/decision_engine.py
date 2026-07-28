from dataclasses import dataclass


@dataclass
class DecisionIntelligenceEngine:
    """
    Intelligence decision coordinator.
    """

    scorer: object
    replay: object


    def evaluate(
        self,
        alternatives
    ):

        ranked = sorted(
            alternatives,
            key=self.scorer.score,
            reverse=True,
        )

        winner = ranked[0]

        self.replay.record(
            winner
        )

        return winner
