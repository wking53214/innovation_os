from innovation_os.review.engine import ReviewEngine


def test_create_review():

    engine = ReviewEngine()

    review = engine.create_review(
        review_id="REVIEW-0001",
        target_id="IDEA-0001",
        strengths=[
            "High potential impact",
        ],
        weaknesses=[
            "Requires validation",
        ],
        risks=[
            "Adoption risk",
        ],
        recommendations=[
            "Run pilot",
        ],
        score=85,
    )

    assert review.review_id == "REVIEW-0001"
    assert review.score == 85


def test_get_review():

    engine = ReviewEngine()

    engine.create_review(
        review_id="REVIEW-0002",
        target_id="IDEA-0002",
        strengths=[],
        weaknesses=[],
        risks=[],
        recommendations=[],
        score=70,
    )

    review = engine.get_review(
        "REVIEW-0002"
    )

    assert review.review_id == "REVIEW-0002"
    assert review.target_id == "IDEA-0002"
    assert review.score == 70
