from dataclasses import dataclass, field
import uuid


@dataclass
class IntelligenceNode:

    node_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    name: str = ""

    capabilities: list = field(
        default_factory=list
    )

    status: str = "offline"
