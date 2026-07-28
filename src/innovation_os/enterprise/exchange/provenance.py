from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class ProvenanceRecord:


    source_system: str

    request_id: str

    created_at: datetime = (
        datetime.now(timezone.utc)
    )
