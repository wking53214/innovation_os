from dataclasses import dataclass, field


@dataclass
class FeedbackEngine:
    """
    Captures intelligence feedback signals.
    """

    feedback: list = field(
        default_factory=list
    )


    def record(
        self,
        feedback
    ):

        self.feedback.append(
            feedback
        )

        return feedback


    def latest(self):

        if not self.feedback:
            return None

        return self.feedback[-1]
