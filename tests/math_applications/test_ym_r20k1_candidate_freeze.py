from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research/real_math/millennium/yang_mills"
FIXTURE = YM / "09_trace/ym_r20k1_candidate_freeze_fixture.py"
INERT = YM / "05_oracles/ym_r20k1_inert_scalar_falsifier.py"


def _module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_documents_match_result_blind_fixture() -> None:
    module = _module("ym_r20k1_candidate", FIXTURE)
    expected = module.build_documents()
    assert set(expected) == set(module.PATHS)
    for name, relative in module.PATHS.items():
        assert _load(ROOT / relative) == expected[name], name


def test_repaired_public_receipt_is_exactly_acknowledged_before_candidate() -> None:
    module = _module("ym_r20k1_durability", FIXTURE)
    doc = module.build_documents()["durability"]
    public = doc["public_receipt"]
    path = ROOT / public["path"]
    assert doc["durable_state"] == "MATERIALIZED"
    assert doc["literal_hook_status"] == "ALREADY_MATERIALIZED"
    assert doc["hook_result"]["durable_receipt_pointer"].startswith(
        f"git+https://github.com/SzeChunYiu/RAKL_math.git@{module.PUBLIC_RECEIPT_COMMIT}"
    )
    assert doc["hook_result"]["receipt_canonical_sha256"] == module.PRE_RECEIPT_CANONICAL_SHA256
    assert hashlib.sha256(path.read_bytes()).hexdigest() == public["raw_sha256"]
    blob = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", f"{module.PUBLIC_RECEIPT_COMMIT}:{public['path']}"],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    assert blob == public["git_blob"]
    selected = {
        row["retrieval_id"]: row["payload_hash"]
        for row in doc["hook_result"]["receipt"]["selected_retrievals"]
    }
    assert selected["YM-R20-lesson"] == "18c39a9a7ea90fede4fb3672d1e777886fea7e88e094f453bb8fada799018a73"
    assert selected["global-failure-atlas"] == "db809b89815e0ca6a58eaa915e531bcd52d127f5449469dd087f349763f69d11"


