#!/usr/bin/env python3
"""Minimal foundation validator.

This script intentionally avoids third-party dependencies. It checks that the
repository foundation files exist and that JSON ledgers/schemas/registries parse.
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
    "docs/USER_OPERATING_PROFILE.md",
    "protocols/START_HERE_FOR_MODELS.md",
    "protocols/BOOT_PROTOCOL.md",
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
