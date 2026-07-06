#!/usr/bin/env python3
"""Minimal foundation validator.

This script intentionally avoids third-party dependencies. It checks that the
repository foundation files exist and that JSON ledgers/schemas parse.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/PURPOSE.md",
    "docs/PERSONAL_USE_ASSUMPTIONS.md",
    "docs/REPOSITORY_AS_LLM_MEMORY.md",
    "protocols/START_HERE_FOR_MODELS.md",
    "protocols/IDEA_MATURATION_PIPELINE.md",
    "protocols/CLAIM_LIFECYCLE.md",
    "protocols/HANDOFF_CONTRACT.md",
    "schemas/claim.schema.json",
    "schemas/evidence.schema.json",
    "schemas/handoff-package.schema.json",
    "ledgers/CLAIM_LEDGER.json",
    "ledgers/EVIDENCE_LEDGER.json",
]

JSON_FILES = [
    "schemas/claim.schema.json",
    "schemas/evidence.schema.json",
    "schemas/handoff-package.schema.json",
    "schemas/memory-entry.schema.json",
    "schemas/behavioral-rule.schema.json",
    "ledgers/CLAIM_LEDGER.json",
    "ledgers/EVIDENCE_LEDGER.json",
    "ledgers/MODEL_DECISION_LEDGER.json",
    "ledgers/QUARANTINE_LEDGER.json",
]

BANNED_ASSURANCE_PHRASES = [
    "safe for production",
    "fully verified",
    "no vulnerabilities",
    "certified",
]


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
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8").lower()
        for phrase in BANNED_ASSURANCE_PHRASES:
            if phrase in text and path.name != "REPORT_TRUST_CALIBRATION.md":
                errors.append(f"restricted phrase '{phrase}' appears in {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    errors = require_files() + parse_json_files() + check_banned_phrases()
    if errors:
        print("Foundation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Foundation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
