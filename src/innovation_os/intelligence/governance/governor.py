from dataclasses import dataclass, field

from .policy import IntelligencePolicy
from .guardrails import IntelligenceGuardrails
from .approval import ApprovalDecision


@dataclass
class IntelligenceGovernor:
    """
    Governance control point.
    """

    policy: IntelligencePolicy = field(
        default_factory=IntelligencePolicy
    )

    guardrails: IntelligenceGuardrails = field(
        default_factory=IntelligenceGuardrails
    )


    def authorize(
        self,
        operation,
        confidence=1.0
    ):

        if not self.policy.permits(
            operation
        ):
            return ApprovalDecision(
                False,
                "operation_not_allowed"
            )


        if not self.guardrails.validate(
            confidence
        ):
            return ApprovalDecision(
                False,
                "confidence_invalid"
            )


        return ApprovalDecision(
            True,
            "approved"
        )
