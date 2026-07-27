from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Artifact:

    artifact_id: str
    artifact_type: str
    name: str
    source: str
    project_id: str
    metadata: Optional[dict] = None
    idea_id: Optional[str] = None


    @property
    def filename(self):
        """
        Backward compatibility
        with legacy code registry.
        """
        return self.name


    @property
    def language(self):
        """
        Backward compatibility
        with legacy code registry.
        """
        if self.metadata:
            return self.metadata.get("language")

        return None



class ArtifactRegistry:


    def __init__(self):

        self.artifacts: Dict[str, Artifact] = {}
        self.counter = 0
        self.idea_links = {}



    def register(
        self,
        *args,
        **kwargs,
    ):

        """
        Supports:

        New:
            register(Artifact)

        Legacy:
            register(filename, path, language)
        """


        if (
            len(args) == 1
            and isinstance(args[0], Artifact)
        ):

            artifact = args[0]


        elif len(args) == 3:

            filename, path, language = args

            self.counter += 1

            artifact = Artifact(
                artifact_id=f"CODE-{self.counter:05d}",
                artifact_type="CODE",
                name=filename,
                source=path,
                project_id="UNKNOWN",
                metadata={
                    "language": language
                },
            )


        else:

            raise TypeError(
                "Invalid artifact registration format"
            )


        self.artifacts[
            artifact.artifact_id
        ] = artifact


        return artifact



    def get(
        self,
        artifact_id: str,
    ):

        return self.artifacts.get(
            artifact_id
        )



    def link_idea(
        self,
        artifact_id: str,
        idea_id: str,
    ):

        artifact = self.artifacts.get(
            artifact_id
        )

        if artifact:

            artifact.idea_id = idea_id


        if artifact_id not in self.idea_links:

            self.idea_links[artifact_id] = []


        self.idea_links[
            artifact_id
        ].append(
            idea_id
        )


        return True



    def ideas_for(
        self,
        artifact_id: str,
    ):

        return self.idea_links.get(
            artifact_id,
            [],
        )



    def search_by_project(
        self,
        project_id: str,
    ) -> List[Artifact]:

        return [
            artifact
            for artifact in self.artifacts.values()
            if artifact.project_id == project_id
        ]



    def list_all(self):

        return list(
            self.artifacts.values()
        )
