from __future__ import annotations

from typing import Any, Dict

from innovation_os.events import EventFactory


class EventIngestionPipeline:

    def __init__(self):
        self.factory = EventFactory()

    def ingest(
        self,
        payload: Dict[str, Any],
    ):

        return self.factory.create(
            event_type=payload.get(
                "source",
                "unknown",
            ),
            payload=payload,
        )
