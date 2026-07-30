from dataclasses import dataclass, field
from typing import List



@dataclass
class RepositoryIntelligence:

    name: str
    path: str

    artifacts: int = 0

    code_files: int = 0
    documents: int = 0
    resources: int = 0

    modules: List[str] = field(
        default_factory=list
    )



class RepositoryArtifactEngine:


    def analyze(
        self,
        artifacts,
    ):

        if not artifacts:

            return RepositoryIntelligence(
                name="UNKNOWN",
                path="",
            )


        name = artifacts[0].project_id


        result = RepositoryIntelligence(
            name=name,
            path="",
        )


        result.artifacts = len(
            artifacts
        )


        for artifact in artifacts:

            if artifact.artifact_type == "CODE":

                result.code_files += 1

                if artifact.name.endswith(".py"):

                    result.modules.append(
                        artifact.name
                    )


            elif artifact.artifact_type == "DOCUMENT":

                result.documents += 1


            else:

                result.resources += 1


        return result
