from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
MATERIALIZER = BASE / "05_falsification/c052_hostile_escape_cell_materializer.py"
RECEIPT = BASE / "05_falsification/O9d12a2a1b_C052_HOSTILE_SUPPORTED_ESCAPE_CELL_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c052_hostile_materializer", MATERIALIZER)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def test_hostile_cell_is_lexicographically_first_complete_escape_cell() -> None:
    value = module()
    receipt = value.materialize()
    assert json.loads(RECEIPT.read_text(encoding="utf-8")) == receipt
    assert receipt["world_id"] == "C052-HOSTILE-SUPPORTED-ESCAPE-CELL-v1"
    assert receipt["selection_rank"] == 1
    assert receipt["selection_rule_id"] == (
        "INDEPENDENT-SYMBOLIC-SUPPORT-SOLVER-WITH-NO-FORCED-MAGIC-CONFLICT-v1"
    )
    assert receipt["support_checks"]["parent_encoded_length"] == 2 * receipt["cell"]["k"]
    assert receipt["support_checks"]["current_encoded_length"] == 2 * (receipt["cell"]["k"] + 1)
    assert receipt["support_checks"]["parent_padding"] in {0, 1}
    assert receipt["support_checks"]["current_padding"] in {0, 1}
    assert receipt["certificate"]["all_h1_through_h7_in_literal_payload"] is True
    assert receipt["certificate"]["universally_forced_unequal_coordinates"] == []
    assert "unsat_preserving_witness_family" not in receipt["certificate"]
    assert receipt["semantic_status_after_review"] == "CANNOT_CHECK_CERTIFICATE_INSUFFICIENT"
    assert receipt["native_gate_after_review"] == "BLOCKED"
    assert receipt["certificate"]["classifier_branch_expected"] == "ESCAPE_ADMISSIBLE"
    assert receipt["certificate"]["not_overlap_witness"] is True
    assert receipt["authority"]["computation_is_proof"] is False
    assert receipt["authority"]["root"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_hostile_materializer_is_independent_of_classifier_decoder_and_sat() -> None:
    source = MATERIALIZER.read_text(encoding="utf-8")
    forbidden = [
        "c052_support_phase_classifier",
        "C041_fx_sat_one_sided",
        "decode_formula",
        "is_satisfiable",
        "def compare_languages",
        "def test_intersection",
    ]
    assert not any(token in source for token in forbidden)
