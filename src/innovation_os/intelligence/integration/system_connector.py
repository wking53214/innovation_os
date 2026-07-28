from dataclasses import dataclass


@dataclass
class IntelligenceSystemConnector:
    """
    Adapter boundary for external Innovation OS systems.
    """

    bridge: object


    def attach(
        self,
        name,
        component
    ):

        return self.bridge.connect(
            name,
            component
        )
