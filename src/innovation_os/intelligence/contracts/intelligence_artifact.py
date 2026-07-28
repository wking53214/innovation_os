from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
import uuid


@dataclass
class IntelligenceArtifact:
    """
    Canonical intelligence exchange object.

    Shared output contract between intelligence engines,
    reasoning systems, and decision layers.
    """

    artifact_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    intelligence_type: str = ""

    source_system: str = ""

    subject: Optional[str] = None

    observation: Dict[str, Any] = field(
        default_factory=dict
    )

    evidence: List[Dict[str, Any]] = field(
        default_factory=list
    )

    confidence: float = 0.0

    relationships: List[Dict[str, Any]] = field(
        default_factory=list
    )

    provenance: Dict[str, Any] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    def validate(self) -> bool:
        return (
            bool(self.intelligence_type)
            and bool(self.source_system)
            and 0.0 <= self.confidence <= 1.0
        )
