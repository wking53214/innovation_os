from dataclasses import dataclass, field
from datetime import datetime


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
            "timestamp": datetime.utcnow().isoformat(),
        }

        self.entries.append(
            entry
        )

        return entry


    def count(self):

        return len(
            self.entries
        )
