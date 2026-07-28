from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class CertificationReport:

    system: str = ""

    checks: list = field(
        default_factory=list
    )

    passed: bool = False

    score: float = 0.0

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
