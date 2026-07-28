from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class TelemetryEvent:

    event_type: str

    payload: dict

    event_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
