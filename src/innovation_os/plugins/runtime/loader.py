class PluginLoader:


    def __init__(
        self,
        registry
    ):

        self.registry = registry


    def discover(
        self,
        plugins
    ):

        loaded = []

        for plugin, metadata in plugins:

            self.registry.register(
                plugin,
                metadata
            )

            loaded.append(
                metadata.name
            )

        return loaded
