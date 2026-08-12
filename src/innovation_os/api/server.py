from dataclasses import asdict

from innovation_os.search.engine import (
    SearchEngine,
)


class InnovationAPI:


    def __init__(self):

        self.search = SearchEngine()
        self.nodes = {}


    def status(self):

        return {
            "system": "Innovation OS",
            "status": "operational",
        }


    def add_node(
        self,
        node_id,
        node_type,
        label,
    ):

        self.nodes[node_id] = {
            "id": node_id,
            "type": node_type,
            "label": label,
        }

        self.search.index(
            node_id,
            node_type,
            label,
        )

        return self.nodes[node_id]


    def get_node(
        self,
        node_id,
    ):

        return self.nodes.get(
            node_id
        )


    def search_nodes(
        self,
        query,
    ):

        results = self.search.search(
            query
        )

        return [
            asdict(result)
            for result in results
        ]
