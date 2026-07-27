from dataclasses import dataclass, field
from typing import List


@dataclass
class NaturePattern:
    pattern_id: str
    organism: str
    mechanism: str
    observed_behavior: str
    transferable_principle: str
    applications: List[str] = field(default_factory=list)
