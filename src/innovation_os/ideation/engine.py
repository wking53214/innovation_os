from typing import List, Optional

from innovation_os.ideation.models import Idea


class IdeationEngine:

    def __init__(self):
        self.ideas: List[Idea] = []

    def generate_idea(
        self,
        idea_id: str,
        problem_id: str,
        title: str,
        description: str,
        sources: List[str],
        confidence: float,
        tags: List[str] = None,
    ) -> Idea:

        idea = Idea(
            idea_id=idea_id,
            problem_id=problem_id,
            title=title,
            description=description,
            sources=sources,
            confidence=confidence,
            tags=tags or [],
        )

        self.ideas.append(idea)

        return idea

    def get_idea(
        self,
        idea_id: str,
    ) -> Optional[Idea]:

        for idea in self.ideas:
            if idea.idea_id == idea_id:
                return idea

        return None

    def find_by_problem(
        self,
        problem_id: str,
    ) -> List[Idea]:

        return [
            idea
            for idea in self.ideas
            if idea.problem_id == problem_id
        ]
