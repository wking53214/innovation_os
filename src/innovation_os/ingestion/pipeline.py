from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict


class SignalIngestionPipeline:

    def normalize(
        self,
        payload: Dict[str, Any],
    ) -> Dict[str, Any]:

        return {
            "timestamp": datetime.now(
                timezone.utc
            ),
            "signal_type": payload.get(
                "source",
                "unknown",
            ),
            "payload": payload,
        }


class IngestionPipeline(SignalIngestionPipeline):
    """
    Backward-compatible ingestion interface.
    Preserves existing MVP test contract.
    """

    pass


class IngestionPipeline(SignalIngestionPipeline):
    """
    Backward-compatible MVP ingestion interface.
    """

    def ingest(self, directory):

        from pathlib import Path
        from dataclasses import dataclass

        @dataclass
        class IngestionArtifact:
            artifact_type: str
            path: str
            name: str
            content: str = ""

        artifacts = []

        root = Path(directory)

        if root.exists():
            for item in root.rglob("*"):
                if item.is_file():
                    try:
                        content = item.read_text()
                    except Exception:
                        content = ""

                    artifacts.append(
                        IngestionArtifact(
                            artifact_type="CODE",
                            path=str(item),
                            name=item.name,
                            content=content,
                        )
                    )

        return artifacts
