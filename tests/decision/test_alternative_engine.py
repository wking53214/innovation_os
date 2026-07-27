from src.innovation_os.decision.alternative_engine import (
    AlternativeEngine,
)


def test_create_alternative():
    engine = AlternativeEngine()

    alternative = engine.create_alternative(
        alternative_id="ALT-0001",
        name="Option A",
        predicted_outcome="Fast implementation",
        risks=[
            "Limited scalability",
        ],
        benefits=[
            "Lower complexity",
        ],
        assumptions=[
            "Small user base",
        ],
        confidence=0.80,
    )

    assert alternative.alternative_id == "ALT-0001"
    assert alternative.name == "Option A"
    assert alternative.confidence == 0.80


def test_get_alternative():
    engine = AlternativeEngine()

    engine.create_alternative(
        alternative_id="ALT-0001",
        name="Option B",
        predicted_outcome="Better scalability",
        risks=[],
        benefits=[
            "Long-term flexibility",
        ],
        assumptions=[],
        confidence=0.90,
    )

    alternative = engine.get_alternative(
        "ALT-0001"
    )

    assert alternative is not None
    assert alternative.name == "Option B"


def test_compare_alternatives():
    engine = AlternativeEngine()

    engine.create_alternative(
        alternative_id="ALT-0001",
        name="Option A",
        predicted_outcome="Outcome A",
        risks=[],
        benefits=[],
        assumptions=[],
        confidence=0.70,
    )

    engine.create_alternative(
        alternative_id="ALT-0002",
        name="Option B",
        predicted_outcome="Outcome B",
        risks=[],
        benefits=[],
        assumptions=[],
        confidence=0.85,
    )

    results = engine.compare(
        [
            "ALT-0001",
            "ALT-0002",
        ]
    )

    assert len(results) == 2
