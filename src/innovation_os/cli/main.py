import sys

from src.innovation_os.ingest.pipeline import (
    KnowledgeIngestionPipeline,
)

from src.innovation_os.code_scanner.scanner import (
    CodeScanner,
)


def show_help():

    print(
"""
Innovation OS CLI

Commands:

  ingest <folder>
      Import documents and code

  scan <folder>
      Scan code artifacts

  demo
      Run innovation demonstration

  status
      Show system status
"""
    )


def ingest(folder):

    pipeline = KnowledgeIngestionPipeline()

    result = pipeline.ingest(folder)

    print("Innovation OS Ingestion Report")
    print("-" * 40)

    print(
        "Documents:",
        len(result["documents"])
    )

    print(
        "Code:",
        len(result["code"])
    )

    print(
        "Total:",
        result["total"]
    )


def scan(folder):

    scanner = CodeScanner()

    results = scanner.scan_directory(
        folder
    )

    print("Code Scan Report")
    print("-" * 40)

    for artifact in results:
        print(
            artifact.file_name,
            artifact.language
        )

    print()
    print(
        "Files Found:",
        len(results)
    )


def status():

    print(
"""
Innovation OS Status

Core Systems:
✓ Problem Engine
✓ Ideation Engine
✓ Review Engine
✓ Solution Engine
✓ Code Registry
✓ Knowledge Graph
✓ Storage Layer
✓ Ingestion Pipeline
"""
    )


def main():

    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "ingest":

        ingest(sys.argv[2])

    elif command == "scan":

        scan(sys.argv[2])

    elif command == "status":

        status()

    elif command == "demo":

        from demos.run_innovation_demo import (
            run_demo,
        )

        run_demo()

    else:

        show_help()


if __name__ == "__main__":
    main()
