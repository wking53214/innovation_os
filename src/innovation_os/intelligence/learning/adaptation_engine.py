from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class AdaptationEngine:
    """
    Converts feedback into intelligence adjustments.
    """

    adjustments: Dict[str, Any] = field(
        default_factory=dict
    )


    def adapt(
        self,
        feedback
    ):

        self.adjustments[
            "last_feedback"
        ] = feedback

        return self.adjustments
