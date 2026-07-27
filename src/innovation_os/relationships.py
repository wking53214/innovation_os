from dataclasses import dataclass
from datetime import datetime


@dataclass
class Relationship:
    source_id: str
    target_id: str
    relationship_type: str
    created: datetime = datetime.now()


class RelationshipEngine:
    def __init__(self):
        self.relationships = []

    def connect(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str,
    ):
        relationship = Relationship(
            source_id=source_id,
            target_id=target_id,
            relationship_type=relationship_type,
        )

        self.relationships.append(relationship)

        return relationship

    def find_connections(self, object_id: str):
        return [
            r
            for r in self.relationships
            if r.source_id == object_id
            or r.target_id == object_id
        ]