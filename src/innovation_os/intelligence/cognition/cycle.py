from dataclasses import dataclass


@dataclass
class CognitiveCycle:
    """
    Single cognitive execution cycle.
    """

    observer: object
    perceiver: object
    reasoner: object
    learner: object


    def execute(
        self,
        signal
    ):

        observation = self.observer.observe(
            signal
        )

        perception = self.perceiver.perceive(
            observation
        )

        inference = self.reasoner.reason(
            perception
        )

        self.learner.learn(
            inference
        )

        return inference
