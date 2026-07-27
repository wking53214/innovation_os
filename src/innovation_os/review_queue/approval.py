from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class ReviewItem:

    item_id: str
    source_id: str
    target_id: str
    relationship: str
    confidence: float
    status: str = "PENDING"
    reviewed_at: datetime = None


class ApprovalQueue:


    def __init__(self):

        self.items: List[ReviewItem] = []
        self.counter = 1


    def submit(
        self,
        source_id,
        target_id,
        relationship,
        confidence,
    ):

        item = ReviewItem(
            item_id=f"REVIEW-{self.counter:04d}",
            source_id=source_id,
            target_id=target_id,
            relationship=relationship,
            confidence=confidence,
        )

        self.items.append(item)

        self.counter += 1

        return item


    def approve(
        self,
        item_id,
    ):

        item = self.get(item_id)

        item.status = "APPROVED"
        item.reviewed_at = datetime.now()

        return item


    def reject(
        self,
        item_id,
    ):

        item = self.get(item_id)

        item.status = "REJECTED"
        item.reviewed_at = datetime.now()

        return item


    def get(
        self,
        item_id,
    ):

        for item in self.items:

            if item.item_id == item_id:
                return item

        return None


    def pending(self):

        return [
            item
            for item in self.items
            if item.status == "PENDING"
        ]
