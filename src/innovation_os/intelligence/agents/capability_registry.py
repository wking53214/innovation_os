from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class CapabilityRegistry:
    """
    Registry of available intelligence capabilities.
    """

    capabilities: Dict[str, Any] = field(
        default_factory=dict
    )


    def register(
        self,
        name,
        capability
    ):

        self.capabilities[name] = capability

        return capability


    def get(
        self,
        name
    ):

        return self.capabilities.get(
            name
        )


    def list(self):

        return list(
            self.capabilities.keys()
        )
