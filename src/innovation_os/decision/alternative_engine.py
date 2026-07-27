from typing import List, Optional

from src.innovation_os.decision.alternatives import (
    DecisionAlternative,
)


class AlternativeEngine:

    def __init__(self):
        self.alternatives: List[DecisionAlternative] = []

    def create_alternative(
        self,
        alternative_id: str,
        name: str,
        predicted_outcome: str,
        risks: List[str],
        benefits: List[str],
        assumptions: List[str],
        confidence: float,
    ) -> DecisionAlternative:

        alternative = DecisionAlternative(
            alternative_id=alternative_id,
            name=name,
            predicted_outcome=predicted_outcome,
            risks=risks,
            benefits=benefits,
            assumptions=assumptions,
            confidence=confidence,
        )

        self.alternatives.append(alternative)

        return alternative

    def get_alternative(
        self,
        alternative_id: str,
    ) -> Optional[DecisionAlternative]:

        for alternative in self.alternatives:
            if alternative.alternative_id == alternative_id:
                return alternative

        return None

    def compare(
        self,
        alternative_ids: List[str],
    ) -> List[DecisionAlternative]:

        return [
            alternative
            for alternative in self.alternatives
            if alternative.alternative_id in alternative_ids
        ]
