from innovation_os.ingest.pipeline import (
    KnowledgeIngestionPipeline,
)

from innovation_os.registry.artifact_registry import (
    ArtifactRegistry,
)

from innovation_os.relationship_engine.discovery import (
    RelationshipDiscoveryEngine,
)


class FullIngestionWorkflow:


    def __init__(self):

        self.pipeline = KnowledgeIngestionPipeline()
        self.registry = ArtifactRegistry()
        self.relationships = (
            RelationshipDiscoveryEngine()
        )


    def run(
        self,
        directory: str,
    ):

        ingestion = self.pipeline.ingest(
            directory
        )

        registered = []

        for artifact in ingestion["code"]:

            item = self.registry.register(
                artifact.file_name,
                artifact.path,
                artifact.language,
            )

            registered.append(
                item
            )


        return {
            "documents": len(
                ingestion["documents"]
            ),
            "code_registered": len(
                registered
            ),
            "total": ingestion["total"],
        }