def test_exact_symbolic_candidate_and_quantifiers_are_frozen_without_values() -> None:
    module = _module("ym_r20k1_scope", FIXTURE)
    candidate = module.build_documents()["candidate"]
    statement = candidate["candidate_statement"]
    assert statement == {
        "lower_base_factor": "L(g)=1-b_0 g^2-C_beta g^4",
        "scalar_margin": "M(g)=L(g)^2-rho-(C_K/c_K)g^2",
        "existence_claim": "there exists epsilon>0 such that L(g)>=0 and M(g)>=0 for every 0<g<=epsilon",
        "conditional_implication": "under the frozen source hypotheses and scalar inequalities, ||K_{k+1}||_{k+1} <= c_K g_{k+1}^2",
        "derivation_shape_to_check_later": [
            "g_{k+1} >= g_k L(g_k)",
            "c_K g_{k+1}^2 >= c_K g_k^2 L(g_k)^2 when L(g_k)>=0",
            "rho c_K g_k^2+C_K g_k^4 <= c_K g_k^2 L(g_k)^2 when M(g_k)>=0",
        ],
    }
    assert candidate["quantifier_order"].startswith("FOR_ALL source-bound constants")
    assert {row["status"] for row in candidate["proof_obligations"]} == {"FROZEN_UNEVALUATED"}
    o1 = next(row for row in candidate["proof_obligations"] if row["id"] == "O1-SOURCE-UNIFORMITY")
    assert o1["required_source_constants"] == ["rho", "c_K", "C_K", "b_0", "C_beta"]
    assert set(o1["required_source_constants"]) == set(candidate["symbolic_constants"]) - {"epsilon"}
    assert candidate["future_result_lesson_contract"]["current_status"] == "NO_RESULT_NO_LESSON"
    assert candidate["authority"]["mathematical_result_credit"] is False
    assert candidate["authority"]["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    serialized = json.dumps(candidate, sort_keys=True)
    for forbidden in (
        "epsilon=",
        "rho=",
        "C_K=",
        "b_0=",
        "observed_result",
        "PROVED_RESULT",
    ):
        assert forbidden not in serialized


def test_result_branches_and_evaluation_firewall_are_frozen() -> None:
    module = _module("ym_r20k1_firewall", FIXTURE)
    docs = module.build_documents()
    candidate = docs["candidate"]
    authorization = docs["authorization"]
    assert candidate["allowed_result_branches"] == [
        "CONDITIONAL_UNIFORM_SCALAR_SLACK_PROVED",
        "SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT",
        "SCALAR_EXISTENCE_OR_COMPOSITION_REFUTED",
        "CANNOT_CHECK",
    ]
    assert candidate["target_access"] == {
        "falsifier_imported_or_executed": False,
        "source_uniformity_checked": False,
        "scalar_existence_checked": False,
        "threshold_derived_or_tested": False,
        "result_accessed": False,
    }
    assert authorization["current_round_falsifier_execution_authorized"] is False
    assert authorization["source_constant_extraction_authorized"] is False
    assert authorization["symbolic_or_numeric_threshold_derivation_authorized"] is False
    assert authorization["result_classification_authorized"] is False


def test_candidate_trace_chain_uses_standard_empty_hash_seal() -> None:
    module = _module("ym_r20k1_trace", FIXTURE)
    trace = module.build_documents()["trace"]
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        payload = dict(entry)
        declared = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert declared == module.canonical_hash(payload)
        previous = declared


def test_framework_diff_is_exact_and_math_candidate_gates_are_unchanged() -> None:
    module = _module("ym_r20k1_framework", FIXTURE)
    actual = subprocess.run(
        [
            "git", "-C", str(ROOT / "framework/RAKL"), "diff", "--name-only",
            f"{module.PRE_FRAMEWORK_SHA}..{module.CURRENT_FRAMEWORK_SHA}",
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.splitlines()
    assert set(actual) == (
        set(module.NON_METHOD_FRAMEWORK_DIFF)
        | set(module.METHOD_ADJACENT_OPTIONAL_UNWIRED_DIFF)
        | set(module.POST_496_NON_METHOD_FRAMEWORK_DIFF)
        | set(module.POST_E3FFC_NON_METHOD_FRAMEWORK_DIFF)
    )
    assert set(module.METHOD_ADJACENT_OPTIONAL_UNWIRED_DIFF) == {
        "src/rakl/structural_transport_v2.py",
        "tests/test_structural_transport_v2.py",
    }
    protected_math_prefixes = (
        "src/rakl/math_", "src/rakl/research_", "src/rakl/semantic_shortcut.py",
        "src/rakl/framework_candidate_freeze.py", "src/rakl/pre_scratch_fibre_freeze.py",
        "schemas/math-", "schemas/research-", "skills/rakl-core/workflows/mathematical-research.md",
    )
    assert not any(path.startswith(protected_math_prefixes) for path in actual)
    framework = module.build_documents()["framework"]
    review = framework["pre_candidate_to_current_review"]
    assert review["method_adjacent_classification"] == "METHOD_ADJACENT_OPTIONAL_UNWIRED_REVIEWED"
    assert review["structural_transport_ancestry_sha"] == module.STRUCTURAL_TRANSPORT_ANCESTRY_SHA
    assert review["post_496_non_method_publication_or_empirical_research_paths"] == list(
        module.POST_496_NON_METHOD_FRAMEWORK_DIFF
    )
    successor = review["latest_non_method_successor"]
    assert successor == {
        "from_sha": module.PRE_LATEST_NON_METHOD_SUCCESSOR_SHA,
        "to_sha": module.CURRENT_FRAMEWORK_SHA,
        "classification": "NON_METHOD_PAPER2_CAPABILITY_INTERFACE_CHALLENGER_REVIEWED",
        "changed_paths": list(module.POST_E3FFC_NON_METHOD_FRAMEWORK_DIFF),
        "ym_mathematical_gate_changed": False,
    }
    assert review["core_pre_candidate_contracts_changed"] is False
    assert "neither prove nor refute" in review["same_domain_scalar_effect"]
    assert framework["freeze_binding"]["authoritative_framework_sha"] == module.CURRENT_FRAMEWORK_SHA
    assert framework["verdict"] == "CURRENT_UNCHANGED"
    assert framework["licenses_candidate_materialization"] is True
    assert framework["grants_scientific_authority"] is False


def test_falsifier_is_actually_inert() -> None:
    module = _module("ym_r20k1_inert", INERT)
    fixture = _module("ym_r20k1_falsifier_hash", FIXTURE)
    raw_sha256 = hashlib.sha256(INERT.read_bytes()).hexdigest()
    assert raw_sha256 == fixture.INERT_FALSIFIER_RAW_SHA256
    assert fixture.inert_falsifier_raw_sha256(ROOT) == raw_sha256
    docs = fixture.build_documents()
    assert docs["manifest"]["raw_sha256"] == raw_sha256
    assert docs["receipt"]["full_document_integrity"]["byte_inputs"]["inert_falsifier"]["raw_sha256"] == raw_sha256
    with pytest.raises(module.TargetEvaluationNotAuthorized):
        module.evaluate()
    source = INERT.read_text(encoding="utf-8")
    for forbidden in ("sympy", "mpmath", "subprocess", "scipy", "requests"):
        assert forbidden not in source


def test_stale_falsifier_hash_fails_before_document_materialization(monkeypatch) -> None:
    fixture = _module("ym_r20k1_stale_falsifier_hash", FIXTURE)
    monkeypatch.setattr(fixture, "INERT_FALSIFIER_RAW_SHA256", "0" * 64)
    with pytest.raises(RuntimeError, match="inert falsifier byte hash mismatch"):
        fixture.build_documents()
