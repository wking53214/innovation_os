from innovation_os.plugins.contracts import (
    PluginMetadata,
)


class PluginRegistry:


    def __init__(self):

        self.plugins = {}


    def register(
        self,
        plugin,
        metadata: PluginMetadata
    ):

        self.plugins[
            metadata.name
        ] = {
            "plugin": plugin,
            "metadata": metadata,
        }

        return metadata


    def get(
        self,
        name
    ):

        entry = self.plugins.get(
            name
        )

        if entry:

            return entry["plugin"]

        return None


    def list(
        self
    ):

        return [
            item["metadata"]
            for item in self.plugins.values()
        ]
