from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List



@dataclass
class DecisionRecord:

    decision_id: str

    title: str

    rationale: str

    alternatives: List[str]

    outcome: str

    created_at: datetime

    metadata: dict = field(
        default_factory=dict
    )



class DecisionTracker:


    def __init__(self):

        self.decisions: Dict[
            str,
            DecisionRecord
        ] = {}


    def record(
        self,
        decision_id: str,
        title: str,
        rationale: str,
        alternatives=None,
        outcome="",
        metadata=None,
    ):

        decision = DecisionRecord(
            decision_id=decision_id,
            title=title,
            rationale=rationale,
            alternatives=alternatives or [],
            outcome=outcome,
            created_at=datetime.now(),
            metadata=metadata or {},
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



    def all(self):

        return list(
            self.decisions.values()
        )



    def link_to_graph(
        self,
        graph,
        decision_id: str,
        item_id: str,
    ):

        decision = self.get(
            decision_id
        )


        if not decision:

            return False


        graph.add_node(
            decision_id,
            "DECISION",
            title=decision.title,
        )


        graph.connect(
            decision_id,
            item_id,
            "INFLUENCED",
        )


        return True
