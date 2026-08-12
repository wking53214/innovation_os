from innovation_os.intelligence.lifecycle import (
    LifecycleManager,
)


def test_lifecycle():

    lifecycle = LifecycleManager()

    assert lifecycle.active() is False

    lifecycle.transition(
        "active"
    )

    assert lifecycle.active() is True
    assert lifecycle.state == "active"
    assert lifecycle.history == [
        {"from": "initialized", "to": "active"}
    ]

    lifecycle.transition(
        "stopped"
    )

    assert lifecycle.active() is False
    assert lifecycle.history[-1] == {"from": "active", "to": "stopped"}
