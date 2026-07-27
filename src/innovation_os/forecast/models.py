from dataclasses import dataclass, field
from typing import List


@dataclass
class Scenario:
    scenario_id: str
    solution_id: str
    name: str
    outcome: str
    impacts: List[str]
    probability: float
    risks: List[str] = field(default_factory=list)
