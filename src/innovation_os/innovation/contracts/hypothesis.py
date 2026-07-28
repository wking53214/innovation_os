from dataclasses import dataclass, field
import uuid


@dataclass
class InnovationHypothesis:

    hypothesis_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    statement: str = ""

    confidence: float = 0.0

    evidence: list = field(
        default_factory=list
    )
