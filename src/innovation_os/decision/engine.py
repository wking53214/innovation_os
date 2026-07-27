from typing import List, Optional

from src.innovation_os.decision.models import Decision


class DecisionEngine:
    def __init__(self):
        self.decisions: List[Decision] = []

    def create_decision(
        self,
        decision_id: str,
        problem_id: str,
        context: str,
        options: List[str],
        selected_option: str,
        rejected_options: List[str],
        assumptions: List[str],
        confidence: float,
        approval: str,
        alternatives: List[str] = None,
    ) -> Decision:

        decision = Decision(
            decision_id=decision_id,
            problem_id=problem_id,
            context=context,
            options=options,
            selected_option=selected_option,
            rejected_options=rejected_options,
            assumptions=assumptions,
            confidence=confidence,
            approval=approval,
            alternatives=alternatives or [],
        )

        self.decisions.append(decision)

        return decision

    def get_decision(
        self,
        decision_id: str,
    ) -> Optional[Decision]:

        for decision in self.decisions:
            if decision.decision_id == decision_id:
                return decision

        return None

    def get_decisions_for_problem(
        self,
        problem_id: str,
    ) -> List[Decision]:

        return [
            decision
            for decision in self.decisions
            if decision.problem_id == problem_id
        ]
