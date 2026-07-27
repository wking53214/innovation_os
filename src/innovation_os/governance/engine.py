from typing import List, Optional

from src.innovation_os.governance.models import (
    ApprovalRecord,
)


class ApprovalEngine:

    def __init__(self):
        self.records: List[ApprovalRecord] = []

    def submit_approval(
        self,
        approval_id: str,
        target_id: str,
        reviewer: str,
        decision: str,
        rationale: str,
    ) -> ApprovalRecord:

        record = ApprovalRecord(
            approval_id=approval_id,
            target_id=target_id,
            reviewer=reviewer,
            decision=decision,
            rationale=rationale,
        )

        self.records.append(record)

        return record

    def get_approval(
        self,
        approval_id: str,
    ) -> Optional[ApprovalRecord]:

        for record in self.records:
            if record.approval_id == approval_id:
                return record

        return None

    def get_for_target(
        self,
        target_id: str,
    ) -> List[ApprovalRecord]:

        return [
            record
            for record in self.records
            if record.target_id == target_id
        ]
