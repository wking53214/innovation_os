from dataclasses import dataclass, field
import uuid


@dataclass
class Incident:

    incident_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    service: str = ""

    severity: str = "low"

    status: str = "open"
