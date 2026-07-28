class TaskDecomposer:


    def decompose(
        self,
        task
    ):

        return [
            {
                "parent": task.task_id,
                "step": step
            }
            for step in task.steps
        ]
