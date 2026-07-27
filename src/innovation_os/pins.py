from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Pin:
    id: str
    object_id: str
    context: str
    reason: str
    created: datetime = field(default_factory=datetime.now)
    resolved: bool = False


class PinRegistry:
    def __init__(self):
        self.pins = []

    def create_pin(
        self,
        pin_id: str,
        object_id: str,
        context: str,
        reason: str,
    ):
        pin = Pin(
            id=pin_id,
            object_id=object_id,
            context=context,
            reason=reason,
        )

        self.pins.append(pin)

        return pin

    def find_pin(self, pin_id: str) -> Optional[Pin]:
        for pin in self.pins:
            if pin.id == pin_id:
                return pin

        return None