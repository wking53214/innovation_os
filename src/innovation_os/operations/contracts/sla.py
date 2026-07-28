from dataclasses import dataclass


@dataclass
class SLARecord:

    service: str = ""

    target_uptime: float = 99.9

    current_uptime: float = 100.0
