from dataclasses import dataclass, field
import uuid


@dataclass
class ImprovementProposal:

    proposal_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    target_component: str = ""

    recommendation: str = ""

    confidence: float = 0.0

    approved: bool = False
