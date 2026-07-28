from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Hypothesis:

    statement: str = ""

    supporting_data: Dict[str, Any] = field(
        default_factory=dict
    )

    confidence: float = 0.0

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )
