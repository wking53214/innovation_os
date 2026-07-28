from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class IntelligenceConnector(ABC):
    """
    External system integration boundary.
    Connectors produce normalized intelligence inputs.
    """

    name: str = "unknown"

    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def collect(self) -> Dict[str, Any]:
        pass
