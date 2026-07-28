from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class DecisionResult:

    decision_id: str = ""

    problem_id: str = ""

    context: str = ""

    options: List[Any] = field(
        default_factory=list
    )

    selected_option: Any = None

    rejected_options: List[Any] = field(
        default_factory=list
    )

    assumptions: List[Any] = field(
        default_factory=list
    )

    confidence: float = 0.0

    approval: str = ""

    decision: Any = None

    rationale: str = ""
