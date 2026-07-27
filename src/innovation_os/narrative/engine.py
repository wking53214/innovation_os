from dataclasses import dataclass
from typing import List


@dataclass
class Narrative:

    title: str
    summary: str
    artifacts: List[str]



class ExecutiveNarrativeEngine:


    def generate(
        self,
        project_name: str,
        description: str,
        artifacts: List[str],
    ):

        summary = (
            f"{project_name} represents "
            f"{description}. "
            f"The system includes "
            f"{len(artifacts)} major components "
            f"that contribute to the overall capability."
        )


        return Narrative(
            title=project_name,
            summary=summary,
            artifacts=artifacts,
        )
