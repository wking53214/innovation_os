from dataclasses import dataclass


@dataclass
class TaskRouter:
    """
    Routes intelligence tasks to capabilities.
    """

    registry: object


    def route(
        self,
        task_type,
        payload
    ):

        capability = self.registry.get(
            task_type
        )

        if capability is None:
            raise ValueError(
                f"Unknown capability: {task_type}"
            )

        return capability(
            payload
        )
