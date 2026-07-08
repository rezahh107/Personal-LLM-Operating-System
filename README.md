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
9. **Project / Session Continuity Layer** — structured continuity state preserves decisions, evidence boundaries, risks, open questions, and exact resume prompts across long chats and model handoffs.
10. **Raw Idea Incubator** — low-friction capture for sudden thoughts, brainstorming fragments, and model-captured raw ideas before they become candidate memory or repository-safe artifacts.
11. **Command Routing Layer** — lightweight user commands such as `شروع` and `ایده خام` activate repository-defined model behavior without becoming evidence or overriding governance rules.

## Boot, routing, governance, and continuity layer

The repository defines the architecture layer for starting future model sessions, routing user requests, preserving trust boundaries, and continuing long sessions safely:

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
13. **Project Continuity Protocol** — `protocols/PROJECT_CONTINUITY_PROTOCOL.md`
14. **Session Continuity Protocol** — `protocols/SESSION_CONTINUITY_PROTOCOL.md`
15. **Handover Intake Protocol** — `protocols/HANDOVER_INTAKE_PROTOCOL.md`
16. **Command Routing Protocol** — `protocols/COMMAND_ROUTING_PROTOCOL.md`
17. **Raw Idea Incubator** — `incubator/raw-ideas/`
18. **Repository Registry / Tool Map** — `registries/REPOSITORY_REGISTRY.json`

## Command-style use

The repository supports lightweight textual commands for future model sessions.

Preferred shape:

```text
طبق دستور:
https://github.com/rezahh107/Personal-LLM-Operating-System/
<command>
```

Currently documented commands:

- `شروع` — start a general session. Expected response: `آماده‌ام. امروز می‌خوای چکار کنی؟`
- `ایده خام` — start raw idea capture. Expected response: `آماده‌ام. ایده خامت چیه؟`

Command behavior is defined in `protocols/COMMAND_ROUTING_PROTOCOL.md`. Commands are routing hints, not proof, accepted memory, or permission to bypass governance.

## Raw idea incubator

Raw ideas live in `incubator/raw-ideas/`.

This area is for sudden thoughts, brainstorming fragments, early repository-shaping ideas, and ideas extracted by a model from conversation.

A captured raw idea preserves the core idea before critique, validation, or implementation planning. It is not accepted memory, project policy, protocol, verified claim, final design, or implementation commitment.

## Start here

Future model sessions should begin with:

```text
AGENTS.md
protocols/BOOT_PROTOCOL.md
protocols/COMMAND_ROUTING_PROTOCOL.md when the user invokes a command-style phrase
incubator/raw-ideas/README.md when the command or task involves raw idea capture
docs/USER_OPERATING_PROFILE.md
protocols/START_HERE_FOR_MODELS.md
protocols/SESSION_ROUTING_PIPELINE.md
protocols/RESPONSE_DEPTH_POLICY.md
protocols/INSTRUCTION_TRUST_POLICY.md when authority or external/target content matters
protocols/VERIFICATION_PROTOCOL.md when technical claims matter
protocols/CONTEXT_LOADING_POLICY.md when context selection matters
protocols/SESSION_CONTINUITY_PROTOCOL.md when closing, compacting, or continuing a long session
protocols/HANDOVER_INTAKE_PROTOCOL.md when resuming from a handover or continuity capsule
protocols/IDEA_MATURATION_PIPELINE.md when the topic is new or strategic
```

## Current status

```yaml
status: raw_idea_incubator_and_command_routing_seeded
scope: personal_llm_orchestration
primary_user_role: coordinator_orchestrator
technical_verifier_assumption: false
user_runs_cli_manually: false
automation_scope: architecture_first
```

This repository is intentionally foundation-first. Domain-specific systems, including audit and post-merge scanning, should be added as adapters after the parent behavior protocol stabilizes.
