from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Inference:

    conclusion: str = ""

    reasoning: Dict[str, Any] = field(
        default_factory=dict
    )

    confidence: float = 0.0

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )
