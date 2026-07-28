from dataclasses import dataclass, field


@dataclass
class KnowledgeFabric:
    """
    Intelligence knowledge graph foundation.
    """

    entities: list = field(
        default_factory=list
    )

    relationships: list = field(
        default_factory=list
    )


    def add_entity(
        self,
        entity
    ):

        self.entities.append(
            entity
        )

        return entity


    def add_relationship(
        self,
        relationship
    ):

        self.relationships.append(
            relationship
        )

        return relationship


    def entity_count(self):

        return len(
            self.entities
        )
