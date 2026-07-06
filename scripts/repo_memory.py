#!/usr/bin/env python3
"""Model-facing repository memory operations.

This script is not the user's primary interface. It exists for models,
automations, and CI to validate governed memory artifacts.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

CLAIM_STATES = {
    "draft",
    "candidate",
    "challenged",
    "validated",
    "accepted",
    "quarantined",
    "deprecated",
    "rejected",
}

CLAIM_SOURCES = {"user", "llm", "tool", "validator", "ci", "web", "repo"}

ASSURANCE_PHRASES = [
    "fully verified",
    "safe for production",
    "no vulnerabilities",
    "all tests passed",
    "tests passed",
    "ran the tests",
    "certified",
    "compliant",
    "secure",
]

EXECUTION_HINTS = [
    "ran the tests",
    "tests passed",
    "all tests passed",
    "executed",
    "workflow passed",
    "ci passed",
]


def load_json(path: Path) -> tuple[Any | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except Exception as exc:
        return None, [f"{path.relative_to(ROOT)}: invalid JSON: {exc}"]


def require_keys(obj: dict[str, Any], keys: list[str], path: Path) -> list[str]:
    errors: list[str] = []
    for key in keys:
        if key not in obj:
            errors.append(f"{path.relative_to(ROOT)}: missing required key `{key}`")
    return errors


def parse_json_directory(directory: str) -> list[str]:
    errors: list[str] = []
    base = ROOT / directory
    if not base.exists():
        return errors
    for path in sorted(base.glob("*.json")):
        _, path_errors = load_json(path)
        errors.extend(path_errors)
    return errors


def has_assurance_phrase(text: str) -> str | None:
    low = text.lower()
    for phrase in ASSURANCE_PHRASES:
        if phrase in low:
            return phrase
    return None


def has_execution_hint(text: str) -> str | None:
    low = text.lower()
    for phrase in EXECUTION_HINTS:
        if phrase in low:
            return phrase
    return None


def validate_claim(obj: dict[str, Any], path: Path) -> list[str]:
    errors = require_keys(obj, ["id", "text", "state", "source", "scope"], path)
    if errors:
        return errors

    state = obj.get("state")
    source = obj.get("source")
    evidence_refs = obj.get("evidence_refs", [])
    text = str(obj.get("text", ""))

    if state not in CLAIM_STATES:
        errors.append(f"{path.relative_to(ROOT)}: invalid claim state `{state}`")
    if source not in CLAIM_SOURCES:
        errors.append(f"{path.relative_to(ROOT)}: invalid claim source `{source}`")
    if not isinstance(evidence_refs, list):
        errors.append(f"{path.relative_to(ROOT)}: evidence_refs must be an array")

    phrase = has_assurance_phrase(text)
    if phrase and state in {"validated", "accepted"}:
        errors.append(
            f"{path.relative_to(ROOT)}: assurance phrase `{phrase}` is not allowed in {state} claim text"
        )

    exec_hint = has_execution_hint(text)
    if source == "llm" and exec_hint and not evidence_refs:
        errors.append(
            f"{path.relative_to(ROOT)}: LLM claim implies execution via `{exec_hint}` without evidence_refs"
        )

    if state == "accepted" and source == "llm" and not evidence_refs:
        errors.append(
            f"{path.relative_to(ROOT)}: LLM-sourced accepted claim requires evidence_refs or user approval evidence"
        )

    return errors


def validate_evidence(obj: dict[str, Any], path: Path) -> list[str]:
    errors = require_keys(obj, ["id", "type", "source_authority", "summary"], path)
    if errors:
        return errors
    if obj.get("source_authority") == "llm" and obj.get("type") in {"tool_output", "ci_result", "validator_result"}:
        errors.append(
            f"{path.relative_to(ROOT)}: LLM cannot be source authority for tool/CI/validator evidence"
        )
    return errors


def validate_handoff(obj: dict[str, Any], path: Path) -> list[str]:
    required = [
        "task_goal",
        "accepted_facts",
        "candidate_claims",
        "known_limits",
        "allowed_next_actions",
        "forbidden_next_actions",
    ]
    errors = require_keys(obj, required, path)
    if errors:
        return errors

    for key in ["accepted_facts", "candidate_claims", "known_limits", "allowed_next_actions", "forbidden_next_actions"]:
        if not isinstance(obj.get(key), list):
            errors.append(f"{path.relative_to(ROOT)}: `{key}` must be an array")

    accepted_text = " ".join(str(item) for item in obj.get("accepted_facts", []))
    if any(word in accepted_text.lower() for word in ["proved", "ready", "fully verified"]):
        if not obj.get("evidence_refs"):
            errors.append(
                f"{path.relative_to(ROOT)}: accepted facts contain authority language without evidence_refs"
            )

    if not obj.get("known_limits"):
        errors.append(f"{path.relative_to(ROOT)}: handoff must preserve known_limits")
    if not obj.get("forbidden_next_actions"):
        errors.append(f"{path.relative_to(ROOT)}: handoff must declare forbidden_next_actions")
    if not obj.get("stop_conditions"):
        errors.append(f"{path.relative_to(ROOT)}: handoff must declare stop_conditions")

    return errors


def validate_memory_entry(obj: dict[str, Any], path: Path) -> list[str]:
    return require_keys(obj, ["id", "classification", "content", "status"], path)


def validate_ledger(obj: dict[str, Any], path: Path) -> list[str]:
    errors = require_keys(obj, ["version", "entries"], path)
    if not errors and not isinstance(obj.get("entries"), list):
        errors.append(f"{path.relative_to(ROOT)}: entries must be an array")
    return errors


def validate_state_machine(obj: dict[str, Any], path: Path) -> list[str]:
    errors = require_keys(obj, ["states", "allowed_transitions", "forbidden_transitions"], path)
    if errors:
        return errors
    states = set(obj.get("states", []))
    if not CLAIM_STATES.issubset(states):
        errors.append(f"{path.relative_to(ROOT)}: state machine is missing claim lifecycle states")
    for transition in obj.get("allowed_transitions", []):
        if transition.get("from") not in states or transition.get("to") not in states:
            errors.append(f"{path.relative_to(ROOT)}: transition references unknown state {transition}")
    return errors


def validate_path(path: Path) -> list[str]:
    obj, errors = load_json(path)
    if errors:
        return errors
    assert obj is not None

    name = path.name
    rel = str(path.relative_to(ROOT))

    if name == "claim-lifecycle.machine.json":
        return validate_state_machine(obj, path)
    if rel.startswith("ledgers/"):
        return validate_ledger(obj, path)
    if "claim" in name and isinstance(obj, dict):
        return validate_claim(obj, path)
    if "evidence" in name and isinstance(obj, dict):
        return validate_evidence(obj, path)
    if "handoff" in name and isinstance(obj, dict):
        return validate_handoff(obj, path)
    if "memory" in name and isinstance(obj, dict):
        return validate_memory_entry(obj, path)
    return []


def validate_fixtures() -> list[str]:
    errors: list[str] = []
    valid_dir = ROOT / "fixtures" / "valid"
    invalid_dir = ROOT / "fixtures" / "invalid"

    for path in sorted(valid_dir.glob("*.json")):
        path_errors = validate_path(path)
        if path_errors:
            errors.extend([f"valid fixture failed: {error}" for error in path_errors])

    for path in sorted(invalid_dir.glob("*.json")):
        path_errors = validate_path(path)
        if not path_errors:
            errors.append(f"invalid fixture unexpectedly passed: {path.relative_to(ROOT)}")

    return errors


def validate_repository() -> list[str]:
    errors: list[str] = []

    for directory in ["schemas", "ledgers", "templates"]:
        errors.extend(parse_json_directory(directory))

    errors.extend(validate_path(ROOT / "schemas" / "claim-lifecycle.machine.json"))

    for path in sorted((ROOT / "ledgers").glob("*.json")):
        errors.extend(validate_ledger(load_json(path)[0], path))

    errors.extend(validate_fixtures())
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Model-facing governed memory operations")
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
