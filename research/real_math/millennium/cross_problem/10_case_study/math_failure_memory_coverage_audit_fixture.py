#!/usr/bin/env python3
"""Build the math-first failure-memory coverage audit.

This is an application-method audit.  It never turns repository conformance
into mathematics and it does not promote a RAKL framework change.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
MILLENNIUM = ROOT / "research/real_math/millennium"
OUT = MILLENNIUM / "cross_problem/10_case_study/MATH_FAILURE_MEMORY_COVERAGE_AUDIT_20260812.json"

APPLICATION_BASE = "a060514e894ec6566b01bb4c89a8aa806ef0048c"
FRAMEWORK_LIVE = "9da0f4d331e9ae61f1309b3a006d7a3c67fa217c"
LEGACY_FAILURE = "F-O9D12A2A1A1B-FIXED-LAMBDA-GLOBAL-STATE-FACTORIZATION"

CANONICAL_FIELDS = (
    "failure_id",
    "atom_id",
    "candidate_id",
    "context_packet_hash",
    "research_trace_event_id",
    "method_family",
    "failure_mode",
    "residual_signature",
    "broken_assumptions",
    "scope_conditions",
    "competing_diagnoses",
    "selected_diagnosis",
    "diagnosis_status",
    "evidence_pointers",
    "falsifier_or_attempt",
    "observed_result",
    "local_repair_attempts",
    "timestamp",
    "artifact_hash",
)

SEVEN_FIELD_MAP = {
    "attempted_mathematical_implication": ["method_family", "broken_assumptions"],
    "exact_result_or_failure": ["failure_mode", "observed_result"],
    "supported_and_competing_causes": [
        "competing_diagnoses",
        "selected_diagnosis",
        "diagnosis_status",
    ],
    "scope": ["scope_conditions"],
    "mathematical_falsifier": ["falsifier_or_attempt"],
    "mathematical_repair": ["local_repair_attempts"],
    "proof_or_source_evidence": ["evidence_pointers"],
}

NONEMPTY_CANONICAL_FIELDS = {
    "failure_id",
    "atom_id",
    "candidate_id",
    "context_packet_hash",
    "research_trace_event_id",
    "method_family",
    "failure_mode",
    "residual_signature",
    "scope_conditions",
    "competing_diagnoses",
    "diagnosis_status",
    "evidence_pointers",
    "falsifier_or_attempt",
    "observed_result",
    "timestamp",
    "artifact_hash",
}


def semantic(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def artifact_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(semantic(payload)).hexdigest()


def is_present(value: object) -> bool:
    return value is not None and value != "" and value != []


def canonical_missing(experience: dict) -> list[str]:
    missing = []
    for field in CANONICAL_FIELDS:
        if field not in experience:
            missing.append(field)
        elif field in NONEMPTY_CANONICAL_FIELDS and not is_present(experience[field]):
            missing.append(field)
    return missing


def seven_field_missing(experience: dict) -> list[str]:
    missing = []
    for lesson_field, fields in SEVEN_FIELD_MAP.items():
        if lesson_field == "supported_and_competing_causes":
            # OBSERVED_ONLY correctly leaves selected_diagnosis empty while
            # preserving live alternatives and the bounded authority status.
            required = ("competing_diagnoses", "diagnosis_status")
        else:
            required = tuple(fields)
        if any(not is_present(experience.get(field)) for field in required):
            missing.append(lesson_field)
    return missing


def lane_for(path: Path) -> str:
    relative = path.relative_to(MILLENNIUM)
    return relative.parts[0]


def collect() -> list[tuple[Path, dict, str]]:
    rows: list[tuple[Path, dict, str]] = []
    for path in sorted(MILLENNIUM.rglob("*.json")):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(value, dict):
            continue
        experiences = value.get("experiences")
        if not isinstance(experiences, list):
            experiences = []
        for experience in experiences:
            if isinstance(experience, dict) and is_present(experience.get("failure_id")):
                rows.append((path, experience, "experiences"))
        experience = value.get("experience")
        if isinstance(experience, dict) and is_present(experience.get("failure_id")):
            rows.append((path, experience, "experience"))
    return rows


def build() -> dict:
    rows = collect()
    lane_counts = Counter(lane_for(path) for path, _, _ in rows)
    unique_failure_ids = {experience["failure_id"] for _, experience, _ in rows}
    canonical_gaps = []
    seven_field_gaps = []
    canonical_complete = 0
    seven_field_complete = 0
    canonical_complete_ids: set[str] = set()
    seven_field_complete_ids: set[str] = set()
    for path, experience, source_shape in rows:
        missing = canonical_missing(experience)
        seven_missing = seven_field_missing(experience)
        if missing:
            canonical_gaps.append(
                {
                    "failure_id": experience["failure_id"],
                    "path": path.relative_to(ROOT).as_posix(),
                    "source_shape": source_shape,
                    "authority": experience.get("authority", "UNSPECIFIED"),
                    "missing_canonical_fields": missing,
                    "missing_seven_field_lessons": seven_missing,
                    "existing_mathematical_content": {
                        key: experience[key]
                        for key in ("failure_mode", "diagnosis", "scope_conditions", "repair")
                        if key in experience
                    },
                }
            )
        else:
            canonical_complete += 1
            canonical_complete_ids.add(experience["failure_id"])
        if seven_missing:
            seven_field_gaps.append(
                {
                    "failure_id": experience["failure_id"],
                    "path": path.relative_to(ROOT).as_posix(),
                    "source_shape": source_shape,
                    "authority": experience.get("authority", "UNSPECIFIED"),
                    "missing_seven_field_lessons": seven_missing,
                }
            )
        else:
            seven_field_complete += 1
            seven_field_complete_ids.add(experience["failure_id"])

    if len(rows) != 102 or canonical_complete != 100 or seven_field_complete != 101:
        raise RuntimeError(
            "unexpected frozen audit population: "
            f"total={len(rows)} canonical={canonical_complete} seven={seven_field_complete}"
        )
    if [row["failure_id"] for row in seven_field_gaps] != [LEGACY_FAILURE]:
        raise RuntimeError("unexpected mathematical lesson coverage gap")
    if len(unique_failure_ids) != 48 or len(seven_field_complete_ids) != 47:
        raise RuntimeError("unexpected unique failure-id coverage")

    value = {
        "artifact_hash": "",
        "audit_id": "MATH-FAILURE-MEMORY-COVERAGE-AUDIT-20260812",
        "schema_version": "1.0.0",
        "as_of_utc": "2026-08-12T09:15:00Z",
        "object": "Application-local mathematical failure experience across P versus NP and the Millennium lanes",
        "quantity_of_interest": (
            "Whether every registered failure experience exposes the seven mathematical lesson fields "
            "needed to diagnose why a mathematical implication failed and select a falsifiable repair"
        ),
        "authority_universe": {
            "application_repository_sha": APPLICATION_BASE,
            "framework_live_sha": FRAMEWORK_LIVE,
            "pending_or_open_pr_material_counted": False,
        },
        "credit_boundary": {
            "mathematical_credit_units": 0,
            "framework_promotion": False,
            "independent_review": False,
            "statement": (
                "This coverage audit improves failure-memory completeness only. Git, CI, schemas, hashes, "
                "chronology, counts, and the audit itself create no mathematical result."
            ),
        },
        "seven_field_mapping": SEVEN_FIELD_MAP,
        "coverage": {
            "failure_experiences_scanned": len(rows),
            "files_scanned_with_experiences": len({path for path, _, _ in rows}),
            "unique_failure_ids": len(unique_failure_ids),
            "duplicate_rows_preserved": len(rows) - len(unique_failure_ids),
            "canonical_schema_complete_experiences": canonical_complete,
            "canonical_schema_gap_experiences": len(canonical_gaps),
            "unique_failure_ids_with_canonical_row": len(canonical_complete_ids),
            "seven_field_math_complete_experiences": seven_field_complete,
            "seven_field_math_gap_experiences": len(seven_field_gaps),
            "unique_failure_ids_with_seven_field_row": len(seven_field_complete_ids),
            "lane_counts": dict(sorted(lane_counts.items())),
            "canonical_schema_gaps": canonical_gaps,
            "seven_field_math_gaps": seven_field_gaps,
        },
        "bounded_diagnosis": {
            "status": "SUPPORTED_BOUNDED",
            "observation": (
                "101 of 102 embedded rows, covering 47 of 48 unique failure ids, expose the seven mathematical "
                "lesson ingredients. "
                "The sole mathematical-lesson gap is a proposal-shadow legacy P-vs-NP entry that uses an older "
                "compact vocabulary. Two entries have canonical identity/shape gaps, but the Hodge entry already "
                "contains all seven mathematical lesson coordinates."
            ),
            "supported_cause": (
                "The legacy proposal-shadow record was embedded without normalization into the canonical "
                "FailureExperience vocabulary; this is an application memory-normalization gap, not evidence "
                "that its mathematical diagnosis is true or false."
            ),
            "competing_causes": [
                "the compact entry was intentionally noncanonical because its authority is proposal-shadow",
                "a canonical successor exists elsewhere but was not linked into this snapshot",
                "the source mathematical diagnosis itself may remain under-supported",
            ],
            "falsifier": (
                "Produce a merged, append-only canonical successor for the same failure id that supplies every "
                "seven-field ingredient and explicitly supersedes the compact snapshot entry."
            ),
            "repair": (
                "Preserve the legacy bytes; add a canonical successor/correction or explicitly exclude the "
                "proposal-shadow row from canonical failure-lattice counts. Future mathematical failures must "
                "record competing causes before selecting a diagnosis."
            ),
        },
        "framework_owner_audit": {
            "verdict": "EXISTING_METHOD_SURFACE_APPLICATION_ROUTING_GAP",
            "new_method_surface_justified": False,
            "existing_owners": [
                "src/rakl/failure_lattice.py::FailureExperience",
                "src/rakl/challenge_learning.py::ChallengeLearningCase",
                "research/SELF_RAKL_RESEARCH_042.md::FailureCauseDAG",
                "skills/rakl-core/workflows/failure-diagnosis.md",
            ],
            "narrowing_of_prior_proposal": (
                "The global atlas proposal to add a mathematical failure-cause compiler is not yet evidence "
                "for a new RAKL operator: the current framework already owns competing diagnosis, failure-cause "
                "atoms, discriminating challenges, and next-action routing. The evidenced gap is application-side "
                "normalization and activation on mathematical cases."
            ),
            "fresh_assurance_required": True,
            "next_framework_discriminator": (
                "Freeze matched mathematical failure cases with hidden gold causes and compare incumbent routing "
                "against an application adapter on cause attribution, repeat-failure avoidance, viable-route "
                "preservation, and correct CANNOT_CHECK behavior."
            ),
            "promotion_state": "NO_FRAMEWORK_DELTA_PROPOSED_OR_PROMOTED",
        },
        "root_status": "ALL_UNSOLVED_ROOTS_OPEN_NO_SOLUTION_CERTIFICATE",
    }
    value["artifact_hash"] = artifact_hash(value)
    return value


def main() -> None:
    OUT.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
