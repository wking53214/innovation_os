from dataclasses import dataclass
from typing import List


@dataclass
class MatchResult:
    artifact_id: str
    idea_id: str
    confidence: float
    matched_terms: List[str]
