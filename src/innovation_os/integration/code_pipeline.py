from src.innovation_os.code_scanner.scanner import (
    CodeScanner,
)

from src.innovation_os.registry.artifact_registry import (
    ArtifactRegistry,
)

from src.innovation_os.graph.models import (
    InnovationGraph,
)


class CodeIntegrationPipeline:

    def __init__(self):

        self.scanner = CodeScanner()
        self.registry = ArtifactRegistry()
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

            code_artifact = self.registry.register(
                artifact.file_name,
                artifact.path,
                artifact.language,
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
