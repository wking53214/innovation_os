from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class SystemObservation:

    component: str = ""

    metric: str = ""

    value: float = 0.0

    timestamp: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
