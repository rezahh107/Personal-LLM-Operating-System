#!/usr/bin/env python3
"""Fail-clean governed memory validator.

Model/CI-facing only. The user is not expected to run this manually.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MACHINE_PATH = ROOT / "schemas" / "claim-lifecycle.machine.json"

STATES = {"draft", "candidate", "challenged", "validated", "accepted", "quarantined", "deprecated", "rejected"}
SOURCES = {"user", "llm", "tool", "validator", "ci", "web", "repo"}
EXEC_HINTS = ["ran the tests", "tests passed", "all tests passed", "workflow passed", "ci passed"]
AUTHORITY_HINTS = ["proved", "ready", "fully verified"]

LEGACY_REGISTRY_ENTRY_STATUSES = {"active", "candidate", "no_verified_repo", "explicit_context_only", "deprecated"}
LEGACY_REGISTRY_REPO_VERIFICATIONS = {"connector_verified", "explicit_context", "inferred_from_name", "unknown"}
GOVERNANCE_AUTHORITIES = {"advisory", "accepted_decision", "project_contract", "frozen_contract"}
EPISTEMIC_SUPPORT = {"unsupported", "source_supported", "observed", "reproduced", "test_verified", "expert_verified"}
VERIFICATION_STATUSES = {
    "not_checked",
    "statically_inspected",
    "source_supported",
    "tool_observed",
    "reproduced",
    "test_verified",
    "fixture_verified",
    "externally_reviewed",
    "not_verifiable",
    "insufficient_evidence",
}
LIFECYCLE_STATUSES = {"candidate", "active", "stale", "superseded", "deprecated", "rejected", "archived"}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: Path) -> tuple[Any | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except Exception as exc:
        return None, [f"{rel(path)}: invalid JSON: {exc}"]


def require_object(obj: Any, path: Path) -> list[str]:
    return [] if isinstance(obj, dict) else [f"{rel(path)}: expected JSON object"]


def require_keys(obj: Any, path: Path, keys: list[str]) -> list[str]:
    errors = require_object(obj, path)
    if errors:
        return errors
    return [f"{rel(path)}: missing required key `{key}`" for key in keys if key not in obj]


def reject_unknown_keys(obj: Any, path: Path, allowed_keys: set[str]) -> list[str]:
    if not isinstance(obj, dict):
        return []
    return [f"{rel(path)}: unknown key `{key}`" for key in sorted(set(obj) - allowed_keys)]


def require_string_field(obj: dict[str, Any], path: Path, key: str, *, non_empty: bool = True) -> list[str]:
    value = obj.get(key)
    if not isinstance(value, str):
        return [f"{rel(path)}: `{key}` must be a string"]
    if non_empty and not value:
        return [f"{rel(path)}: `{key}` must be a non-empty string"]
    return []


def has_any(text: str, phrases: list[str]) -> str | None:
    text_lower = text.lower()
    for phrase in phrases:
        if phrase in text_lower:
            return phrase
    return None


def validate_claim(obj: Any, path: Path) -> list[str]:
    errors = require_keys(obj, path, ["id", "text", "state", "source", "scope"])
    if errors:
        return errors
    assert isinstance(obj, dict)
    state = obj.get("state")
    source = obj.get("source")
    evidence_refs = obj.get("evidence_refs", [])
    text = str(obj.get("text", ""))
    if state not in STATES:
        errors.append(f"{rel(path)}: invalid claim state `{state}`")
    if source not in SOURCES:
        errors.append(f"{rel(path)}: invalid claim source `{source}`")
    if not isinstance(evidence_refs, list):
        errors.append(f"{rel(path)}: evidence_refs must be an array")
    if state == "accepted" and source == "llm" and not evidence_refs:
        errors.append(f"{rel(path)}: LLM-sourced accepted claim requires evidence_refs or user-approval evidence")
    exec_hint = has_any(text, EXEC_HINTS)
    if source == "llm" and exec_hint and not evidence_refs:
        errors.append(f"{rel(path)}: LLM claim implies execution via `{exec_hint}` without evidence_refs")
    if state in {"validated", "accepted"} and has_any(text, AUTHORITY_HINTS) and not evidence_refs:
        errors.append(f"{rel(path)}: authority language requires evidence_refs")
    return errors


def validate_handoff(obj: Any, path: Path) -> list[str]:
    required = [
        "task_goal",
        "accepted_facts",
        "candidate_claims",
        "known_limits",
        "allowed_next_actions",
        "forbidden_next_actions",
        "stop_conditions",
    ]
    errors = require_keys(obj, path, required)
    if errors:
        return errors
    assert isinstance(obj, dict)
    list_fields = [
        "accepted_facts",
        "candidate_claims",
        "known_limits",
        "allowed_next_actions",
        "forbidden_next_actions",
        "stop_conditions",
    ]
    type_errors = [f"{rel(path)}: `{field}` must be an array" for field in list_fields if not isinstance(obj.get(field), list)]
    if type_errors:
        return type_errors
    accepted_text = " ".join(str(item) for item in obj.get("accepted_facts", []))
    if has_any(accepted_text, AUTHORITY_HINTS) and not obj.get("evidence_refs"):
        errors.append(f"{rel(path)}: accepted facts contain authority language without evidence_refs")
    if not obj.get("known_limits"):
        errors.append(f"{rel(path)}: handoff must preserve known_limits")
    if not obj.get("forbidden_next_actions"):
        errors.append(f"{rel(path)}: handoff must declare forbidden_next_actions")
    if not obj.get("stop_conditions"):
        errors.append(f"{rel(path)}: handoff must declare stop_conditions")
    return errors


def validate_memory_entry(obj: Any, path: Path) -> list[str]:
    return require_keys(obj, path, ["id", "classification", "content", "status"])


def validate_evidence(obj: Any, path: Path) -> list[str]:
    errors = require_keys(obj, path, ["id", "type", "source_authority", "summary"])
    if errors:
        return errors
    assert isinstance(obj, dict)
    if obj.get("source_authority") == "llm" and obj.get("type") in {"tool_output", "ci_result", "validator_result"}:
        errors.append(f"{rel(path)}: LLM cannot be source authority for tool/CI/validator evidence")
    return errors


def validate_ledger(obj: Any, path: Path) -> list[str]:
    errors = require_keys(obj, path, ["version", "entries"])
    if errors:
        return errors
    assert isinstance(obj, dict)
    if not isinstance(obj.get("entries"), list):
        errors.append(f"{rel(path)}: entries must be an array")
    return errors


def enum_error(path: Path, key: str, value: Any, allowed: set[str]) -> list[str]:
    if not isinstance(value, str):
        return [f"{rel(path)}: `{key}` must be a string"]
    if value not in allowed:
        allowed_text = ", ".join(sorted(allowed))
        return [f"{rel(path)}: invalid {key} `{value}`; expected one of: {allowed_text}"]
    return []


def validate_new_registry_entry(entry: dict[str, Any], path: Path) -> list[str]:
    entry_allowed = {
        "domain",
        "description",
        "primary_repo",
        "related_repos",
        "load_rule",
        "when_to_use",
        "when_not_to_use",
        "governance_authority",
        "epistemic_support",
        "verification_status",
        "lifecycle_status",
        "notes",
    }
    related_allowed = {"repo", "relationship", "verification_status", "epistemic_support", "lifecycle_status", "notes"}
    errors = require_keys(entry, path, sorted(entry_allowed))
    errors.extend(reject_unknown_keys(entry, path, entry_allowed))
    for key in ["domain", "description", "load_rule", "when_to_use", "when_not_to_use", "notes"]:
        errors.extend(require_string_field(entry, path, key))
    if entry.get("primary_repo") is not None and not isinstance(entry.get("primary_repo"), str):
        errors.append(f"{rel(path)}: primary_repo must be a string or null")
    errors.extend(enum_error(path, "governance_authority", entry.get("governance_authority"), GOVERNANCE_AUTHORITIES))
    errors.extend(enum_error(path, "epistemic_support", entry.get("epistemic_support"), EPISTEMIC_SUPPORT))
    errors.extend(enum_error(path, "verification_status", entry.get("verification_status"), VERIFICATION_STATUSES))
    errors.extend(enum_error(path, "lifecycle_status", entry.get("lifecycle_status"), LIFECYCLE_STATUSES))
    related_repos = entry.get("related_repos")
    if not isinstance(related_repos, list):
        errors.append(f"{rel(path)}: related_repos must be an array")
        return errors
    for repo_index, repo_entry in enumerate(related_repos):
        repo_path = Path(f"{rel(path)}.related_repos[{repo_index}]")
        errors.extend(require_keys(repo_entry, repo_path, ["repo", "relationship", "verification_status", "epistemic_support", "lifecycle_status"]))
        if not isinstance(repo_entry, dict):
            continue
        errors.extend(reject_unknown_keys(repo_entry, repo_path, related_allowed))
        for key in ["repo", "relationship"]:
            errors.extend(require_string_field(repo_entry, repo_path, key))
        if "notes" in repo_entry:
            errors.extend(require_string_field(repo_entry, repo_path, "notes", non_empty=False))
        errors.extend(enum_error(repo_path, "verification_status", repo_entry.get("verification_status"), VERIFICATION_STATUSES))
        errors.extend(enum_error(repo_path, "epistemic_support", repo_entry.get("epistemic_support"), EPISTEMIC_SUPPORT))
        errors.extend(enum_error(repo_path, "lifecycle_status", repo_entry.get("lifecycle_status"), LIFECYCLE_STATUSES))
    return errors


def validate_legacy_registry_entry(entry: dict[str, Any], path: Path) -> list[str]:
    entry_allowed = {
        "domain",
        "description",
        "primary_repo",
        "related_repos",
        "load_rule",
        "when_to_use",
        "when_not_to_use",
        "status",
        "notes",
    }
    related_allowed = {"repo", "relationship", "verification", "notes"}
    errors = require_keys(entry, path, sorted(entry_allowed))
    errors.extend(reject_unknown_keys(entry, path, entry_allowed))
    for key in ["domain", "description", "load_rule", "when_to_use", "when_not_to_use", "status", "notes"]:
        errors.extend(require_string_field(entry, path, key))
    if entry.get("primary_repo") is not None and not isinstance(entry.get("primary_repo"), str):
        errors.append(f"{rel(path)}: primary_repo must be a string or null")
    status = entry.get("status")
    if isinstance(status, str) and status not in LEGACY_REGISTRY_ENTRY_STATUSES:
        allowed = ", ".join(sorted(LEGACY_REGISTRY_ENTRY_STATUSES))
        errors.append(f"{rel(path)}: invalid status `{status}`; expected one of: {allowed}")
    related_repos = entry.get("related_repos")
    if not isinstance(related_repos, list):
        errors.append(f"{rel(path)}: related_repos must be an array")
        return errors
    for repo_index, repo_entry in enumerate(related_repos):
        repo_path = Path(f"{rel(path)}.related_repos[{repo_index}]")
        errors.extend(require_keys(repo_entry, repo_path, ["repo", "relationship", "verification"]))
        if not isinstance(repo_entry, dict):
            continue
        errors.extend(reject_unknown_keys(repo_entry, repo_path, related_allowed))
        for key in ["repo", "relationship", "verification"]:
            errors.extend(require_string_field(repo_entry, repo_path, key))
        if "notes" in repo_entry:
            errors.extend(require_string_field(repo_entry, repo_path, "notes", non_empty=False))
        verification = repo_entry.get("verification")
        if isinstance(verification, str) and verification not in LEGACY_REGISTRY_REPO_VERIFICATIONS:
            allowed = ", ".join(sorted(LEGACY_REGISTRY_REPO_VERIFICATIONS))
            errors.append(f"{rel(repo_path)}: invalid verification `{verification}`; expected one of: {allowed}")
    return errors


def validate_repository_registry(obj: Any, path: Path) -> list[str]:
    root_allowed = {"version", "status", "last_reviewed", "principle", "entries"}
    errors = require_keys(obj, path, ["version", "status", "principle", "entries"])
    if errors:
        return errors
    assert isinstance(obj, dict)
    errors.extend(reject_unknown_keys(obj, path, root_allowed))
    for key in ["version", "status", "principle"]:
        errors.extend(require_string_field(obj, path, key))
    if "last_reviewed" in obj:
        errors.extend(require_string_field(obj, path, "last_reviewed"))
    if not isinstance(obj.get("entries"), list):
        errors.append(f"{rel(path)}: entries must be an array")
        return errors
    seen_domains: set[str] = set()
    new_keys = {"governance_authority", "epistemic_support", "verification_status", "lifecycle_status"}
    for index, entry in enumerate(obj.get("entries", [])):
        entry_path = Path(f"{rel(path)}#entries[{index}]")
        if not isinstance(entry, dict):
            errors.extend(require_object(entry, entry_path))
            continue
        domain = entry.get("domain")
        if isinstance(domain, str):
            if domain in seen_domains:
                errors.append(f"{rel(entry_path)}: duplicate domain `{domain}`")
            seen_domains.add(domain)
        if any(key in entry for key in new_keys):
            errors.extend(validate_new_registry_entry(entry, entry_path))
        else:
            errors.extend(validate_legacy_registry_entry(entry, entry_path))
    return errors


def load_machine() -> tuple[dict[str, Any] | None, list[str]]:
    machine, errors = load_json(MACHINE_PATH)
    if errors:
        return None, errors
    errors = require_keys(machine, MACHINE_PATH, ["states", "allowed_transitions", "forbidden_transitions"])
    if errors:
        return None, errors
    assert isinstance(machine, dict)
    if not isinstance(machine.get("states"), list) or not isinstance(machine.get("allowed_transitions"), list) or not isinstance(machine.get("forbidden_transitions"), list):
        return None, [f"{rel(MACHINE_PATH)}: states and transition collections must be arrays"]
    return machine, []


def validate_state_machine(obj: Any, path: Path) -> list[str]:
    errors = require_keys(obj, path, ["states", "allowed_transitions", "forbidden_transitions"])
    if errors:
        return errors
    assert isinstance(obj, dict)
    if not isinstance(obj.get("states"), list):
        return [f"{rel(path)}: states must be an array"]
    states = set(obj.get("states", []))
    if not STATES.issubset(states):
        errors.append(f"{rel(path)}: missing lifecycle states")
    return errors


def validate_transition(obj: Any, path: Path, machine: dict[str, Any] | None = None) -> list[str]:
    errors = require_keys(obj, path, ["id", "entity_type", "entity_id", "from", "to", "by", "reason", "timestamp"])
    if errors:
        return errors
    assert isinstance(obj, dict)
    if obj.get("entity_type") != "claim":
        return errors
    if machine is None:
        machine, machine_errors = load_machine()
        if machine_errors:
            return machine_errors
        assert machine is not None
    from_state = obj.get("from")
    to_state = obj.get("to")
    states = set(machine.get("states", []))
    if from_state not in states:
        errors.append(f"{rel(path)}: unknown from state `{from_state}`")
    if to_state not in states:
        errors.append(f"{rel(path)}: unknown to state `{to_state}`")
    for transition in machine.get("forbidden_transitions", []):
        if isinstance(transition, dict) and transition.get("from") == from_state and transition.get("to") == to_state:
            errors.append(f"{rel(path)}: forbidden transition {from_state} -> {to_state}: {transition.get('reason', 'forbidden')}")
    allowed = None
    for transition in machine.get("allowed_transitions", []):
        if isinstance(transition, dict) and transition.get("from") == from_state and transition.get("to") == to_state:
            allowed = transition
            break
    if allowed is None:
        errors.append(f"{rel(path)}: transition {from_state} -> {to_state} is not allowed")
    else:
        for key in allowed.get("requires", []):
            if not obj.get(key):
                errors.append(f"{rel(path)}: transition {from_state} -> {to_state} requires `{key}`")
    return errors


def validate_transition_ledger(obj: Any, path: Path) -> list[str]:
    errors = validate_ledger(obj, path)
    if errors:
        return errors
    assert isinstance(obj, dict)
    machine, machine_errors = load_machine()
    if machine_errors:
        return machine_errors
    assert machine is not None
    for index, entry in enumerate(obj.get("entries", [])):
        errors.extend(validate_transition(entry, Path(f"{rel(path)}#entries[{index}]"), machine))
    return errors


def validate_path(path: Path) -> list[str]:
    obj, errors = load_json(path)
    if errors:
        return errors
    assert obj is not None
    name = path.name
    path_text = rel(path)
    if path_text == "registries/REPOSITORY_REGISTRY.json" or name.startswith("repository_registry"):
        return validate_repository_registry(obj, path)
    if name == "claim-lifecycle.machine.json":
        return validate_state_machine(obj, path)
    if name == "STATE_TRANSITION_LEDGER.json":
        return validate_transition_ledger(obj, path)
    if path_text.startswith("ledgers/"):
        return validate_ledger(obj, path)
    if "state_transition" in name or "transition" in name:
        return validate_transition(obj, path)
    if "claim" in name:
        return validate_claim(obj, path)
    if "handoff" in name:
        return validate_handoff(obj, path)
    if "evidence" in name:
        return validate_evidence(obj, path)
    if "memory" in name:
        return validate_memory_entry(obj, path)
    if path_text.startswith("fixtures/"):
        return require_object(obj, path)
    return []


def parse_json_directory(directory: str) -> list[str]:
    errors: list[str] = []
    base = ROOT / directory
    if not base.exists():
        return errors
    for path in sorted(base.glob("*.json")):
        _, path_errors = load_json(path)
        errors.extend(path_errors)
    return errors


def validate_fixtures() -> list[str]:
    errors: list[str] = []
    valid_dir = ROOT / "fixtures" / "valid"
    if valid_dir.exists():
        for path in sorted(valid_dir.glob("*.json")):
            path_errors = validate_path(path)
            if path_errors:
                errors.extend([f"valid fixture failed: {error}" for error in path_errors])
    invalid_dir = ROOT / "fixtures" / "invalid"
    if invalid_dir.exists():
        for path in sorted(invalid_dir.glob("*.json")):
            path_errors = validate_path(path)
            if not path_errors:
                errors.append(f"invalid fixture unexpectedly passed: {rel(path)}")
    return errors


def validate_repository() -> list[str]:
    errors: list[str] = []
    for directory in ["schemas", "ledgers", "templates", "registries"]:
        errors.extend(parse_json_directory(directory))
    errors.extend(validate_path(MACHINE_PATH))
    for path in sorted((ROOT / "ledgers").glob("*.json")):
        errors.extend(validate_path(path))
    for path in sorted((ROOT / "registries").glob("*.json")):
        errors.extend(validate_path(path))
    errors.extend(validate_fixtures())
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate governed memory artifacts")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="validate repository memory artifacts and fixtures")
    args = parser.parse_args(argv)
    if args.command == "validate":
        errors = validate_repository()
        if errors:
            print("Governed memory validation failed:")
            for error in errors:
                print(f"- {error}")
            return 1
        print("Governed memory validation passed.")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
