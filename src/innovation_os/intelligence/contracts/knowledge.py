from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Knowledge:
    value: Any = None
    metadata: Dict[str, Any] = field(default_factory=dict)
