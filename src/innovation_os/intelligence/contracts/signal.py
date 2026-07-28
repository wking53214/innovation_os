from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Signal:

    source: str = ""

    signal_type: str = ""

    payload: Any = None

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    value: Any = None
