import tempfile
import os

from src.innovation_os.integration.code_pipeline import (
    CodeIntegrationPipeline,
)


def test_code_pipeline():

    with tempfile.TemporaryDirectory() as directory:

        file_path = os.path.join(
            directory,
            "engine.py",
        )

        with open(
            file_path,
            "w",
        ) as file:
            file.write(
                "# governance engine"
            )


        pipeline = CodeIntegrationPipeline()

        results = pipeline.process(
            directory
        )

        assert len(results) == 1
        assert results[0].language == "Python"

        node = pipeline.graph.nodes[
            results[0].artifact_id
        ]

        assert node.node_type == "CODE"
