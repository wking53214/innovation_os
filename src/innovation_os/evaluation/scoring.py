from dataclasses import dataclass


@dataclass
class Score:

    name: str

    value: float



class EvaluationEngine:


    def evaluate(
        self,
        result
    ):

        confidence = getattr(
            result,
            "confidence",
            0.0
        )

        return Score(
            name="confidence",
            value=confidence
        )
