from dataclasses import dataclass, field
from typing import List



@dataclass
class ExtractedIdea:

    idea_id: str
    title: str
    source: str
    keywords: List[str] = field(
        default_factory=list
    )



class IdeaExtractor:


    KEYWORDS = {
        "sentinel": "Sentinel OS",
        "gsa": "Governed Secure AI Gateway",
        "synapsis": "Synapsis",
        "governance": "AI Governance",
        "graph": "Knowledge Graph",
    }



    def extract(
        self,
        artifact,
    ):

        content = getattr(
            artifact,
            "content",
            "",
        ).lower()


        ideas = []


        counter = 1


        for keyword, title in self.KEYWORDS.items():

            if keyword in content:

                ideas.append(
                    ExtractedIdea(
                        idea_id=f"IDEA-{counter:05d}",
                        title=title,
                        source=artifact.path,
                        keywords=[
                            keyword
                        ],
                    )
                )

                counter += 1


        return ideas



    def extract_many(
        self,
        artifacts,
    ):

        results = []


        for artifact in artifacts:

            results.extend(
                self.extract(
                    artifact
                )
            )


        return results
