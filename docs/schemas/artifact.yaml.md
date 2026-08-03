# Artifact schema

`record_type: artifact` — code or document identity (path, hash, optional body).

```yaml
schema_version: "1"
record_type: artifact

artifact_id: <slug>
title: <string>
kind: source|doc|config|other
status: active|missing|superseded

filenames:
  - <string>
canonical_path: <string|null>
content_hash: <sha256|null>
language: <string|null>
line_count: <int|null>

summary: <string|null>
symbols_named: []

body_available: full|partial|none|missing
body_ref: <path within repo or external|null>
# Prefer storing large bodies as files under memory/artifacts/files/ and set body_ref

related_decisions: []
related_episodes: []
related_frames: []

provenance: VERIFIED|ATTESTED|ESTIMATED|MIXED
confidence: 0.0-1.0

created_at: null
updated_at: null
notes: null
ingest_tags: []
```

**Rules:** Prefer hash + path over duplicating huge sources in Episode YAML. If recovery fails (`CANNOT ACCESS FILE`), `body_available: missing` and keep filename-only inventory.
