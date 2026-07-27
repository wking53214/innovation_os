from dataclasses import dataclass, field
from typing import List


@dataclass
class DecisionAlternative:
    alternative_id: str
    name: str
    predicted_outcome: str
    risks: List[str]
    benefits: List[str]
    assumptions: List[str]
    confidence: float
