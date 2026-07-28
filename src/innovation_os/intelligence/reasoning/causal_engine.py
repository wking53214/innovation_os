from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class CausalEngine:
    """
    Models cause and effect relationships.
    """

    relationships: List[Dict[str, str]] = field(
        default_factory=list
    )


    def connect(
        self,
        cause,
        effect
    ):

        relation = {
            "cause": cause,
            "effect": effect,
        }

        self.relationships.append(
            relation
        )

        return relation


    def causes(self, effect):

        return [
            r["cause"]
            for r in self.relationships
            if r["effect"] == effect
        ]
