from dataclasses import dataclass, field


@dataclass
class LifecycleManager:
    """
    Controls intelligence subsystem lifecycle.
    """

    state: str = "initialized"

    history: list = field(
        default_factory=list
    )


    def transition(
        self,
        new_state
    ):

        self.history.append(
            {
                "from": self.state,
                "to": new_state,
            }
        )

        self.state = new_state

        return self.state


    def active(self):

        return self.state == "active"
