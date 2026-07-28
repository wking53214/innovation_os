from innovation_os.intelligence.registry import (
    IntelligenceRegistry,
)


def test_registry():

    registry = IntelligenceRegistry()

    registry.register(
        "runtime",
        object()
    )

    assert "runtime" in registry.inventory()
