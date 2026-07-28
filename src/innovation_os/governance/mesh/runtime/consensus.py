class GovernanceConsensus:


    def approve(
        self,
        evaluations
    ):

        if not evaluations:

            return False


        return all(
            item["compliant"]
            for item in evaluations
        )
