from innovation_os.governance.engine import (
    ApprovalEngine,
)


def test_create_approval():

    engine = ApprovalEngine()

    approval = engine.submit_approval(
        approval_id="APPROVAL-0001",
        target_id="SOLUTION-0001",
        reviewer="Human Reviewer",
        decision="APPROVED",
        rationale="Meets requirements",
    )

    assert approval.decision == "APPROVED"
    assert approval.target_id == "SOLUTION-0001"


def test_get_approval():

    engine = ApprovalEngine()

    engine.submit_approval(
        approval_id="APPROVAL-0002",
        target_id="SOLUTION-0002",
        reviewer="Reviewer",
        decision="REJECTED",
        rationale="Too risky",
    )

    result = engine.get_approval(
        "APPROVAL-0002"
    )

    assert result is not None
    assert result.decision == "REJECTED"


def test_get_target_approvals():

    engine = ApprovalEngine()

    engine.submit_approval(
        approval_id="APPROVAL-0003",
        target_id="SOLUTION-0003",
        reviewer="Reviewer",
        decision="NEEDS_REVIEW",
        rationale="Requires testing",
    )

    results = engine.get_for_target(
        "SOLUTION-0003"
    )

    assert len(results) == 1
