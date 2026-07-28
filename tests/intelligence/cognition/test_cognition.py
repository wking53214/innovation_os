from innovation_os.intelligence.cognition import (
    Observer,
    Perceiver,
    Reasoner,
    Learner,
    CognitiveCycle,
    AdaptiveLoop,
)


def test_cognitive_cycle():

    cycle = CognitiveCycle(
        Observer(),
        Perceiver(),
        Reasoner(),
        Learner(),
    )

    result = cycle.execute(
        "signal"
    )

    assert result["type"] == "inference"


def test_adaptive_loop():

    cycle = CognitiveCycle(
        Observer(),
        Perceiver(),
        Reasoner(),
        Learner(),
    )

    loop = AdaptiveLoop(
        cycle
    )

    results = loop.run(
        [
            "a",
            "b",
        ]
    )

    assert len(results) == 2
