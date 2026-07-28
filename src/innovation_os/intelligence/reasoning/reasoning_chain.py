from dataclasses import dataclass, field
from typing import List, Any


@dataclass
class ReasoningChain:
    """
    Ordered reasoning execution trace.
    """

    steps: List[Any] = field(
        default_factory=list
    )


    def add(self, step):

        self.steps.append(step)

        return step


    def execute(self):

        return self.steps
