from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class IntelligencePolicy:
    """
    Defines intelligence execution constraints.
    """

    name: str = "default"

    allowed_operations: list[str] = field(
        default_factory=lambda: [
            "observe",
            "infer",
            "explain",
        ]
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )


    def permits(self, operation: str):

        return operation in self.allowed_operations
