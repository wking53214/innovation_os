from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ReleaseManifest:

    version: str = ""

    components: list = field(
        default_factory=list
    )

    certified: bool = False

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
