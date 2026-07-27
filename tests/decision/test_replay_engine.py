from src.innovation_os.decision.replay_engine import (
    ReplayEngine,
)


def test_create_replay():
    engine = ReplayEngine()

    replay = engine.create_replay(
        decision_id="DECISION-0001",
        original_choice="Option B",
        original_assumptions=[
            "Growth would be moderate",
            "Resources would remain available",
        ],
        new_information=[
            "Demand increased significantly",
        ],
        reconsidered_options=[
            "Option C",
        ],
        conclusion=(
            "Original decision was reasonable "
            "based on available information."
        ),
    )

    assert replay.decision_id == "DECISION-0001"
    assert replay.original_choice == "Option B"
    assert len(replay.new_information) == 1


def test_get_replay():
    engine = ReplayEngine()

    engine.create_replay(
        decision_id="DECISION-0002",
        original_choice="Option A",
        original_assumptions=[],
        new_information=[
            "New constraint discovered",
        ],
        reconsidered_options=[
            "Option B",
        ],
        conclusion="Review required.",
    )

    replay = engine.get_replay(
        "DECISION-0002"
    )

    assert replay is not None
    assert replay.original_choice == "Option A"
