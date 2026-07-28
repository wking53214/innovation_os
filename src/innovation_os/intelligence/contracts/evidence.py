from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Evidence:

    source: str = ""

    evidence_type: str = ""

    content: Any = None

    confidence: float = 0.0

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )
