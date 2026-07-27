from dataclasses import dataclass
from typing import Dict, List


@dataclass
class RelationshipSuggestion:

    source_id: str
    target_id: str
    relationship: str
    confidence: float
    evidence: List[str]


class RelationshipDiscoveryEngine:

    def __init__(self):
        self.suggestions = []

    def discover(
        self,
        source_id: str,
        source_terms: List[str],
        targets: Dict[str, List[str]],
    ):

        results = []

        for target_id, target_terms in targets.items():

            matched = [
                term
                for term in source_terms
                if term in target_terms
            ]

            if matched:

                confidence = (
                    len(matched)
                    /
                    len(target_terms)
                ) * 100

                suggestion = RelationshipSuggestion(
                    source_id=source_id,
                    target_id=target_id,
                    relationship="POSSIBLY_SUPPORTS",
                    confidence=round(
                        confidence,
                        2,
                    ),
                    evidence=matched,
                )

                results.append(
                    suggestion
                )

                self.suggestions.append(
                    suggestion
                )

        return results
