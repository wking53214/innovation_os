from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class TrustRecord:


    node_id: str

    trust_score: float

    verified: bool = False


    metadata: dict = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
