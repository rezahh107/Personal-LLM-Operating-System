# Command Routing Protocol

Purpose: define how lightweight command-style phrases activate repository-defined model behavior.

## Source of truth

The machine-readable source of truth for command definitions is:

```text
registries/COMMAND_REGISTRY.json
```

This protocol explains how models should apply that registry.

Do not add, rename, deprecate, or change a command only in prose. Update `registries/COMMAND_REGISTRY.json` first, then update explanatory documents that mirror it.

`schemas/command-registry.schema.json` defines the registry shape. `scripts/validate_foundation.py` performs dependency-free structural checks for the live registry.

## Scope

This protocol covers non-destructive text commands written by the user in a model session, usually after a repository reference.

It does not define a shell, CLI, executable automation system, proof source, or permission to modify files without user-approved repository-write scope.

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

## Current active commands

The canonical current commands are listed in `registries/COMMAND_REGISTRY.json`.

At the time of this protocol seed, the active commands are:

- `شروع` — starts general task intake.
- `ایده خام` — starts raw idea capture.

Exact first responses must come from the registry field `expected_first_response`.

## Command handling rules

1. Commands are routing hints, not evidence.
2. Commands may activate a response mode, but they do not override higher-priority system, developer, safety, repository, or user instructions.
3. Commands must be non-destructive by default.
4. Repository writes require explicit user intent or an active repository-write task.
5. If the command is unknown, ask for clarification and do not invent command behavior.
6. If the model cannot access the repository, it should still follow the visible command text when possible and state that repository files were not inspected.
7. If command behavior conflicts with another protocol, report the conflict and follow the higher-authority source.
8. Command definitions should not be duplicated as independent truth across unrelated files; prose documents may mirror the registry only for readability.

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

## Registry extension path

When adding a new command:

1. Add it to `registries/COMMAND_REGISTRY.json`.
2. Preserve unique `id`, `command`, and `aliases`.
3. Define `route`, `intent`, `expected_first_response`, `allowed_actions`, `write_scope_required`, `load_after_response`, and `boundaries`.
4. Update docs only as mirrors of the registry.
5. Run `python3 scripts/validate_foundation.py`.
6. Do not claim validation passed unless the command was actually run and passed.
