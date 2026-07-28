from dataclasses import dataclass, field


@dataclass
class ExecutionGraph:
    """
    Tracks intelligence execution dependencies.
    """

    nodes: list = field(
        default_factory=list
    )

    edges: list = field(
        default_factory=list
    )


    def add_node(
        self,
        node
    ):

        self.nodes.append(
            node
        )

        return node


    def connect(
        self,
        source,
        target
    ):

        self.edges.append(
            (
                source,
                target,
            )
        )

        return (
            source,
            target,
        )
