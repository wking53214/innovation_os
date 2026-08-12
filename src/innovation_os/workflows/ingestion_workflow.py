from innovation_os.ingest.pipeline import (
    KnowledgeIngestionPipeline,
)

from innovation_os.registry.artifact_registry import (
    ArtifactRegistry,
)

from innovation_os.registry.shared_registries import (
    SharedRegistries,
)

from innovation_os.relationship_engine.discovery import (
    RelationshipDiscoveryEngine,
)

from innovation_os.provenance import (
    ProvenanceStatus,
)

from typing import Optional


class FullIngestionWorkflow:


    def __init__(
        self,
        shared: Optional[SharedRegistries] = None,
    ):

        bundle = shared or SharedRegistries()

        self.pipeline = KnowledgeIngestionPipeline()
        self.provenance = bundle.provenance
        self.context_envelopes = bundle.context_envelopes
        self.registry: ArtifactRegistry = bundle.registry
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

            #
            # Same reasoning as code_pipeline.py: a directory scan
            # carries no authorship signal, so PROVENANCE_UNCERTAIN
            # is the honest status rather than a guess.
            #
            item = self.registry.register(
                artifact.file_name,
                artifact.path,
                artifact.language,
                provenance_status=ProvenanceStatus.PROVENANCE_UNCERTAIN,
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
