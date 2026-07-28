from dataclasses import dataclass


@dataclass
class DecisionScorer:
    """
    Scores decision alternatives.
    """


    def score(
        self,
        alternative
    ):

        return (
            alternative.expected_value
            -
            alternative.risk
        )
