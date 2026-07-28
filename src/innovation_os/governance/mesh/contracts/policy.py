from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid



@dataclass
class GovernancePolicy:


    policy_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )


    name: str = ""

    rules: dict = field(
        default_factory=dict
    )


    version: str = "1.0"


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
