import json
from dataclasses import asdict

from src.innovation_os.continuity import ContinuityState


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