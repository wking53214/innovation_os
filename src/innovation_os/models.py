from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Problem:
    id: str
    title: str
    description: str
    created: datetime = field(default_factory=datetime.now)


@dataclass
class Question:
    id: str
    question: str
    related_problem: Optional[str] = None
    created: datetime = field(default_factory=datetime.now)


@dataclass
class Concept:
    id: str
    name: str
    description: str
    related_problem: Optional[str] = None
    created: datetime = field(default_factory=datetime.now)


@dataclass
class Decision:
    id: str
    description: str
    selected_option: Optional[str] = None
    alternatives: List[str] = field(default_factory=list)
    created: datetime = field(default_factory=datetime.now)


@dataclass
class ArtifactRecord:
    id: str
    name: str
    artifact_type: str
    location: str
    created: datetime = field(default_factory=datetime.now)


@dataclass
class Relationship:
    source_id: str
    target_id: str
    relationship_type: str