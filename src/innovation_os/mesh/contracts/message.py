from dataclasses import dataclass, field
import uuid


@dataclass
class MeshMessage:

    message_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    source: str = ""

    target: str = ""

    payload: dict = field(
        default_factory=dict
    )
