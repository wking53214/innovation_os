"""
Rewritten from the former tests against provenance/tracker.py, a third
provenance store keeping an append-only list of source references per item.
That store is gone. The same intent (one artifact accumulating a record of
where it came from over time) is expressed against the canonical store.
"""

from innovation_os.provenance import (
    ProvenanceEngine,
    ProvenanceStatus,
)


def test_source_references_accumulate():

    engine = ProvenanceEngine()

    engine.register(
        "IDEA-SENTINEL",
        ProvenanceStatus.USER_ESTABLISHED,
        source="sentinel_notes.md",
    )

    engine.add_history(
        "IDEA-SENTINEL",
        "DOCUMENT:sentinel_notes.md",
    )

    engine.add_history(
        "IDEA-SENTINEL",
        "CODE:gsa_gateway.py",
    )

    record = engine.get(
        "IDEA-SENTINEL"
    )

    assert len(record.history) == 2

    assert record.history[0] == "DOCUMENT:sentinel_notes.md"

    assert record.history[-1] == "CODE:gsa_gateway.py"

    #
    # Appearing in a later artifact does not change who originated the idea.
    #
    assert record.status is ProvenanceStatus.USER_ESTABLISHED
