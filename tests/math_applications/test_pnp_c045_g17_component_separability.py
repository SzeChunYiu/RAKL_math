from __future__ import annotations

import copy
import hashlib
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
PATH = PNP / "05_falsification/c045_g17_component_separability.py"
RECEIPT = PNP / "05_falsification/C045_G17_COMPONENT_SEPARABILITY_RECEIPT_20260812.json"
RESULT = PNP / "04_candidates/C045_G17_COMPONENT_SEPARABILITY_RESULT_20260812.md"
C043 = PNP / "05_falsification/C043_FIRST_ROW_SPLIT_RECEIPT_20260812.json"
C044 = PNP / "04_candidates/C044_RETROSPECTIVE_Q16_MULTIPLEXING_RESULT_20260812.md"
DAG = PNP / "02_problem_dag/O9d12a2a1b_C045_DELTA_20260812.json"
CASE = PNP / "07_memory/O9d12a2a1b_C045_RETROSPECTIVE_TASK_EPISODE_CASE_STUDY_20260812.json"
REVIEW = PNP / "08_reviews/O9d12a2a1b_C045_EXPERT_CELL_REVIEW_20260812.json"
TRACE = PNP / "09_trace/O9d12a2a1b_C045_RETROSPECTIVE_RECONCILIATION_TRACE_AND_METRICS_20260812.json"

spec = spec_from_file_location("c045_retrospective", PATH)
mod = module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(mod)


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _entry_hash(value: dict) -> str:
    payload = {key: child for key, child in value.items() if key != "artifact_hash"}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_c045_finite_calibration_reproduces_exact_quantitative_core() -> None:
    out = mod.verify()
    receipt = _load(RECEIPT)
    assert out == {
        "unsat_word_count": 10,
        "new_edge_count": 10,
        "local_uncovered_active_cells": 0,
        "status": "CALIBRATION_MATCH",
    }
    assert out["unsat_word_count"] == receipt["length32"]["count"]
    assert out["new_edge_count"] == len(receipt["length32"]["new_edges"])
    assert out["local_uncovered_active_cells"] == receipt["local_cover"]["uncovered_active_cells"]
    assert mod.all_length32_unsat() == sorted(f"{r:016b}{c:016b}" for r, c in mod.NEW_EDGES)


def test_c045_hand_length_scope_and_full_history_projection_claims_are_bound() -> None:
    receipt = _load(RECEIPT)
    # The only raw lengths 31/32 under the frozen formula are the stated cases.
    cases = []
    for v in range(1, 128):
        for m in range(1, 32):
            a, b = v.bit_length(), m.bit_length()
            raw = 6 + 2 * a + 2 * b + 3 * m * (a + 1)
            if raw in (31, 32):
                cases.append((v, m, raw))
    assert sorted(cases) == sorted([(v, 1, 31) for v in range(8, 16)] + [(2, 2, 32), (3, 2, 32)])
    assert receipt["length32"]["candidate_parameter_pairs"] == {
        "satisfiable_only": [["v=8..15", "m=1"]],
        "potential_unsat": [[2, 2], [3, 2]],
    }

    parent = _load(C043)["full_accumulated_G16"]
    nonempty_types = [row for row in parent["row_types"] if row["complement_neighborhood"]]
    assert all(row["vertices_truncated"] is False for row in nonempty_types)
    old_active_rows = {member for row in nonempty_types for member in row["vertices"]}
    new_rows = {row for row, _ in mod.NEW_EDGES}
    assert old_active_rows.isdisjoint(new_rows)
    assert all(65536 + offset >= 65536 for _, offset in mod.NEW_EDGES)
    gate = receipt["component_gate"]
    assert gate["row_projections_disjoint"] is True
    assert gate["column_projections_disjoint"] is True
    assert gate["cross_component_complement_cells"] == []


def test_c045_explicit_three_bit_cover_separates_all_38_active_cells() -> None:
    receipt = _load(RECEIPT)
    signs = mod.signatures()
    assert signs["bad"] == []
    assert {str(k): v for k, v in signs["rows"].items()} == receipt["local_cover"]["row_signatures"]
    assert {str(k): v for k, v in signs["cols"].items()} == receipt["local_cover"]["column_signatures"]
    edges = set(mod.NEW_EDGES)
    active = sum((r, c) not in edges for r in signs["rows"] for c in signs["cols"])
    assert active == receipt["local_cover"]["active_cells"] == 38


