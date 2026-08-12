from datetime import datetime


from innovation_os.history.evolution import (
    InnovationEvolutionEngine,
)


def test_evolution_history():


    engine = InnovationEvolutionEngine()


    engine.record(
        "IDEA-SENTINEL",
        "CREATED",
        "Initial concept",
        datetime(2025,1,1),
    )


    engine.record(
        "IDEA-SENTINEL",
        "IMPLEMENTED",
        "First code version",
        datetime(2026,1,1),
    )


    result = engine.history(
        "IDEA-SENTINEL"
    )


    assert len(result) == 2

    assert (
        result[0].event_type
        ==
        "CREATED"
    )

    assert (
        result[1].event_type
        ==
        "IMPLEMENTED"
    )
