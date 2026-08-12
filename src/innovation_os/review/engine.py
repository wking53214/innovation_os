from typing import List, Optional

from innovation_os.review.models import Review


class ReviewEngine:

    def __init__(self):
        self.reviews: List[Review] = []

    def create_review(
        self,
        review_id: str,
        target_id: str,
        strengths: List[str],
        weaknesses: List[str],
        risks: List[str],
        recommendations: List[str],
        score: float,
    ) -> Review:

        review = Review(
            review_id=review_id,
            target_id=target_id,
            strengths=strengths,
            weaknesses=weaknesses,
            risks=risks,
            recommendations=recommendations,
            score=score,
        )

        self.reviews.append(review)

        return review

    def get_review(
        self,
        review_id: str,
    ) -> Optional[Review]:

        for review in self.reviews:
            if review.review_id == review_id:
                return review

        return None
