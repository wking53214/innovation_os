import json

from src.innovation_os.continuity import ContinuityEngine
from src.innovation_os.packet import ContinuityPacketExporter


def test_export_continuity_packet(tmp_path):
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
        next_action="Continue development",
    )

    exporter = ContinuityPacketExporter()

    filename = tmp_path / "packet.json"

    result = exporter.export(
        state,
        str(filename),
    )

    assert result == str(filename)
    assert filename.exists()

    with open(filename, "r", encoding="utf-8") as file:
        packet = json.load(file)

    assert packet["packet_type"] == "innovation_os_continuity_packet"
    assert packet["state"]["id"] == "STATE-0001"