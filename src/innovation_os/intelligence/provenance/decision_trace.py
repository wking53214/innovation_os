from dataclasses import dataclass, field
from typing import List, Any


@dataclass
class DecisionTrace:
    """
    Explainable reasoning trace.
    """

    steps: List[Any] = field(
        default_factory=list
    )


    def add(self, step):

        self.steps.append(
            step
        )


    def replay(self):

        return self.steps
