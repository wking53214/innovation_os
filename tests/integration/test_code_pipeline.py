import tempfile
import os

from innovation_os.integration.code_pipeline import (
    CodeIntegrationPipeline,
)
from innovation_os.provenance import ProvenanceStatus


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


def test_code_pipeline_registers_uncertain_provenance():
    """
    A directory scan has no authorship signal, so every artifact it
    registers should land as PROVENANCE_UNCERTAIN, not a guess.
    """

    with tempfile.TemporaryDirectory() as directory:

        with open(
            os.path.join(directory, "engine.py"),
            "w",
        ) as file:
            file.write("# governance engine")

        pipeline = CodeIntegrationPipeline()
        results = pipeline.process(directory)

        record = pipeline.provenance.get(
            results[0].artifact_id
        )

        assert record is not None
        assert record.status is ProvenanceStatus.PROVENANCE_UNCERTAIN

        envelope = pipeline.context_envelopes.get(
            results[0].artifact_id
        )

        assert envelope.artifact_id == results[0].artifact_id
