from dataclasses import dataclass
from typing import Any


@dataclass
class IntelligenceResponse:
    artifact: Any
    confidence: float
    status: str = "complete"
