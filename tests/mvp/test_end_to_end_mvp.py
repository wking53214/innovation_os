import tempfile
from pathlib import Path


from src.innovation_os.archive.archive_loader import (
    ArchiveLoader,
)

from src.innovation_os.ingestion.pipeline import (
    IngestionPipeline,
)

from src.innovation_os.provenance.provenance import (
    ProvenanceEngine,
)

from src.innovation_os.relationships import (
    RelationshipEngine,
)



def test_innovation_os_mvp_flow():

    with tempfile.TemporaryDirectory() as directory:

        project = Path(directory)

        code = project / "sentinel.py"

        code.write_text(
            """
class Sentinel:
    pass
"""
        )


        #
        # Load archive
        #

        archive = ArchiveLoader().load(
            directory
        )


        assert len(
            archive.artifacts
        ) == 1



        #
        # Normalize ingestion
        #

        artifacts = IngestionPipeline().ingest(
            directory
        )


        assert artifacts[0].artifact_type == "CODE"



        #
        # Provenance
        #

        provenance = ProvenanceEngine()


        record = provenance.register(
            "CODE-001",
            archive.source,
        )


        assert record.source == directory



        #
        # Relationships
        #

        relationships = RelationshipEngine()


        relationships.connect(
            "IDEA-001",
            "CODE-001",
            "IMPLEMENTED_BY",
        )


        links = relationships.find_connections(
            "IDEA-001"
        )


        assert len(links) == 1
