from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ComplianceTrace:

    records: list = field(
        default_factory=list
    )


    def record(
        self,
        action,
        status
    ):

        entry = {
            "action": action,
            "status": status,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self.records.append(
            entry
        )

        return entry


    def latest(self):

        if not self.records:
            return None

        return self.records[-1]
