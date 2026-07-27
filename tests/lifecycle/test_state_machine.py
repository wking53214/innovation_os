from src.innovation_os.lifecycle.state_machine import (
    InnovationLifecycleEngine,
    LifecycleState,
)


def test_lifecycle_progression():

    engine = InnovationLifecycleEngine()

    record = engine.create(
        "PROJECT-001"
    )


    assert record.state == LifecycleState.IDEA


    assert engine.transition(
        "PROJECT-001",
        LifecycleState.VALIDATED,
    )


    assert engine.transition(
        "PROJECT-001",
        LifecycleState.DESIGNED,
    )


    assert record.state == LifecycleState.DESIGNED


def test_invalid_transition():

    engine = InnovationLifecycleEngine()

    engine.create(
        "PROJECT-001"
    )


    assert not engine.transition(
        "PROJECT-001",
        LifecycleState.DEPLOYED,
    )
