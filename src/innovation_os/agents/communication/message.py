from dataclasses import dataclass
from datetime import datetime, timezone
import uuid


@dataclass
class AgentMessage:

    sender: str

    receiver: str

    payload: dict

    message_id: str = uuid.uuid4().hex

    created_at: datetime = datetime.now(
        timezone.utc
    )
