# Commands and Raw Ideas

Purpose: explain the repository-wide command protocol and the raw idea incubator in one model-facing and user-facing place.

## Summary

This repository supports lightweight text commands that the user can paste into any language model session.

Preferred command shape:

```text
طبق دستور:
https://github.com/rezahh107/Personal-LLM-Operating-System/
<command>
```

The repository URL tells the model which operating layer to use. The command tells the model which behavior to activate.

Commands are not a shell, CLI, executable script, proof source, or permission system. They are routing hints for model behavior.

## Source of truth

The canonical machine-readable source for command definitions is:

```text
registries/COMMAND_REGISTRY.json
```

The schema is:

```text
schemas/command-registry.schema.json
```

This document is an explanatory guide. If this guide and the registry disagree, treat the registry as the command-definition source and report the documentation drift.

## Repository-wide applicability

The command protocol is repository-wide.

It can be used before any domain-specific work, including audit, GitHub repair, prompt engineering, image workflow, research, document production, Elementor/EV4 work, or future adapters.

A command selects the first behavior mode. After that, ordinary routing still applies through `protocols/SESSION_ROUTING_PIPELINE.md`.

Example:

```text
طبق دستور:
https://github.com/rezahh107/Personal-LLM-Operating-System/
ایده خام
```

The model should respond with the `expected_first_response` defined for that command in `registries/COMMAND_REGISTRY.json`.

Then the user can describe an idea about any domain. The model should preserve the core idea first and only load domain-specific context if the follow-up task needs it.

## Current commands

Current commands are defined in `registries/COMMAND_REGISTRY.json`.

At this seed stage, the active user-facing commands are:

| Command | Purpose |
|---|---|
| `شروع` | Start a general session using this repository as operating context. |
| `ایده خام` | Start raw idea capture before critique, validation, or maturation. |

The canonical behavior for commands is defined by the registry and applied through `protocols/COMMAND_ROUTING_PROTOCOL.md`.

## How models should handle commands

When a command is recognized:

1. Apply `protocols/COMMAND_ROUTING_PROTOCOL.md` first.
2. Read the exact expected first response from `registries/COMMAND_REGISTRY.json`.
3. Do not summarize the repository unless the command asks for it.
4. Do not invent behavior for unknown commands.
5. Do not treat the command as evidence.
6. Do not treat the command as write permission.
7. Continue normal routing after the command's first behavior is activated.

If the model cannot access GitHub, it should still follow the visible command text when possible and state that repository files were not inspected.

## Raw idea incubator

Raw ideas live in:

```text
incubator/raw-ideas/
```

This area is for:

- sudden thoughts;
- brainstorming fragments;
- early repository-shaping ideas;
- reusable ideas extracted by a model from conversation;
- future workflow, protocol, registry, adapter, prompt, or tool concepts.

## Raw idea boundary

A raw idea preserves possibility, not truth.

A raw idea is not:

- accepted memory;
- project policy;
- a verified claim;
- a repository rule;
- a final protocol;
- a final architecture;
- an implementation commitment.

Raw ideas may later enter `protocols/IDEA_MATURATION_PIPELINE.md`, but they do not bypass maturation, review, verification, provenance, or memory promotion.

## Model-captured raw idea behavior

When a conversation produces a reusable raw idea, the model may capture it if repository-write scope is active or provide a ready-to-save file if write scope is unavailable.

The model must preserve the user's core idea before critique or improvement.

A captured raw idea should include:

- core idea;
- user's raw intent;
- conversation context;
- why it may matter later;
- what it is not;
- possible future development;
- open questions;
- next review trigger.

Preferred standalone template:

```text
incubator/raw-ideas/_model_capture_template.md
```

Fast inbox path:

```text
incubator/raw-ideas/INBOX.md
```

Standalone captured idea path:

```text
incubator/raw-ideas/captured/YYYY-MM-DD-short-title.md
```

## When to use `INBOX.md` vs `captured/`

Use `INBOX.md` when:

- the idea is short;
- the user is brainstorming quickly;
- there is not enough context for a standalone file;
- the goal is only not to forget it.

Use `captured/` when:

- the idea came from several conversation turns;
- the model can identify a stable core idea;
- the idea is likely to be revisited;
- the idea may later become a protocol, checklist, registry entry, adapter, or workflow rule.

## Future command expansion

All future command-style behaviors must be defined in `registries/COMMAND_REGISTRY.json` first.

After the registry is updated, update `protocols/COMMAND_ROUTING_PROTOCOL.md` and this guide only as explanatory mirrors.

The foundation validator checks the registry for required structure, duplicate command names and aliases, and the two seed commands.
