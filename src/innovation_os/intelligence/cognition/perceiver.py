from dataclasses import dataclass


@dataclass
class Perceiver:
    """
    Extracts meaning from observations.
    """

    def perceive(
        self,
        observation
    ):

        return {
            "type": "perception",
            "input": observation,
        }
