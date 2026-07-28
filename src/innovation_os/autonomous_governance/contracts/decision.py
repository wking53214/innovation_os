from dataclasses import dataclass, field
import uuid


@dataclass
class GovernanceDecision:

    decision_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    action: str = ""

    approved: bool = False

    reason: str = ""
