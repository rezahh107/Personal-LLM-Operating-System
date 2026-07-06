# Personal LLM Operating System

A personal repository for structuring, governing, and reusing the user’s way of working with language models.

This repository treats the repo as **LLM memory**: a durable, structured context layer that future model sessions can read before working on a specific domain such as audit, GitHub repair, prompt engineering, image workflows, research, image generation, or document production.

## Core idea

```text
The repository is memory.
Memory must be governed.
LLMs may generate work, but no single model silently becomes the source of truth.
```

The user is the coordinator and goal owner, not the technical verifier for most specialist claims. Technical certainty must come from tools, validators, evidence, source review, fixtures, CI checks, or explicit uncertainty handling.

## Repository pillars

1. **Repository as LLM Memory** — stable, scoped, source-aware memory for future model sessions.
2. **Idea Maturation Pipeline** — a repeatable path for turning rough thoughts into mature artifacts.
3. **Model Workforce Architecture** — clear model roles such as Inspector, Skeptic, Builder, Reporter, and Handoff Writer.
4. **Claim Lifecycle** — every important assertion moves through draft, candidate, challenged, validated, accepted, quarantined, deprecated, or rejected states.
5. **Handoff Contracts** — model outputs must preserve evidence, uncertainty, limits, and allowed next actions for downstream models.
6. **Governed Memory Runtime** — model-facing scripts, fixtures, ledgers, and CI checks prevent the repository from becoming a prose-only policy book.
7. **Domain Adapters** — audit, GitHub repair, prompt engineering, image workflows, and other domains inherit the parent protocol.
8. **Trust / Provenance / Verification Layer** — governance authority, epistemic support, verification status, and lifecycle status are separate.

## Boot, routing, and governance layer

The repository defines the architecture layer for starting future model sessions, routing user requests, and preserving trust boundaries:

1. **Boot Protocol** — `protocols/BOOT_PROTOCOL.md`
2. **User Operating Profile** — `docs/USER_OPERATING_PROFILE.md`
3. **Session / Context Routing** — `protocols/SESSION_ROUTING_PIPELINE.md`
4. **Response Depth Policy** — `protocols/RESPONSE_DEPTH_POLICY.md`
5. **External Knowledge Policy** — `protocols/EXTERNAL_KNOWLEDGE_POLICY.md`
6. **Knowledge Capture Protocol** — `protocols/KNOWLEDGE_CAPTURE_PROTOCOL.md`
7. **Memory Lifecycle / Review / Decay** — `protocols/MEMORY_REVIEW_AND_DECAY.md`
8. **Instruction Trust Policy** — `protocols/INSTRUCTION_TRUST_POLICY.md`
9. **Verification Protocol** — `protocols/VERIFICATION_PROTOCOL.md`
10. **Provenance Policy** — `protocols/PROVENANCE_POLICY.md`
11. **Context Loading Policy** — `protocols/CONTEXT_LOADING_POLICY.md`
12. **Multi-Model Review Policy** — `protocols/MULTI_MODEL_REVIEW_POLICY.md`
13. **Repository Registry / Tool Map** — `registries/REPOSITORY_REGISTRY.json`

## Start here

Future model sessions should begin with:

```text
AGENTS.md
protocols/BOOT_PROTOCOL.md
docs/USER_OPERATING_PROFILE.md
protocols/START_HERE_FOR_MODELS.md
protocols/SESSION_ROUTING_PIPELINE.md
protocols/RESPONSE_DEPTH_POLICY.md
protocols/INSTRUCTION_TRUST_POLICY.md when authority or external/target content matters
protocols/VERIFICATION_PROTOCOL.md when technical claims matter
protocols/CONTEXT_LOADING_POLICY.md when context selection matters
protocols/IDEA_MATURATION_PIPELINE.md when the topic is new or strategic
```

## Current status

```yaml
status: trust_provenance_verification_hardening
scope: personal_llm_orchestration
primary_user_role: coordinator_orchestrator
technical_verifier_assumption: false
user_runs_cli_manually: false
automation_scope: architecture_first
```

This repository is intentionally foundation-first. Domain-specific systems, including audit and post-merge scanning, should be added as adapters after the parent behavior protocol stabilizes.
