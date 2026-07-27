from pathlib import Path
import tempfile


from src.innovation_os.history.importer import (
    InnovationHistoryImporter,
)



def test_history_import():

    with tempfile.TemporaryDirectory() as directory:

        file = Path(directory) / "notes.md"

        file.write_text(
            """
            Sentinel OS governance architecture
            """
        )


        result = InnovationHistoryImporter().import_directory(
            directory
        )


        assert len(result) == 1

        assert (
            "sentinel"
            in result[0].keywords
        )

        assert (
            result[0].artifact_type
            ==
            "DOCUMENT"
        )
