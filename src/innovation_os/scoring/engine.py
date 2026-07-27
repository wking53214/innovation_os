from dataclasses import dataclass


@dataclass
class InnovationScore:

    artifact_id: str
    score: float
    factors: dict



class InnovationScoringEngine:


    def calculate(
        self,
        artifact_id: str,
        impact: float,
        alignment: float,
        readiness: float,
        assets: float,
        complexity: float,
    ):

        score = (
            impact
            + alignment
            + readiness
            + assets
            - complexity
        ) / 4


        return InnovationScore(
            artifact_id,
            round(score, 2),
            {
                "impact": impact,
                "alignment": alignment,
                "readiness": readiness,
                "assets": assets,
                "complexity": complexity,
            },
        )


    def rank(
        self,
        scores,
    ):

        return sorted(
            scores,
            key=lambda item: item.score,
            reverse=True,
        )
