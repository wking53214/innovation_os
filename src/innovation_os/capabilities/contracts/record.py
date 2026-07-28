from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class CapabilityRecord:


    capability_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )


    name: str = ""

    category: str = ""

    provider: str = ""

    version: str = "1.0"


    metadata: dict = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
