from innovation_os.continuity import ContinuityEngine


def test_create_continuity_state():
    engine = ContinuityEngine()

    state = engine.create_state(
        state_id="STATE-0001",
        title="Innovation OS Development",
        current_problem="Preserve and continue complex ideation",
        active_concepts=[
            "Relationship Engine",
            "Pin Registry",
        ],
        active_pins=[
            "PIN-0001",
        ],
        next_action="Build continuity restoration",
    )

    assert state.id == "STATE-0001"
    assert state.title == "Innovation OS Development"
    assert "PIN-0001" in state.active_pins


def test_restore_continuity_state():
    engine = ContinuityEngine()

    engine.create_state(
        state_id="STATE-0001",
        title="Innovation OS Development",
        current_problem="Testing restoration",
        active_concepts=[],
        active_pins=[],
        next_action="Continue",
    )

    restored = engine.restore_state("STATE-0001")

    assert restored is not None
    assert restored.current_problem == "Testing restoration"