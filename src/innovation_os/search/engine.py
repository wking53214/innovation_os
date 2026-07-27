from dataclasses import dataclass
from typing import List


@dataclass
class SearchResult:

    node_id: str
    node_type: str
    label: str
    score: float


class SearchEngine:


    def __init__(self):

        self.nodes = []


    def index(
        self,
        node_id,
        node_type,
        label,
    ):

        self.nodes.append(
            {
                "id": node_id,
                "type": node_type,
                "label": label,
            }
        )


    def search(
        self,
        query: str,
    ) -> List[SearchResult]:

        results = []

        query = query.lower()

        for node in self.nodes:

            label = node["label"].lower()

            if query in label:

                results.append(
                    SearchResult(
                        node_id=node["id"],
                        node_type=node["type"],
                        label=node["label"],
                        score=1.0,
                    )
                )

        return results
