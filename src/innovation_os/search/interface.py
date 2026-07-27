from dataclasses import dataclass
from typing import List


@dataclass
class SearchResult:

    item_id: str
    item_type: str
    name: str
    score: float



class InnovationSearch:


    def __init__(self):

        self.items = []



    def index(
        self,
        item_id: str,
        item_type: str,
        name: str,
    ):

        self.items.append(
            {
                "id": item_id,
                "type": item_type,
                "name": name,
            }
        )



    def search(
        self,
        query: str,
    ) -> List[SearchResult]:

        results = []

        query = query.lower()


        for item in self.items:

            name = item["name"].lower()

            if query in name:

                results.append(
                    SearchResult(
                        item["id"],
                        item["type"],
                        item["name"],
                        1.0,
                    )
                )


        return results
