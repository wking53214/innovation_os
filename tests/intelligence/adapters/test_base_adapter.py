from innovation_os.intelligence.adapters import PatternAdapter


def test_pattern_adapter():

    adapter = PatternAdapter()

    artifact = adapter.process(
        {"test": True}
    )

    assert artifact.intelligence_type == "pattern"
