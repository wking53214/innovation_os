from src.innovation_os.timeline.engine import (
    TimelineEngine,
)


def test_timeline_record():

    engine = TimelineEngine()

    event = engine.record(
        "EVENT-001",
        "PROJECT-001",
        "CREATED",
        "Project initialized",
    )


    assert event.artifact_id == "PROJECT-001"
    assert event.event_type == "CREATED"


def test_timeline_history():

    engine = TimelineEngine()

    engine.record(
        "EVENT-001",
        "PROJECT-001",
        "IDEA",
        "Initial concept",
    )

    engine.record(
        "EVENT-002",
        "PROJECT-001",
        "IMPLEMENTATION",
        "Code created",
    )


    history = engine.history(
        "PROJECT-001"
    )


    assert len(history) == 2
    assert history[0].event_type == "IDEA"
    assert history[1].event_type == "IMPLEMENTATION"
