import tempfile
import os

from src.innovation_os.code_scanner.scanner import (
    CodeScanner,
)


def test_code_scanner():

    with tempfile.TemporaryDirectory() as directory:

        file_path = os.path.join(
            directory,
            "example.py",
        )

        with open(
            file_path,
            "w",
        ) as file:

            file.write(
                "# innovation engine\n"
            )

        scanner = CodeScanner()

        results = scanner.scan_directory(
            directory
        )

        assert len(results) == 1
        assert results[0].language == "Python"
        assert "innovation" in results[0].detected_terms
