from dataclasses import dataclass
from datetime import datetime


@dataclass
class VersionRecord:

    artifact_id: str
    version: str
    created: datetime
    status: str



class VersionRegistry:


    def __init__(self):

        self.records = []


    def register(
        self,
        artifact_id: str,
        version: str,
        status: str,
    ):

        record = VersionRecord(
            artifact_id,
            version,
            datetime.utcnow(),
            status,
        )

        self.records.append(record)

        return record



    def get(
        self,
        artifact_id: str,
    ):

        return [
            item
            for item in self.records
            if item.artifact_id == artifact_id
        ]
