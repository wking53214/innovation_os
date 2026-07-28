from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class IntelligenceResponse:
    """
    External intelligence response contract.
    """

    success: bool

    artifact_id: str | None = None

    confidence: float | None = None

    data: Dict[str, Any] | None = None
