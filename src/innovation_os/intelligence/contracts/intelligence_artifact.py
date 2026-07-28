from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict
import uuid


@dataclass
class IntelligenceArtifact:

    intelligence_type: str = ""

    source_system: str = ""

    confidence: float = 0.0

    payload: Any = None

    observation: Any = None

    artifact_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    provenance: Dict[str, Any] = field(
        default_factory=dict
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


    @property
    def identifier(self):

        return self.artifact_id


    def validate(self):

        return (
            bool(self.artifact_id)
            and 0.0 <= self.confidence <= 1.0
        )
