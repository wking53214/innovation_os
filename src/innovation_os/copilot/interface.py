from dataclasses import dataclass
from typing import List


@dataclass
class CopilotResponse:

    question: str
    findings: List[str]
    actions: List[str]


class InnovationCopilot:


    def __init__(self):

        self.knowledge = []


    def add(
        self,
        item: str,
    ):

        self.knowledge.append(
            item
        )


    def ask(
        self,
        question: str,
    ):

        terms = set(
            question.lower().split()
        )

        findings = []

        for item in self.knowledge:

            item_terms = set(
                item.lower().split()
            )

            if terms.intersection(
                item_terms
            ):

                findings.append(
                    item
                )


        actions = []

        if findings:

            actions.append(
                "Review related innovation artifacts"
            )


        return CopilotResponse(
            question,
            findings,
            actions,
        )
