from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class ScannedArtifact:
    artifact_id: str
    file_name: str
    path: str
    language: str
    size_bytes: int
    detected_terms: List[str] = field(default_factory=list)
    idea_id: str = ""
    scanned_at: datetime = field(default_factory=datetime.now)
