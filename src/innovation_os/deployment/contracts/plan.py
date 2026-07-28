from dataclasses import dataclass, field
import uuid


@dataclass
class DeploymentPlan:

    plan_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    environment: str = ""

    services: list = field(
        default_factory=list
    )

    approved: bool = False
