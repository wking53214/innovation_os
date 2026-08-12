from innovation_os.health.monitor import (
    InnovationHealthMonitor,
)


def test_orphan_detection():

    monitor = InnovationHealthMonitor()

    issues = monitor.analyze(
        [
            {
                "id": "IDEA-001",
                "type": "IDEA",
            }
        ]
    )


    assert len(issues) == 1
    assert issues[0].issue_type == "ORPHAN_IDEA"


def test_clean_project():

    monitor = InnovationHealthMonitor()

    issues = monitor.analyze(
        [
            {
                "id": "PROJECT-001",
                "type": "PROJECT",
                "decision": "DECISION-001",
            }
        ]
    )


    assert len(issues) == 0
