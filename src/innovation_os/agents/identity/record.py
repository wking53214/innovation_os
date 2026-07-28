from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class AgentIdentity:


    agent_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )


    name: str = ""

    version: str = "1.0"


    capabilities: list[str] = field(
        default_factory=list
    )


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
