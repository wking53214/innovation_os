from dataclasses import dataclass, field


@dataclass
class MetricsCollector:
    """
    Collects intelligence runtime metrics.
    """

    metrics: dict = field(
        default_factory=dict
    )


    def increment(
        self,
        metric
    ):

        self.metrics[metric] = (
            self.metrics.get(
                metric,
                0
            ) + 1
        )

        return self.metrics[metric]


    def get(
        self,
        metric
    ):

        return self.metrics.get(
            metric,
            0
        )
