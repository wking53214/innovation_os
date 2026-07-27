from dataclasses import dataclass, field
from typing import List


@dataclass
class DecisionRecord:

    decision_id: str
    problem: str
    options: List[str]
    selected: str
    reasoning: str
    outcome: str = ""


class DecisionIntelligenceEngine:


    def __init__(self):

        self.decisions = {}


    def create(
        self,
        decision_id: str,
        problem: str,
        options: List[str],
        selected: str,
        reasoning: str,
        outcome: str = "",
    ):

        decision = DecisionRecord(
            decision_id=decision_id,
            problem=problem,
            options=options,
            selected=selected,
            reasoning=reasoning,
            outcome=outcome,
        )


        self.decisions[decision_id] = decision

        return decision


    def get(
        self,
        decision_id: str,
    ):

        return self.decisions.get(
            decision_id
        )


    def replay(
        self,
        decision_id: str,
    ):

        decision = self.get(
            decision_id
        )

        if not decision:
            return None


        return {
            "problem": decision.problem,
            "options": decision.options,
            "selected": decision.selected,
            "reasoning": decision.reasoning,
            "outcome": decision.outcome,
        }
