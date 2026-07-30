from dataclasses import dataclass

from src.innovation_os.repository.mapper import (
    RepositoryMapper,
)

from src.innovation_os.intelligence.repository_intelligence import (
    RepositoryArtifactEngine,
)



@dataclass
class ProjectScanResult:

    name: str
    artifacts: int
    code_files: int
    documents: int
    resources: int



class ProjectScanner:


    def __init__(self):

        self.mapper = RepositoryMapper()

        self.engine = RepositoryArtifactEngine()



    def scan(
        self,
        directory: str,
    ):

        artifacts = self.mapper.map_repository(
            directory
        )


        intelligence = self.engine.analyze(
            artifacts
        )


        return ProjectScanResult(
            name=intelligence.name,
            artifacts=intelligence.artifacts,
            code_files=intelligence.code_files,
            documents=intelligence.documents,
            resources=intelligence.resources,
        )
