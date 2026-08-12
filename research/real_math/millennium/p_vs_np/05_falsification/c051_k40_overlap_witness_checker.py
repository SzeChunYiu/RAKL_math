from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve()
PNP = HERE.parents[1]
SOURCE = PNP / "04_candidates/C041_fx_sat_one_sided.py"
CERT = PNP / "04_candidates/O9d12a2a1b_C051_K40_EXACT_OVERLAP_WITNESS_20260812.json"


def _source_module():
    spec = importlib.util.spec_from_file_location("pnp_c041_c051_check", SOURCE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _parent_formula(m):
    L = lambda variable, negated=False: (variable, negated)
    clauses = (
        (L(1), L(1), L(1)),
        (L(1, True), L(1, True), L(1, True)),
        (L(1), L(1), L(2, True)),
        (L(2), L(2, True), L(1)),
        (L(3), L(2), L(1, True)),
        (L(2), L(1, True), L(2)),
        (L(1, True), L(2), L(1, True)),
    )
    return m.Formula3CNF(3, clauses, "C051_EXACT_WITNESS")


def _current_formula(m):
    clause = ((1, False), (1, False), (1, False))
    return m.Formula3CNF(1, (clause,) * 11, "C051_EXACT_WITNESS")


def evaluate() -> dict:
    m = _source_module()
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    parent = _parent_formula(m)
    current = _current_formula(m)
    pw = m.encode_formula(parent)
    cw = m.encode_formula(current)
    h = "1" + pw[40:]
    p = cw[:41]
    assert pw == cert["exact_witness"]["parent"]["word"]
    assert cw == cert["exact_witness"]["current"]["word"]
    assert len(pw) == 80 and len(cw) == 82
    assert not m.is_satisfiable(parent)
    assert m.decode_formula(pw).decoder_branch == "CANONICAL_MAGIC_LONG_FORM"
    assert m.decode_formula(cw).decoder_branch == "CANONICAL_MAGIC_LONG_FORM"
    assert h == p == cert["exact_witness"]["parent"]["transpose_label_1_suffix"]
    return {
        "status": "PASS_RECORD_CHECK_ONLY",
        "proof_authority": 0,
        "k": 40,
        "parent_encoded_length": len(pw),
        "current_encoded_length": len(cw),
        "parent_unsat": True,
        "exact_interface_equality": True,
        "shared_label": h,
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    }


if __name__ == "__main__":
    print(json.dumps(evaluate(), indent=2, sort_keys=True))
