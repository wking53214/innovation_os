from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class IntelligenceRequest:
    input: Any
    context: Optional[Dict[str, Any]] = None
    objective: Optional[str] = None
