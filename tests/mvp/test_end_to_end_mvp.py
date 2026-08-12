import tempfile
from pathlib import Path


from innovation_os.archive.archive_loader import (
    ArchiveLoader,
)

from innovation_os.ingestion.pipeline import (
    IngestionPipeline,
)

from innovation_os.provenance import (
    ProvenanceEngine,
    ProvenanceStatus,
)

from innovation_os.relationships import (
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


        #
        # A directory scan establishes where the file was found, not who
        # originated the idea in it. PROVENANCE_UNCERTAIN is the honest
        # category for an ingest path that cannot show origin.
        #
        record = provenance.register(
            "CODE-001",
            ProvenanceStatus.PROVENANCE_UNCERTAIN,
            source=archive.source,
        )


        assert record.source == directory

        assert record.status is ProvenanceStatus.PROVENANCE_UNCERTAIN



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