def test_c045_global_claim_is_upper_only_and_math_lesson_is_projection_collision() -> None:
    receipt = _load(RECEIPT)
    result = RESULT.read_text(encoding="utf-8")
    c044 = C044.read_text(encoding="utf-8")
    assert receipt["global_conclusion"]["proved"] == "rho(G17) <= sigma(G17) <= 4"
    assert "rho(G_{16})\\le\\rho(Q_{16})\\le3" in c044
    for forbidden in ["rho(G17)=4", "rho(G17)>3", "circuit lower bound", "P != NP"]:
        assert forbidden in receipt["global_conclusion"]["not_proved"]
    assert "Fresh columns alone never couple backward" in result
    assert "first row-projection collision" in result.lower()
    assert receipt["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_c045_receipts_trace_and_shadow_authority_fail_closed() -> None:
    for path in [RECEIPT, DAG, CASE, REVIEW, TRACE]:
        value = _load(path)
        assert value["artifact_hash"] == _canonical_hash(value)

    trace = _load(TRACE)
    previous = "sha256:959a2fd74585a8f8356ff4a9b7a4653a541bcd19e24f54c77fbd80f16c154aa6"
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        assert entry["artifact_hash"] == _entry_hash(entry)
        previous = entry["artifact_hash"]
    assert trace["authority"] == "PROPOSAL_SHADOW_RETROSPECTIVE_TRUTH_CHECK_ONLY"
    assert trace["RAKL_CYCLE_METRICS"]["retained_semantic_novelty"] == {
        "KNOWLEDGE": 0,
        "OPERATOR": 0,
        "EXPERIENCE_PATTERN": 0,
        "OBSTRUCTION": 0,
        "RELATION": 0,
        "PATH": 0,
        "META_METHOD": 0,
        "note": "All nonzero observations are proposal/shadow only; raw files, commits, CI and prose are not learning.",
    }

    case = _load(CASE)
    assert case["authority"] == "PROPOSAL_SHADOW_RETROSPECTIVE_TRUTH_CHECK_ONLY"
    assert case["reusable_obstruction_or_lesson"]["statement"].startswith(
        "For the frozen one-sided recursive family"
    )
    # It is deliberately a noncanonical wrapper, not a promoted TaskEpisode.
    schema = _load(ROOT / "framework/RAKL/schemas/task-episode.schema.json")
    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(case))
    assert errors
    assert case["RAKL_METHOD_CASE_STUDY"]["credit_policy"].startswith(
        "All mathematical and method records remain proposal/shadow"
    )

FAILURE = PNP / "07_memory/O9d12a2a1b_C045_U17_COUPLING_FAILURE_DELTA_20260812.json"
LESSON = PNP / "10_feedback/C045_ROW_PROJECTION_COLLISION_MATHEMATICAL_LESSON_20260812.json"


def test_c045_canonical_failure_and_math_only_lesson_are_runtime_valid() -> None:
    from rakl.failure_lattice import reconstruct_failure_lattice
    from rakl.schema_reference_constraints import check_reference_constraints

    failure = _load(FAILURE)
    schema = _load(ROOT / "framework/RAKL/schemas/failure-experience-lattice.schema.json")
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(failure)
    assert check_reference_constraints(failure, schema) == ()
    lattice = reconstruct_failure_lattice(failure)
    assert len(lattice.experiences) == 1 and lattice.links == ()
    experience = failure["experiences"][0]
    assert experience["artifact_hash"] == _canonical_hash(experience)
    assert experience["diagnosis_status"] == "SUPPORTED"
    assert "does not establish" in experience["selected_diagnosis"]

    lesson = _load(LESSON)
    assert lesson["artifact_hash"] == _canonical_hash(lesson)
    assert lesson["mathematical_saturation_credit"] is True
    assert lesson["strict_rakl_discovery_credit"] is False
    assert lesson["protected_novelty_promotion"] is False
    assert "necessary for backward coupling" in lesson["mathematical_statement"]
    assert any("not sufficient for cover growth" in item for item in lesson["non_guarantees"])
    assert "Git/PR/branch state" in lesson["assurance_only_zero_credit"]
