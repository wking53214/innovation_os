from dataclasses import dataclass, field
from datetime import datetime, timezone



@dataclass
class CapabilityEvaluation:


    capability_id: str


    quality_score: float = 0.0

    trust_score: float = 0.0

    compatibility_score: float = 0.0


    approved: bool = False


    evaluated_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )


    def overall_score(
        self
    ):

        return (
            self.quality_score * 0.4
            +
            self.trust_score * 0.4
            +
            self.compatibility_score * 0.2
        )
