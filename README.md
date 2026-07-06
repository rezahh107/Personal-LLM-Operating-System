# Personal LLM Operating System

A personal repository for structuring, governing, and reusing the user’s way of working with language models.

This repository treats the repo as **LLM memory**: a durable, structured context layer that future model sessions can read before working on a specific domain such as audit, GitHub repair, prompt engineering, image workflows, research, image generation, or document production.

## Core idea

```text
The repository is memory.
Memory must be governed.
LLMs may generate work, but no single model silently becomes the source of truth.
```

The user is the coordinator and goal owner, not the technical verifier for most specialist claims. Technical certainty must come from tools, validators, evidence, second-model critique, stronger-model review, or explicit uncertainty handling.

## Repository pillars

1. **Repository as LLM Memory** — stable, scoped, source-aware memory for future model sessions.
2. **Idea Maturation Pipeline** — a repeatable path for turning rough thoughts into mature artifacts.
3. **Model Workforce Architecture** — clear model roles such as Inspector, Skeptic, Builder, Reporter, and Handoff Writer.
4. **Claim Lifecycle** — every important assertion moves through draft, candidate, challenged, validated, accepted, quarantined, deprecated, or rejected states.
5. **Handoff Contracts** — model outputs must preserve evidence, uncertainty, limits, and allowed next actions for downstream models.
6. **Governed Memory Runtime** — model-facing scripts, fixtures, ledgers, and CI checks prevent the repository from becoming a prose-only policy book.
7. **Domain Adapters** — audit, GitHub repair, prompt engineering, image workflows, and other domains inherit the parent protocol.

## Start here

Future model sessions should begin with:

```text
AGENTS.md
protocols/START_HERE_FOR_MODELS.md
protocols/IDEA_MATURATION_PIPELINE.md when the topic is new or strategic
```

## Current status

```yaml
status: governed_memory_runtime_mvp
scope: personal_llm_orchestration
primary_user_role: coordinator_orchestrator
technical_verifier_assumption: false
user_runs_cli_manually: false
```

This repository is intentionally foundation-first. Domain-specific systems, including audit and post-merge scanning, should be added as adapters after the parent behavior protocol stabilizes.
