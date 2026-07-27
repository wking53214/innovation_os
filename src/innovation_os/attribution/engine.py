from dataclasses import dataclass
from typing import List


@dataclass
class Attribution:

    artifact_id: str
    project_id: str
    confidence: float
    matched_terms: List[str]



class CodeAttributionEngine:


    def __init__(self):

        self.projects = {}



    def register_project(
        self,
        project_id: str,
        keywords: List[str],
    ):

        self.projects[project_id] = [
            word.lower()
            for word in keywords
        ]



    def attribute(
        self,
        artifact_id: str,
        content: str,
    ):

        matches = []

        normalized = content.lower()


        for project_id, keywords in self.projects.items():

            found = [
                keyword
                for keyword in keywords
                if keyword in normalized
            ]

            if found:

                confidence = (
                    len(found)
                    /
                    len(keywords)
                ) * 100


                matches.append(
                    Attribution(
                        artifact_id,
                        project_id,
                        round(confidence, 2),
                        found,
                    )
                )


        return matches
