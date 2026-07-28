from dataclasses import dataclass, field
import uuid


@dataclass
class OptimizationProposal:

    proposal_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    target: str = ""

    recommendation: str = ""

    confidence: float = 0.0

    approved: bool = False
