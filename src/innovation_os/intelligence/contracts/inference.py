from dataclasses import dataclass, field
from typing import Any, Dict
import uuid


@dataclass
class Inference:
    inference_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    conclusion: str = ""
    reasoning: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.0
