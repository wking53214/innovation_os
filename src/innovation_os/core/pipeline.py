from dataclasses import dataclass, field
from typing import List


@dataclass
class InnovationPipelineResult:
    problem_id: str
    ideas: List[str] = field(default_factory=list)
    aligned: bool = False
    reviewed: bool = False
    nature_patterns: List[str] = field(default_factory=list)
    solution_id: str = ""
    approved: bool = False


class InnovationPipeline:

    def __init__(self):
        self.results = []

    def run(
        self,
        problem_id: str,
        ideas: List[str],
        alignment_score: float,
        review_complete: bool,
        nature_patterns: List[str],
        solution_id: str,
        approved: bool,
    ) -> InnovationPipelineResult:

        result = InnovationPipelineResult(
            problem_id=problem_id,
            ideas=ideas,
            aligned=alignment_score >= 70,
            reviewed=review_complete,
            nature_patterns=nature_patterns,
            solution_id=solution_id,
            approved=approved,
        )

        self.results.append(result)

        return result

    def get(
        self,
        problem_id: str,
    ):

        for result in self.results:
            if result.problem_id == problem_id:
                return result

        return None
