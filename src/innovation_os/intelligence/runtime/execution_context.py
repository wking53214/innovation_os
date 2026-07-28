from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict
import uuid


@dataclass
class ExecutionContext:
    """
    Runtime context for intelligence execution.
    """

    execution_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    started_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )

    input_data: Any = None

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    state: Dict[str, Any] = field(
        default_factory=dict
    )
