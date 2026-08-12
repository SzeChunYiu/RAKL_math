from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / (
    "research/real_math/millennium/yang_mills/08_reviews/"
    "YM-S1a2c_R13_RETROSPECTIVE_AUDIT_20260812.json"
)


def _load() -> dict:
    value = json.loads(AUDIT.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(document: dict) -> str:
    subject = copy.deepcopy(document)
    subject["artifact_hash"] = ""
    raw = json.dumps(
        subject, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_r13_retrospective_math_scope_and_interfaces_are_exact() -> None:
    audit = _load()
    assert audit["artifact_hash"] == _canonical_hash(audit)
    assert audit["subject"] == {
        "pull_request": 240,
        "original_head": "90ff9f31d29be9317e9f7a77b8d82fcb7cd32f8b",
        "original_base": "7c44a3a19f79e4beb41af6b55b1bb1cc043d8d42",
        "latest_main_audited": "45db03f76b8aee94e7f3e40c6633c347f372a809",
        "framework_pin_audited": "43897d3afaf0038385102d5acc64793c05ec40f0",
    }
    assert audit["exact_statement"]["status"] == (
        "BOUNDED_RETROSPECTIVE_DERIVATION_SURVIVES"
    )
    assert [step["verdict"] for step in audit["derivation_audit"]] == [
        "PASS_WITH_EXPLICIT_PURE_GAUGE_SCOPE",
        "PASS_AFTER_RETROSPECTIVE_INTERFACE_EXPLICITATION",
        "PASS_BOUNDED",
        "PASS",
        "PASS",
    ]
    assert set(audit["transfer_interfaces"]) == {
        "source_A_to_source_B",
        "finite_to_infinite",
        "polynomial_to_continuous",
        "forbidden_transfers",
    }
    assert all(item["result"].startswith("NOT_TRIGGERED") for item in audit["falsifiers"])


def test_r13_public_history_fails_strict_chronology_without_impossibility() -> None:
    audit = _load()
    chronology = audit["chronology_audit"]
    assert chronology["result_commit"] == {
        "sha": "680de024ec8419147063bf1952ec9f77cfe13fec",
        "committed_at": "2026-08-12T02:12:11Z",
    }
    assert chronology["purported_pre_candidate_fibre_commit"] == {
        "sha": "0b7fd0ab92cb3af1082ac83bdaf502c86636ae00",
        "committed_at": "2026-08-12T02:12:34Z",
        "parent": "680de024ec8419147063bf1952ec9f77cfe13fec",
    }
    assert chronology["verdict"] == "FAIL_STRICT_PRE_CANDIDATE_CHRONOLOGY"
    assert audit["classification"] == {
        "mathematical_truth_check": "PASS_BOUNDED_RETROSPECTIVE",
        "strict_rakl_discovery": "FAIL",
        "overall_pr_state": "DRAFT_BLOCKED_FROM_READY_OR_MERGE",
        "failure_type": "BOUNDED_PROCESS_APPLICABILITY_FAILURE",
        "mathematical_impossibility": False,
        "issue_238_closed": False,
        "independent_review_credit": "0/3",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    }
    assert audit["current_main_failure_atlas_boundary"] == {
        "failure_mechanism": "FM-YM-SAME-THEORY-INTERFACE-AND-DENSITY",
        "status": "SUPPORTED_INTERFACE_FAILURE_UNIQUE_MATHEMATICAL_CAUSE_OPEN",
        "effect_of_r13": "At most the finite-to-infinite reflection-positivity sub-interface is supported retrospectively. Exact covariance-to-transfer moments, a common invariant source algebra, and post-null-quotient density remain unbound, so the current Yang-Mills cause stays open.",
        "impossibility_claimed": False,
    }


def test_r13_authority_and_lesson_remain_proposal_only() -> None:
    audit = _load()
    assert audit["proposal_only_rakl_lesson"] == {
        "id": "L-YM-R13-PUBLIC-PARENT-BEFORE-PROOF-PROPOSAL",
        "status": "PROPOSAL_ONLY_NOT_PROMOTED",
        "text": "For a theorem-like application step, make the complete current-gate packet, including obstruction-transformation review and public pre-candidate trace, a public parent of the first result-capable commit. A prospective issue contract does not substitute for those content-bound artifacts, and later files cannot backfill chronology.",
        "validation_obligation": "On a fresh child atom, require the gate receipt commit to be an ancestor of the candidate commit and make tests fail if any required current-framework event or content-bound artifact is absent.",
        "framework_authority": False,
        "mathematical_credit": False,
    }
    assert audit["authority_contract"] == {
        "grants_strict_discovery_credit": False,
        "grants_theorem_or_novelty_authority": False,
        "grants_root_authority": False,
        "grants_review_independence": False,
        "may_backfill_chronology": False,
        "may_promote_lesson": False,
        "git_ci_schema_hash_runtime_math_credit": 0,
    }
