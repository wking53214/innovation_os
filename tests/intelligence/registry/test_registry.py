from innovation_os.intelligence.registry import (
    ComponentRegistry,
)


def test_registry():

    registry = ComponentRegistry()

    registry.register(
        "runtime",
        object()
    )

    assert "runtime" in registry.inventory()
