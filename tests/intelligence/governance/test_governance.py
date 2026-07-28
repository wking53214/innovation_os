from innovation_os.intelligence.governance import (
    IntelligenceGovernor,
)


def test_governance():

    governor = IntelligenceGovernor()

    result = governor.authorize(
        "infer",
        .9
    )

    assert result.approved
