from dataclasses import dataclass


@dataclass
class ApprovalDecision:
    """
    Governance approval result.
    """

    approved: bool

    reason: str = ""
