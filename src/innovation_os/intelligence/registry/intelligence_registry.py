from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class ComponentRegistry:
    """
    Central registry for intelligence components.
    """

    components: Dict[str, Any] = field(
        default_factory=dict
    )


    def register(
        self,
        name,
        component
    ):

        self.components[name] = component

        return component


    def resolve(
        self,
        name
    ):

        return self.components.get(
            name
        )


    def inventory(self):

        return list(
            self.components.keys()
        )
