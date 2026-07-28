from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class IntelligenceRequest:
    """
    External intelligence request contract.
    """

    payload: Any

    source: str = "api"

    metadata: Dict[str, Any] | None = None
