from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class IntelligenceMetrics:
    """
    Runtime intelligence measurement system.
    """

    counters: Dict[str, int] = field(
        default_factory=dict
    )

    values: Dict[str, Any] = field(
        default_factory=dict
    )


    def increment(
        self,
        metric: str,
        amount: int = 1
    ):

        self.counters[metric] = (
            self.counters.get(metric, 0)
            + amount
        )


    def record(
        self,
        metric: str,
        value
    ):

        self.values[metric] = value


    def get(
        self,
        metric: str,
        default=None
    ):

        if metric in self.counters:
            return self.counters[metric]

        return self.values.get(
            metric,
            default
        )


    def snapshot(self):

        return {
            "counters": self.counters,
            "values": self.values,
        }
