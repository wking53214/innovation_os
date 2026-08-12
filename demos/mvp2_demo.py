import tempfile
import os

from innovation_os.workflows.ingestion_workflow import (
    FullIngestionWorkflow,
)

from innovation_os.api.server import (
    InnovationAPI,
)


def run_demo():

    print("=" * 60)
    print("INNOVATION OS MVP 2.0 DEMONSTRATION")
    print("=" * 60)


    with tempfile.TemporaryDirectory() as folder:

        with open(
            os.path.join(folder, "governance_engine.py"),
            "w",
        ) as file:
            file.write(
                "# AI governance security pipeline"
            )


        with open(
            os.path.join(folder, "sentinel_idea.md"),
            "w",
        ) as file:
            file.write(
                "# Sentinel governance platform idea"
            )


        workflow = FullIngestionWorkflow()

        result = workflow.run(
            folder
        )


        api = InnovationAPI()

        api.add_node(
            "PROJECT-001",
            "PROJECT",
            "Sentinel Governance Platform",
        )


        print()
        print("INGESTION RESULTS")
        print("-" * 60)

        print(
            "Documents:",
            result["documents"]
        )

        print(
            "Code Registered:",
            result["code_registered"]
        )

        print(
            "Total Artifacts:",
            result["total"]
        )


        print()
        print("SEARCH TEST")
        print("-" * 60)

        matches = api.search_nodes(
            "Governance"
        )

        for match in matches:
            print(
                match["node_id"],
                "-",
                match["label"],
            )


    print()
    print("=" * 60)
    print("STEP 50 COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
