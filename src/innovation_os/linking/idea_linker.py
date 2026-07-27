from dataclasses import dataclass, field
from typing import Dict, List



@dataclass
class IdeaLink:

    idea_id: str
    artifact_ids: List[str] = field(
        default_factory=list
    )



class IdeaLinker:


    def __init__(self):

        self.links: Dict[str, IdeaLink] = {}



    def link(
        self,
        idea_id: str,
        artifact_id: str,
    ):

        if idea_id not in self.links:

            self.links[idea_id] = IdeaLink(
                idea_id=idea_id
            )


        self.links[
            idea_id
        ].artifact_ids.append(
            artifact_id
        )


        return self.links[
            idea_id
        ]



    def artifacts_for(
        self,
        idea_id: str,
    ):

        if idea_id not in self.links:

            return []


        return self.links[
            idea_id
        ].artifact_ids



    def ideas_for_artifact(
        self,
        artifact_id: str,
    ):

        results = []


        for idea in self.links.values():

            if artifact_id in idea.artifact_ids:

                results.append(
                    idea.idea_id
                )


        return results
