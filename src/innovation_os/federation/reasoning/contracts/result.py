from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid



@dataclass
class FederatedReasoningResult:


    reasoning_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )


    source_node: str = ""

    subject: str = ""

    conclusion: str = ""


    evidence: list = field(
        default_factory=list
    )


    confidence: float = 0.0


    provenance: dict = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
