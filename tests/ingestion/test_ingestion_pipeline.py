import tempfile
from pathlib import Path

from src.innovation_os.ingestion.pipeline import (
    IngestionPipeline,
)



def test_ingestion_pipeline():

    with tempfile.TemporaryDirectory() as directory:

        file = Path(directory) / "engine.py"

        file.write_text(
            "print('test')"
        )


        pipeline = IngestionPipeline()

        result = pipeline.ingest(
            directory
        )


        assert len(result) == 1
        assert result[0].artifact_type == "CODE"
