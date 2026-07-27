from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class InnovationNode:

    node_id: str
    node_type: str
    name: str
    relationships: List[str] = field(
        default_factory=list
    )



class PersonalInnovationMap:


    def __init__(self):

        self.nodes: Dict[str, InnovationNode] = {}



    def add_node(
        self,
        node_id: str,
        node_type: str,
        name: str,
    ):

        node = InnovationNode(
            node_id,
            node_type,
            name,
        )

        self.nodes[node_id] = node

        return node



    def connect(
        self,
        source_id: str,
        target_id: str,
    ):

        source = self.nodes.get(
            source_id
        )

        if source:

            source.relationships.append(
                target_id
            )

        return True



    def get_connections(
        self,
        node_id: str,
    ):

        node = self.nodes.get(
            node_id
        )

        if not node:

            return []

        return node.relationships



    def build_project_view(
        self,
        project_id: str,
    ):

        return {
            "project": project_id,
            "nodes": [
                node
                for node in self.nodes.values()
                if project_id in node.relationships
                or node.node_id == project_id
            ],
        }
