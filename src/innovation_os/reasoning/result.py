from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ReasoningResult:

    subject: str = ""

    summary: str = ""

    conclusion: Any = None

    evidence: Dict[str, Any] = field(
        default_factory=dict
    )

    confidence: float = 0.0

    reasoning_path: List[str] = field(
        default_factory=list
    )

    supporting_artifacts: List[Any] = field(
        default_factory=list
    )
