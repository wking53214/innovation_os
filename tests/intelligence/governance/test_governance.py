from innovation_os.intelligence.governance import (
    RuntimePolicy,
    AccessControl,
    DecisionGuard,
    ComplianceTrace,
)


def test_runtime_policy():

    policy = RuntimePolicy(
        blocked_operations=[
            "delete"
        ]
    )

    assert policy.allows(
        "read"
    )

    assert not policy.allows(
        "delete"
    )



def test_access_control():

    user = AccessControl(
        role="user"
    )

    admin = AccessControl(
        role="admin"
    )

    assert user.can_execute(
        "normal"
    )

    assert admin.can_execute(
        "restricted"
    )



def test_decision_guard():

    guard = DecisionGuard(
        minimum_confidence=0.8
    )

    assert guard.approve(
        0.9
    )

    assert not guard.approve(
        0.4
    )



def test_compliance_trace():

    trace = ComplianceTrace()

    trace.record(
        "decision",
        "approved"
    )

    assert trace.latest()["status"] == "approved"
