from pathlib import Path
from typing import List

from src.innovation_os.importer.importer import (
    InnovationImporter,
)

from src.innovation_os.code_scanner.scanner import (
    CodeScanner,
)


class KnowledgeIngestionPipeline:

    def __init__(self):
        self.importer = InnovationImporter()
        self.scanner = CodeScanner()


    def ingest(
        self,
        directory: str,
    ):

        path = Path(directory)

        documents = []
        code = []

        documents.extend(
            self.importer.import_directory(
                str(path)
            )
        )

        code.extend(
            self.scanner.scan_directory(
                str(path)
            )
        )

        return {
            "documents": documents,
            "code": code,
            "total": (
                len(documents)
                +
                len(code)
            ),
        }
