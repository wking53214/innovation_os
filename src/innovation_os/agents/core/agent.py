from dataclasses import dataclass, field
import uuid
from datetime import datetime, timezone


@dataclass
class Agent:

    name: str

    capability: str

    agent_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )

    state: dict = field(
        default_factory=dict
    )


    def execute(
        self,
        task
    ):

        return {
            "agent": self.name,
            "task": task,
            "capability": self.capability,
            "status": "complete"
        }
