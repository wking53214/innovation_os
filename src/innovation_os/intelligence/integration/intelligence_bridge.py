from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class IntelligenceBridge:
    """
    Connection layer between intelligence and OS subsystems.
    """

    systems: Dict[str, Any] = field(
        default_factory=dict
    )


    def connect(
        self,
        name,
        system
    ):

        self.systems[name] = system

        return system


    def get(
        self,
        name
    ):

        return self.systems.get(name)


    def connected_systems(self):

        return list(
            self.systems.keys()
        )
