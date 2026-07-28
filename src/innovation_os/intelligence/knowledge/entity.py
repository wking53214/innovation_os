from dataclasses import dataclass, field
import uuid


@dataclass
class KnowledgeEntity:
    """
    Core intelligence knowledge object.
    """

    name: str
    entity_type: str
    attributes: dict = field(
        default_factory=dict
    )
    entity_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )
