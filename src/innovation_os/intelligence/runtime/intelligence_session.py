from dataclasses import dataclass, field
from typing import List, Any


@dataclass
class IntelligenceSession:
    """
    Tracks intelligence execution history.
    """

    artifacts: List[Any] = field(
        default_factory=list
    )

    events: List[Any] = field(
        default_factory=list
    )

    def add_artifact(self, artifact):
        self.artifacts.append(artifact)

    def add_event(self, event):
        self.events.append(event)
