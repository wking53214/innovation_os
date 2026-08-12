from innovation_os.code_scanner.scanner import (
    CodeScanner,
)

from innovation_os.registry.artifact_registry import (
    ArtifactRegistry,
)

from innovation_os.registry.shared_registries import (
    SharedRegistries,
)

from innovation_os.graph.models import (
    InnovationGraph,
)

from innovation_os.provenance import (
    ProvenanceStatus,
)

from typing import Optional


class CodeIntegrationPipeline:

    def __init__(
        self,
        shared: Optional[SharedRegistries] = None,
    ):

        #
        # No shared bundle given -- fall back to a private, isolated
        # set. This is the previous default behavior and is what the
        # existing tests construct. Pass a SharedRegistries to make
        # this pipeline agree with another one on artifact_ids and
        # provenance history instead of tracking its own island.
        #
        bundle = shared or SharedRegistries()

        self.scanner = CodeScanner()
        self.provenance = bundle.provenance
        self.context_envelopes = bundle.context_envelopes
        self.registry: ArtifactRegistry = bundle.registry
        self.graph = InnovationGraph()


    def process(
        self,
        directory: str,
    ):

        scanned = self.scanner.scan_directory(
            directory
        )

        registered = []

        for artifact in scanned:

            #
            # A directory scan has no authorship signal: no git
            # blame, no commit metadata, nothing distinguishing
            # human-written from AI-assisted code. Even git history
            # wouldn't help here -- this project's commits are
            # authored uniformly regardless of who/what wrote the
            # content. PROVENANCE_UNCERTAIN is the honest status,
            # not a placeholder: "the record does not permit
            # determination" is a true statement about what a bare
            # file scan knows (status.py, Article II).
            #
            code_artifact = self.registry.register(
                artifact.file_name,
                artifact.path,
                artifact.language,
                provenance_status=ProvenanceStatus.PROVENANCE_UNCERTAIN,
            )

            self.graph.add_node(
                code_artifact.artifact_id,
                "CODE",
                code_artifact.filename,
            )

            registered.append(
                code_artifact
            )

        return registered
