from dataclasses import dataclass
from typing import Dict, List


@dataclass
class PortfolioItem:

    artifact_id: str
    name: str
    category: str
    priority: str
    status: str


class InnovationPortfolioEngine:


    def __init__(self):

        self.items: Dict[str, PortfolioItem] = {}


    def add(
        self,
        artifact_id: str,
        name: str,
        category: str,
        priority: str,
        status: str,
    ):

        item = PortfolioItem(
            artifact_id,
            name,
            category,
            priority,
            status,
        )

        self.items[artifact_id] = item

        return item


    def get(
        self,
        artifact_id: str,
    ):

        return self.items.get(
            artifact_id
        )


    def list_active(self) -> List[PortfolioItem]:

        return [
            item
            for item in self.items.values()
            if item.status != "ARCHIVED"
        ]


    def by_priority(
        self,
        priority: str,
    ):

        return [
            item
            for item in self.items.values()
            if item.priority == priority
        ]
