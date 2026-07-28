class AgentCoordinator:


    def __init__(
        self,
        registry
    ):

        self.registry = registry



    def assign(
        self,
        task
    ):


        candidates = []

        for capability in (
            task.required_capabilities
        ):

            candidates.extend(
                self.registry.find_capability(
                    capability
                )
            )



        if not candidates:

            return False



        selected = candidates[0]


        task.assigned_agent = (
            selected.agent_id
        )


        task.status = (
            "assigned"
        )


        return selected
