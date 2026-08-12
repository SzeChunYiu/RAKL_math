from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003_abel001_c002_result_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("rh_abel_c002_result", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_result_documents_are_deterministic_and_chronology_bound() -> None:
    module = _module()
    docs = module.build_documents()
    for name, relative in module.PATHS.items():
        assert json.loads((ROOT / relative).read_text(encoding="utf-8")) == docs[name]
    result = docs["result"]
    assert result["chronology"]["proof_input_commit"] == module.PROOF_INPUT_COMMIT
    assert result["chronology"]["proof_inputs_frozen_before_execution"] is True
    assert result["status"] == "PASS_SAME_CONTEXT_HAND_PROOF_RECORD_CHECK"


def test_exact_result_is_mathematical_and_strictly_scoped() -> None:
    result = _module().build_documents()["result"]
    exact = json.dumps(result["exact_mathematical_result"], sort_keys=True)
    for required in ("nonintegral", "b_n'(t)", "Bellotti", "natural_order_identity", "m=6k", "n=1"):
        assert required in exact
    assert result["authority"] == {
        "same_context_hand_derivation": True,
        "formal": False,
        "independent": False,
        "novelty": False,
        "riemann_hypothesis": False,
        "root": "OPEN_NO_SOLUTION_CERTIFICATE",
    }
    assert result["global_ledger_updated"] is False


def test_seven_field_lesson_excludes_operational_math_credit() -> None:
    lesson = _module().build_documents()["lesson"]
    seven = lesson["seven_field_math_lesson"]
    assert set(seven) == {
        "attempted_implication", "exact_result_or_failure", "supported_and_competing_causes",
        "scope", "falsifier", "mathematical_repair", "proof_and_source_evidence",
    }
    assert "zero mathematical credit" in seven["proof_and_source_evidence"]
    assert lesson["deduplication"]["assurance_metadata_mathematical_credit"] == 0
    assert lesson["deduplication"]["global_ledger_updated"] is False


def test_result_trace_extends_frozen_parent_chain() -> None:
    trace = _module().build_documents()["trace"]
    previous = "sha256:dd91e3ac103cd8edbdffb1a058326bf422a53262525087d5d9ababaccf2ac70a"
    assert [row["event_type"] for row in trace["entries"]] == ["FALSIFIER_RUN", "RESULT_RECORDED", "RESIDUAL_OPENED", "REVIEWED"]
    for row in trace["entries"]:
        assert row["previous_event_hash"] == previous
        previous = row["artifact_hash"]


def test_result_round_revalidates_latest_framework_without_authority_inflation() -> None:
    module = _module()
    revalidation = module.build_documents()["framework_result_revalidation"]
    assert revalidation["framework_main_at_result_recording"] == module.FRAMEWORK_RESULT_LIVE
    assert revalidation["protected_math_surface_hashes_unchanged_from_proof_freeze"] is True
    assert revalidation["verdict"] == "CURRENT_NONBLOCKING_NO_NEW_APPLICABLE_CANONICAL_MATH_GATE"
    assert revalidation["grants_mathematical_or_scientific_authority"] is False
