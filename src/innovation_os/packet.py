import json
from dataclasses import asdict

from innovation_os.continuity import ContinuityState


class ContinuityPacketExporter:

    def export(self, state: ContinuityState, filename: str):
        packet = {
            "packet_type": "innovation_os_continuity_packet",
            "version": "1.0",
            "state": asdict(state),
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                packet,
                file,
                indent=2,
                default=str,
            )

        return filename


class ContinuityPacketImporter:

    def import_packet(self, filename: str):
        with open(filename, "r", encoding="utf-8") as file:
            packet = json.load(file)

        state = packet["state"]

        return ContinuityState(
            id=state["id"],
            title=state["title"],
            current_problem=state["current_problem"],
            active_concepts=state["active_concepts"],
            active_pins=state["active_pins"],
            next_action=state["next_action"],
        )