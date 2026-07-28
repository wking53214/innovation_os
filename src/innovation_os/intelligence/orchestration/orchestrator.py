from dataclasses import dataclass, field


@dataclass
class IntelligenceOrchestrator:
    """
    Coordinates intelligence execution.
    """

    planner: object
    priority: object
    graph: object

    history: list = field(
        default_factory=list
    )


    def execute(
        self,
        objective
    ):

        tasks = self.planner.plan(
            objective
        )

        results = []

        for task in tasks:

            scored = self.priority.score(
                task
            )

            self.graph.add_node(
                scored
            )

            results.append(
                scored
            )

        self.history.extend(
            results
        )

        return results
