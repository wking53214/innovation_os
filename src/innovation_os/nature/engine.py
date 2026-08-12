from typing import List, Optional

from innovation_os.nature.models import (
    NaturePattern,
)


class NatureInspiredEngine:

    def __init__(self):
        self.patterns: List[NaturePattern] = []

    def register_pattern(
        self,
        pattern_id: str,
        organism: str,
        mechanism: str,
        observed_behavior: str,
        transferable_principle: str,
        applications: List[str] = None,
    ) -> NaturePattern:

        pattern = NaturePattern(
            pattern_id=pattern_id,
            organism=organism,
            mechanism=mechanism,
            observed_behavior=observed_behavior,
            transferable_principle=transferable_principle,
            applications=applications or [],
        )

        self.patterns.append(pattern)

        return pattern

    def get_pattern(
        self,
        pattern_id: str,
    ) -> Optional[NaturePattern]:

        for pattern in self.patterns:
            if pattern.pattern_id == pattern_id:
                return pattern

        return None

    def find_by_principle(
        self,
        principle: str,
    ) -> List[NaturePattern]:

        return [
            pattern
            for pattern in self.patterns
            if pattern.transferable_principle == principle
        ]
