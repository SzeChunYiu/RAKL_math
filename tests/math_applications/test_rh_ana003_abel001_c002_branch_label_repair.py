from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003_abel001_c002_branch_label_repair_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("rh_abel_c002_label_repair", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_append_only_branch_label_correction_is_deterministic() -> None:
    module = _module()
    docs = module.build_documents()
    for name, relative in module.PATHS.items():
        assert json.loads((ROOT / relative).read_text(encoding="utf-8")) == docs[name]
    correction = docs["correction"]
    assert correction["corrected_classification"] == module.FROZEN_LABEL
    assert correction["append_only_decision"]["historical_files_rewritten"] is False
    assert correction["append_only_decision"]["invalid_label_quarantined"] is True
    assert correction["append_only_decision"]["mathematical_proof_quarantined"] is False


def test_repair_has_zero_math_credit_and_preserves_source_bytes() -> None:
    module = _module()
    docs = module.build_documents()
    assert module.raw_hash(module.RESULT) == module.RESULT_RAW
    assert module.raw_hash(module.MANIFEST) == module.MANIFEST_RAW
    assert docs["correction"]["credit"]["mathematical"] == 0
    assert docs["correction"]["credit"]["saturation"] == 0
    assert docs["correction"]["global_ledger_updated"] is False
    assert docs["receipt"]["mathematical_proof_or_lesson_modified"] is False


def test_original_contract_contains_only_correct_success_branch() -> None:
    module = _module()
    candidate = json.loads(module.CANDIDATE.read_text(encoding="utf-8"))
    proof_input = json.loads(module.PROOF_INPUT.read_text(encoding="utf-8"))
    assert candidate["allowed_result_branches"] == proof_input["allowed_result_branches"]
    assert module.FROZEN_LABEL in candidate["allowed_result_branches"]
    assert module.INVALID_LABEL not in candidate["allowed_result_branches"]
