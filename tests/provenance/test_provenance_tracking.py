from src.innovation_os.provenance.provenance import (
    ProvenanceEngine,
)



def test_provenance_tracking():

    engine = ProvenanceEngine()


    record = engine.register(
        "CODE-001",
        "github://sentinel_os",
    )


    engine.link(
        "CODE-001",
        "PROJECT-SENTINEL",
    )


    result = engine.get(
        "CODE-001"
    )


    assert result.source == "github://sentinel_os"
    assert "PROJECT-SENTINEL" in result.relationships
