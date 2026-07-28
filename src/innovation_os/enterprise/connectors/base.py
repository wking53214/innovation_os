from innovation_os.enterprise.contracts import (
    ConnectorContract,
    ConnectorIdentity,
)



class BaseConnector(
    ConnectorContract
):


    def __init__(
        self,
        name,
        provider
    ):

        self.identity = ConnectorIdentity(
            name=name,
            provider=provider,
        )


        self.connected = False



    def connect(
        self
    ):

        self.connected = True

        return True



    def disconnect(
        self
    ):

        self.connected = False

        return True



    def health(
        self
    ):

        return {
            "connector":
            self.identity.name,

            "connected":
            self.connected
        }
