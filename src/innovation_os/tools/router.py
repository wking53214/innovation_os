class ToolRouter:


    def __init__(
        self,
        registry
    ):

        self.registry = registry


    def route(
        self,
        request
    ):

        tool = self.registry.get(
            request
        )

        return tool
