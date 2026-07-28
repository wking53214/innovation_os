from dataclasses import dataclass, field


@dataclass
class KnowledgeInference:
    """
    Generates derived knowledge relationships.
    """

    relationships: list = field(
        default_factory=list
    )


    def infer(
        self,
        relationship
    ):

        self.relationships.append(
            relationship
        )

        return relationship
