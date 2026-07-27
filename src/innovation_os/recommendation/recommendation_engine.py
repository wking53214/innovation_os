from dataclasses import dataclass
from typing import List



@dataclass
class Recommendation:

    item_id: str
    action: str
    reason: str
    priority: str



class RecommendationEngine:


    def recommend(
        self,
        item_id: str,
        score: float,
        relationships: int = 0,
        duplicates: int = 0,
    ) -> Recommendation:


        if duplicates > 0:

            return Recommendation(
                item_id,
                "Review Existing Work",
                "Similar concepts already exist",
                "MEDIUM",
            )


        if score >= 75 and relationships > 0:

            return Recommendation(
                item_id,
                "Continue Development",
                "High innovation value with connected evidence",
                "HIGH",
            )


        if score >= 40:

            return Recommendation(
                item_id,
                "Develop Further",
                "Promising but requires additional maturity",
                "MEDIUM",
            )


        return Recommendation(
            item_id,
            "Archive and Monitor",
            "Insufficient evidence of maturity",
            "LOW",
        )
