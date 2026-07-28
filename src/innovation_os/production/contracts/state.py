from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class RuntimeState:

    service: str = ""

    status: str = "starting"

    health: str = "unknown"

    metadata: dict = field(
        default_factory=dict
    )

    updated_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
