import tempfile
from pathlib import Path


from src.innovation_os.code.relationship_extractor import (
    CodeRelationshipExtractor,
)



def test_code_relationship_extraction():

    with tempfile.TemporaryDirectory() as directory:

        file = Path(directory) / "engine.py"

        file.write_text(
            """
import os
import json
"""
        )


        result = CodeRelationshipExtractor().analyze(
            str(file)
        )


        assert "os" in result.imports
        assert len(result.relationships) == 2

        assert (
            result.relationships[0].relationship_type
            == "IMPORT"
        )
