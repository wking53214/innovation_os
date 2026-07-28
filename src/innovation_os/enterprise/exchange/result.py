from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ExchangeResult:


    approved: bool

    reason: str

    artifact: object = None


    timestamp: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
