class ToolRegistry:


    def __init__(self):

        self.tools = {}


    def register(
        self,
        name,
        handler
    ):

        self.tools[name] = handler


    def get(
        self,
        name
    ):

        return self.tools.get(name)


    def list_tools(self):

        return list(
            self.tools.keys()
        )
