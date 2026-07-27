from typing import Dict, List

from src.innovation_os.matching.models import (
    MatchResult,
)


class IdeaMatchingEngine:

    def __init__(self):
        self.matches = []

    def match(
        self,
        artifact_id: str,
        detected_terms: List[str],
        ideas: Dict[str, List[str]],
    ) -> List[MatchResult]:

        results = []

        for idea_id, keywords in ideas.items():

            matched = [
                term
                for term in detected_terms
                if term in keywords
            ]

            if matched:

                confidence = (
                    len(matched)
                    /
                    len(keywords)
                ) * 100

                result = MatchResult(
                    artifact_id=artifact_id,
                    idea_id=idea_id,
                    confidence=round(
                        confidence,
                        2,
                    ),
                    matched_terms=matched,
                )

                results.append(result)
                self.matches.append(result)

        return results


    def get_matches(
        self,
        artifact_id: str,
    ):

        return [
            match
            for match in self.matches
            if match.artifact_id == artifact_id
        ]
