from dataclasses import dataclass


@dataclass
class IntelligenceFabric:

    name: str = ""

    connected_systems: int = 0

    active: bool = False
