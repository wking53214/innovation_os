from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List


@dataclass
class ProvenanceRecord:

    artifact_id: str
    source: str
    created_at: str
    metadata: Dict[str, str] = field(
        default_factory=dict
    )
    history: List[str] = field(
        default_factory=list
    )


class ProvenanceEngine:


    def __init__(self):

        self.records = {}


    def register(
        self,
        artifact_id: str,
        source: str,
        metadata=None,
    ):

        record = ProvenanceRecord(
            artifact_id=artifact_id,
            source=source,
            created_at=datetime.now(timezone.utc).isoformat(),
            metadata=metadata or {},
        )


        self.records[artifact_id] = record

        return record


    def add_history(
        self,
        artifact_id: str,
        event: str,
    ):

        record = self.records.get(
            artifact_id
        )

        if record:

            record.history.append(
                event
            )


    def get(
        self,
        artifact_id: str,
    ):

        return self.records.get(
            artifact_id
        )
