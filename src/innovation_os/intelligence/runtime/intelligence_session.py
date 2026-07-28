from dataclasses import dataclass, field


@dataclass
class IntelligenceSession:

    context: object

    artifacts: list = field(
        default_factory=list
    )


    def add(
        self,
        artifact
    ):

        self.artifacts.append(
            artifact
        )
