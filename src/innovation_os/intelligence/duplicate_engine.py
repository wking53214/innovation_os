from dataclasses import dataclass
from typing import Dict, List


@dataclass
class DuplicateMatch:

    source_id: str
    match_id: str
    similarity: float
    shared_terms: List[str]



class DuplicateConceptEngine:


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



    def compare(
        self,
        threshold: float = 50.0,
    ) -> List[DuplicateMatch]:

        results = []

        ids = list(
            self.items.keys()
        )


        for index, source_id in enumerate(ids):

            for match_id in ids[index + 1:]:

                source_terms = set(
                    self.items[source_id]
                )

                match_terms = set(
                    self.items[match_id]
                )


                shared = sorted(
                    source_terms.intersection(
                        match_terms
                    )
                )


                if not shared:

                    continue


                similarity = round(
                    (
                        len(shared)
                        /
                        max(
                            len(
                                source_terms.union(
                                    match_terms
                                )
                            ),
                            1,
                        )
                    )
                    * 100,
                    2,
                )


                if similarity >= threshold:

                    results.append(
                        DuplicateMatch(
                            source_id,
                            match_id,
                            similarity,
                            shared,
                        )
                    )


        return results
