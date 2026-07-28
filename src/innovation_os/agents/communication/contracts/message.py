from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class AgentMessage:


    message_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )


    sender: str = ""

    receiver: str = ""

    message_type: str = ""

    payload: dict = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
