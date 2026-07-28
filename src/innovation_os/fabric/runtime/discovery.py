class FabricDiscovery:


    def __init__(
        self,
        registry
    ):

        self.registry = registry



    def find_capability(
        self,
        capability
    ):

        return [

            node

            for node
            in self.registry.list_nodes()

            if capability
            in node.capabilities

        ]
