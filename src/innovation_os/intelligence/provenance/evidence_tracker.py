from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class EvidenceTracker:
    """
    Maintains evidence supporting inference.
    """

    evidence: List[Dict[str, Any]] = field(
        default_factory=list
    )


    def add(
        self,
        evidence_item
    ):

        self.evidence.append(
            evidence_item
        )

        return evidence_item


    def all(self):

        return self.evidence
