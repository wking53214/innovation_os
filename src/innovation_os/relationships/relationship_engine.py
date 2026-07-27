from dataclasses import dataclass, field
from typing import Dict, List



@dataclass
class Relationship:

    source_id: str
    target_id: str
    relationship_type: str



class RelationshipEngine:


    def __init__(self):

        self.relationships: List[
            Relationship
        ] = []



    def connect(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str,
    ):

        relationship = Relationship(
            source_id,
            target_id,
            relationship_type,
        )


        self.relationships.append(
            relationship
        )


        return relationship



    def related_to(
        self,
        item_id: str,
    ):

        return [
            relationship
            for relationship in self.relationships
            if (
                relationship.source_id == item_id
                or
                relationship.target_id == item_id
            )
        ]





    def find_connections(
        self,
        item_id: str,
    ):

        """
        Backward compatibility wrapper.

        Returns all relationships connected
        to an item.
        """

        return self.related_to(
            item_id
        )

    def find_links(
        self,
        source_id: str,
        relationship_type=None,
    ):

        return [
            relationship
            for relationship in self.relationships
            if (
                relationship.source_id == source_id
                and
                (
                    relationship_type is None
                    or
                    relationship.relationship_type
                    == relationship_type
                )
            )
        ]
