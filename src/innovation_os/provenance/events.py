"""
Provenance event taxonomy and lineage edges.

Source: Cognitive Continuity Constitution, Article II.A (events) and
Article II.B (lineage). Unlike status.py's six categories, Article II.A/II.B
are NOT ratified as of this file. This module implements the mechanism so
it is ready when ratification happens. Building it does not ratify it
(Article XVII.A: no self-authentication). Nothing in this package wires
these types into a status determination on its own.

Two additive concepts:

    ProvenanceEvent -- a typed thing that happened to an artifact's
                        provenance. Broader than a status change: a
                        QUOTATION must be recorded but must NOT move status
                        (Article II.D, quotation is not adoption). from_status
                        and to_status are None for events that don't assert
                        a category change.

    LineageEdge      -- a directed link from a derived artifact back to the
                         material it came from (Article II.B). This is
                         distinct from ProvenanceEngine.link(), which is a
                         legacy freeform, undirected tag on a single record.
                         Do not collapse the two without checking both call
                         sites -- that collapse is what created the
                         three-competing-stores problem this package was
                         already rewritten once to fix.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from .status import ProvenanceStatus


class ProvenanceEventType(Enum):

    ORIGIN = "ORIGIN"
    MODIFICATION = "MODIFICATION"
    QUOTATION = "QUOTATION"
    ADOPTION = "ADOPTION"
    REJECTION = "REJECTION"
    DERIVATION = "DERIVATION"
    SUPERSESSION = "SUPERSESSION"
    ERASURE = "ERASURE"


@dataclass
class ProvenanceEvent:

    artifact_id: str
    event_type: ProvenanceEventType
    at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    reason: str = ""

    #
    # None for events that don't assert a category change (QUOTATION,
    # DERIVATION). Set for events produced alongside a status transition
    # (ADOPTION, REJECTION, MODIFICATION, and ORIGIN at registration).
    #
    from_status: Optional[ProvenanceStatus] = None
    to_status: Optional[ProvenanceStatus] = None

    #
    # The other artifact involved, for events that reference one
    # (QUOTATION target, DERIVATION source).
    #
    related_artifact_id: Optional[str] = None


@dataclass
class LineageEdge:
    """
    to_artifact_id was derived from from_artifact_id.

    relation is freeform ("SUMMARIZES", "DERIVED_FROM", "TRANSLATES", ...)
    because Article II.B does not close this taxonomy the way Article II
    closes the status categories. Do not validate it against a fixed set.
    """

    from_artifact_id: str
    to_artifact_id: str
    relation: str = "DERIVED_FROM"
    at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    reason: str = ""
