from dataclasses import dataclass, field


@dataclass
class IntelligenceModule:

    name: str

    path: str

    dependencies: list = field(
        default_factory=list
    )

    consumers: list = field(
        default_factory=list
    )
