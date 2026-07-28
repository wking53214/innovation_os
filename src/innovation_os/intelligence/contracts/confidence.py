from dataclasses import dataclass


@dataclass
class Confidence:
    score: float = 0.0
    rationale: str = ""

    def validate(self):
        return 0.0 <= self.score <= 1.0
