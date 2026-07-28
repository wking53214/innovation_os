from dataclasses import dataclass, field


@dataclass
class Learner:
    """
    Updates intelligence state from outcomes.
    """

    memory: list = field(
        default_factory=list
    )


    def learn(
        self,
        result
    ):

        self.memory.append(
            result
        )

        return result
