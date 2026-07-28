from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Metric:

    name: str
    value: float
    timestamp: datetime


class Metrics:

    def __init__(self):

        self.items = []


    def record(
        self,
        name,
        value
    ):

        self.items.append(
            Metric(
                name=name,
                value=value,
                timestamp=datetime.now(
                    timezone.utc
                ),
            )
        )


    def export(self):

        return [
            {
                "name": x.name,
                "value": x.value,
                "timestamp": x.timestamp.isoformat(),
            }
            for x in self.items
        ]
