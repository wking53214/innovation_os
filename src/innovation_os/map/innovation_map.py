from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class InnovationNode:

    node_id: str
    node_type: str
    label: str


@dataclass
class InnovationConnection:

    source: str
    target: str
    relationship: str


class InnovationMap:


    def __init__(self):

        self.nodes: Dict[str, InnovationNode] = {}
        self.connections: List[InnovationConnection] = []


    def add_node(
        self,
        node_id: str,
        node_type: str,
        label: str,
    ):

        self.nodes[node_id] = InnovationNode(
            node_id,
            node_type,
            label,
        )


    def connect(
        self,
        source: str,
        target: str,
        relationship: str,
    ):

        self.connections.append(
            InnovationConnection(
                source,
                target,
                relationship,
            )
        )


    def get_connections(
        self,
        node_id: str,
    ):

        return [
            connection
            for connection in self.connections
            if (
                connection.source == node_id
                or connection.target == node_id
            )
        ]


    def get_node(
        self,
        node_id: str,
    ):

        return self.nodes.get(
            node_id
        )
