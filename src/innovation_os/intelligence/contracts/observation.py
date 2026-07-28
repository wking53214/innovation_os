from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Observation:

    source: str = ""

    subject: str = ""

    data: Any = None

    confidence: float = 0.0

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    value: Any = None
