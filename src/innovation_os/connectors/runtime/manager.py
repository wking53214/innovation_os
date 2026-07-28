from innovation_os.connectors.contracts import (
    ConnectorEvent,
)


class ConnectorManager:


    def __init__(
        self,
        registry
    ):

        self.registry = registry


    def collect(
        self,
        connector_name
    ):

        connector = self.registry.get(
            connector_name
        )

        if connector is None:

            return []


        results = connector.collect()


        return [
            ConnectorEvent(
                connector=connector_name,
                event_type="collection",
                payload=item,
            )
            for item in results
        ]
