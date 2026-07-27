import sys

from src.innovation_os.ingest.pipeline import (
    KnowledgeIngestionPipeline,
)


def main():

    if len(sys.argv) < 2:
        print(
            "Usage: python -m src.innovation_os.ingest <folder>"
        )
        return

    pipeline = KnowledgeIngestionPipeline()

    result = pipeline.ingest(
        sys.argv[1]
    )

    print("=" * 50)
    print("INNOVATION OS INGESTION REPORT")
    print("=" * 50)

    print(
        "Documents:",
        len(result["documents"])
    )

    print(
        "Code Files:",
        len(result["code"])
    )

    print(
        "Total Artifacts:",
        result["total"]
    )


if __name__ == "__main__":
    main()
