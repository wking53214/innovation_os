from dataclasses import dataclass
from typing import List


@dataclass
class DecisionReplay:
    decision_id: str
    original_choice: str
    original_assumptions: List[str]
    new_information: List[str]
    reconsidered_options: List[str]
    conclusion: str
