from dataclasses import dataclass, field
import uuid


@dataclass
class Task:

    objective: str

    task_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    steps: list = field(
        default_factory=list
    )

    status: str = "created"



class TaskPlanner:


    def create_plan(
        self,
        objective
    ):

        task = Task(
            objective=objective
        )

        task.steps = [
            "observe",
            "analyze",
            "execute",
            "evaluate",
        ]

        return task
