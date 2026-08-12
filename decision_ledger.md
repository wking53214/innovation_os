# Decision Ledger

Every important decision receives a permanent record.

---

# DEC-0001

## Decision

Example:

Create an Innovation OS instead of a simple idea notebook.

---

## Date

2026-07-27

---

## Context

Why was this decision considered?

---

## Options Considered

A.

B.

C.

---

## Selected Option

---

## Reason Selected

---

## Alternatives Rejected

---

## Expected Impact

---

## Related Objects

Problems:

Concepts:

Artifacts:

Questions:

---

## Status

Active

---

# DEC-0002

## Decision

Split disposition of the Cognitive Continuity Constitution v1.1 draft, provision by provision, rather than ratifying or rejecting it as a single unit.

---

## Date

2026-08-12

---

## Context

v1.1 arrived as a single bundled draft touching multiple articles. Article II.A (provenance events) and II.B (lineage edges) were already built and tested in the codebase. The draft also reintroduced a seventh provenance category ("PROVENANCE EXTERNAL TO CURRENT RECORD") that the V1 consolidation had already explicitly rejected. Five further provisions (I.G, III.F, XI.A, XII.E, XVII.A-D) had not been reviewed at all.

Article XV.A (Context Envelope) was not identified as part of v1.1 until later in the same working session. It was initially treated as pre-existing V1.0 content and only confirmed as v1.1-sourced (V1.0's Article XV did not contain this text) after the codebase's context envelope mechanism had already been scoped and built as unratified mechanism. It is included in this decision for that reason, not because it was reviewed alongside the original six items.

---

## Options Considered

A.

Ratify or reject v1.1 as a single all-or-nothing unit.

B.

Split disposition by provision: ratify what's built and uncontested, reject what conflicts with an already-settled decision, defer what's unreviewed.

C.

Leave the whole draft UNRESOLVED indefinitely.

---

## Selected Option

B

---

## Reason Selected

All-or-nothing treatment (A) would either force rejecting working, tested code over one bad provision, or force ratifying an unreviewed batch of provisions just to keep what was already built. Leaving it open (C) preserves the exact ambiguity, a proposal with no formal disposition, that the provenance system exists to prevent.

---

## Alternatives Rejected

A, C (see Reason Selected).

---

## Expected Impact

RATIFIED:
- Article II.A (provenance events)
- Article II.B (lineage edges)

REJECTED:
- Seventh provenance category ("PROVENANCE EXTERNAL TO CURRENT RECORD") — the six-category taxonomy in provenance/status.py remains closed

UNRESOLVED, queued for individual review:
- Article I.G (dependency-aware erasure)
- Article III.F (transformation integrity)
- Article XI.A (conflict-tier classification)
- Article XII.E (simulation-assumption protection)
- Article XVII.A-D (self-authentication/contamination safeguards)
- Article XV.A (context envelope) — mechanism already built (context_envelope/ package) and live on master; built-and-tested is not itself ratification (Article XVII.A: no self-authentication)

---

## Related Objects

Problems:

Concepts: provenance store, context envelope, Cognitive Continuity Constitution Article II, Article XV.A

Artifacts: src/innovation_os/provenance/, src/innovation_os/context_envelope/

Questions:

---

## Status

Active