from dataclasses import dataclass
from typing import List


@dataclass
class ResearchAnswer:

    query: str
    matches: List[str]
    confidence: float


class ResearchAssistant:


    def __init__(self):

        self.knowledge = []


    def add_knowledge(
        self,
        item: str,
    ):

        self.knowledge.append(
            item
        )


    def answer(
        self,
        query: str,
    ):

        query_terms = set(
            query.lower().split()
        )

        matches = []

        for item in self.knowledge:

            item_terms = set(
                item.lower().split()
            )

            if query_terms.intersection(
                item_terms
            ):
                matches.append(
                    item
                )


        confidence = 0

        if matches:

            confidence = min(
                len(matches) * 25,
                100,
            )


        return ResearchAnswer(
            query=query,
            matches=matches,
            confidence=confidence,
        )
