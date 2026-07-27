from dataclasses import dataclass



@dataclass
class InnovationScore:

    item_id: str
    score: float
    classification: str



class InnovationScoringEngine:


    def calculate(
        self,
        item_id: str,
        artifacts: int = 0,
        concepts: int = 0,
        decisions: int = 0,
        connections: int = 0,
    ):

        score = (
            artifacts * 2
            +
            concepts * 3
            +
            decisions * 2
            +
            connections
            +
            2
        )


        score = min(
            score,
            100,
        )


        if score >= 75:

            classification = "HIGH POTENTIAL"

        elif score >= 40:

            classification = "DEVELOPING"

        else:

            classification = "EARLY"


        return InnovationScore(
            item_id,
            score,
            classification,
        )
