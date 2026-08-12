import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BSD = ROOT / "research/real_math/millennium/birch_swinnerton_dyer"
FROZEN_PACKET = BSD / "01_frontier/BSD_A1a1_R12_PRE_CANDIDATE_PACKET_20260812.json"
HISTORICAL_RESULT = BSD / "00_sources/BSD_A1a1_R12_PINFINITY_VP_BINDING_RESULT_20260812.json"
HISTORICAL_TRACE = BSD / "09_trace/BSD_A1a1_R12_PRE_CANDIDATE_TRACE_20260812.json"
CORRECTION = BSD / "00_sources/BSD_A1a1_R12_APPEND_ONLY_MATHEMATICAL_CORRECTION_20260812.json"
REVALIDATION = BSD / "07_memory/BSD_A1a1_R12_LIVE_MAIN_REVALIDATION_20260812.json"
CORRECTION_TRACE = BSD / "09_trace/BSD_A1a1_R12_APPEND_ONLY_CORRECTION_TRACE_20260812.json"


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _artifact_hash(value: dict) -> str:
    payload = dict(value)
    payload.pop("artifact_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def test_r12_historical_scientific_files_are_preserved_byte_for_byte():
    assert _sha256(FROZEN_PACKET) == "923a4d51b287e17cb95d5b529241ce08b67bdcb5810d52dca0f836460ec2bcb4"
    assert _sha256(HISTORICAL_RESULT) == "21612360d0e25ca72e8c627fccdc4de777d5ffafeb570b587639d864415e9823"
    assert _sha256(HISTORICAL_TRACE) == "1f6cd309e51eed47966ea120d091e30902127a72d6c92d30805d034049a02624"


def test_r12_correction_separates_frozen_authority_from_later_corroboration():
    correction = _load(CORRECTION)
    assert "episode_id" not in correction
    assert correction["chronology_boundary"]["historical_files_rewritten"] is False
    assert correction["chronology_boundary"]["repairs_original_chronology"] is False
    assert correction["source_authority_correction"]["sole_frozen_prospective_authority"]["id"] == (
        "DOI:10.4007/annals.2020.191.2.1"
    )
    kim = correction["source_authority_correction"]["post_freeze_corroboration"]
    assert kim["id"] == "arXiv:2109.12344v3"
    assert kim["authority_role"] == "POST_FREEZE_CORROBORATION_ONLY"
    assert kim["may_repair_frozen_fibre_membership"] is False


def test_r12_correction_states_the_exact_coefficient_comparison_proof():
    proof = _load(CORRECTION)["exact_coefficient_comparison"]
    assert proof["map"] == "phi: H^1_f(Q,V_pE) -> Sel_{p^infinity}(E/Q)"
    assert proof["image"] == "Sel_{p^infinity}(E/Q)^div"
    assert proof["kernel"] == "a full Z_p-lattice in H^1_f(Q,V_pE)"
    assert proof["quotient"] == "Sel_{p^infinity}(E/Q) / im(phi) is finite"
    assert proof["conclusion"] == (
        "corank_Zp Sel_{p^infinity}(E/Q) = dim_Qp H^1_f(Q,V_pE)"
    )
    assert proof["sha_finiteness_required"] is False
    assert proof["selmer_structure_scope"] == "USUAL_KUMMER_BLOCH_KATO_ONLY"


def test_r12_correction_preserves_r11_route_and_canonicalizes_glue_aliases():
    correction = _load(CORRECTION)
    r11 = correction["r11_residual_reconciliation"]
    assert r11["residual_id"] == "COMPLEX_RANK2_TO_SHARP_DERIVED_HEEGNER_KOLYVAGIN_OR_KURIHARA_ORDER_OPEN"
    assert r11["status"] == "OPEN_PRESERVED"
    assert r11["relation"] == "POSSIBLE_SUBROUTE_TO_EXACT_VP_DIMENSION_UPPER_BOUND_NOT_CLOSED"

    aliases = correction["full_bsd_residual_aliases"]
    canonical = "MORDELL_WEIL_SHA_REGULATOR_TAMAGAWA_TORSION_PERIOD_COMPLEX_LEADING_TERM_GLUE_OPEN"
    assert aliases["canonical_id"] == canonical
    assert set(aliases["legacy_aliases"]) == {
        "FULL_BSD_LEADING_TERM_GLUE_OPEN",
        "SELMER_TO_MORDELL_WEIL_SHA_REGULATOR_TAMAGAWA_TORSION_COMPLEX_LEADING_TERM_GLUE",
    }
    assert aliases["mathematical_status_changed"] is False


def test_r12_live_revalidation_binds_exact_current_application_and_framework():
    revalidation = _load(REVALIDATION)
    assert "episode_id" not in revalidation
    assert revalidation["application_main"]["commit"] == "451d9506d365f06eb314323523ba123edd3ffb32"
    assert revalidation["application_main"]["tree"] == "ee0c402754b1133a1bb6765946519d0fa530b943"
    assert revalidation["framework_main"]["commit"] == "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
    assert revalidation["framework_main"]["tree"] == "e5b344db2a1e48f7075388b96fa2aa44c086e399"
    assert revalidation["historical_cycle"]["frozen_packet_preserved"] is True
    assert revalidation["historical_cycle"]["current_state_grants_retroactive_discovery_credit"] is False
    assert revalidation["round_scope"]["math_only_ledger_changed"] is False
    assert revalidation["round_scope"]["failure_cause_atlas_changed"] is False


def test_r12_correction_artifacts_are_hash_bound_and_append_to_the_result_trace():
    correction = _load(CORRECTION)
    revalidation = _load(REVALIDATION)
    trace = _load(CORRECTION_TRACE)
    assert correction["artifact_hash"] == _artifact_hash(correction)
    assert revalidation["artifact_hash"] == _artifact_hash(revalidation)
    assert trace["base_last_event_hash"] == "sha256:249649b26096a20fae9f9b478a0409903d57ab09c0b30e5ea206a8ea6a7c85d3"
    previous = trace["base_last_event_hash"]
    for event in trace["entries"]:
        assert event["previous_event_hash"] == previous
        assert event["artifact_hash"] == _artifact_hash(event)
        previous = event["artifact_hash"]
    assert trace["terminal_event_hash"] == previous
    assert trace["entries"][0]["evidence_pointers"] == [
        "00_sources/BSD_A1a1_R12_APPEND_ONLY_MATHEMATICAL_CORRECTION_20260812.json"
    ]
