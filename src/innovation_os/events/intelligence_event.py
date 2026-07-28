from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict
import uuid


@dataclass
class IntelligenceEvent:

    event_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    event_type: str = "signal"

    payload: Dict[str, Any] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc
        )
    )


class EventFactory:

    def create(
        self,
        event_type: str,
        payload: Dict[str, Any],
    ) -> IntelligenceEvent:

        return IntelligenceEvent(
            event_type=event_type,
            payload=payload,
        )
