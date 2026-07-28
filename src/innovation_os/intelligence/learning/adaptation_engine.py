from dataclasses import dataclass, field


@dataclass
class AdaptationEngine:
    """
    Converts feedback into intelligence adaptations.
    """

    adaptations: list = field(
        default_factory=list
    )


    def adapt(
        self,
        feedback
    ):

        update = {
            "source": feedback,
            "status": "adapted",
        }

        self.adaptations.append(
            update
        )

        return update



    def count(self):

        return len(
            self.adaptations
        )
