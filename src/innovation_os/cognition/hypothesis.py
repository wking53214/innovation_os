from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class Hypothesis:

    statement: str

    confidence: float = 0.5

    evidence: list = field(
        default_factory=list
    )

    hypothesis_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )


class HypothesisEngine:

    def __init__(self):

        self.hypotheses = []


    def create(
        self,
        statement,
        confidence=0.5,
        evidence=None
    ):

        hypothesis = Hypothesis(
            statement=statement,
            confidence=confidence,
            evidence=evidence or []
        )

        self.hypotheses.append(
            hypothesis
        )

        return hypothesis


    def all(self):

        return self.hypotheses
