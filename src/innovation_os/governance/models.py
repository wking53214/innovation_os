from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ApprovalRecord:
    approval_id: str
    target_id: str
    reviewer: str
    decision: str
    rationale: str
    created: datetime = field(default_factory=datetime.now)
