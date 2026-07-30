from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List



@dataclass
class ProvenanceRecord:

    artifact_id: str
    source: str
    created: datetime
    relationships: List[str] = field(
        default_factory=list
    )



class ProvenanceEngine:


    def __init__(self):

        self.records: Dict[
            str,
            ProvenanceRecord
        ] = {}



    def register(
        self,
        artifact_id: str,
        source: str,
    ):

        record = ProvenanceRecord(
            artifact_id=artifact_id,
            source=source,
            created=datetime.now(timezone.utc),
        )


        self.records[
            artifact_id
        ] = record


        return record



    def link(
        self,
        artifact_id: str,
        relationship: str,
    ):

        record = self.records.get(
            artifact_id
        )


        if record:

            record.relationships.append(
                relationship
            )


        return record



    def get(
        self,
        artifact_id: str,
    ):

        return self.records.get(
            artifact_id
        )
