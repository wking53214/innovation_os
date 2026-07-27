from src.innovation_os.provenance.tracker import (
    ProvenanceTracker,
)



def test_provenance_tracking():

    tracker = ProvenanceTracker()


    tracker.record(
        "IDEA-SENTINEL",
        "DOCUMENT",
        "sentinel_notes.md",
    )


    tracker.record(
        "IDEA-SENTINEL",
        "CODE",
        "gsa_gateway.py",
    )


    history = tracker.history(
        "IDEA-SENTINEL"
    )


    assert len(history) == 2

    assert (
        history[0].source_reference
        ==
        "sentinel_notes.md"
    )

    assert (
        tracker.latest(
            "IDEA-SENTINEL"
        ).source_reference
        ==
        "gsa_gateway.py"
    )
