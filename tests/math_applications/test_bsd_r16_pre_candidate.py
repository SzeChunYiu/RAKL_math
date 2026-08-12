from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "research/real_math/millennium/birch_swinnerton_dyer/09_trace/bsd_r16_cassels_tate_pre_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("bsd_r16_pre", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_bsd_r16_documents_are_exact_result_blind_freeze() -> None:
    module = _module()
    expected = module.build_documents()
    for key, relative in module.PATHS.items():
        assert json.loads((ROOT / relative).read_text()) == expected[key]
    gate = expected["gate"]
    assert gate["target_access"] == {
        "cassels_tate_primary_source_accessed": False,
        "result_observed": False,
        "result_classified": False,
    }
    assert gate["authority"]["candidate_generation_allowed"] is False
    assert gate["future_result_lesson_contract"]["current_status"] == "NO_RESULT_NO_LESSON"
    assert len(gate["future_result_lesson_contract"]["required_seven_fields"]) == 7
    assert gate["gate_reports"] == {"context": "PASS", "memory": "PASS", "shortcut": "CANNOT_CHECK", "trace_integrity": "PASS"}


def test_bsd_r16_discriminator_preserves_exact_radical_quotient_distinction() -> None:
    docs = _module().build_documents()
    gate = docs["gate"]
    serialized = json.dumps(docs, sort_keys=True)
    assert "maximal divisible subgroup" in serialized
    assert "Sha/D" in serialized
    assert "p=2" in serialized
    assert gate["allowed_result_branches"] == [
        "FORCES_ZERO_DIVISIBLE_CORANK",
        "PARITY_ONLY_ON_DIVISIBLE_CORANK",
        "PAIRING_DESCENDS_ONLY_TO_QUOTIENT_NO_DIVISIBLE_CORANK_CONTROL",
        "CANNOT_CHECK_EXACT_SOURCE_SCOPE",
    ]
    assert "fails if" in gate["predeclared_falsifier"]
    for forbidden in ("RESULT_PROVED", "D=0 is proved", "independent peer review"):
        assert forbidden not in serialized
