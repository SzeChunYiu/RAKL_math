"""Assurance checks for the frozen C041 rule, not native-result evidence."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

import jsonschema


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE_PATH = (
    ROOT
    / "research"
    / "real_math"
    / "millennium"
    / "p_vs_np"
    / "04_candidates"
    / "C041_fx_sat_one_sided.py"
)
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FREEZE_PATH = PNP / "09_trace/O9d12a2a1b_C041_FX_SAT_CANDIDATE_FREEZE_20260812.json"
TRACE_PATH = PNP / "09_trace/O9d12a2a1b_C041_CANDIDATE_TRACE_20260812.json"


def _load_candidate():
    spec = importlib.util.spec_from_file_location("c041_fx_sat_one_sided", CANDIDATE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_canonical_decoder_round_trip_and_malformed_polarity() -> None:
    candidate = _load_candidate()
    formula = candidate.Formula3CNF(
        3,
        (
            ((1, False), (2, True), (3, False)),
            ((1, True), (2, False), (3, True)),
        ),
        "TEST_SOURCE",
    )
    encoded = candidate.encode_formula(formula)
    decoded = candidate.decode_formula(encoded)

    assert len(encoded) % 2 == 0
    assert decoded.variable_count == formula.variable_count
    assert decoded.clauses == formula.clauses
    assert decoded.decoder_branch == "CANONICAL_MAGIC_LONG_FORM"
    assert candidate.is_satisfiable(candidate.decode_formula("0000")) is False
    assert candidate.is_satisfiable(candidate.decode_formula("0101")) is True


def test_sat_reduction_has_the_frozen_direction_and_linear_encoding() -> None:
    candidate = _load_candidate()
    satisfiable = candidate.Formula3CNF(
        1,
        (((1, False), (1, False), (1, False)),),
        "TEST_SOURCE",
    )
    contradictory = candidate.CONTRADICTION

    sat_level, sat_row, sat_column = candidate.sat_reduction(satisfiable)
    assert candidate.graph_edge_has_np_witness(
        sat_level, sat_row, sat_column, (True,)
    )

    unsat_level, unsat_row, unsat_column = candidate.sat_reduction(contradictory)
    assert all(
        not candidate.graph_edge_has_np_witness(
            unsat_level, unsat_row, unsat_column, assignment
        )
        for assignment in product((False, True), repeat=1)
    )
    assert len(candidate.encode_formula(satisfiable)) <= 32


def test_rule_is_one_sided_and_seed_identity_is_frozen() -> None:
    candidate = _load_candidate()
    assert candidate.SEED_LEVEL == 2
    assert candidate.SEED_COMPLEMENT == frozenset(
        {(0, 0), (2, 1), (1, 2), (2, 2)}
    )
    # The short code is part of the frozen syntax, not an evaluated LP result.
    assert candidate.complement_contains(3, 0, 4)
    assert not candidate.complement_contains(3, 4, 0)
    assert not candidate.complement_contains(3, 4, 4)


def test_candidate_evaluator_predictions_and_chronology_are_frozen() -> None:
    freeze = json.loads(FREEZE_PATH.read_text(encoding="utf-8"))
    assert freeze["candidate_id"] == "C041-FX-SAT-ONE-SIDED-v1"
    assert freeze["candidate_code"]["sha256"] == _sha256(CANDIDATE_PATH)
    evaluator = PNP / "05_falsification/c041_exact_extension_gate.py"
    assert freeze["evaluator"]["sha256"] == _sha256(evaluator)
    assert freeze["evaluator"]["maximum_child_complement_edges"] == 5
    assert freeze["predictions_frozen_before_native_output"][
        "residual_augmentation"
    ] == "UNKNOWN"
    assert freeze["chronology"] == {
        "candidate_and_evaluator_frozen_before_native_output": True,
        "native_output_accessed": False,
        "no_post_result_threshold_rescue": True,
    }
    assert freeze["artifact_hash"] == _canonical_hash(freeze)


def test_candidate_trace_extends_the_pre_candidate_chain() -> None:
    trace = json.loads(TRACE_PATH.read_text(encoding="utf-8"))
    schema = json.loads(
        (ROOT / "framework/RAKL/schemas/math-research-trace.schema.json").read_text(
            encoding="utf-8"
        )
    )
    jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    ).validate(trace)
    previous = ""
    for entry in trace["entries"]:
        assert entry["previous_event_hash"] == previous
        previous = entry["artifact_hash"]
    last = trace["entries"][-1]
    assert last["event_type"] == "CANDIDATE_PROPOSED"
    assert "candidate_id:C041-FX-SAT-ONE-SIDED-v1" in last["outputs"]
    assert "native_output_accessed:false" in last["outputs"]
    assert last["artifact_hash"] == _canonical_hash(last)
