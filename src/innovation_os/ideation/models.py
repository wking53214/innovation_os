from dataclasses import dataclass, field
from typing import List


@dataclass
class Idea:
    idea_id: str
    problem_id: str
    title: str
    description: str
    sources: List[str]
    confidence: float
    tags: List[str] = field(default_factory=list)
