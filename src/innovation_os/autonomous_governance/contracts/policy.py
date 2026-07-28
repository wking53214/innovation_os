from dataclasses import dataclass, field
import uuid


@dataclass
class GovernancePolicy:

    policy_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    name: str = ""

    rule: str = ""

    version: str = "1.0"
