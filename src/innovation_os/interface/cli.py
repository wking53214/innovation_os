from dataclasses import dataclass
from typing import List


@dataclass
class InterfaceResponse:

    title: str
    sections: List[str]



class InnovationInterface:


    def status(
        self,
        artifacts: int,
        projects: int,
        ideas: int,
    ):

        return InterfaceResponse(
            "Innovation OS Status",
            [
                f"Artifacts: {artifacts}",
                f"Projects: {projects}",
                f"Ideas: {ideas}",
            ],
        )


    def summarize(
        self,
        title: str,
        items: List[str],
    ):

        return InterfaceResponse(
            title,
            items,
        )
