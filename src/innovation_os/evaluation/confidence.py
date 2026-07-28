from __future__ import annotations

from typing import Any, Dict


class ConfidenceEvaluator:

    def evaluate(
        self,
        artifact: Dict[str, Any],
    ) -> float:

        if not artifact:
            return 0.0

        return 0.5
