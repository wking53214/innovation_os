from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class MemoryArtifact:

    identifier: str

    content: dict

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    metadata: dict = field(
        default_factory=dict
    )
