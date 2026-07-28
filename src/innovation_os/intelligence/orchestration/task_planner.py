from dataclasses import dataclass


@dataclass
class TaskPlanner:
    """
    Converts objectives into executable tasks.
    """

    def plan(
        self,
        objective
    ):

        return [
            {
                "task": objective,
                "status": "planned",
            }
        ]
