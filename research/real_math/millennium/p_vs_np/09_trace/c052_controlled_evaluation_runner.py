"""Execute the three frozen C052 controlled worlds in mandatory order."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
CLASSIFIER_PATH = BASE / "04_candidates/c052_support_phase_classifier.py"
FALSIFIER_PATH = BASE / "05_falsification/c052_independent_classifier_falsifier.py"
CLASSIFIER_IDENTITY = BASE / "04_candidates/O9d12a2a1b_C052_TARGET_BLIND_CLASSIFIER_IDENTITY_20260812.json"
FALSIFIER_IDENTITY = BASE / "05_falsification/O9d12a2a1b_C052_INDEPENDENT_HOSTILE_FALSIFIER_IDENTITY_20260812.json"
AUTHORIZATION = BASE / "09_trace/O9d12a2a1b_C052_EVALUATION_AUTHORIZATION_20260812.json"
HOSTILE = BASE / "05_falsification/O9d12a2a1b_C052_HOSTILE_SUPPORTED_ESCAPE_CELL_20260812.json"
C050_SOURCE = BASE / "05_falsification/O9d12a2a1b_C050_K15_PROOF_CHECK_RESULT_20260812.json"
C051_SOURCE = BASE / "05_falsification/O9d12a2a1b_C051_K19_PROOF_RESULT_20260812.json"
OUTPUT = BASE / "05_falsification/O9d12a2a1b_C052_CONTROLLED_EVALUATION_RESULT_20260812.json"
EXECUTED_AT = "2026-08-12T12:51:27Z"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _raw_sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _seal(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


def _cell(*, k: int, a: int, m: int, a_plus: int, m_plus: int) -> dict:
    def raw(aa: int, mm: int) -> int:
        return 6 + 2 * aa + 2 * mm.bit_length() + 3 * mm * (1 + aa)

    parent_raw = raw(a, m)
    current_raw = raw(a_plus, m_plus)
    return {
        "k": k,
        "a": a,
        "b": m.bit_length(),
        "m": m,
        "v_range": [1 << (a - 1), (1 << a) - 1],
        "parent_padding": parent_raw % 2,
        "a_plus": a_plus,
        "b_plus": m_plus.bit_length(),
        "m_plus": m_plus,
        "v_plus_range": [1 << (a_plus - 1), (1 << a_plus) - 1],
        "current_padding": current_raw % 2,
        "literal_index_quantifier": "ALL_LEGAL_1_TO_V",
        "literal_sign_quantifier": "BOTH",
    }


def _hostile_cell() -> dict:
    source = _load(HOSTILE)["cell"]
    return _cell(
        k=source["k"],
        a=source["a"],
        m=source["m"],
        a_plus=source["a_plus"],
        m_plus=source["m_plus"],
    )


def _compact_audit(audit: dict) -> dict:
    recomputed = audit["independent_recomputation"]
    return {
        "outcome": audit["outcome"],
        "expected_branch": audit["expected_branch"],
        "reason": audit["reason"],
        "recomputed_support_phase_quantifier_coverage": audit["recomputed_support_phase_quantifier_coverage"],
        "classifier_certificate_reused": audit["classifier_certificate_reused"],
        "recomputed_support": recomputed.get("support"),
        "recomputed_phi_c0": recomputed.get("phi_c0"),
        "recomputed_first_conflict": recomputed.get("first_conflict"),
        "recomputed_coordinates_sha256": "sha256:" + hashlib.sha256(
            json.dumps(recomputed.get("coordinates"), sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def run() -> dict:
    authorization = _load(AUTHORIZATION)
    if authorization["identities"] != {
        "classifier_raw_sha256": _raw_sha(CLASSIFIER_IDENTITY),
        "falsifier_raw_sha256": _raw_sha(FALSIFIER_IDENTITY),
    }:
        raise RuntimeError("public identity bytes differ from the frozen authorization")
    c050 = _load(C050_SOURCE)
    c051 = _load(C051_SOURCE)
    if c050["exact_mathematical_result"]["separation"] != (
        "Every h in H_15 has h[3]=1, while every p in P_16 has p[3]=MAGIC[3]=0."
    ):
        raise RuntimeError("C050 regression source does not state the frozen bit-3 world")
    if c051["decisive_falsifier_result"] != (
        "Every h in H_19 has h[3]=1 and every p in P_20 has p[3]=0."
    ):
        raise RuntimeError("C051 regression source does not state the frozen bit-3 world")
    classifier = _load_module("c052_controlled_classifier", CLASSIFIER_PATH)
    falsifier = _load_module("c052_controlled_falsifier", FALSIFIER_PATH)
    world_inputs = [
        (
            "C050-k15-bounded-regression",
            "FORCED_CONFLICT",
            [
                ("C050-current-a2-m2", _cell(k=15, a=1, m=3, a_plus=2, m_plus=2)),
                ("C050-current-a4-m1", _cell(k=15, a=1, m=3, a_plus=4, m_plus=1)),
            ],
            {"path": str(C050_SOURCE.relative_to(ROOT)), "raw_sha256": _raw_sha(C050_SOURCE)},
        ),
        (
            "C051-k19-bounded-regression",
            "FORCED_CONFLICT",
            [("C051-current-a3-m2", _cell(k=19, a=1, m=4, a_plus=3, m_plus=2))],
            {"path": str(C051_SOURCE.relative_to(ROOT)), "raw_sha256": _raw_sha(C051_SOURCE)},
        ),
        (
            "C052-HOSTILE-SUPPORTED-ESCAPE-CELL-v1",
            "ESCAPE_ADMISSIBLE",
            [("C052-hostile-first-authorized-cell", _hostile_cell())],
            {"path": str(HOSTILE.relative_to(ROOT)), "raw_sha256": _raw_sha(HOSTILE)},
        ),
    ]
    worlds: list[dict] = []
    all_pass = True
    for world_id, expected_branch, inputs, source in world_inputs:
        cases: list[dict] = []
        for case_id, cell in inputs:
            classified = classifier.classify(cell)
            audited = falsifier.audit(cell, classified)
            passed = classified["branch"] == expected_branch and audited["outcome"] == "CLASSIFIER_SURVIVES"
            all_pass &= passed
            cases.append({
                "case_id": case_id,
                "cell": cell,
                "expected_branch": expected_branch,
                "classifier_branch": classified["branch"],
                "classifier_certificate": classified["certificate"],
                "falsifier": _compact_audit(audited),
                "passed": passed,
            })
        worlds.append({
            "world_id": world_id,
            "source": source,
            "cases": cases,
            "classifier_branches": [case["classifier_branch"] for case in cases],
            "falsifier_outcomes": [case["falsifier"]["outcome"] for case in cases],
            "passed": all(case["passed"] for case in cases),
        })
    if not all_pass:
        raise RuntimeError("one or more frozen controlled worlds failed")
    raw_result = _seal({
        "schema_version": "1.0.0",
        "result_id": "PNP-C052-CONTROLLED-CLASSIFIER-EVALUATION-20260812",
        "atom_id": "O9d12a2a1b-C052",
        "executed_at_utc": EXECUTED_AT,
        "authorization": {
            "path": str(AUTHORIZATION.relative_to(ROOT)),
            "artifact_hash": authorization["artifact_hash"],
            "identity_public_merge": authorization["identity_public_merge"],
        },
        "implementation_bytes": {
            "classifier_path": str(CLASSIFIER_PATH.relative_to(ROOT)),
            "classifier_raw_sha256": _raw_sha(CLASSIFIER_PATH),
            "falsifier_path": str(FALSIFIER_PATH.relative_to(ROOT)),
            "falsifier_raw_sha256": _raw_sha(FALSIFIER_PATH),
            "byte_distinct": _raw_sha(CLASSIFIER_PATH) != _raw_sha(FALSIFIER_PATH),
            "falsifier_imports_classifier": False,
        },
        "execution_order": [world["world_id"] for world in worlds],
        "worlds": worlds,
        "verdict": "PASS_CONTROLLED_WORLDS",
        "exact_bounded_result": {
            "regressions": "Both complete C050 current support cells and the C051 current support cell retain the exact h[3]=1 versus MAGIC[3]=0 conflict under the total classifier.",
            "hostile_escape": "The authorized controlled cell k=20, parent (a,b,m)=(3,2,2), current (a_plus,b_plus,m_plus)=(2,2,3), has exact adjacent support and no universally forced unequal coordinate among h[0] through h[7].",
            "logical_consequence": "The local forced-MAGIC-conflict obstruction is not universal over supported adjacent cells. This says nothing about actual language intersection in the escape cell.",
        },
        "raw_pre_review_proposed_lesson": {
            "status": "ZERO_CREDIT_SUPERSEDED_CERTIFICATE",
            "attempted_implication": "The repeated C050/C051 bit-3 conflict might persist across every adjacent support cell represented by the C052 support/phase coordinates.",
            "exact_result_or_failure": "That implication is not universal: the bounded hostile k=20 support cell is ESCAPE_ADMISSIBLE for the local eight-coordinate obstruction, while the frozen k=15 and k=19 regression worlds remain FORCED_CONFLICT.",
            "supported_and_competing_causes": "Supported bounded cause is the parent a=3 token width: complete v=4..7 and legal-index coverage makes each encountered variable-code bit nonconstant, and sign bits are also nonconstant. Rejected causes include chosen padding, one representative v, omitted signs, h[0]/h[1] conflation, regression drift, and an inferred language intersection.",
            "scope": "C050 k=15, C051 k=19, and the controlled k=20 hostile cell under the exact C041 syntax and local coordinates 0..7; no native class, semantic UNSAT, intersection, cover, circuit, or root claim.",
            "mathematical_falsifier": "Any failed support equation, omitted v/index/sign case, a forced unequal coordinate in the hostile cell, or failure to reproduce either regression refutes the bounded result.",
            "repair_or_next_discriminator": "Freeze a target-blind native parametric evaluation identity over an explicit cell domain; classify the whole frozen domain rather than selecting another favorable k, and preserve all four branches.",
            "proof_and_source_evidence": "C050/C051 exact hand certificates plus the independently materialized hostile receipt, classifier certificates, and separately recomputed falsifier audits recorded here. The computation is bounded evidence, not formal proof or independent peer review.",
        },
        "authority": {
            "bounded_mathematical_result": True,
            "computation_is_proof": False,
            "formal_proof": False,
            "independent_peer_review": False,
            "native_parametric_evaluation_executed": False,
            "root": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
        "next_gate": "SUPERSEDED_BY_POST_EXECUTION_SEMANTIC_REVIEW",
    })
    raw_result["raw_pre_review_artifact_hash"] = raw_result.pop("artifact_hash")
    raw_result["raw_execution_verdict"] = raw_result.pop("verdict")
    raw_result["verdict"] = "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT"
    raw_result["native_parametric_gate"] = "BLOCKED"
    raw_result["superseded_by"] = "research/real_math/millennium/p_vs_np/08_reviews/O9d12a2a1b_C052_V1_CONTROLLED_SEMANTIC_FALSIFICATION_20260812.json"
    raw_result["authority"] = {
        "raw_v1_program_agreement_preserved": True,
        "v1_evaluator_mathematical_credit": 0,
        "computation_is_proof": False,
        "formal_proof": False,
        "independent_peer_review": False,
        "native_parametric_evaluation_executed": False,
        "root": "OPEN_NO_SOLUTION_CERTIFICATE",
    }
    raw_result["next_gate"] = "FREEZE_V2_UNSAT_AWARE_CLASSIFIER_AND_FRESH_HOSTILE_WORLD_BEFORE_EXECUTION"
    return _seal(raw_result)


def write() -> dict:
    receipt = run()
    OUTPUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return receipt


if __name__ == "__main__":
    write()
