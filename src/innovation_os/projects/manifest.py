from dataclasses import dataclass
from typing import List


@dataclass
class ProjectManifest:

    project_id: str
    name: str
    description: str
    repositories: List[str]
    tags: List[str]



class ProjectRegistry:


    def __init__(self):

        self.projects = {}


    def register(
        self,
        manifest: ProjectManifest,
    ):

        self.projects[
            manifest.project_id
        ] = manifest

        return manifest


    def get(
        self,
        project_id: str,
    ):

        return self.projects.get(
            project_id
        )


    def list_projects(self):

        return list(
            self.projects.values()
        )
