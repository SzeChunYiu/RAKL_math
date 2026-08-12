from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PNP = ROOT / "research/real_math/millennium/p_vs_np"
FIXTURE = PNP / "09_trace/c047_orientation_repair_candidate_fixture.py"
VERIFIER = PNP / "09_trace/verify_c047_candidate_freeze_packet.py"
EVALUATOR = PNP / "05_falsification/c047_orientation_feasibility_evaluator.py"
ARTIFACTS = {
    "candidate": PNP / "04_candidates/O9d12a2a1b_C047_ORIENTATION_ONLY_SEPARATION_LEMMA_FREEZE_20260812.json",
    "evaluator_manifest": PNP / "05_falsification/O9d12a2a1b_C047_ORIENTATION_FEASIBILITY_EVALUATOR_FREEZE_20260812.json",
    "authorization": PNP / "09_trace/O9d12a2a1b_C047_EVALUATION_AUTHORIZATION_20260812.json",
    "trace": PNP / "09_trace/O9d12a2a1b_C047_CANDIDATE_FREEZE_TRACE_20260812.json",
    "feedback": PNP / "10_feedback/C047_COARSE_REPAIR_INTERFACE_CONGRUENCE_APPLICATION_FEEDBACK_PROPOSAL_20260812.json",
    "receipt": PNP / "09_trace/O9d12a2a1b_C047_CANDIDATE_FREEZE_RECEIPT_20260812.json",
}


def _module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_c047_candidate_documents_match_public_pre_candidate_parent() -> None:
    fixture = _module("pnp_c047_candidate", FIXTURE)
    expected = fixture.build_documents()
    assert fixture.PRE_CANDIDATE_FREEZE_SHA == "d84e3814f1d8f355246f2bddb6982c3a1859fb6c"
    assert set(expected) == set(ARTIFACTS)
    for name, path in ARTIFACTS.items():
        assert _load(path) == expected[name]


def test_c047_candidate_exactly_scopes_orientation_only_family() -> None:
    candidate = _load(ARTIFACTS["candidate"])
    assert candidate["candidate_id"] == "C047-ORIENTATION-ONLY-SEPARATION-LEMMA-v1"
    assert candidate["family_definition"]["variants"] == ["MIRROR_ONLY", "TWO_SIDED_OLD_NEW_PLUS_PREFIX_MIRROR"]
    assert "literal matrix transpose with suffix c on the fresh row" in candidate["family_definition"]["excluded_variants"]
    assert candidate["statement"]["quantifier"] == "for every integer n >= 18 and each frozen orientation-only variant"
    assert candidate["predicted_discriminator"] == {
        "low_inherited_case": "first bit 0 versus first MAGIC bit 1",
        "all_zero_case": "first two bits 10 versus first two MAGIC bits 11",
        "canonical_mirror_case": "1||MAGIC begins 1111 while MAGIC begins 1110",
    }
    assert candidate["target_access"] == {
        "decoder_imported_or_executed": False,
        "evaluator_imported_or_executed": False,
        "later_target_enumerated": False,
        "later_target_result_accessed": False,
        "finite_collision_level_selected": False,
    }
    assert candidate["credit_boundary"]["candidate_freeze_mathematical_result_credit"] is False


def test_c047_evaluator_is_inert_and_no_execution_is_authorized() -> None:
    manifest = _load(ARTIFACTS["evaluator_manifest"])
    authorization = _load(ARTIFACTS["authorization"])
    assert manifest["status"] == "FROZEN_INERT_NOT_IMPORTED_NOT_EXECUTED"
    assert manifest["evaluator"]["raw_sha256"] == hashlib.sha256(EVALUATOR.read_bytes()).hexdigest()
    assert authorization["current_task_evaluator_execution_authorized"] is False
    assert authorization["later_target_access_authorized"] is False
    source = EVALUATOR.read_text(encoding="utf-8")
    for forbidden in ("C041_fx_sat_one_sided", "decode_formula", "is_satisfiable", "materialize_complement", "subprocess"):
        assert forbidden not in source


def test_c047_trace_appends_candidate_without_result_event() -> None:
    trace = _load(ARTIFACTS["trace"])
    assert len(trace["entries"]) == 9
    assert trace["entries"][-1]["event_type"] == "CANDIDATE_PROPOSED"
    assert trace["entries"][-1]["previous_event_hash"] == trace["entries"][-2]["artifact_hash"]
    text = json.dumps(trace, sort_keys=True)
    assert "FALSIFIER_RUN" not in text
    assert "RESULT_RECORDED" not in text


def test_c047_feedback_is_proposal_only() -> None:
    feedback = _load(ARTIFACTS["feedback"])
    assert feedback["status"] == "APPLICATION_FEEDBACK_PROPOSAL_ONLY_NOT_PROMOTED"
    assert feedback["authority"]["framework_evolution_authority"] is False
    assert feedback["authority"]["fresh_self_rakl_assurance_required"] is True
    assert feedback["credit"]["feedback_transport_mathematical_saturation_credit"] is False


def test_c047_candidate_verifier_rejects_mutation(tmp_path: Path) -> None:
    verifier = _module("pnp_c047_candidate_verify", VERIFIER)
    assert verifier.audit_packet(ROOT) == ()
    for path in [*ARTIFACTS.values(), EVALUATOR]:
        target = tmp_path / path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())
    candidate_path = tmp_path / ARTIFACTS["candidate"].relative_to(ROOT)
    candidate = _load(candidate_path)
    candidate["statement"]["quantifier"] = "HOSTILE_WEAKENING"
    candidate_path.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert any("candidate: digest mismatch" in error for error in verifier.audit_packet(tmp_path))
