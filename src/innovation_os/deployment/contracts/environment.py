from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Environment:

    name: str = ""

    variables: dict = field(
        default_factory=dict
    )

    status: str = "created"

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
