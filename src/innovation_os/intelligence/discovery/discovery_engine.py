from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class DiscoveryEngine:
    """
    Discovers patterns and structures
    from intelligence inputs.
    """

    discoveries: List[Dict[str, Any]] = field(
        default_factory=list
    )


    def discover(
        self,
        data
    ):

        result = {
            "type": "discovery",
            "input": data,
        }

        self.discoveries.append(
            result
        )

        return result


    def history(self):

        return self.discoveries
