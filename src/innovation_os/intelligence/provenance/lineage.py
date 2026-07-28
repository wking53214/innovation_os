from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class IntelligenceLineage:
    """
    Tracks intelligence origin chain.
    """

    records: List[Dict[str, Any]] = field(
        default_factory=list
    )


    def record(
        self,
        artifact_id,
        source
    ):

        item = {
            "artifact_id": artifact_id,
            "source": source,
        }

        self.records.append(
            item
        )

        return item


    def history(self):

        return self.records
