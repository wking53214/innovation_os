from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class KnowledgeRecord:

    key: str

    content: Any

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )
