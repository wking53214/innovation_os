class MetricsRegistry:


    def __init__(self):

        self.metrics = {}


    def increment(
        self,
        name,
        amount=1
    ):

        self.metrics[name] = (
            self.metrics.get(
                name,
                0
            )
            + amount
        )


    def get(
        self,
        name
    ):

        return self.metrics.get(
            name,
            0
        )


    def snapshot(
        self
    ):

        return dict(
            self.metrics
        )
