class AdaptiveModel:


    def __init__(self):

        self.weights = {}


    def update(
        self,
        strategy,
        reward
    ):

        self.weights[strategy] = (
            self.weights.get(
                strategy,
                0
            ) + reward
        )


    def best_strategy(
        self
    ):

        if not self.weights:

            return None

        return max(
            self.weights,
            key=self.weights.get
        )
