from dataclasses import dataclass, field


@dataclass
class IntelligenceAgent:
    """
    Autonomous intelligence execution boundary.
    """

    name: str

    router: object

    memory: object | None = None

    history: list = field(
        default_factory=list
    )


    def execute(
        self,
        task,
        payload
    ):

        result = self.router.route(
            task,
            payload
        )

        self.history.append(
            {
                "task": task,
                "result": result,
            }
        )

        return result
