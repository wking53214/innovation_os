from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from .base import IntelligenceConnector


class RepositoryConnector(IntelligenceConnector):

    name = "repository"

    def __init__(self, path: str):
        self.path = Path(path)

    def connect(self) -> bool:
        return self.path.exists()

    def collect(self) -> Dict[str, Any]:
        files = []

        if self.path.exists():
            for item in self.path.rglob("*"):
                if item.is_file():
                    files.append(str(item))

        return {
            "source": self.name,
            "path": str(self.path),
            "file_count": len(files),
            "files": files,
        }
