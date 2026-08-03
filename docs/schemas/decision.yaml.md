# Decision schema

`record_type: decision` — durable answer to “why did I do this this way?”

```yaml
schema_version: "1"
record_type: decision

decision_id: <slug>
title: <short human label>
domain: <string|null>
status: active|superseded|contested|deferred

question: <design question>
chose: <what was chosen>
rejected:
  - item: <string>
    why_rejected: <string|null>
    provenance: ATTESTED|VERIFIED|ESTIMATED
constraints:
  - item: <string>
    provenance: ATTESTED|VERIFIED|ESTIMATED
    basis: <optional>

rationale_provenance: ATTESTED|VERIFIED|ESTIMATED|MIXED
rationale_quality: strong|partial|missing
confidence: 0.0-1.0

supersedes: []
superseded_by: null
related_decisions:
  - decision_id: <id>
    relation: depends_on|conflicts_with|refines|enables

frames: []          # frame_id list
artifacts: []       # artifact_id list
evidence_episodes: []

open_implications: []

created_at: null
updated_at: null
attested_by: null
ingest_tags: []
notes: null
```

**Rules:** `decision_id` stable once published; material new choice → new id or explicit supersession. Full code/maps live on Artifact/Frame, not here.
