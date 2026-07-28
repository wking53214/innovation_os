from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ConceptMapper:
    """
    Maps concepts and semantic relationships.
    """

    concepts: Dict[str, List[str]] = field(
        default_factory=dict
    )


    def map(
        self,
        concept,
        related
    ):

        self.concepts.setdefault(
            concept,
            []
        ).append(
            related
        )

        return self.concepts[concept]
