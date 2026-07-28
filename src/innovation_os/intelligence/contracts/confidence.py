from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Confidence:

    score: float = 0.0

    rationale: str = ""

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )


    def validate(self):

        return 0.0 <= self.score <= 1.0
