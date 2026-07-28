class MetricCollector:


    def __init__(self):

        self.metrics = []



    def record(
        self,
        metric
    ):

        self.metrics.append(
            metric
        )

        return metric



    def all(
        self
    ):

        return list(
            self.metrics
        )
