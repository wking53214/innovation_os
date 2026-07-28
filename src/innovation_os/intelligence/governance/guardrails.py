from dataclasses import dataclass


@dataclass
class IntelligenceGuardrails:
    """
    Safety boundary for intelligence execution.
    """

    max_confidence_threshold: float = 1.0


    def validate(self, confidence):

        return (
            0 <= confidence <=
            self.max_confidence_threshold
        )
