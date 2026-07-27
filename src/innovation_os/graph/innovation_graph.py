from dataclasses import dataclass, field
from typing import Dict, List



@dataclass
class GraphNode:

    node_id: str
    node_type: str
    metadata: dict = field(
        default_factory=dict
    )



@dataclass
class GraphEdge:

    source: str
    target: str
    relationship: str



class InnovationGraph:


    def __init__(self):

        self.nodes: Dict[str, GraphNode] = {}

        self.edges: List[GraphEdge] = []



    def add_node(
        self,
        node_id: str,
        node_type: str,
        **metadata,
    ):

        node = GraphNode(
            node_id=node_id,
            node_type=node_type,
            metadata=metadata,
        )

        self.nodes[node_id] = node

        return node



    def connect(
        self,
        source: str,
        target: str,
        relationship: str,
    ):

        edge = GraphEdge(
            source=source,
            target=target,
            relationship=relationship,
        )

        self.edges.append(
            edge
        )

        return edge



    def related(
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
