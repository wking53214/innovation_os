from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict
import uuid


@dataclass
class Evidence:
    evidence_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    source: str = ""
    evidence_type: str = ""
    content: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
