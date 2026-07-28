from dataclasses import dataclass


@dataclass
class KnowledgeRelationship:
    """
    Relationship between intelligence entities.
    """

    source_id: str
    target_id: str
    relation_type: str
    confidence: float = 1.0
