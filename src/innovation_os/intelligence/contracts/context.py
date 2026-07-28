from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Context:
    data: Dict[str, Any] = field(default_factory=dict)
