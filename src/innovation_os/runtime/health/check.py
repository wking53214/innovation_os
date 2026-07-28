from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class HealthStatus:

    status: str

    timestamp: datetime


class HealthChecker:


    def check(
        self
    ):

        return HealthStatus(
            status="healthy",
            timestamp=datetime.now(
                timezone.utc
            )
        )
