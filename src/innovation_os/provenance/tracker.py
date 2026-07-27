from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List



@dataclass
class ProvenanceRecord:

    item_id: str

    source_type: str

    source_reference: str

    created_at: datetime

    metadata: dict = field(
        default_factory=dict
    )



class ProvenanceTracker:


    def __init__(self):

        self.records: Dict[
            str,
            List[ProvenanceRecord]
        ] = {}



    def record(
        self,
        item_id: str,
        source_type: str,
        source_reference: str,
        metadata=None,
    ):

        record = ProvenanceRecord(
            item_id=item_id,
            source_type=source_type,
            source_reference=source_reference,
            created_at=datetime.now(),
            metadata=metadata or {},
        )


        if item_id not in self.records:

            self.records[item_id] = []


        self.records[item_id].append(
            record
        )


        return record



    def history(
        self,
        item_id: str,
    ):

        return self.records.get(
            item_id,
            [],
        )



    def latest(
        self,
        item_id: str,
    ):

        history = self.history(
            item_id
        )

        if not history:

            return None


        return history[-1]
