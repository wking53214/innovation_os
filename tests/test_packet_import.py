from src.innovation_os.continuity import ContinuityEngine
from src.innovation_os.packet import (
    ContinuityPacketExporter,
    ContinuityPacketImporter,
)


def test_import_continuity_packet(tmp_path):
    engine = ContinuityEngine()

    original_state = engine.create_state(
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
        next_action="Continue development",
    )

    exporter = ContinuityPacketExporter()

    filename = tmp_path / "continuity_packet.json"

    exporter.export(
        original_state,
        str(filename),
    )

    importer = ContinuityPacketImporter()

    restored_state = importer.import_packet(
        str(filename)
    )

    assert restored_state.id == "STATE-0001"
    assert restored_state.title == "Innovation OS Development"
    assert restored_state.current_problem == (
        "Preserve and continue complex ideation"
    )
    assert "Relationship Engine" in restored_state.active_concepts
    assert "PIN-0001" in restored_state.active_pins