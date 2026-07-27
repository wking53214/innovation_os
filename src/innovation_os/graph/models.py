from dataclasses import dataclass
from typing import Dict, List


@dataclass
class GraphNode:
    node_id: str
    node_type: str
    label: str


@dataclass
class GraphRelationship:
    source_id: str
    target_id: str
    relationship: str


class InnovationGraph:

    def __init__(self):
        self.nodes: Dict[str, GraphNode] = {}
        self.relationships: List[GraphRelationship] = []

    def add_node(
        self,
        node_id: str,
        node_type: str,
        label: str,
    ):

        node = GraphNode(
            node_id=node_id,
            node_type=node_type,
            label=label,
        )

        self.nodes[node_id] = node

        return node


    def connect(
        self,
        source_id: str,
        target_id: str,
        relationship: str,
    ):

        edge = GraphRelationship(
            source_id=source_id,
            target_id=target_id,
            relationship=relationship,
        )

        self.relationships.append(edge)

        return edge


    def get_connections(
        self,
        node_id: str,
    ):

        return [
            edge
            for edge in self.relationships
            if edge.source_id == node_id
            or edge.target_id == node_id
        ]
