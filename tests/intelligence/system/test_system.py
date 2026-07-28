from innovation_os.intelligence.system import (
    create_intelligence_system,
)


def test_intelligence_system():

    system = create_intelligence_system()

    artifact = system.process(
        {
            "event": "integration_test"
        }
    )

    assert artifact

    assert system.metrics.get(
        "executions"
    ) == 1

    assert len(
        system.memory.history()
    ) == 1
