from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid



@dataclass
class FederatedKnowledgeArtifact:


    artifact_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )


    source_node: str = ""

    knowledge_type: str = ""

    content: dict = field(
        default_factory=dict
    )


    confidence: float = 0.0


    provenance: dict = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )
