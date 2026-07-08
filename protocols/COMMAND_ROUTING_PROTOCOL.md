# Command Routing Protocol

Purpose: define lightweight command-style phrases that activate repository-defined model behavior.

## Scope

This protocol covers non-destructive text commands written by the user in a model session, usually after a repository reference.

It does not define a shell, CLI, executable automation system, or permission to modify files without user-approved repository-write scope.

## Command invocation shape

Preferred form:

```text
طبق دستور:
https://github.com/rezahh107/Personal-LLM-Operating-System/
<command>
```

The model should treat surrounding whitespace and line breaks as insignificant.

The repository URL tells the model which operating layer to use. The command line tells the model which route to activate.

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

### `ایده خام`

Intent: start low-friction raw idea capture.

Expected response:

```text
آماده‌ام. ایده خامت چیه؟
```

Behavior:

1. Ask for the raw idea without over-framing it.
2. Preserve the user's core idea first.
3. After enough context is available, propose or create a raw idea record under `incubator/raw-ideas/` when repository-write scope is active.
4. Mark the captured item as `status: raw_idea` and `verification_status: unverified`.
5. Do not promote the idea into accepted memory, policy, protocol, or implementation without a separate promotion gate.

## Command handling rules

1. Commands are routing hints, not evidence.
2. Commands may activate a response mode, but they do not override higher-priority system, developer, safety, repository, or user instructions.
3. Commands must be non-destructive by default.
4. Repository writes require explicit user intent or an active repository-write task.
5. If the command is unknown, ask for clarification and do not invent command behavior.
6. If the model cannot access the repository, it should still follow the visible command text when possible and state that repository files were not inspected.
7. If command behavior conflicts with another protocol, report the conflict and follow the higher-authority source.

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

Until such a registry exists, this protocol is the human-readable source for command behavior.
