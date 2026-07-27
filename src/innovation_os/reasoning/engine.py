from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Insight:

    subject: str
    summary: str
    supporting_artifacts: List[str]



class ReasoningEngine:


    def __init__(self):

        self.context: Dict[str, List[str]] = {}


    def add_context(
        self,
        subject: str,
        artifacts: List[str],
    ):

        self.context[subject] = artifacts



    def analyze(
        self,
        subject: str,
    ):

        artifacts = self.context.get(
            subject,
            [],
        )


        if not artifacts:

            return Insight(
                subject,
                "No innovation context found.",
                [],
            )


        summary = (
            f"{subject} is connected to "
            f"{len(artifacts)} innovation artifacts."
        )


        return Insight(
            subject,
            summary,
            artifacts,
        )
