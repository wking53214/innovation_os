from dataclasses import dataclass
from typing import List


@dataclass
class AlignmentResult:
    idea_id: str
    problem_id: str
    score: float
    aligned: bool
    reasons: List[str]


class ProblemAlignmentEngine:

    def __init__(self):
        self.results = []

    def evaluate(
        self,
        idea_id: str,
        problem_id: str,
        score: float,
        reasons: List[str],
    ) -> AlignmentResult:

        result = AlignmentResult(
            idea_id=idea_id,
            problem_id=problem_id,
            score=score,
            aligned=score >= 70,
            reasons=reasons,
        )

        self.results.append(result)

        return result

    def get_result(
        self,
        idea_id: str,
    ):

        for result in self.results:
            if result.idea_id == idea_id:
                return result

        return None
