from dataclasses import dataclass


@dataclass
class ExecutionResult:

    task_id: str

    output: object

    status: str



class ExecutionEngine:


    def execute(
        self,
        task,
        function=None
    ):

        output = None

        if function:

            output = function()


        task.status = "complete"

        return ExecutionResult(
            task_id=task.task_id,
            output=output,
            status=task.status
        )
