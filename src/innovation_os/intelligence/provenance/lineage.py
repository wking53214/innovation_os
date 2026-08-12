"""
Intelligence-side view onto the canonical provenance store.

Formerly a second, disconnected provenance store holding its own
artifact_id/source dicts. It is now a thin facade over ProvenanceEngine, so
intelligence-side callers keep their import and method names while writing
into the one store.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from innovation_os.provenance import (
    ProvenanceEngine,
    ProvenanceStatus,
)


@dataclass
class IntelligenceLineage:
    """
    Tracks intelligence origin chain.
    """

    engine: ProvenanceEngine = field(
        default_factory=ProvenanceEngine
    )

    def record(
        self,
        artifact_id,
        source,
        status: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """
        Record an artifact's origin.

        Runtime intelligence paths frequently cannot establish origin.
        Omitting `status` records PROVENANCE_UNCERTAIN, which is Article II's
        label for exactly that condition. This is not a guess and must not be
        read as one; it is the record declining to assert what it cannot show.
        """

        resolved = (
            ProvenanceStatus.PROVENANCE_UNCERTAIN
            if status is None
            else status
        )

        record = self.engine.register(
            artifact_id,
            resolved,
            source=source,
        )

        return {
            "artifact_id": record.artifact_id,
            "source": record.source,
            "status": record.status,
        }

    def history(self) -> List[Dict[str, Any]]:

        return [
            {
                "artifact_id": r.artifact_id,
                "source": r.source,
                "status": r.status,
            }
            for r in self.engine.records.values()
        ]
