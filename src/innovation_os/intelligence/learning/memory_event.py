from dataclasses import dataclass
from datetime import datetime


@dataclass
class MemoryEvent:
    """
    Intelligence learning memory unit.
    """

    event_type: str
    payload: dict
    timestamp: str = None


    def __post_init__(self):

        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()
