from dataclasses import dataclass


@dataclass
class IntelligenceSettings:
    """
    Intelligence runtime configuration.
    """

    enabled: bool = True

    max_execution_depth: int = 10

    confidence_threshold: float = .5
