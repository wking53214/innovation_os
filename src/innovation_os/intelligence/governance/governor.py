from dataclasses import dataclass


@dataclass
class IntelligenceGovernor:
    """
    Compatibility governance coordinator.

    Coordinates policy, access, and decision controls.
    """

    policy: object = None
    access_control: object = None
    decision_guard: object = None
    compliance_trace: object = None


    def evaluate(
        self,
        operation: str,
        confidence: float = 1.0
    ):

        if self.policy:
            if not self.policy.allows(operation):
                self._trace(
                    operation,
                    "blocked"
                )
                return False

        if self.decision_guard:
            if not self.decision_guard.approve(confidence):
                self._trace(
                    operation,
                    "rejected"
                )
                return False

        self._trace(
            operation,
            "approved"
        )

        return True


    def _trace(
        self,
        operation,
        status
    ):

        if self.compliance_trace:
            self.compliance_trace.record(
                operation,
                status
            )
