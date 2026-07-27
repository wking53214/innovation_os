from dataclasses import dataclass
from typing import List


@dataclass
class SimilarityResult:

    source_id: str
    target_id: str
    score: float
    shared_terms: List[str]


class SimilarityEngine:


    def __init__(self):

        self.items = {}


    def add(
        self,
        item_id: str,
        terms: List[str],
    ):

        self.items[item_id] = [
            term.lower()
            for term in terms
        ]


    def compare(
        self,
        source_id: str,
        terms: List[str],
    ):

        results = []

        source_terms = [
            term.lower()
            for term in terms
        ]


        for target_id, target_terms in self.items.items():

            if target_id == source_id:
                continue


            shared = [
                term
                for term in source_terms
                if term in target_terms
            ]


            if shared:

                score = (
                    len(shared)
                    /
                    max(
                        len(source_terms),
                        len(target_terms),
                    )
                ) * 100


                results.append(
                    SimilarityResult(
                        source_id=source_id,
                        target_id=target_id,
                        score=round(
                            score,
                            2,
                        ),
                        shared_terms=shared,
                    )
                )


        return results
