from __future__ import annotations

import importlib.util
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
RUNNER = BASE / "09_trace/c052_controlled_evaluation_runner.py"
RESULT = BASE / "05_falsification/O9d12a2a1b_C052_CONTROLLED_EVALUATION_RESULT_20260812.json"
SEMANTIC = BASE / "08_reviews/O9d12a2a1b_C052_V1_CONTROLLED_SEMANTIC_FALSIFICATION_20260812.json"
PROOF = BASE / "04_candidates/O9d12a2a1b_C052_K20_UNSAT_AWARE_LOCAL_ESCAPE_HAND_PROOF_20260812.json"
LESSON = BASE / "07_memory/O9d12a2a1b_C052_LOCAL_OBSTRUCTION_ESCAPE_MATHEMATICAL_LESSON_20260812.json"
FAILURE = BASE / "07_memory/O9d12a2a1b_C052_LOCAL_CONFLICT_UNIVERSALITY_FAILURE_EXPERIENCE_20260812.json"
V1_FAILURE = BASE / "07_memory/O9d12a2a1b_C052_V1_UNSAT_SUBSET_OMISSION_FAILURE_EXPERIENCE_20260812.json"
TRACE = BASE / "09_trace/O9d12a2a1b_C052_CONTROLLED_EVALUATION_TRACE_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c052_controlled_runner", RUNNER)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def test_raw_controlled_evaluation_receipt_matches_exact_rerun_but_is_not_promoted() -> None:
    receipt = module().run()
    assert json.loads(RESULT.read_text(encoding="utf-8")) == receipt
    assert [world["world_id"] for world in receipt["worlds"]] == [
        "C050-k15-bounded-regression",
        "C051-k19-bounded-regression",
        "C052-HOSTILE-SUPPORTED-ESCAPE-CELL-v1",
    ]
    assert receipt["worlds"][0]["classifier_branches"] == [
        "FORCED_CONFLICT",
        "FORCED_CONFLICT",
    ]
    assert receipt["worlds"][1]["classifier_branches"] == ["FORCED_CONFLICT"]
    assert receipt["worlds"][2]["classifier_branches"] == ["ESCAPE_ADMISSIBLE"]
    assert all(world["falsifier_outcomes"] == ["CLASSIFIER_SURVIVES"] * len(world["cases"]) for world in receipt["worlds"])
    assert receipt["raw_execution_verdict"] == "PASS_CONTROLLED_WORLDS"
    assert receipt["verdict"] == "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT"
    assert receipt["native_parametric_gate"] == "BLOCKED"
    assert receipt["authority"]["v1_evaluator_mathematical_credit"] == 0
    assert receipt["next_gate"] == "FREEZE_V2_UNSAT_AWARE_CLASSIFIER_AND_FRESH_HOSTILE_WORLD_BEFORE_EXECUTION"
    semantic = json.loads(SEMANTIC.read_text(encoding="utf-8"))
    assert semantic["raw_execution_verdict_preserved"] == "PASS_CONTROLLED_WORLDS"
    assert semantic["semantic_outcome"] == "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT"
    assert semantic["v1_controlled_gate"] == "FAILED_BLOCKED"
    assert semantic["native_parametric_gate"] == "BLOCKED"


def test_semantic_falsification_states_exact_failure_and_limits() -> None:
    semantic = json.loads(SEMANTIC.read_text(encoding="utf-8"))
    lesson = semantic["seven_field_failure_lesson"]
    assert set(lesson) == {
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "falsifier",
        "mathematical_repair",
        "proof_and_source_evidence",
    }
    assert "UNSAT subset" in lesson["exact_result_or_failure"]
    assert semantic["same_context_review_is_independent_peer_review"] is False
    assert semantic["repairs_v1_retroactively"] is False
    assert semantic["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_runner_never_imports_decoder_or_sat_surfaces() -> None:
    source = RUNNER.read_text(encoding="utf-8")
    for forbidden in ("C041_fx_sat_one_sided", "decode_formula", "is_satisfiable", "materialize_complement"):
        assert forbidden not in source


def test_math_lesson_and_failure_lattice_capture_the_bounded_counterpattern() -> None:
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    fields = lesson["seven_field_math_lesson"]
    assert set(fields) == {
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "falsifier",
        "mathematical_repair",
        "proof_and_source_evidence",
    }
    assert lesson["mathematical_unit_count"] == 1
    assert lesson["deduplication"]["software_process_credit"] == 0
    assert "not an intersection witness" in fields["exact_result_or_failure"]
    assert lesson["evidence_pointers"][0] == str(PROOF.relative_to(ROOT))
    failure = json.loads(FAILURE.read_text(encoding="utf-8"))
    assert failure["failure_id"] == "F-PNP-C052-LOCAL-FORCED-CONFLICT-UNIVERSALITY-REFUTED"
    assert failure["diagnosis_status"] == "SUPPORTED_BOUNDED_NOT_UNIQUE_GLOBAL_CAUSE"
    assert [relation["target_failure_id"] for relation in failure["typed_relations"]] == [
        "F-PNP-C050-K15-FIXED-VARIABLE-BIT-VERSUS-MAGIC",
        "F-PNP-C051-K19-FIXED-VARIABLE-BIT-VERSUS-MAGIC",
    ]
    v1_failure = json.loads(V1_FAILURE.read_text(encoding="utf-8"))
    assert v1_failure["failure_id"] == "F-PNP-C052-V1-UNSAT-SUBSET-OMISSION"
    assert v1_failure["observed_result"].startswith("Raw candidate/falsifier agreement")
    assert v1_failure["diagnosis_status"] == "SUPPORTED"


def test_controlled_trace_appends_falsifier_result_and_residual_with_valid_hash_chain() -> None:
    trace = json.loads(TRACE.read_text(encoding="utf-8"))
    assert [entry["event_type"] for entry in trace["entries"][-5:]] == [
        "FALSIFIER_RUN",
        "REVIEWED",
        "RESULT_RECORDED",
        "RESIDUAL_OPENED",
        "RESULT_RECORDED",
    ]
    for previous, current in zip(trace["entries"], trace["entries"][1:]):
        assert current["previous_event_hash"] == previous["artifact_hash"]
    for entry in trace["entries"][-5:]:
        core = dict(entry)
        observed = core.pop("artifact_hash")
        expected = "sha256:" + hashlib.sha256(
            json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        assert observed == expected
