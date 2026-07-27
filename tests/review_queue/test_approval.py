from src.innovation_os.review_queue.approval import (
    ApprovalQueue,
)


def test_review_submission():

    queue = ApprovalQueue()

    item = queue.submit(
        "CODE-00001",
        "IDEA-001",
        "POSSIBLY_SUPPORTS",
        66.67,
    )

    assert item.status == "PENDING"
    assert item.item_id == "REVIEW-0001"


def test_review_approval():

    queue = ApprovalQueue()

    item = queue.submit(
        "CODE-00001",
        "IDEA-001",
        "POSSIBLY_SUPPORTS",
        80,
    )

    result = queue.approve(
        item.item_id
    )

    assert result.status == "APPROVED"


def test_review_rejection():

    queue = ApprovalQueue()

    item = queue.submit(
        "CODE-00002",
        "IDEA-002",
        "POSSIBLY_SUPPORTS",
        20,
    )

    result = queue.reject(
        item.item_id
    )

    assert result.status == "REJECTED"
