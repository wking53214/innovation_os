from dataclasses import dataclass, field


@dataclass
class DecisionContext:
    """
    Context container for intelligence decisions.
    """

    objective: str
    inputs: dict = field(
        default_factory=dict
    )
