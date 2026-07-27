import tempfile
import os

from src.innovation_os.workflows.ingestion_workflow import (
    FullIngestionWorkflow,
)


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
