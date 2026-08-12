"""
Article II.A (provenance events) and II.B (lineage) guarantees.

Neither is ratified. These tests check the mechanism works, not that it is
constitutional law. See events.py docstring.
"""

from innovation_os.provenance import (
    ProvenanceEngine,
    ProvenanceEventType,
    ProvenanceStatus,
)


def test_registration_logs_an_origin_event():

    engine = ProvenanceEngine()

    record = engine.register(
        "IDEA-100",
        ProvenanceStatus.ASSISTANT_PROPOSED,
    )

    assert len(record.events) == 1

    assert record.events[0].event_type is ProvenanceEventType.ORIGIN

    assert record.events[0].to_status is ProvenanceStatus.ASSISTANT_PROPOSED


def test_adoption_preserves_machine_origin_after_status_moves():
    """
    Article XIII.A: human adoption changes current status but does not
    erase the machine's role in originating the discovery.
    """

    engine = ProvenanceEngine()

    engine.register(
        "DEC-100",
        ProvenanceStatus.ASSISTANT_PROPOSED,
    )

    engine.set_status(
        "DEC-100",
        ProvenanceStatus.USER_ACCEPTED,
        reason="Human explicitly adopted in review",
    )

    record = engine.get(
        "DEC-100"
    )

    #
    # Current status advanced.
    #
    assert record.status is ProvenanceStatus.USER_ACCEPTED

    #
    # But the event log still shows the machine origin. This is the
    # concrete guarantee behind "adoption does not erase origin".
    #
    event_types = [e.event_type for e in record.events]

    assert event_types == [
        ProvenanceEventType.ORIGIN,
        ProvenanceEventType.ADOPTION,
    ]

    assert record.events[0].to_status is ProvenanceStatus.ASSISTANT_PROPOSED

    assert record.events[1].from_status is ProvenanceStatus.ASSISTANT_PROPOSED

    assert record.events[1].to_status is ProvenanceStatus.USER_ACCEPTED


def test_rejection_is_logged_as_a_rejection_event():

    engine = ProvenanceEngine()

    engine.register(
        "DEC-101",
        ProvenanceStatus.ASSISTANT_PROPOSED,
    )

    engine.set_status(
        "DEC-101",
        ProvenanceStatus.REJECTED,
    )

    record = engine.get(
        "DEC-101"
    )

    assert record.events[-1].event_type is ProvenanceEventType.REJECTION


def test_quotation_does_not_change_status():
    """
    Article II.D: quotation is not adoption.
    """

    engine = ProvenanceEngine()

    engine.register(
        "NOTE-100",
        ProvenanceStatus.ASSISTANT_PROPOSED,
    )

    engine.register(
        "NOTE-101",
        ProvenanceStatus.USER_ESTABLISHED,
    )

    event = engine.quote(
        "NOTE-101",
        quoted_artifact_id="NOTE-100",
        reason="Referenced the assistant's earlier proposal",
    )

    record = engine.get(
        "NOTE-101"
    )

    assert event.event_type is ProvenanceEventType.QUOTATION

    #
    # Status is untouched. Quoting an ASSISTANT-PROPOSED note does not
    # make the quoting artifact ASSISTANT-PROPOSED, and does not adopt
    # the quoted note either.
    #
    assert record.status is ProvenanceStatus.USER_ESTABLISHED

    assert engine.get("NOTE-100").status is ProvenanceStatus.ASSISTANT_PROPOSED

    assert event.related_artifact_id == "NOTE-100"


def test_derive_creates_a_directed_lineage_edge():
    """
    Article II.B: a derived artifact must be traceable back to its source.
    """

    engine = ProvenanceEngine()

    engine.register(
        "SUMMARY-100",
        ProvenanceStatus.ASSISTANT_PROPOSED,
    )

    edge = engine.derive(
        from_artifact_id="TRANSCRIPT-001",
        to_artifact_id="SUMMARY-100",
        relation="SUMMARIZES",
    )

    assert edge.relation == "SUMMARIZES"

    sources = engine.sources_of(
        "SUMMARY-100"
    )

    assert len(sources) == 1

    assert sources[0].from_artifact_id == "TRANSCRIPT-001"

    #
    # The derivation is also visible on the record's own event log, not
    # only in the engine-level edge list.
    #
    record = engine.get(
        "SUMMARY-100"
    )

    assert record.events[-1].event_type is ProvenanceEventType.DERIVATION

    assert record.events[-1].related_artifact_id == "TRANSCRIPT-001"


def test_derive_from_untracked_source_is_allowed():
    """
    The source of a derivation need not itself be a tracked provenance
    record -- e.g. raw external material with no record of its own.
    """

    engine = ProvenanceEngine()

    engine.register(
        "SUMMARY-101",
        ProvenanceStatus.ASSISTANT_PROPOSED,
    )

    edge = engine.derive(
        from_artifact_id="EXTERNAL:some_pdf.pdf",
        to_artifact_id="SUMMARY-101",
    )

    assert edge.from_artifact_id == "EXTERNAL:some_pdf.pdf"


def test_derive_requires_a_registered_target():

    engine = ProvenanceEngine()

    try:
        engine.derive(
            from_artifact_id="SOURCE-001",
            to_artifact_id="NEVER-REGISTERED",
        )

        assert False, "expected KeyError"

    except KeyError:
        pass


def test_derivatives_of_finds_the_other_direction():

    engine = ProvenanceEngine()

    engine.register(
        "DERIVED-A",
        ProvenanceStatus.ASSISTANT_PROPOSED,
    )

    engine.register(
        "DERIVED-B",
        ProvenanceStatus.ASSISTANT_PROPOSED,
    )

    engine.derive("ROOT-001", "DERIVED-A")

    engine.derive("ROOT-001", "DERIVED-B")

    derivatives = engine.derivatives_of(
        "ROOT-001"
    )

    assert {e.to_artifact_id for e in derivatives} == {
        "DERIVED-A",
        "DERIVED-B",
    }
