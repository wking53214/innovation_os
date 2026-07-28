from dataclasses import dataclass


@dataclass
class TrustDecision:

    component: str = ""

    trusted: bool = False

    score: float = 0.0
