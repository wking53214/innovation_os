from innovation_os.intelligence.kernel import IntelligenceRegistry


def test_registry_engine():

    registry = IntelligenceRegistry()

    engine = object()

    registry.register_engine(
        "test",
        engine
    )

    assert registry.get_engine("test") is engine
