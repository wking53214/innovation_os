from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class PatternEvolution:
    """
    Tracks changing intelligence patterns.
    """

    patterns: List[Dict] = field(
        default_factory=list
    )


    def evolve(
        self,
        pattern,
        change
    ):

        result = {
            "pattern": pattern,
            "change": change,
        }

        self.patterns.append(
            result
        )

        return result
