# Frame schema

`record_type: frame` — durable conceptual lens (technical, scriptural, symbolic, mixed).

```yaml
schema_version: "1"
record_type: frame

frame_id: <slug>
title: <string>
kind: technical|scriptural|theological|symbolic|process|legal|mixed
status: active|superseded|contested|draft
domain: <string|null>

summary: <string>
scope: <string>

question: <string|null>
chose: <string|null>
rejected: []
binding:
  level: binding|heuristic|illustrative|unknown
  statement: <string|null>
  provenance: ATTESTED|VERIFIED|ESTIMATED|UNKNOWN

mapping_entries:
  - entry_id: <optional>
    source: <string>
    source_ref: <string|null>
    target: <string>
    meaning: <string>
    direction: source_to_target|bidirectional|unknown
    provenance: ATTESTED|VERIFIED|ESTIMATED
    basis: <string|null>
    status: active|deprecated|uncertain

structure:
  ordered: true|false
  nodes: []

rationale_provenance: ATTESTED|VERIFIED|ESTIMATED|MIXED|UNKNOWN
rationale_quality: strong|partial|missing
coverage_quality: strong|partial|missing
confidence:
  identity: 0.0
  ontology_rationale: 0.0
  mapping_fidelity: 0.0

supersedes: []
superseded_by: null
related_frames: []
evidence_episodes: []
decisions_using: []
artifacts_related: []

ingest_tags: []
needs_human_attestation: []
attested_by: null
created_at: null
updated_at: null
notes: null
```

**Rules:** Do not omit scriptural/theological frames. `binding.level` must be explicit. Incomplete maps use `coverage_quality: partial`.
