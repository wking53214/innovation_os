from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class ContinuityState:
    id: str
    title: str
    current_problem: str
    active_concepts: List[str]
    active_pins: List[str]
    next_action: str
    created: datetime = field(default_factory=datetime.now)


class ContinuityEngine:
    def __init__(self):
        self.states = []

    def create_state(
        self,
        state_id: str,
        title: str,
        current_problem: str,
        active_concepts: List[str],
        active_pins: List[str],
        next_action: str,
    ):
        state = ContinuityState(
            id=state_id,
            title=title,
            current_problem=current_problem,
            active_concepts=active_concepts,
            active_pins=active_pins,
            next_action=next_action,
        )

        self.states.append(state)

        return state

    def restore_state(self, state_id: str):
        for state in self.states:
            if state.id == state_id:
                return state

        return None