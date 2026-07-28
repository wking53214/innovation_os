from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ExplanationGraph:
    """
    Graph representation of explanations.
    """

    nodes: Dict[str, dict] = field(
        default_factory=dict
    )

    edges: List[tuple] = field(
        default_factory=list
    )


    def add_node(
        self,
        node_id,
        data=None
    ):

        self.nodes[node_id] = data or {}

        return node_id


    def connect(
        self,
        source,
        target
    ):

        self.edges.append(
            (source, target)
        )

        return (source, target)
