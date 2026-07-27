from dataclasses import dataclass, field
from typing import Any, List



@dataclass
class InnovationSnapshot:

    item_id: str

    name: str

    status: str = "UNKNOWN"

    artifacts: List[Any] = field(
        default_factory=list
    )

    history: List[Any] = field(
        default_factory=list
    )

    decisions: List[Any] = field(
        default_factory=list
    )

    provenance: List[Any] = field(
        default_factory=list
    )



class DashboardBuilder:


    def build(
        self,
        item_id: str,
        name: str,
        memory_result,
    ):

        return InnovationSnapshot(
            item_id=item_id,
            name=name,
            status="ACTIVE",
            artifacts=memory_result.artifacts,
            history=memory_result.history,
            decisions=memory_result.decisions,
            provenance=memory_result.provenance,
        )
