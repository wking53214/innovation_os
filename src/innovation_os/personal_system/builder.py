from dataclasses import dataclass
from typing import Dict, List


@dataclass
class SystemNode:

    node_id: str
    category: str
    name: str



@dataclass
class SystemLink:

    source: str
    relationship: str
    target: str



class PersonalSystemBuilder:


    def __init__(self):

        self.nodes: Dict[str, SystemNode] = {}
        self.links: List[SystemLink] = []


    def add_node(
        self,
        node_id: str,
        category: str,
        name: str,
    ):

        node = SystemNode(
            node_id,
            category,
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

        link = SystemLink(
            source,
            relationship,
            target,
        )

        self.links.append(link)

        return link



    def ecosystem(
        self,
    ):

        return {
            "nodes": list(self.nodes.values()),
            "relationships": self.links,
        }



    def find_category(
        self,
        category: str,
    ):

        return [
            node
            for node in self.nodes.values()
            if node.category == category
        ]
