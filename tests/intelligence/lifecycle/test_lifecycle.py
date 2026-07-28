from innovation_os.intelligence.lifecycle import (
    LifecycleManager,
)


def test_lifecycle():

    lifecycle = LifecycleManager()

    lifecycle.transition(
        "active"
    )

    assert lifecycle.active()
