from dataclasses import dataclass
from typing import List


@dataclass
class Recommendation:

    source_id: str
    recommendation: str
    reasoning: str
    confidence: float



class RecommendationEngine:


    def __init__(self):

        self.rules = []


    def add_rule(
        self,
        keyword: str,
        recommendation: str,
    ):

        self.rules.append(
            (
                keyword.lower(),
                recommendation,
            )
        )


    def recommend(
        self,
        artifact_id: str,
        terms: List[str],
    ):

        results = []

        normalized = [
            term.lower()
            for term in terms
        ]


        for keyword, suggestion in self.rules:

            if keyword in normalized:

                results.append(
                    Recommendation(
                        artifact_id,
                        suggestion,
                        f"Matched capability: {keyword}",
                        80.0,
                    )
                )


        return results
