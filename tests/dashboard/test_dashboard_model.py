from src.innovation_os.dashboard.dashboard_model import (
    DashboardBuilder,
)



class FakeMemory:


    artifacts = [
        "code.py"
    ]

    history = [
        "created"
    ]

    decisions = [
        "decision"
    ]

    provenance = [
        "source"
    ]



def test_dashboard_snapshot():

    result = DashboardBuilder().build(
        "PROJECT-SENTINEL",
        "Sentinel",
        FakeMemory(),
    )


    assert (
        result.item_id
        ==
        "PROJECT-SENTINEL"
    )


    assert (
        result.status
        ==
        "ACTIVE"
    )


    assert len(
        result.artifacts
    ) == 1
