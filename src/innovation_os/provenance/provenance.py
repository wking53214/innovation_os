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

        self.status = resolved

        return transition


class ProvenanceEngine:

    def __init__(self):

        self.records: Dict[
            str,
            ProvenanceRecord
        ] = {}

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
