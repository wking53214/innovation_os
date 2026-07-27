from dataclasses import dataclass
from typing import List


@dataclass
class Opportunity:

    source_id: str
    target_id: str
    opportunity_type: str
    shared_terms: List[str]
    score: float



class OpportunityDetectionEngine:


    def __init__(self):

        self.items = {}


    def add(
        self,
        artifact_id: str,
        terms: List[str],
    ):

        self.items[artifact_id] = [
            term.lower()
            for term in terms
        ]


    def discover(
        self,
        artifact_id: str,
        terms: List[str],
    ):

        results = []

        source_terms = {
            term.lower()
            for term in terms
        }


        for target_id, target_terms in self.items.items():

            if target_id == artifact_id:
                continue


            shared = list(
                source_terms.intersection(
                    target_terms
                )
            )


            if shared:

                score = (
                    len(shared)
                    /
                    len(source_terms)
                ) * 100


                results.append(
                    Opportunity(
                        artifact_id,
                        target_id,
                        "RELATED_ASSET",
                        shared,
                        round(score, 2),
                    )
                )


        return results
