import tempfile
import os

from src.innovation_os.ingest.pipeline import (
    KnowledgeIngestionPipeline,
)


def test_ingestion_pipeline():

    with tempfile.TemporaryDirectory() as directory:

        with open(
            os.path.join(
                directory,
                "idea.md",
            ),
            "w",
        ) as file:
            file.write(
                "# Innovation"
            )

        with open(
            os.path.join(
                directory,
                "engine.py",
            ),
            "w",
        ) as file:
            file.write(
                "# governance engine"
            )


        pipeline = KnowledgeIngestionPipeline()

        result = pipeline.ingest(
            directory
        )

        assert result["total"] == 2
        assert len(result["documents"]) == 1
        assert len(result["code"]) == 1
