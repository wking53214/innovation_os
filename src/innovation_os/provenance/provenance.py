"""
Canonical provenance store.

This module supersedes the former provenance/engine.py and
provenance/tracker.py, which defined competing ProvenanceRecord shapes under
colliding class names. Their useful fields (metadata, history) were merged
here. There is exactly one provenance store in this package.

Two distinct facts are tracked per artifact and must not be conflated:

    status  -- WHO originated it (Article II taxonomy, closed set)
    source  -- WHERE it came from (freeform locator: a path, a URI, a
               conversation id). Carries no authority claim.

A status change is recorded as a transition, never as a silent overwrite.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional

from .status import ProvenanceStatus
from .events import LineageEdge, ProvenanceEvent, ProvenanceEventType

#
# Default mapping from a status transition's destination to an Article
# II.A event type. Not itself constitutional text -- Article II.A lists
# the event types but does not prescribe this mapping. Anything not listed
# here (e.g. a transition to UNRESOLVED) is logged as MODIFICATION.
#
_EVENT_TYPE_FOR_STATUS = {
    ProvenanceStatus.USER_ACCEPTED: ProvenanceEventType.ADOPTION,
    ProvenanceStatus.REJECTED: ProvenanceEventType.REJECTION,
}


@dataclass
class StatusTransition:
    """
    One provenance status change. The prior status is retained here so it
    survives the change.
    """

    artifact_id: str
    from_status: ProvenanceStatus
    to_status: ProvenanceStatus
    at: datetime
    reason: str = ""


@dataclass
class ProvenanceRecord:

    artifact_id: str

    #
    # Article II category. Required, no default: registration without an
    # explicit determination is a TypeError, not a guess.
    #
    status: ProvenanceStatus

    #
    # Freeform locator. Not an authority claim.
    #
    source: str = ""

    created: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    relationships: List[str] = field(
        default_factory=list
    )

    #
    # Merged from the former engine.py.
    #
    metadata: Dict[str, str] = field(
        default_factory=dict
    )

    history: List[str] = field(
        default_factory=list
    )

    transitions: List[StatusTransition] = field(
        default_factory=list
    )

    #
    # Article II.A typed events. Superset of `transitions`: every status
    # change also produces an event here, plus event types that never
    # touch status (QUOTATION, DERIVATION). Additive -- `transitions`
    # keeps its original meaning and existing callers are unaffected.
    #
    events: List[ProvenanceEvent] = field(
        default_factory=list
    )

    @property
    def initial_status(self) -> ProvenanceStatus:
        """
        The status this artifact was first registered under, recovered from
        the transition log. Never lost, however many changes follow.
        """

        if self.transitions:
            return self.transitions[0].from_status

        return self.status

    def apply_status(
        self,
        new_status,
        reason: str = "",
    ) -> StatusTransition:
        """
        The only supported path for changing status. Appends a transition
        recording the prior value, then advances the current value.

        A re-affirmation of the same status is still recorded. An explicit
        restatement of provenance is itself a fact about the record.
        """

        resolved = ProvenanceStatus.coerce(
            new_status
        )

        transition = StatusTransition(
            artifact_id=self.artifact_id,
            from_status=self.status,
            to_status=resolved,
            at=datetime.now(timezone.utc),
            reason=reason,
        )

        self.transitions.append(
            transition
        )

        #
        # Article II.A: a later event does not silently rewrite an earlier
        # one. transitions[] already guarantees this for status; events[]
        # gives the same guarantee a typed name (ADOPTION, REJECTION, ...)
        # instead of a bare status pair.
        #
        self.events.append(
            ProvenanceEvent(
                artifact_id=self.artifact_id,
                event_type=_EVENT_TYPE_FOR_STATUS.get(
                    resolved,
                    ProvenanceEventType.MODIFICATION,
                ),
                reason=reason,
                from_status=transition.from_status,
                to_status=transition.to_status,
            )
        )

        self.status = resolved

        return transition


class ProvenanceEngine:

    def __init__(self):

        self.records: Dict[
            str,
            ProvenanceRecord
        ] = {}

        #
        # Article II.B lineage edges. Kept at the engine level, not on a
        # single record, because a derivation has two endpoints and the
        # source artifact may not itself be a tracked record (e.g. raw
        # external material).
        #
        self.edges: List[LineageEdge] = []

    def register(
        self,
        artifact_id: str,
        status,
        source: str = "",
        metadata: Optional[dict] = None,
    ) -> ProvenanceRecord:
        """
        Register an artifact under an Article II category.

        `status` is positional and second. A caller written against the old
        freeform signature will pass a locator here and fail loudly with
        ValueError rather than silently recording a bogus category.
        """

        record = ProvenanceRecord(
            artifact_id=artifact_id,
            status=ProvenanceStatus.coerce(
                status
            ),
            source=source,
            created=datetime.now(timezone.utc),
            metadata=metadata or {},
        )

        self.records[artifact_id] = record

        #
        # Registration is the ORIGIN event (Article II.A). Logged here so
        # every tracked artifact has one, unconditionally.
        #
        record.events.append(
            ProvenanceEvent(
                artifact_id=artifact_id,
                event_type=ProvenanceEventType.ORIGIN,
                to_status=record.status,
            )
        )

        return record

    def set_status(
        self,
        artifact_id: str,
        new_status,
        reason: str = "",
    ) -> StatusTransition:

        record = self.records.get(
            artifact_id
        )

        if record is None:
            raise KeyError(
                f"Unknown artifact: {artifact_id!r}"
            )

        return record.apply_status(
            new_status,
            reason=reason,
        )

    def transitions(
        self,
        artifact_id: str,
    ) -> List[StatusTransition]:

        record = self.records.get(
            artifact_id
        )

        if record is None:
            return []

        return record.transitions

    def link(
        self,
        artifact_id: str,
        relationship: str,
    ):

        record = self.records.get(
            artifact_id
        )

        if record:
            record.relationships.append(
                relationship
            )

        return record

    def add_history(
        self,
        artifact_id: str,
        event: str,
    ):
        """
        Merged from the former engine.py. Free-text audit events. Not a
        provenance determination; use set_status for that.
        """

        record = self.records.get(
            artifact_id
        )

        if record:
            record.history.append(
                event
            )

        return record

    def get(
        self,
        artifact_id: str,
    ) -> Optional[ProvenanceRecord]:

        return self.records.get(
            artifact_id
        )

    def quote(
        self,
        artifact_id: str,
        quoted_artifact_id: str,
        reason: str = "",
    ) -> ProvenanceEvent:
        """
        Record that `artifact_id` quotes `quoted_artifact_id`.

        Article II.D: quotation is not adoption. This never touches
        `status`. If you want adoption, call set_status with USER_ACCEPTED.
        """

        record = self.records.get(
            artifact_id
        )

        if record is None:
            raise KeyError(
                f"Unknown artifact: {artifact_id!r}"
            )

        event = ProvenanceEvent(
            artifact_id=artifact_id,
            event_type=ProvenanceEventType.QUOTATION,
            reason=reason,
            related_artifact_id=quoted_artifact_id,
        )

        record.events.append(
            event
        )

        return event

    def derive(
        self,
        from_artifact_id: str,
        to_artifact_id: str,
        relation: str = "DERIVED_FROM",
        reason: str = "",
    ) -> LineageEdge:
        """
        Record that `to_artifact_id` was derived from `from_artifact_id`
        (Article II.B). `to_artifact_id` must already be a registered
        record; `from_artifact_id` need not be (it may be raw external
        material with no provenance record of its own).
        """

        to_record = self.records.get(
            to_artifact_id
        )

        if to_record is None:
            raise KeyError(
                f"Unknown artifact: {to_artifact_id!r}"
            )

        edge = LineageEdge(
            from_artifact_id=from_artifact_id,
            to_artifact_id=to_artifact_id,
            relation=relation,
            reason=reason,
        )

        self.edges.append(
            edge
        )

        to_record.events.append(
            ProvenanceEvent(
                artifact_id=to_artifact_id,
                event_type=ProvenanceEventType.DERIVATION,
                reason=reason,
                related_artifact_id=from_artifact_id,
            )
        )

        return edge

    def sources_of(
        self,
        artifact_id: str,
    ) -> List[LineageEdge]:
        """Edges where `artifact_id` is the derived (to) side."""

        return [
            e for e in self.edges
            if e.to_artifact_id == artifact_id
        ]

    def derivatives_of(
        self,
        artifact_id: str,
    ) -> List[LineageEdge]:
        """Edges where `artifact_id` is the source (from) side."""

        return [
            e for e in self.edges
            if e.from_artifact_id == artifact_id
        ]

    def events_for(
        self,
        artifact_id: str,
    ) -> List[ProvenanceEvent]:

        record = self.records.get(
            artifact_id
        )

        return record.events if record else []
