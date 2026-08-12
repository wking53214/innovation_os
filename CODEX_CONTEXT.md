# Codex Context: Innovation OS

## Purpose

Innovation OS is a Python 3.11+ prototype for preserving the traceability of
innovation work: from a problem through ideas, decisions, review, approval,
and implementation.  Its operating principle is: **AI proposes, systems
evaluate, humans authorize**.

The repository also contains a local-first "living-brain" memory ledger.  It
captures the rationale behind design decisions in YAML, with explicit evidence
and provenance, rather than attempting to replace Git or act as a chatbot.

## Repository layout

```text
src/innovation_os/              # Python implementation (341 .py files)
tests/                          # pytest suite (245 tests at last verification)
docs/                           # MVP, development, architecture, schemas, V2 plans
memory/                         # file-based decision/episode/artifact ledger
demos/                          # runnable MVP/demo scripts
CEE-0001/                       # captured concept/conversation materials
*.md (repository root)          # product and subsystem design notes
pyproject.toml                  # package and pytest configuration
```

The project uses the `src/` layout and setuptools.  The distribution is named
`innovation-os`, while much of the current code imports modules as
`src.innovation_os...`; preserve the import style already used by nearby code
unless deliberately undertaking a packaging cleanup.

## Architecture

### Core innovation flow

The intended business flow is:

```text
Problem -> Ideation -> Alignment -> Review -> Nature-inspired translation
        -> Solution -> Forecast / Code Registry -> Human approval
```

The original MVP is composed of small, mostly in-memory engines and dataclass
models.  Important areas include:

- `core/`, `models.py`: shared pipeline/result and basic record models.
- `ideation/`, `problem/`, `review/`, `branches/`, `decision/`, `solution/`:
  the innovation lifecycle.
- `registry/`, `code_registry/`, `code_scanner/`, `repository/`, `archive/`:
  artifact and repository ingestion/mapping.
- `graph/`, `graph_storage/`, `relationships/`, `relationship_engine/`,
  `linking/`, `matching/`, `similarity/`, `search/`: connection, discovery,
  storage, and retrieval capabilities.
- `provenance/`, `timeline/`, `history/`, `memory/`, `continuity.py`, `pins.py`:
  historical context and traceability.
- `governance/`, `review_queue/`, `health/`, `lifecycle/`, `forecast/`,
  `nature/`: evaluation, approval, reporting, and supporting analyses.
- `api/`, `cli/`, `ingest/`, `workflows/`, `integration/`: lightweight entry
  points and composition helpers.

There are some historical overlaps (for example `decision/` and `decisions/`,
and two graph implementations).  Treat them as existing compatibility/MVP
surfaces; do not merge or remove them incidentally.

### Intelligence V2

`src/innovation_os/intelligence/` is the larger, newer subsystem.  It is
organized around stable contracts and an `IntelligenceArtifact` output:

```text
signals (observations, repository events, telemetry, external payloads)
  -> IntelligenceSystem / Runtime
  -> cognitive pipeline
  -> governed intelligence artifact
```

Its principal groups are `contracts/`, `engines/`, `kernel/`, `runtime/`,
`pipeline/`, `cognition/`, `knowledge/`, `reasoning/`, `governance/`,
`integration/`, and `observability/`.  The canonicalization plans and export
inventories under `docs/architecture/intelligence_v2/` are the reference when
working in this subsystem.  Maintain immutable identity, confidence,
provenance, metadata, serialization compatibility, deterministic bootstrap,
and backwards compatibility as described there.

### Living-brain ledger

`memory/` contains one YAML record per decision or episode, with schemas in
`docs/schemas/`.  Core records are `Decision`, `Episode`, `Frame`, and
`Artifact`; provenance is labelled `ATTESTED`, `VERIFIED`, or `ESTIMATED`.
Use these records for durable rationale and evidence.  Keep inferred material
separate from settled/attested facts.

The current seed records concern the OBSERVE (clinical risk) and PERCEIVE
(governance/consensus) systems.  They explicitly say the consolidated kernels
are **not production-ready**, and that governance enforcement remains
advisory/default-off unless enabled.  The ledger is file-based; no runtime
query engine is currently implemented for it.

## Conventions

- Use standard-library Python only unless a change explicitly adds a dependency;
  `pyproject.toml` currently declares no runtime dependencies.
- Models are generally `@dataclass` types; engines are stateful classes with
  simple CRUD/query methods and in-memory lists or dictionaries.
- Prefer type annotations and keep methods narrowly focused.  Existing
  formatting is simple, with occasional generous vertical whitespace; match
  the edited module rather than applying a repo-wide reformat.
- Place feature tests under the matching `tests/<area>/` directory.  Test files
  use `test_*.py` and pytest's plain `assert` style.
- Keep provenance/traceability intact when changing decision, graph, registry,
  or memory behavior.  Human approval is a deliberate control point.
- Do not treat architecture inventories, release manifests, or the memory
  ledger as generated disposable files without confirming their role first.

## Commands

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
pytest -q
python3 demos/run_innovation_demo.py
python -m src.innovation_os.cli.main status
```

`pytest.ini`/`pyproject.toml` point pytest at `tests/` and add the repository
root to its Python path.

## Current verified state (2026-08-03)

- Branch: `main`.
- Test verification: `pytest -q` completed successfully with **245 passed**
  in 1.56 seconds.
- The package is an MVP/foundation with broad subsystem coverage; the
  documentation calls the v0.1.0 MVP foundation complete, while the separate
  OBSERVE/PERCEIVE records explicitly withhold production-readiness.
- Pre-existing working-tree changes were preserved: `innovation_os_bootstrap.zip`
  is deleted and `LICENSE` is untracked.  This context file is an additional
  documentation change.

## Useful references

- `README.md`: short project overview and basic commands.
- `ARCHITECTURE.md` and `docs/ARCHITECTURE.md`: MVP/system layer descriptions.
- `docs/DEVELOPMENT.md`: local development workflow.
- `RELEASE.md`: v0.1.0 foundation release scope.
- `docs/INNOVATION_OS_LIVING_BRAIN.md`: memory-ledger intent and capture flow.
- `docs/architecture/intelligence_v2/`: V2 contracts, inventories, and
  consolidation/canonicalization guidance.
