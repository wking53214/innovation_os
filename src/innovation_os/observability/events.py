from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


@dataclass
class IntelligenceEvent:

    event_type: str
    payload: Dict[str, Any]

    timestamp: datetime = datetime.utcnow()
