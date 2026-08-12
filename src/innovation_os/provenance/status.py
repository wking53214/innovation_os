"""
Canonical provenance taxonomy.

Source of truth: Cognitive Continuity Constitution, Article II (ratified).

These six categories are closed. Do not add, rename, or merge members
without a ratified amendment to Article II. The enum values below are the
exact Article II labels so that serialized records match the ratified text.

Article II, operative constraint:

    The system must not guess provenance. A machine-generated concept does
    not become human-originated merely because it later appears in a
    human-authored artifact unless the record establishes human adoption.

PROVENANCE_UNCERTAIN is the honest label for "the record does not permit
determination". It is not a default and must never be applied to stand in
for a category the record could actually establish.
"""

from enum import Enum


class ProvenanceStatus(Enum):

    #
    # The human explicitly originated, defined, or established the concept.
    #
    USER_ESTABLISHED = "USER-ESTABLISHED"

    #
    # The machine proposed the concept and the human subsequently and
    # explicitly adopted it.
    #
    USER_ACCEPTED = "USER-ACCEPTED"

    #
    # The machine introduced the concept and the human has not adopted it.
    #
    ASSISTANT_PROPOSED = "ASSISTANT-PROPOSED"

    #
    # The concept has been discussed but no final human determination exists.
    #
    UNRESOLVED = "UNRESOLVED"

    #
    # The human explicitly rejected or corrected the concept.
    #
    REJECTED = "REJECTED"

    #
    # The available record does not permit reliable determination of origin.
    #
    PROVENANCE_UNCERTAIN = "PROVENANCE UNCERTAIN"

    @classmethod
    def coerce(
        cls,
        value,
    ):
        """
        Resolve a value to a canonical ProvenanceStatus.

        Accepts a ProvenanceStatus, an Article II label ("USER-ESTABLISHED"),
        or a member name ("USER_ESTABLISHED"), case-insensitively.

        Raises ValueError for anything else. This is the gate that stops an
        artifact from being registered under an undefined category, which is
        how the old freeform `source` string was being misused.
        """

        if isinstance(value, cls):
            return value

        if isinstance(value, str):

            key = (
                value.strip()
                .upper()
                .replace("-", "_")
                .replace(" ", "_")
            )

            if key in cls.__members__:
                return cls.__members__[key]

        raise ValueError(
            "Undefined provenance category: "
            f"{value!r}. Article II defines exactly six: "
            + ", ".join(m.value for m in cls)
        )
