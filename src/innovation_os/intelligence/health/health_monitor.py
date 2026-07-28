from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class IntelligenceHealthMonitor:
    """
    Intelligence subsystem health boundary.
    """

    checks: Dict[str, Any] = field(
        default_factory=dict
    )


    def register(
        self,
        component,
        status
    ):

        self.checks[component] = status

        return status


    def healthy(self):

        return all(
            self.checks.values()
        )
