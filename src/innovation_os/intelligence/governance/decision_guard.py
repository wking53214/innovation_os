from dataclasses import dataclass


@dataclass
class DecisionGuard:
    """
    Validates intelligence decisions before execution.
    """

    minimum_confidence: float = 0.5


    def approve(
        self,
        confidence: float
    ) -> bool:

        return confidence >= self.minimum_confidence
