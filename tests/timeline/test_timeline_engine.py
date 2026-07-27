from datetime import datetime

from src.innovation_os.timeline.engine import (
    TimelineEngine,
)


def test_timeline_ordering():

    engine = TimelineEngine()


    engine.add_event(
        "EVENT-002",
        "PROJECT-001",
        "IMPLEMENTED",
        datetime(2026, 3, 1),
        "Code created",
    )


    engine.add_event(
        "EVENT-001",
        "PROJECT-001",
        "IDEA",
        datetime(2026, 1, 1),
        "Initial concept",
    )


    history = engine.history(
        "PROJECT-001"
    )


    assert history[0].event_type == "IDEA"
    assert history[1].event_type == "IMPLEMENTED"



def test_missing_history():

    engine = TimelineEngine()


    result = engine.history(
        "UNKNOWN"
    )


    assert len(result) == 0
