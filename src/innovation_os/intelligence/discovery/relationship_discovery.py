from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class RelationshipDiscovery:
    """
    Identifies relationships between
    intelligence entities.
    """

    relationships: List[Dict[str, Any]] = field(
        default_factory=list
    )


    def discover(
        self,
        source,
        target,
        relationship_type="related"
    ):

        relationship = {
            "source": source,
            "target": target,
            "type": relationship_type,
        }

        self.relationships.append(
            relationship
        )

        return relationship
