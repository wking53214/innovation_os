from typing import List, Optional

from src.innovation_os.branches.models import Branch


class BranchEngine:

    def __init__(self):
        self.branches: List[Branch] = []

    def create_branch(
        self,
        branch_id: str,
        parent_id: str,
        problem_id: str,
        title: str,
        description: str,
        status: str = "ACTIVE",
    ) -> Branch:

        branch = Branch(
            branch_id=branch_id,
            parent_id=parent_id,
            problem_id=problem_id,
            title=title,
            description=description,
            status=status,
        )

        self.branches.append(branch)

        return branch

    def get_branch(
        self,
        branch_id: str,
    ) -> Optional[Branch]:

        for branch in self.branches:
            if branch.branch_id == branch_id:
                return branch

        return None

    def get_child_branches(
        self,
        parent_id: str,
    ) -> List[Branch]:

        return [
            branch
            for branch in self.branches
            if branch.parent_id == parent_id
        ]

    def update_status(
        self,
        branch_id: str,
        status: str,
    ) -> Optional[Branch]:

        branch = self.get_branch(branch_id)

        if branch:
            branch.status = status

        return branch
