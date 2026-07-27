from dataclasses import dataclass
from typing import Dict, List


@dataclass
class GraphNode:

    node_id: str
    node_type: str
    name: str



@dataclass
class GraphRelationship:

    source: str
    target: str
    relationship: str



class KnowledgeGraph:


    def __init__(self):

        self.nodes: Dict[str, GraphNode] = {}
        self.relationships: List[GraphRelationship] = []



    def add_node(
        self,
        node_id: str,
        node_type: str,
        name: str,
    ):

        node = GraphNode(
            node_id,
            node_type,
            name,
        )

        self.nodes[node_id] = node

        return node



    def connect(
        self,
        source: str,
        target: str,
        relationship: str,
    ):

        edge = GraphRelationship(
            source,
            target,
            relationship,
        )

        self.relationships.append(
            edge
        )

        return edge



    def neighbors(
        self,
        node_id: str,
    ):

        return [
            edge.target
            for edge in self.relationships
            if edge.source == node_id
        ]



    def related_path(
        self,
        start: str,
        end: str,
    ):

        visited = set()


        def walk(current, path):

            if current == end:

                return path


            visited.add(current)


            for neighbor in self.neighbors(current):

                if neighbor not in visited:

                    result = walk(
                        neighbor,
                        path + [neighbor],
                    )

                    if result:

                        return result


            return None


        return walk(
            start,
            [start],
        )
