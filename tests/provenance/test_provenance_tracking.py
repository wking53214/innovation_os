from innovation_os.provenance import (
    ProvenanceEngine,
    ProvenanceStatus,
)


def test_provenance_tracking():

    engine = ProvenanceEngine()

    engine.register(
        "CODE-001",
        ProvenanceStatus.USER_ESTABLISHED,
        source="github://sentinel_os",
    )

    engine.link(
        "CODE-001",
        "PROJECT-SENTINEL",
    )

    result = engine.get(
        "CODE-001"
    )

    assert result.source == "github://sentinel_os"

    assert result.status is ProvenanceStatus.USER_ESTABLISHED

    assert "PROJECT-SENTINEL" in result.relationships
