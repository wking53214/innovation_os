from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ExecutionTrace:
    """
    Records intelligence execution history.
    """

    entries: list = field(
        default_factory=list
    )


    def record(
        self,
        stage,
        data
    ):

        entry = {
            "stage": stage,
            "data": data,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self.entries.append(
            entry
        )

        return entry


    def count(self):

        return len(
            self.entries
        )
