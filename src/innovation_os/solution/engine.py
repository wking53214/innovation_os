from typing import List, Optional

from src.innovation_os.solution.models import Solution


class SolutionEngine:

    def __init__(self):
        self.solutions: List[Solution] = []

    def create_solution(
        self,
        solution_id: str,
        problem_id: str,
        idea_id: str,
        title: str,
        description: str,
        supporting_artifacts: List[str],
        risks: List[str],
        status: str = "PROPOSED",
    ) -> Solution:

        solution = Solution(
            solution_id=solution_id,
            problem_id=problem_id,
            idea_id=idea_id,
            title=title,
            description=description,
            supporting_artifacts=supporting_artifacts,
            risks=risks,
            status=status,
        )

        self.solutions.append(solution)

        return solution

    def get_solution(
        self,
        solution_id: str,
    ) -> Optional[Solution]:

        for solution in self.solutions:
            if solution.solution_id == solution_id:
                return solution

        return None

    def find_by_problem(
        self,
        problem_id: str,
    ) -> List[Solution]:

        return [
            solution
            for solution in self.solutions
            if solution.problem_id == problem_id
        ]

    def update_status(
        self,
        solution_id: str,
        status: str,
    ) -> Optional[Solution]:

        solution = self.get_solution(solution_id)

        if solution:
            solution.status = status

        return solution
