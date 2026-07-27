from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Solution:
    solution_id: str
    problem_id: str
    idea_id: str
    title: str
    description: str
    supporting_artifacts: List[str]
    risks: List[str]
    status: str = "PROPOSED"
    created: datetime = field(default_factory=datetime.now)
