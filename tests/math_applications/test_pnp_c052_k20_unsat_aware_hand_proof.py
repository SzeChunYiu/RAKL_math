from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/p_vs_np"
CHECKER = BASE / "05_falsification/c052_k20_unsat_aware_hand_proof_checker.py"
PROOF = BASE / "04_candidates/O9d12a2a1b_C052_K20_UNSAT_AWARE_LOCAL_ESCAPE_HAND_PROOF_20260812.json"


def module():
    spec = importlib.util.spec_from_file_location("c052_k20_hand_proof", CHECKER)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def test_k20_hand_proof_matches_independent_exact_checker() -> None:
    proof = module().build_proof()
    assert json.loads(PROOF.read_text(encoding="utf-8")) == proof
    assert proof["claim"] == (
        "Within H_20, no coordinate j in 0..7 is universally fixed to a bit unequal to MAGIC[j]."
    )
    assert proof["support_derivation"] == {
        "parent": "H=16, w=4, R=16+3*2*4=40, padding=0, k=20",
        "current": "H_plus=14, w_plus=3, R_plus=14+3*3*3=41, padding_plus=1, E_plus=42=2*(20+1)",
        "suffix_phase": "phi_c0=(20-16) mod 4=0",
        "index_map": "h[0]=1; h[1..4] are token-2 sign/index bits x[20..23]; h[5..7] are token-3 sign/first-two-index bits x[24..26]",
    }
    assert len(proof["unsat_preserving_witness_family"]) == 44
    assert all(witness["unsat_proof"] == "opposite repeated unit clauses" for witness in proof["unsat_preserving_witness_family"])
    coordinates = proof["coordinate_attainment"]
    assert coordinates[0]["attained_bits_in_H20"] == [1]
    assert coordinates[0]["magic_bit"] == 1
    assert all(item["attained_bits_in_H20"] == [0, 1] for item in coordinates[1:])
    assert all(item["universally_forced_unequal"] is False for item in coordinates)


def test_witness_family_covers_every_v_index_and_both_orders_inside_h20() -> None:
    proof = json.loads(PROOF.read_text(encoding="utf-8"))
    family = proof["unsat_preserving_witness_family"]
    observed = {(item["v"], item["r"], item["clause_order"]) for item in family}
    expected = {
        (v, r, order)
        for v in range(4, 8)
        for r in range(1, v + 1)
        for order in ("positive_then_negative", "negative_then_positive")
    }
    assert observed == expected
    assert all(item["word_length"] == 40 for item in family)
    assert all(len(item["h_label"]) == 21 for item in family)
    assert all(item["h_label"][1:8] == item["word"][20:27] for item in family)


def test_k20_proof_is_retrospective_scoped_and_not_v1_repair() -> None:
    proof = json.loads(PROOF.read_text(encoding="utf-8"))
    assert proof["chronology"] == {
        "constructed_after_v1_result_access": True,
        "prospective_v1_validator_credit": False,
        "repairs_v1_authorization_retroactively": False,
        "strict_context_first_discovery_credit": False,
    }
    assert proof["non_guarantees"] == [
        "not a repair or pass for the frozen v1 classifier/falsifier",
        "not an H_20 intersection P_21 witness",
        "not a decoder, SAT-oracle, cover, circuit, or P-versus-NP result",
        "not formal proof, novelty assurance, or independent peer review",
    ]
    assert proof["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"

