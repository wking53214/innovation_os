class AdaptationEngine:


    def __init__(
        self,
        model
    ):

        self.model = model


    def adapt(
        self,
        strategy,
        reward
    ):

        self.model.update(
            strategy,
            reward
        )

        return {
            "strategy": strategy,
            "updated": True,
            "score": reward
        }
