from src.innovation_os.pins import PinRegistry


def test_create_pin():
    registry = PinRegistry()

    pin = registry.create_pin(
        pin_id="PIN-0001",
        object_id="CON-0001",
        context="AI ideation architecture discussion",
        reason="Potential foundation for continuity engine",
    )

    assert pin.id == "PIN-0001"
    assert pin.object_id == "CON-0001"
    assert pin.context == "AI ideation architecture discussion"
    assert pin.reason == "Potential foundation for continuity engine"


def test_find_pin():
    registry = PinRegistry()

    registry.create_pin(
        pin_id="PIN-0001",
        object_id="CON-0001",
        context="Testing pin retrieval",
        reason="Important concept",
    )

    pin = registry.find_pin("PIN-0001")

    assert pin is not None
    assert pin.object_id == "CON-0001"