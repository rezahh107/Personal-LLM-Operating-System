#!/usr/bin/env python3
"""Minimal foundation validator.

This script intentionally avoids third-party dependencies. It checks that the
repository foundation files exist and that JSON ledgers/schemas/registries parse.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/PURPOSE.md",
    "docs/PERSONAL_USE_ASSUMPTIONS.md",
    "docs/REPOSITORY_AS_LLM_MEMORY.md",
    "docs/USER_OPERATING_PROFILE.md",
    "docs/COMMANDS_AND_RAW_IDEAS.md",
    "protocols/START_HERE_FOR_MODELS.md",
    "protocols/BOOT_PROTOCOL.md",
    "protocols/COMMAND_ROUTING_PROTOCOL.md",
    "protocols/SESSION_ROUTING_PIPELINE.md",
    "protocols/RESPONSE_DEPTH_POLICY.md",
    "protocols/EXTERNAL_KNOWLEDGE_POLICY.md",
    "protocols/KNOWLEDGE_CAPTURE_PROTOCOL.md",
    "protocols/MEMORY_REVIEW_AND_DECAY.md",
    "protocols/INSTRUCTION_TRUST_POLICY.md",
    "protocols/VERIFICATION_PROTOCOL.md",
    "protocols/PROVENANCE_POLICY.md",
    "protocols/CONTEXT_LOADING_POLICY.md",
    "protocols/MULTI_MODEL_REVIEW_POLICY.md",
    "protocols/IDEA_MATURATION_PIPELINE.md",
    "protocols/CLAIM_LIFECYCLE.md",
    "protocols/HANDOFF_CONTRACT.md",
    "protocols/PROJECT_CONTINUITY_PROTOCOL.md",
    "protocols/SESSION_CONTINUITY_PROTOCOL.md",
    "protocols/HANDOVER_INTAKE_PROTOCOL.md",
    "incubator/README.md",
    "incubator/raw-ideas/README.md",
    "incubator/raw-ideas/INBOX.md",
    "incubator/raw-ideas/_model_capture_template.md",
    "templates/session-continuity-capsule.md",
    "templates/session-resume-prompt.md",
    "templates/HANDOVER-MANIFEST.yaml",
    "schemas/claim.schema.json",
    "schemas/evidence.schema.json",
    "schemas/handoff-package.schema.json",
    "schemas/repository-registry.schema.json",
    "schemas/session-continuity.schema.json",
    "schemas/handover-manifest.schema.json",
    "ledgers/CLAIM_LEDGER.json",
    "ledgers/EVIDENCE_LEDGER.json",
    "registries/COMMAND_REGISTRY.json",
    "registries/REPOSITORY_REGISTRY.json",
]

JSON_FILES = [
    "schemas/claim.schema.json",
    "schemas/evidence.schema.json",
    "schemas/handoff-package.schema.json",
    "schemas/memory-entry.schema.json",
    "schemas/behavioral-rule.schema.json",
    "schemas/repository-registry.schema.json",
    "schemas/session-continuity.schema.json",
    "schemas/handover-manifest.schema.json",
    "ledgers/CLAIM_LEDGER.json",
    "ledgers/EVIDENCE_LEDGER.json",
    "ledgers/MODEL_DECISION_LEDGER.json",
    "ledgers/QUARANTINE_LEDGER.json",
    "registries/COMMAND_REGISTRY.json",
    "registries/REPOSITORY_REGISTRY.json",
    "fixtures/valid/session_continuity_minimal.json",
    "fixtures/invalid/session_continuity_missing_resume_prompt.json",
    "fixtures/invalid/session_continuity_unverified_claim_as_decision.json",
    "fixtures/invalid/session_continuity_confirmed_decisions_not_array.json",
    "fixtures/invalid/session_continuity_invalid_decision_status.json",
]

BANNED_ASSURANCE_PHRASES = [
    "safe for " + "production",
    "fully " + "verified",
    "no " + "vulnerabilities",
    "cert" + "ified",
]

BANNED_PHRASE_EXEMPT_FILES = {
    "REPORT_TRUST_CALIBRATION.md",
    "VERIFICATION_PROTOCOL.md",
}

ALLOWED_COMMAND_STATUSES = {"candidate", "active", "deprecated"}


def require_files() -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")
    return errors


def parse_json_files() -> list[str]:
    errors: list[str] = []
    for rel in JSON_FILES:
        path = ROOT / rel
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # pragma: no cover - diagnostic path
            errors.append(f"invalid JSON in {rel}: {exc}")
    return errors


def check_banned_phrases() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or path.name in BANNED_PHRASE_EXEMPT_FILES:
            continue
        text = path.read_text(encoding="utf-8").lower()
        for phrase in BANNED_ASSURANCE_PHRASES:
            if phrase in text:
                errors.append(f"restricted phrase '{phrase}' appears in {path.relative_to(ROOT)}")
    return errors


def require_string(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"command registry field must be a non-empty string: {path}")


def require_bool(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, bool):
        errors.append(f"command registry field must be boolean: {path}")


def require_string_list(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, list):
        errors.append(f"command registry field must be a list: {path}")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"command registry list item must be a non-empty string: {path}[{index}]")


def validate_command_registry() -> list[str]:
    errors: list[str] = []
    path = ROOT / "registries/COMMAND_REGISTRY.json"
    try:
        registry = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - already checked, clearer diagnostic
        return [f"cannot load command registry: {exc}"]

    if not isinstance(registry, dict):
        return ["command registry root must be an object"]

    for field in ["version", "status", "registry_role", "scope", "principle"]:
        require_string(registry.get(field), field, errors)

    if registry.get("registry_role") != "canonical_command_definition_source":
        errors.append("command registry registry_role must be canonical_command_definition_source")

    defaults = registry.get("defaults")
    if not isinstance(defaults, dict):
        errors.append("command registry defaults must be an object")
    else:
        for field in [
            "destructive_actions_allowed",
            "repository_write_allowed_without_explicit_scope",
            "treat_command_as_evidence",
            "bypass_instruction_trust_policy",
            "bypass_verification_protocol",
        ]:
            require_bool(defaults.get(field), f"defaults.{field}", errors)

    commands = registry.get("commands")
    if not isinstance(commands, list) or not commands:
        errors.append("command registry commands must be a non-empty list")
        return errors

    seen_names: set[str] = set()
    seen_ids: set[str] = set()
    for index, command in enumerate(commands):
        base = f"commands[{index}]"
        if not isinstance(command, dict):
            errors.append(f"{base} must be an object")
            continue

        for field in [
            "id",
            "command",
            "language",
            "status",
            "route",
            "intent",
            "expected_first_response",
        ]:
            require_string(command.get(field), f"{base}.{field}", errors)

        command_id = command.get("id")
        if isinstance(command_id, str):
            if command_id in seen_ids:
                errors.append(f"duplicate command id: {command_id}")
            seen_ids.add(command_id)

        command_name = command.get("command")
        if isinstance(command_name, str):
            normalized = command_name.strip()
            if normalized in seen_names:
                errors.append(f"duplicate command or alias: {normalized}")
            seen_names.add(normalized)

        aliases = command.get("aliases")
        require_string_list(aliases, f"{base}.aliases", errors)
        if isinstance(aliases, list):
            for alias in aliases:
                if isinstance(alias, str):
                    normalized = alias.strip()
                    if normalized in seen_names:
                        errors.append(f"duplicate command or alias: {normalized}")
                    seen_names.add(normalized)

        status = command.get("status")
        if isinstance(status, str) and status not in ALLOWED_COMMAND_STATUSES:
            errors.append(f"invalid command status for {base}: {status}")

        require_string_list(command.get("allowed_actions"), f"{base}.allowed_actions", errors)
        require_string_list(command.get("load_after_response"), f"{base}.load_after_response", errors)
        require_string_list(command.get("boundaries"), f"{base}.boundaries", errors)
        require_bool(command.get("write_scope_required"), f"{base}.write_scope_required", errors)

    required_commands = {
        "شروع": "آماده‌ام. امروز می‌خوای چکار کنی؟",
        "ایده خام": "آماده‌ام. ایده خامت چیه؟",
    }
    by_command = {
        command.get("command"): command
        for command in commands
        if isinstance(command, dict) and isinstance(command.get("command"), str)
    }
    for command_name, expected_response in required_commands.items():
        command = by_command.get(command_name)
        if command is None:
            errors.append(f"required command missing from registry: {command_name}")
            continue
        if command.get("expected_first_response") != expected_response:
            errors.append(f"required command has wrong expected response: {command_name}")

    return errors


def main() -> int:
    errors = (
        require_files()
        + parse_json_files()
        + validate_command_registry()
        + check_banned_phrases()
    )
    if errors:
        print("Foundation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Foundation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
