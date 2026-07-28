from .scorer import PerformanceScorer


class EvaluationEngine:


    def __init__(self):

        self.scorer = PerformanceScorer()


    def evaluate(
        self,
        result
    ):

        return self.scorer.score(
            result
        )
