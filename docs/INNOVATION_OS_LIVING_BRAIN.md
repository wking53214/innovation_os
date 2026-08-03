# Innovation OS

Personal living-brain memory for accumulated ideas, design decisions, and code history.

## One question

> When you ask *“why did I do this this way?”* years later, can the system reconstruct the answer from **your** artifacts — not from a generic model guess?

Secondary question:

> Given what you have decided and built, what does that imply 1 / 3 / 5 years out?

## What this is

- A **decision-centric** memory graph: Decisions, Episodes, Frames, Artifacts
- Local-first, evidence-backed, provenance-aware (ATTESTED / VERIFIED / ESTIMATED)
- Compatible with interview-style capture from chat transcripts

## What this is not

- Not a second chatbot
- Not an innovation-management SaaS
- Not a replacement for git (git is evidence; this stores *why*)
- Not Sentinel OS (Sentinel proves automated runtime decisions; this proves *your* design choices)

## Core records

| Record | Role |
|--------|------|
| **Decision** | Durable answer to a design question (`chose`, constraints, supersession) |
| **Episode** | Evidence package from a chat/interview that supports decisions |
| **Frame** | Conceptual lens (technical, scriptural, symbolic) with mapping rows |
| **Artifact** | Code/docs identity (path, hash, optional body) |

Schemas: [`docs/schemas/`](docs/schemas/).

## Layout

```text
innovation_os/
  README.md
  LICENSE
  docs/
    schemas/
      decision.yaml.md
      episode.yaml.md
      frame.yaml.md
      artifact.yaml.md
    interview/
      round1_prompt.md
  memory/
    decisions/     # one YAML file per decision_id
    episodes/      # one YAML file per episode_id
    frames/
    artifacts/
  Domain/          # optional typed helpers (later)
```

## Provenance

| Tag | Meaning |
|-----|---------|
| **ATTESTED** | You explicitly stated intent or confirmed it |
| **VERIFIED** | Observable in code/paste/transcript without embellishment |
| **ESTIMATED** | Inference; never presented as settled fact |

## Capture pipeline

```text
Chat transcript
  → Round 1 inventory (interview)
  → Round 2 gap fill
  → optional attestation
  → merge into Episode YAML
  → extract/update Decision (+ Frame/Artifact) records
  → store under memory/
```

## Relationship to Sentinel OS

| Sentinel OS | Innovation OS |
|-------------|----------------|
| Why an **automated system** decided | Why **you** decided |
| Runtime evidence ledger | Personal design-memory ledger |
| External auditor | Future-you |

## Status

Bootstrap: schemas, memory directories, interview Round 1 prompt.  
No runtime query engine yet — records are file-based YAML.
