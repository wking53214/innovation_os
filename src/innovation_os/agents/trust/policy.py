class AgentTrustPolicy:


    def __init__(
        self,
        minimum_score=0.70
    ):

        self.minimum_score = minimum_score


    def allowed(
        self,
        profile
    ):

        if profile is None:

            return False


        return (
            profile.overall_score()
            >=
            self.minimum_score
        )
