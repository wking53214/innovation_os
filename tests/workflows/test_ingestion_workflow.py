import tempfile
import os

from innovation_os.workflows.ingestion_workflow import (
    FullIngestionWorkflow,
)
from innovation_os.provenance import ProvenanceStatus


def test_full_ingestion_workflow():

    with tempfile.TemporaryDirectory() as directory:

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


        with open(
            os.path.join(
                directory,
                "idea.md",
            ),
            "w",
        ) as file:
            file.write(
                "# innovation idea"
            )


        workflow = FullIngestionWorkflow()

        result = workflow.run(
            directory
        )

        assert result["documents"] == 1
        assert result["code_registered"] == 1
        assert result["total"] == 2


def test_full_ingestion_workflow_registers_uncertain_provenance():

    with tempfile.TemporaryDirectory() as directory:

        with open(
            os.path.join(directory, "engine.py"),
            "w",
        ) as file:
            file.write("# governance engine")

        workflow = FullIngestionWorkflow()
        workflow.run(directory)

        registered_ids = list(
            workflow.registry.artifacts.keys()
        )

        assert len(registered_ids) == 1

        record = workflow.provenance.get(
            registered_ids[0]
        )

        assert record.status is ProvenanceStatus.PROVENANCE_UNCERTAIN
