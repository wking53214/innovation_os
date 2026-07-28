from dataclasses import dataclass, field


@dataclass
class GraphNode:

    name: str

    attributes: dict = field(
        default_factory=dict
    )


class KnowledgeGraph:


    def __init__(self):

        self.nodes = {}
        self.edges = []


    def add_node(
        self,
        name,
        attributes=None
    ):

        node = GraphNode(
            name=name,
            attributes=attributes or {}
        )

        self.nodes[name] = node

        return node


    def connect(
        self,
        source,
        target,
        relationship
    ):

        self.edges.append(
            {
                "source": source,
                "target": target,
                "relationship": relationship,
            }
        )


    def neighbors(
        self,
        node
    ):

        return [
            e
            for e in self.edges
            if e["source"] == node
            or e["target"] == node
        ]
