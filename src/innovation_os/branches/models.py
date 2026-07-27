from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Branch:
    branch_id: str
    parent_id: str
    problem_id: str
    title: str
    description: str
    status: str
    child_branches: List[str] = field(default_factory=list)
    created: datetime = field(default_factory=datetime.now)
