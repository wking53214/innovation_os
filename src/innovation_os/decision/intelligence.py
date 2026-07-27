from dataclasses import dataclass
from typing import List, Optional



@dataclass
class DecisionRecord:

    decision_id: str
    choice: str
    rationale: str
    alternatives: List[str]
    outcome: Optional[str] = None



class DecisionIntelligenceEngine:


    def __init__(self):

        self.decisions = {}



    def record(
        self,
        decision_id: str,
        choice: str,
        rationale: str,
        alternatives: List[str],
        outcome: Optional[str] = None,
    ):

        decision = DecisionRecord(
            decision_id,
            choice,
            rationale,
            alternatives,
            outcome,
        )


        self.decisions[
            decision_id
        ] = decision


        return decision



    def get(
        self,
        decision_id: str,
    ):

        return self.decisions.get(
            decision_id
        )



    def search(
        self,
        term: str,
    ):

        term = term.lower()


        return [
            decision
            for decision in self.decisions.values()
            if (
                term in decision.choice.lower()
                or
                term in decision.rationale.lower()
            )
        ]
