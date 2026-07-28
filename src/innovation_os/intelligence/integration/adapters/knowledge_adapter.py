from dataclasses import dataclass


@dataclass
class KnowledgeAdapter:
    """
    Knowledge graph integration boundary.
    """

    graph=None


    def add_relationship(
        self,
        source,
        target
    ):

        if self.graph and hasattr(
            self.graph,
            "connect"
        ):
            return self.graph.connect(
                source,
                target
            )

        return (
            source,
            target,
        )
