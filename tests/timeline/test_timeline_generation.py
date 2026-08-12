from datetime import datetime

from innovation_os.timeline.engine import (
    TimelineEngine,
)


def test_timeline_generation():

    engine = TimelineEngine()


    engine.add_event(
        "ART-002",
        "Implementation",
        "CODE",
        datetime(2026, 1, 1),
    )


    engine.add_event(
        "ART-001",
        "Idea",
        "CONCEPT",
        datetime(2025, 1, 1),
    )


    result = engine.generate()


    assert result[0].artifact_id == "ART-001"
    assert result[1].artifact_id == "ART-002"
