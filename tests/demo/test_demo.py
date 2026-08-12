from demos.mvp2_demo import (
    run_demo,
)


def test_demo_runs(capsys):

    run_demo()

    output = capsys.readouterr().out

    assert "Documents: 1" in output
    assert "Code Registered: 1" in output
    assert "Total Artifacts: 2" in output
    assert "PROJECT-001 - Sentinel Governance Platform" in output
    assert "STEP 50 COMPLETE" in output
