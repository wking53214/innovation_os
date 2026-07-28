from dataclasses import dataclass


@dataclass
class PriorityEngine:
    """
    Determines task execution priority.
    """

    def score(
        self,
        task
    ):

        return {
            "task": task,
            "priority": 1,
        }
