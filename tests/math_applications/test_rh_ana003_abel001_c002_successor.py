from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003_abel001_c002_successor_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("rh_abel_c002", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_append_only_history_is_byte_bound_and_c001_quarantined() -> None:
    module = _module()
    docs = module.build_documents()
    invalidation = docs["invalidation"]
    assert module.raw_hash(module.OLD_CANDIDATE) == module.OLD_CANDIDATE_RAW_SHA256
    assert module.raw_hash(module.OLD_BINDING) == module.OLD_BINDING_RAW_SHA256
    assert module.raw_hash(module.OLD_TRACE) == module.OLD_TRACE_RAW_SHA256
    assert invalidation["candidate_status"] == (
        "QUARANTINED_STRICT_RAKL_IDENTITY_AND_MALFORMED_O2_PROPOSAL"
    )
    decision = invalidation["fail_closed_decision"]
    assert decision["original_files_rewritten"] is False
    assert decision["original_candidate_identity_quarantined"] is True
    assert decision["retroactive_chronology_repair_claimed"] is False
    assert decision["may_describe_c001_as_strict_rakl_candidate"] is False
    assert decision["may_use_c001_for_evaluation"] is False
    assert decision["new_successor_identity_required"] is True


def test_c002_documents_match_fixture_and_have_new_identity() -> None:
    module = _module()
    expected = module.build_documents()
    assert set(expected) == set(module.PATHS)
    for name, relative in module.PATHS.items():
        assert _load(ROOT / relative) == expected[name]
    candidate = expected["candidate"]
    assert candidate["candidate_id"] == module.NEW_CANDIDATE_ID
    assert candidate["candidate_identity"]["canonical_core_sha256"] != module.OLD_CANDIDATE_CORE_SHA256
    assert candidate["successor_lineage"]["predecessor_quarantined"] is True
    assert candidate["successor_lineage"]["predecessor_chronology_repaired_retroactively"] is False
    assert candidate["successor_lineage"]["result_access_before_successor_freeze"] is False


def test_o2_has_explicit_log_power_everywhere_in_successor() -> None:
    module = _module()
    docs = module.build_documents()
    correct = "C_n(1+(log t)^(n-1))/t^2"
    malformed = "C_n(1+log t^(n-1))/t^2"
    for name in ("candidate", "proof_inputs"):
        text = json.dumps(docs[name], sort_keys=True)
        assert correct in text
        assert malformed not in text
    assert correct in FIXTURE.read_text(encoding="utf-8")
    old = _load(ROOT / module.OLD_CANDIDATE)
    assert malformed in json.dumps(old, sort_keys=True)


def test_correct_binding_uses_context_packet_not_gate_file_digest() -> None:
    module = _module()
    docs = module.build_documents()
    binding = docs["framework_binding"]
    receipt = docs["receipt"]
    assert binding["pre_candidate_packet_hash"] == module.CONTEXT_PACKET_HASH
    assert binding["pre_candidate_packet_hash"] != module.PRE_GATE_RAW_SHA256
    assert binding["predecessor_binding_value"] == module.PRE_GATE_RAW_SHA256
    assert binding["predecessor_chronology_repaired_retroactively"] is False
    assert binding["applies_only_to_candidate_id"] == module.NEW_CANDIDATE_ID
    assert receipt["corrected_binding"]["context_packet_hash"] == module.CONTEXT_PACKET_HASH
    assert receipt["predecessor"]["strict_chronology_repaired_retroactively"] is False


def test_c002_is_inert_and_has_zero_result_credit() -> None:
    module = _module()
    docs = module.build_documents()
    assert docs["authorization"]["current_round_evaluator_execution_authorized"] is False
    assert docs["authorization"]["proof_derivation_authorized"] is False
    assert docs["authorization"]["result_classification_authorized"] is False
    assert docs["manifest"]["status"] == "FROZEN_INERT_NOT_IMPORTED_NOT_EXECUTED"
    assert docs["receipt"]["chronology"]["candidate_result_accessed"] is False
    assert docs["receipt"]["authority"]["target_theorem_truth"] is False
    assert docs["receipt"]["authority"]["mathematical_result_credit"] is False
    assert docs["receipt"]["authority"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"


def test_math_lesson_has_required_seven_fields() -> None:
    module = _module()
    lesson = module.build_documents()["lesson"]
    assert {
        "attempted_implication",
        "exact_result_or_failure",
        "supported_and_competing_causes",
        "scope",
        "mathematical_falsifier",
        "mathematical_repair",
        "proof_source_evidence",
    } <= set(lesson)
    seven_field_text = json.dumps(
        {key: lesson[key] for key in (
            "attempted_implication",
            "exact_result_or_failure",
            "supported_and_competing_causes",
            "scope",
            "mathematical_falsifier",
            "mathematical_repair",
            "proof_source_evidence",
        )},
        sort_keys=True,
    ).lower()
    assert "leading coefficient" in seven_field_text
    assert "fixed n" in seven_field_text
    assert all(
        phrase not in seven_field_text
        for phrase in ("git history", "ci/tests", "schemas/hashes", "strict-discovery chronology")
    )
    assert "zero mathematical lesson credit" in lesson["nonmathematical_governance_note"]
    assert lesson["mathematical_result_credit"] is False
    assert lesson["mathematical_saturation_credit"] is False
