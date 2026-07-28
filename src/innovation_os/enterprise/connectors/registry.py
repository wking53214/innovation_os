class ConnectorRegistry:


    def __init__(
        self
    ):

        self.connectors = {}



    def register(
        self,
        connector
    ):

        self.connectors[
            connector.identity.connector_id
        ] = connector


        return connector



    def get(
        self,
        connector_id
    ):

        return self.connectors.get(
            connector_id
        )



    def list(
        self
    ):

        return list(
            self.connectors.values()
        )
