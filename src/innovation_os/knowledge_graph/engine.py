from dataclasses import dataclass
from typing import List


@dataclass
class GraphRelationship:

    source: str
    relationship: str
    target: str



class KnowledgeGraphEngine:


    def __init__(self):

        self.relationships: List[GraphRelationship] = []


    def connect(
        self,
        source: str,
        relationship: str,
        target: str,
    ):

        edge = GraphRelationship(
            source,
            relationship,
            target,
        )

        self.relationships.append(edge)

        return edge


    def find_connections(
        self,
        artifact_id: str,
    ):

        return [
            edge
            for edge in self.relationships
            if (
                edge.source == artifact_id
                or edge.target == artifact_id
            )
        ]


    def find_by_type(
        self,
        relationship: str,
    ):

        return [
            edge
            for edge in self.relationships
            if edge.relationship == relationship
        ]
