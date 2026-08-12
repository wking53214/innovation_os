from innovation_os.nature.engine import (
    NatureInspiredEngine,
)


def test_register_pattern():

    engine = NatureInspiredEngine()

    pattern = engine.register_pattern(
        pattern_id="NATURE-0001",
        organism="Coral ecosystem",
        mechanism="Adaptive recovery",
        observed_behavior="System adjusts after stress",
        transferable_principle="Resilience through adaptation",
        applications=[
            "Organizational recovery",
        ],
    )

    assert pattern.organism == "Coral ecosystem"
    assert pattern.mechanism == "Adaptive recovery"


def test_get_pattern():

    engine = NatureInspiredEngine()

    engine.register_pattern(
        pattern_id="NATURE-0002",
        organism="Termite colony",
        mechanism="Passive regulation",
        observed_behavior="Controls internal environment",
        transferable_principle="Self-regulation",
    )

    result = engine.get_pattern(
        "NATURE-0002"
    )

    assert result is not None


def test_find_by_principle():

    engine = NatureInspiredEngine()

    engine.register_pattern(
        pattern_id="NATURE-0003",
        organism="Forest",
        mechanism="Interconnected systems",
        observed_behavior="Resource sharing",
        transferable_principle="Distributed cooperation",
    )

    results = engine.find_by_principle(
        "Distributed cooperation"
    )

    assert len(results) == 1
