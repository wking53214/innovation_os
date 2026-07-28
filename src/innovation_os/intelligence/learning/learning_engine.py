from dataclasses import dataclass


@dataclass
class LearningEngine:
    """
    Coordinates learning cycle.
    """

    feedback_engine: object
    adaptation_engine: object


    def learn(
        self,
        signal
    ):

        feedback = self.feedback_engine.record(
            signal
        )

        return self.adaptation_engine.adapt(
            feedback
        )
