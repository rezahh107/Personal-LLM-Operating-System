# Project Continuity Protocol

Purpose: define durable project handover architecture without turning free-form notes into the source of truth.

## Core distinction

```text
Source Archive
≠
Repository Transfer
≠
Project Handover
≠
Session Continuity
```

### Source Archive

A source archive is a source tree snapshot.

It may include files, directories, generated artifacts, or exported source code. It is useful for inspection, but it is not enough for project handover because it does not necessarily preserve:

- repository refs or history;
- uncommitted work;
- evidence boundaries;
- accepted decisions;
- active risks;
- not-run validation;
- exact continuation instructions.

### Repository Transfer

A repository transfer describes the technical state of a repository revision.

It may include:

- repository URL and default branch;
- checked ref, commit SHA, branch, or tag;
- available history or ref limits;
- working tree state;
- uncommitted diff;
- untracked files;
- LFS and submodule status;
- lock files and dependency state;
- validation commands and whether they were actually run.

Repository transfer is necessary for code work, but it is still not a complete project handover.

### Project Handover Package

A project handover package is a durable project continuation object.

It combines four conceptual layers:

1. **Repository Transfer** — exact source/revision/worktree state.
2. **Durable Project Knowledge** — architecture, requirements, ADRs, protocols, constraints, known limitations, roadmap, build/test/release instructions.
3. **Current Operational State** — active branch, active PR, current phase, blockers, next allowed action, open risks, pending review items.
4. **Evidence and Integrity** — evidence map, provenance, verification status, not-run checks, source authority classification, optional hashes where available.

Project handover is larger and more durable than a session continuity capsule.

### Session Continuity Capsule

A session continuity capsule preserves the state of a specific conversation or work session so the user can continue in a new chat or another model.

It is not a complete project archive. It focuses on:

- current mental model;
- confirmed decisions;
- candidate ideas;
- evidence and source map;
- uncertainty;
- active risks;
- not-run checks;
- do-not-assume list;
- exact resume prompt.

## Canonical source principle

Handover documents are rendered views.

The canonical source of truth for a handover package is the structured handover state, not free-form Markdown.

Markdown documents may be used for human readability, but they must not silently become canonical when they diverge from the structured state.

## Structured state requirements

A project handover state should include:

```yaml
handover_type: project_handover
handover_version: string
project_id: string
source_archive: object | null
repository_transfer: object
durable_project_knowledge: object
current_operational_state: object
evidence_and_integrity: object
rendered_views: []
instruction_authority: object
verification_summary: object
known_gaps: []
```

## Truthfulness rules

Every factual project claim in a project handover must be classified as one of:

```yaml
truth_status:
  - evidence-backed
  - derived_with_lineage
  - explicitly_proposed
  - connected_to_structured_gap
  - not_applicable
```

Do not convert:

- conversation assumptions into requirements;
- proposals into accepted decisions;
- code inspection into runtime verification;
- changed code into verified fix;
- documented command into executed command;
- model agreement into proof.

Use `insufficient_evidence` when a required source is unavailable.

## Instruction authority in handover packages

Apply `protocols/INSTRUCTION_TRUST_POLICY.md`.

A handover manifest should classify authority for included content, for example:

```yaml
instruction_authority:
  start_here:
    authority: handover_control_document
  frozen_contract:
    authority: project_frozen_contract
  audit_attachment:
    authority: evidence_only
  web_capture:
    authority: evidence_only
  prior_model_output:
    authority: none_unless_verified
```

## Non-goals for this protocol

This protocol does not implement:

- ZIP generation;
- artifact hashing;
- a renderer;
- a crawler;
- a vector database;
- a background agent;
- automatic memory capture;
- domain-specific implementation logic.

Those may be separate future work only after the structured contract stabilizes.
