from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class FabricNode:


    node_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )


    name: str = ""

    organization: str = ""

    capabilities: list = field(
        default_factory=list
    )


    metadata: dict = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
