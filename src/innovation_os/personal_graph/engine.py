from dataclasses import dataclass
from typing import Dict, List


@dataclass
class InnovationNode:

    node_id: str
    node_type: str
    name: str



@dataclass
class InnovationEdge:

    source: str
    relationship: str
    target: str



class PersonalInnovationGraph:


    def __init__(self):

        self.nodes: Dict[str, InnovationNode] = {}
        self.edges: List[InnovationEdge] = []


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
        source: str,
        relationship: str,
        target: str,
    ):

        edge = InnovationEdge(
            source,
            relationship,
            target,
        )

        self.edges.append(edge)

        return edge



    def neighbors(
        self,
        node_id: str,
    ):

        results = []


        for edge in self.edges:

            if edge.source == node_id:

                results.append(
                    edge.target
                )

            elif edge.target == node_id:

                results.append(
                    edge.source
                )


        return results



    def find_by_type(
        self,
        node_type: str,
    ):

        return [
            node
            for node in self.nodes.values()
            if node.node_type == node_type
        ]
