class ConnectorRegistry:


    def __init__(self):

        self.connectors = {}


    def register(
        self,
        connector,
        metadata
    ):

        self.connectors[
            metadata.name
        ] = {
            "connector": connector,
            "metadata": metadata,
        }

        return metadata


    def get(
        self,
        name
    ):

        item = self.connectors.get(
            name
        )

        if item:

            return item["connector"]

        return None


    def list(self):

        return [
            item["metadata"]
            for item in self.connectors.values()
        ]
