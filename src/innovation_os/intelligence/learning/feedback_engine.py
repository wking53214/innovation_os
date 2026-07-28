from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class FeedbackEngine:
    """
    Captures intelligence performance feedback.
    """

    feedback: List[Dict[str, Any]] = field(
        default_factory=list
    )


    def record(
        self,
        artifact_id,
        outcome,
        score
    ):

        item = {
            "artifact_id": artifact_id,
            "outcome": outcome,
            "score": score,
        }

        self.feedback.append(
            item
        )

        return item


    def history(self):

        return self.feedback
