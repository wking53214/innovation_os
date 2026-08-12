import tempfile
import os

from innovation_os.importer.importer import (
    InnovationImporter,
)


def test_import_markdown():

    with tempfile.TemporaryDirectory() as directory:

        file_path = os.path.join(
            directory,
            "idea.md",
        )

        with open(
            file_path,
            "w",
        ) as file:
            file.write(
                "# New Innovation Idea"
            )

        importer = InnovationImporter()

        results = importer.import_directory(
            directory
        )

        assert len(results) == 1
        assert results[0].artifact_type == "Markdown"
        assert "Innovation" in results[0].preview
