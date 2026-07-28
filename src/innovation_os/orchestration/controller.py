from innovation_os.planning.task import TaskPlanner
from innovation_os.planning.decomposer import TaskDecomposer
from innovation_os.execution.executor import ExecutionEngine


class OrchestrationController:


    def __init__(
        self
    ):

        self.planner = TaskPlanner()
        self.decomposer = TaskDecomposer()
        self.executor = ExecutionEngine()


    def run(
        self,
        objective
    ):

        task = self.planner.create_plan(
            objective
        )

        subtasks = self.decomposer.decompose(
            task
        )

        result = self.executor.execute(
            task
        )

        return {
            "task": task,
            "subtasks": subtasks,
            "result": result,
        }
