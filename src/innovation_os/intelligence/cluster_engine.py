from dataclasses import dataclass
from typing import Dict, List


@dataclass
class InnovationCluster:

    cluster_id: str
    theme: str
    members: List[str]



class IdeaClusterEngine:


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



    def cluster(
        self,
        threshold: float = 50.0,
    ) -> List[InnovationCluster]:

        clusters = []

        visited = set()

        counter = 1


        for item_id, concepts in self.items.items():

            if item_id in visited:

                continue


            members = [
                item_id
            ]


            shared_theme = set(
                concepts
            )


            for other_id, other_concepts in self.items.items():

                if other_id == item_id:

                    continue


                overlap = (
                    len(
                        shared_theme.intersection(
                            other_concepts
                        )
                    )
                    /
                    max(
                        len(shared_theme),
                        1
                    )
                ) * 100


                if overlap >= threshold:

                    members.append(
                        other_id
                    )

                    visited.add(
                        other_id
                    )


            visited.add(
                item_id
            )


            clusters.append(
                InnovationCluster(
                    f"CLUSTER-{counter:03d}",
                    ", ".join(
                        sorted(shared_theme)
                    ),
                    members,
                )
            )


            counter += 1


        return clusters
