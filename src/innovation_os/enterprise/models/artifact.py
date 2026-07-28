from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid



@dataclass
class EnterpriseArtifact:


    artifact_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )


    source_system: str = ""

    artifact_type: str = ""

    payload: dict = field(
        default_factory=dict
    )


    metadata: dict = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
