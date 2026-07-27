from dataclasses import dataclass, field
from typing import List


@dataclass
class Review:
    review_id: str
    target_id: str
    strengths: List[str]
    weaknesses: List[str]
    risks: List[str]
    recommendations: List[str]
    score: float = 0.0
