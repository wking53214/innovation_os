from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class ExperienceEvent:

    agent_id: str

    action: str

    outcome: object

    reward: float

    event_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
