from dataclasses import dataclass
from typing import Dict, List


@dataclass
class PatternResult:

    source_id: str
    target_id: str
    shared_terms: List[str]
    score: float



class PatternDetectionEngine:


    def __init__(self):

        self.items: Dict[str, List[str]] = {}



    def add(
        self,
        item_id: str,
        concepts: List[str],
    ):

        self.items[item_id] = [
            concept.lower()
            for concept in concepts
        ]



    def detect(
        self,
        item_id: str,
    ) -> List[PatternResult]:

        results = []


        if item_id not in self.items:

            return results


        source_terms = set(
            self.items[item_id]
        )


        for target_id, target_terms in self.items.items():

            if target_id == item_id:
                continue


            shared = sorted(
                source_terms.intersection(
                    target_terms
                )
            )


            if shared:

                score = round(
                    (
                        len(shared)
                        /
                        max(
                            len(source_terms),
                            1
                        )
                    )
                    * 100,
                    2,
                )


                results.append(
                    PatternResult(
                        item_id,
                        target_id,
                        shared,
                        score,
                    )
                )


        return results
