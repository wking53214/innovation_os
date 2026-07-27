from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class CodeArtifact:
    artifact_id: str
    file_name: str
    path: str
    idea_id: str
    problem_id: str
    language: str
    purpose: str
    tags: List[str] = field(default_factory=list)
    created: datetime = field(default_factory=datetime.now)
