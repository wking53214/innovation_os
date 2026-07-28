from dataclasses import dataclass, field
from typing import List, Any


@dataclass
class AnomalyDetector:
    """
    Detects unusual intelligence patterns.
    """

    anomalies: List[Any] = field(
        default_factory=list
    )


    def detect(
        self,
        value,
        expected=None
    ):

        anomaly = None

        if expected is not None and value != expected:
            anomaly = {
                "value": value,
                "expected": expected,
            }

            self.anomalies.append(
                anomaly
            )

        return anomaly
