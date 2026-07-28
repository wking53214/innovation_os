class PerformanceScorer:


    def score(
        self,
        outcome
    ):

        if isinstance(
            outcome,
            dict
        ):

            if outcome.get(
                "status"
            ) == "complete":

                return 1.0

        return 0.5
