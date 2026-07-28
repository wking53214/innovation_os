class GovernanceGate:

    def __init__(
        self,
        allowed=True,
    ):

        self.allowed = allowed


    def check(
        self,
        payload,
    ):

        return {
            "approved": self.allowed,
            "payload": payload,
        }
