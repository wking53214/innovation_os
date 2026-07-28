from __future__ import annotations

from typing import Any, Dict


class PersistenceStore:

    def __init__(self):
        self.records: Dict[str, Any] = {}

    def save(
        self,
        key: str,
        value: Any,
    ) -> None:
        self.records[key] = value

    def get(
        self,
        key: str,
    ) -> Any:
        return self.records.get(key)
