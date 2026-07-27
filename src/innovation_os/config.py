from dataclasses import dataclass


@dataclass(frozen=True)
class InnovationOSConfig:

    name: str = "Innovation OS"
    version: str = "1.0.0"
    environment: str = "production"



CONFIG = InnovationOSConfig()
