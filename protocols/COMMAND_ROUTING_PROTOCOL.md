# Command Routing Protocol

Purpose: define lightweight command-style phrases that activate repository-defined model behavior.

## Scope

This protocol covers non-destructive text commands written by the user in a model session, usually after a repository reference.

It does not define a shell, CLI, executable automation system, or permission to modify files without user-approved repository-write scope.

## Repository-wide rule

This protocol is repository-wide.

A command may be used before any domain-specific workflow, including audit, GitHub repair, prompt engineering, image workflow, research, document production, Elementor/EV4 work, or future adapters.

The command selects the initial behavior route. After that, the model must continue through ordinary routing in `protocols/SESSION_ROUTING_PIPELINE.md` and load domain-specific context only when the user's follow-up task needs it.

Commands are allowed to activate behavior. They are not allowed to bypass:

- system or developer instructions;
- safety rules;
- instruction-trust classification;
- evidence requirements;
- verification requirements;
- repository-write boundaries;
- memory promotion gates.

## Command invocation shape

Preferred form:

```text
طبق دستور:
https://github.com/rezahh107/Personal-LLM-Operating-System/
<command>
```

The model should treat surrounding whitespace and line breaks as insignificant.

The repository URL tells the model which operating layer to use. The command line tells the model which route to activate.

If the command includes a later domain topic, route the command first, then classify the domain task normally.

## Current commands

### `شروع`

Intent: start a general model session using this repository as operating context.

Expected response:

```text
آماده‌ام. امروز می‌خوای چکار کنی؟
```

Behavior:

1. Enter boot plus task-intake mode.
2. Do not summarize the repository unless asked.
3. Wait for the user's task.
4. Load deeper context only after the task is known.
5. After the user gives the task, route it through `protocols/SESSION_ROUTING_PIPELINE.md`.

### `ایده خام`

Intent: start low-friction raw idea capture.

Expected response:

```text
آماده‌ام. ایده خامت چیه؟
```

Behavior:

1. Ask for the raw idea without over-framing it.
2. Preserve the user's core idea first.
3. Treat the raw idea as applicable to any domain unless the user narrows it.
4. After enough context is available, propose or create a raw idea record under `incubator/raw-ideas/` when repository-write scope is active.
5. If repository-write scope is not active, provide a ready-to-save raw idea record.
6. Mark the captured item as `status: raw_idea` and `verification_status: unverified`.
7. Do not promote the idea into accepted memory, policy, protocol, or implementation without a separate promotion gate.

## Command handling rules

1. Commands are routing hints, not evidence.
2. Commands may activate a response mode, but they do not override higher-priority system, developer, safety, repository, or user instructions.
3. Commands must be non-destructive by default.
4. Repository writes require explicit user intent or an active repository-write task.
5. If the command is unknown, ask for clarification and do not invent command behavior.
6. If the model cannot access the repository, it should still follow the visible command text when possible and state that repository files were not inspected.
7. If command behavior conflicts with another protocol, report the conflict and follow the higher-authority source.
8. Command definitions should not be duplicated across unrelated files; use this protocol as the canonical command behavior reference until a registry exists.

## Raw idea command boundary

The `ایده خام` command captures possibility, not truth.

A model-captured raw idea may include:

- core idea;
- user raw intent;
- conversation context;
- why it may matter later;
- what it is not;
- possible future development;
- open questions;
- next review trigger.

A model-captured raw idea must not be represented as:

- accepted memory;
- verified claim;
- repository rule;
- implementation commitment;
- final architecture.

## User-facing guide

The user-facing and model-facing overview is `docs/COMMANDS_AND_RAW_IDEAS.md`.

Use that document when a model needs a short explanation of command-style usage and raw idea capture.

## Future extension path

If commands grow beyond a few entries, add a machine-readable command registry with at least:

```yaml
command: string
aliases: list[string]
intent: string
expected_response: string
route: string
allowed_actions: list[string]
write_scope_required: boolean
status: candidate | active | deprecated
```

Until such a registry exists, this protocol is the canonical human-readable source for command behavior.
