"""
Context envelope for artifacts.

Source: Cognitive Continuity Constitution, Article XV.A. Added in the v1.1
draft -- V1.0's Article XV did not contain this text, so unlike Article
II.A/II.B this provision has not yet been through any disposition
decision at all. This module implements the mechanism so it is ready when
ratification happens. Building it does not ratify it (Article XVII.A: no
self-authentication).

Article XV.A: where available, retain contextual information associated
with an artifact -- speaker, temporal position, scope, conditions,
qualifiers, relevant antecedents, preceding/subsequent material,
provenance, lineage, related branches.

Two things this module deliberately does NOT do:

  1. Duplicate provenance/lineage storage. Article II already owns "who
     originated it" (status.py) and "what it derived from"
     (events.py: LineageEdge). This envelope's provenance/lineage fields
     are live lookups against a ProvenanceEngine, not a second copy --
     collapsing that distinction is the same three-competing-stores
     mistake this codebase already paid down once. See
     ContextEnvelopeStore.provenance_of / lineage_of.

  2. Enforce the compression rule. Article XV.A's companion constraint --
     "compressed representations must not increase scope, certainty,
     permanence, or significance" -- has no compression or summarization
     logic in this codebase yet to attach to. CompressionConstraint below
     gives that future logic a checkable shape; nothing here invokes it.

The record-recoverable / analytically-inferred distinction is structural,
not per-field: two dicts, not eight tagged fields, so "where did this
come from" is answerable at a glance rather than by inspecting every key.
Each of the eight dict keys below maps to one collapse the shorthand
formulation warns against if that context is dropped silently instead of
marked absent -- conditions -> conditional-becomes-absolute, scope ->
local-becomes-global, temporal_position -> temporary-becomes-permanent,
qualifiers -> uncertain-becomes-certain.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

from ..provenance import ProvenanceEngine, ProvenanceRecord, LineageEdge


#
# Article XV.A's context fields, minus Provenance and Lineage (see module
# docstring point 1 -- those two are live lookups, not dict entries).
# Freeform keys into the two buckets below, not a closed enum: unlike
# ProvenanceStatus, Article XV.A does not close this set, and
# "antecedents" in particular is open-ended by nature.
#
SPEAKER = "speaker"
TEMPORAL_POSITION = "temporal_position"
SCOPE = "scope"
CONDITIONS = "conditions"
QUALIFIERS = "qualifiers"
ANTECEDENTS = "antecedents"
ADJACENT_MATERIAL = "adjacent_material"
RELATED_BRANCHES = "related_branches"


class ContextOrigin(Enum):
    """Where a piece of context in the envelope came from."""

    RECORD_RECOVERABLE = "RECORD_RECOVERABLE"
    ANALYTICALLY_INFERRED = "ANALYTICALLY_INFERRED"


@dataclass
class CompressionConstraint:
    """
    Article XV.A's preservation rule, as a checkable shape rather than
    prose: a compressed representation must not score True on any axis
    where the original scored False.

    Not enforced anywhere in this module -- there is no compression logic
    yet for it to guard. A future summarizer should compute one of these
    for its input and one for its output and assert nothing flips
    False -> True.
    """

    scope: bool = False
    certainty: bool = False
    permanence: bool = False
    significance: bool = False

    def escalates_beyond(self, original: "CompressionConstraint") -> bool:
        return (
            (self.scope and not original.scope)
            or (self.certainty and not original.certainty)
            or (self.permanence and not original.permanence)
            or (self.significance and not original.significance)
        )


@dataclass
class ContextEnvelope:
    """
    One artifact's Article XV.A context, split by origin.

    recoverable -- context read directly off the record (a logged speaker
                   field, a timestamp, an explicit scope statement).
    inferred    -- context the system worked out rather than found (a
                   guessed antecedent, a scope the system judged from
                   surrounding text). Must never be presented with the
                   confidence of a recoverable fact.

    Keys in both dicts are the module-level constants above. A missing key
    means "not available", not "empty" -- Article XV.A says "where
    available", not "always present".
    """

    artifact_id: str
    recoverable: Dict[str, Any] = field(default_factory=dict)
    inferred: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def get(self, key: str) -> Optional[Any]:
        """
        Recoverable takes precedence if a key exists in both --
        record-recoverable is always the stronger claim.
        """

        if key in self.recoverable:
            return self.recoverable[key]

        return self.inferred.get(key)

    def origin_of(self, key: str) -> Optional[ContextOrigin]:

        if key in self.recoverable:
            return ContextOrigin.RECORD_RECOVERABLE

        if key in self.inferred:
            return ContextOrigin.ANALYTICALLY_INFERRED

        return None


class ContextEnvelopeStore:
    """
    Canonical envelope store, one record per artifact_id. Mirrors
    ProvenanceEngine's shape deliberately -- same "engine holds records
    keyed by artifact_id" convention -- so the two are easy to wire
    together in the same pipeline pass later (Article XV.A's Provenance
    and Lineage fields depend on that engine being attached; see below).
    """

    def __init__(
        self,
        provenance_engine: Optional[ProvenanceEngine] = None,
    ):

        self._envelopes: Dict[str, ContextEnvelope] = {}
        self._provenance_engine = provenance_engine

    def register(self, artifact_id: str) -> ContextEnvelope:

        if artifact_id in self._envelopes:
            return self._envelopes[artifact_id]

        envelope = ContextEnvelope(artifact_id=artifact_id)
        self._envelopes[artifact_id] = envelope

        return envelope

    def set_recoverable(
        self,
        artifact_id: str,
        key: str,
        value: Any,
    ) -> None:

        self._require(artifact_id).recoverable[key] = value

    def set_inferred(
        self,
        artifact_id: str,
        key: str,
        value: Any,
    ) -> None:

        self._require(artifact_id).inferred[key] = value

    def get(self, artifact_id: str) -> ContextEnvelope:

        return self._require(artifact_id)

    def provenance_of(
        self,
        artifact_id: str,
    ) -> Optional[ProvenanceRecord]:
        """
        Article XV.A's "Provenance" field, read live from the attached
        ProvenanceEngine rather than duplicated here. None if no engine
        was attached, or the artifact has no provenance record.
        """

        if self._provenance_engine is None:
            return None

        return self._provenance_engine.get(artifact_id)

    def lineage_of(
        self,
        artifact_id: str,
    ) -> List[LineageEdge]:
        """
        Article XV.A's "Lineage" field: what this artifact derived from.
        Same live-lookup approach as provenance_of -- see module
        docstring. Empty list if no engine was attached.
        """

        if self._provenance_engine is None:
            return []

        return self._provenance_engine.sources_of(artifact_id)

    def _require(self, artifact_id: str) -> ContextEnvelope:

        if artifact_id not in self._envelopes:
            raise ValueError(
                f"Unknown artifact: {artifact_id!r}"
            )

        return self._envelopes[artifact_id]
