from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ServiceRecord:

    name: str = ""

    status: str = "unknown"

    health: str = "unknown"

    metadata: dict = field(
        default_factory=dict
    )

    updated_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
