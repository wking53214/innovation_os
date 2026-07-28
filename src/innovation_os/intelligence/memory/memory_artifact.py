from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class MemoryArtifact:

    identifier: str

    content: dict

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    metadata: dict = field(
        default_factory=dict
    )
