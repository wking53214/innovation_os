from dataclasses import dataclass


@dataclass
class RiskEngine:
    """
    Evaluates decision risk.
    """


    def score(
        self,
        alternative
    ):

        return alternative.risk
