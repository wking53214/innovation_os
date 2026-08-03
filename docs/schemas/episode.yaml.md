# Episode schema

`record_type: episode` — evidence package from a chat/interview.

```yaml
schema_version: "1"
record_type: episode

episode_id: <slug>
title: <short label>
episode_kind: repair|design|exploration|ops|mixed

transcript_span:
  focus: <one line>
  related_topics: []

source_refs:
  - type: transcript|attachment|git|attestation|interview
    locator: <string>
    note: <optional>

question: <string>
chose: <string or unsettled>
rejected: []
constraints: []
open_questions: []

supports_decisions:
  - decision_id: <id>
    strength: supports|weakly_supports|mentions
frames_referenced: []
artifacts_referenced: []

evidence: []
participants_decisions: []

code_evolution: []
final_code:
  available: full|partial|none|missing
  language: unknown
  filename_hint: null
  content_hash: null
  notes: null

structural_snapshot:
  systems_named: []
  symbols_named: []
  identity_sentence: null

provenance:
  question: ATTESTED|VERIFIED|ESTIMATED
  chose: ATTESTED|VERIFIED|ESTIMATED|UNSETTLED
  notes: null

overall_rationale_quality:
  repair: strong|partial|missing
  architecture: strong|partial|missing
  ontology: strong|partial|missing

confidence:
  identity: 0.0
  repair_rationale: 0.0
  architecture_rationale: 0.0
  ontology_rationale: 0.0
  completeness: 0.0

interview:
  rounds_completed: 0
  status: open|ready_to_ingest|ingested
  contamination_flags: []

ingest_tags: []
needs_human_attestation: []
created_at: null
notes: null
```

**Rules:** Episodes cite Decisions; they are not the long-term home of “why.” Prefer Artifact for full source bodies.
