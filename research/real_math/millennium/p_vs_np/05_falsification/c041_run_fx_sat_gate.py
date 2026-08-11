"""Run the post-freeze exact finite gate for C041-FX-SAT-ONE-SIDED-v1."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PNP = HERE.parent
CANDIDATE_PATH = PNP / "04_candidates/C041_fx_sat_one_sided.py"
GATE_PATH = HERE / "c041_exact_extension_gate.py"
FREEZE_PATH = PNP / "09_trace/O9d12a2a1b_C041_FX_SAT_CANDIDATE_FREEZE_20260812.json"
FREEZE_COMMIT = "4627ae32e2d3660a86cc12d327592577adc25e5f"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load frozen module {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


candidate = _load("c041_fx_sat_one_sided_frozen", CANDIDATE_PATH)
gate = _load("c041_exact_extension_gate_frozen", GATE_PATH)
oracle = gate.oracle


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _q(value: Fraction | int) -> dict[str, int]:
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload["artifact_hash"] = ""
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _seed_exact_recheck(parent: set[tuple[int, int]]) -> dict[str, object]:
    original_filters = oracle._relevant_semifilters(3, parent)
    square_filters = oracle._relevant_semifilters(4, parent)
    if original_filters != square_filters:
        raise ArithmeticError("empty-fibre ambient enlargement changed relevance")

    primal = {
        (3, 12): Fraction(1, 2),
        (5, 10): Fraction(1, 2),
        (9, 14): Fraction(1, 2),
    }
    dual = {
        (1, 4): Fraction(1, 2),
        (1, 6, 10): Fraction(1, 2),
        (2, 4): Fraction(1, 2),
    }
    pairs = gate._full_union_pairs(len(parent))
    primal_loads = [
        sum(
            (weight for pair, weight in primal.items() if oracle.pair_covers_semifilter(filt, *pair)),
            Fraction(),
        )
        for filt in square_filters
    ]
    dual_loads = [gate._pair_load(pair, dual.items()) for pair in pairs]
    primal_total = sum(primal.values(), Fraction())
    dual_total = sum(dual.values(), Fraction())
    if min(primal_loads) < 1 or max(dual_loads) > 1 or primal_total != dual_total:
        raise ArithmeticError("seed primal-dual equality recheck failed")
    return {
        "original_ambient_side": 3,
        "square_seed_ambient_side": 4,
        "original_relevant_semifilter_count": len(original_filters),
        "square_seed_relevant_semifilter_count": len(square_filters),
        "relevant_semifilter_families_equal": True,
        "minimum_primal_coverage": _q(min(primal_loads)),
        "maximum_dual_pair_load": _q(max(dual_loads)),
        "primal_total": _q(primal_total),
        "dual_total": _q(dual_total),
        "exact_optimum": _q(primal_total),
        "mathematical_claim": "Empty-fibre square embedding preserves this seed's relevant semi-filter family and exact fractional optimum 3/2.",
    }


def build_receipt() -> dict[str, object]:
    freeze = json.loads(FREEZE_PATH.read_text(encoding="utf-8"))
    if freeze["candidate_code"]["sha256"] != _sha256(CANDIDATE_PATH):
        raise RuntimeError("candidate code differs from the frozen identity")
    if freeze["evaluator"]["sha256"] != _sha256(GATE_PATH):
        raise RuntimeError("evaluator differs from the frozen identity")
    if freeze["chronology"]["native_output_accessed"] is not False:
        raise RuntimeError("freeze chronology does not precede native output")

    parent = set(candidate.SEED_COMPLEMENT)
    child = candidate.materialize_complement(3)
    parent_dual = {
        (1, 4): Fraction(1, 2),
        (1, 6, 10): Fraction(1, 2),
        (2, 4): Fraction(1, 2),
    }
    finite_gate = gate.evaluate_extension_gate(
        parent_side=4,
        child_side=8,
        parent_complement=parent,
        child_complement=child,
        parent_dual=parent_dual,
    )
    receipt: dict[str, object] = {
        "schema_version": "1.0.0",
        "receipt_id": "PNP-C041-FX-SAT-ONE-SIDED-EXACT-GATE-20260812",
        "candidate_id": freeze["candidate_id"],
        "freeze_id": freeze["freeze_id"],
        "freeze_artifact_hash": freeze["artifact_hash"],
        "freeze_commit": FREEZE_COMMIT,
        "candidate_sha256": _sha256(CANDIDATE_PATH),
        "evaluator_sha256": _sha256(GATE_PATH),
        "evaluated_transition": "n=2 to n=3",
        "parent_side": 4,
        "child_side": 8,
        "parent_complement": [list(edge) for edge in sorted(parent)],
        "child_complement": [list(edge) for edge in sorted(child)],
        "added_complement": [list(edge) for edge in sorted(child - parent)],
        "seed_exact_recheck": _seed_exact_recheck(parent),
        "finite_gate": finite_gate,
        "scope": {
            "short_decoder_branch_only": True,
            "magic_coded_sat_slice_evaluated": False,
            "grants_uniform_recurrence": False,
            "grants_asymptotic_authority": False,
            "grants_novelty_authority": False,
            "grants_p_vs_np_authority": False,
        },
        "mathematical_saturation_policy": {
            "credit": "exact seed equality, exact finite relevance/load/augmentation result, and any supported mathematical counterexample",
            "zero_credit": "Git, CI, hashes, schemas, implementation, solver status and runtime",
        },
        "artifact_hash": "",
    }
    receipt["artifact_hash"] = _canonical_hash(receipt)
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(build_receipt(), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
