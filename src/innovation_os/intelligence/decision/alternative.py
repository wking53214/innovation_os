from dataclasses import dataclass


@dataclass
class DecisionAlternative:
    """
    Represents a possible decision path.
    """

    name: str
    expected_value: float = 0.0
    risk: float = 0.0
