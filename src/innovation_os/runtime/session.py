from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class IntelligenceSession:
    session_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )

    events: list = field(default_factory=list)

    artifacts: list = field(default_factory=list)

    def record_event(self, event):
        self.events.append(event)

    def record_artifact(self, artifact):
        self.artifacts.append(artifact)

    def summary(self):
        return {
            "session_id": self.session_id,
            "events": len(self.events),
            "artifacts": len(self.artifacts),
        }
