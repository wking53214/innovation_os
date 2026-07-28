from dataclasses import dataclass, field
import uuid


@dataclass
class V3Foundation:

    foundation_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    version: str = "3.0"

    capabilities: list = field(
        default_factory=list
    )

    status: str = "initializing"
