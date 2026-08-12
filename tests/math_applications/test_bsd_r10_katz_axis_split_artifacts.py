import hashlib
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BASE = REPO_ROOT / "research/real_math/millennium/birch_swinnerton_dyer"
RESIDUALS = [
    "CM_SPECIAL_CELL_COMPLEX_RANK2_TO_ORD_LP_EQ_2_UNSOURCED",
    "CM_SPECIAL_CELL_COMPLEX_RANK2_TO_TRANSVERSE_LOC_NONZERO_UNSOURCED",
    "GENERIC_NON_CM_AND_ARBITRARY_RANK_ARITHMETIC_ENTRY_OPEN",
    "MORDELL_WEIL_SHA_REGULATOR_TAMAGAWA_TORSION_PERIOD_COMPLEX_LEADING_TERM_GLUE_OPEN",
]

def load(rel):
    return json.loads((BASE / rel).read_text())

def test_bsd_r10_scope_and_gate_split_is_only_a_bounded_source_audit():
    src = load("00_sources/BSD_A1a1_R10_KATZ_AXIS_GATE_SPLIT_SOURCE_AUDIT_20260812.json")
    assert src["root_state"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    dim = src["verified_local_decomposition"]["dimension_gate"]
    assert dim["explicitly_invokes_finite_Sha_in_these_displayed_sentences"] is False
    assert dim["explicitly_invokes_ord_Lp_star_eq_1_in_these_displayed_sentences"] is False
    assert dim["hypothesis_removal_authority"].startswith("NONE:")
    loc = src["verified_local_decomposition"]["transverse_localization_gate"]
    assert "finite Sha" in loc["displayed_sufficient_package"]
    assert loc["minimality_or_necessity_authority"].startswith("NONE:")
    assert src["coordinate_axis_audit"]["interpolation_region"].startswith("Theorem 2.1.1")
    assert src["bounded_current_literature_search"]["completeness"].startswith("NOT_CLAIMED")
    assert src["mathematical_credit"].startswith("ZERO:")
    assert src["atlas_warning_preserved"]["id"] == "FM-BSD-ARITHMETIC-PREMISE-REIMPORT"
    assert src["residual_after"] == RESIDUALS

def test_bsd_r10_shadow_episode_is_valid_under_pinned_rakl_and_zero_credit():
    from rakl.experience_substrate import EpisodeOutcome, EpisodeStorageAdmission, TaskEpisode, validate_episode
    raw = load("07_memory/BSD_A1a1_R10_KATZ_AXIS_TASK_EPISODE_SHADOW_20260812.taskepisode")
    ep = TaskEpisode(
        episode_id=raw["episode_id"], task_id=raw["task_id"], atom_id=raw["atom_id"],
        context_hash=raw["context_hash"], problem_signature=tuple(raw["problem_signature"]),
        fibre_snapshot_hash=raw["fibre_snapshot_hash"], operator_ids=tuple(raw["operator_ids"]),
        action_trace=tuple(raw["action_trace"]), observation_ids=tuple(raw["observation_ids"]),
        verification_ids=tuple(raw["verification_ids"]), outcome=EpisodeOutcome(raw["outcome"]),
        residual_signature=tuple(raw["residual_signature"]), evidence_pointers=tuple(raw["evidence_pointers"]),
        artifact_hash=raw["artifact_hash"], timestamp=raw["timestamp"], cost=raw["cost"],
        storage_admission=EpisodeStorageAdmission(raw["storage_admission"]),
    )
    assert validate_episode(ep) == ()
    assert raw["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert raw["novelty_class"]["solved_scoped_subproblem"] is False
    assert raw["residual_signature"] == RESIDUALS
    assert "do not award prospective-freeze" in raw["chronology_boundary"]

def test_bsd_r10_lineage_metrics_and_query_count_are_consistent():
    ep = load("07_memory/BSD_A1a1_R10_KATZ_AXIS_TASK_EPISODE_SHADOW_20260812.taskepisode")
    dg = load("07_memory/BSD_A1a1_R10_KATZ_AXIS_DIAGNOSIS_SHADOW_20260812.json")
    fl = load("07_memory/BSD_A1a1_R10_KATZ_INTERPOLATION_FAILURE_SHADOW_20260812.json")
    ls = load("07_memory/BSD_A1a1_R10_GATE_SPLIT_LESSON_CANDIDATE_20260812.json")
    met = load("07_memory/BSD_A1a1_RAKL_CYCLE_METRICS_20260812_R10.json")
    src = load("00_sources/BSD_A1a1_R10_KATZ_AXIS_GATE_SPLIT_SOURCE_AUDIT_20260812.json")
    assert dg["episode_lineage"] == ep["episode_id"]
    assert fl["diagnosis_lineage"] == dg["diagnosis_id"]
    assert ls["authority"].startswith("CANDIDATE_PROPOSAL_ONLY")
    assert fl["failure_id"] not in ep["episode_id"]
    assert fl["exact_failed_implication"].startswith("ord_{s=1} L(E,s)=2")
    assert len(fl["competing_mathematical_causes"]) == 4
    assert fl["selected_bounded_diagnosis"].startswith("SOURCE_DOES_NOT_LICENSE")
    assert "same-E/Q theorem" in fl["repair_obligation"]
    assert ls["lesson_kind"].startswith("MATHEMATICAL_RESEARCH")
    assert ls["mathematical_credit"].startswith("ZERO_UNTIL")
    for key in ("attempted_mathematical_implication", "exact_mathematical_result", "strongest_supported_mathematical_cause", "competing_mathematical_causes", "justified_scope", "mathematical_falsifier", "resulting_mathematical_repair", "supporting_mathematics"):
        assert ls[key]
    assert met["residual_after"] == ep["residual_signature"] == RESIDUALS
    assert met["resource_proxies"]["primary_literature_search_queries_observed"] == len(src["bounded_current_literature_search"]["queries"]) == 3
    assert all(value == 0 for value in met["retained_semantic_novelty"].values())
    assert met["outcome"]["genuine_lemma_or_transfer_condition_generated"] is False
    assert met["atlas_warning_preserved"] == "FM-BSD-ARITHMETIC-PREMISE-REIMPORT"

def test_bsd_r10_context_and_trace_hashes_and_no_root_promotion():
    ctx = load("01_frontier/BSD_A1a1_R10_KATZ_AXIS_CONTEXT_FIBRE_20260812.json")
    claimed = ctx.pop("fibre_snapshot_hash")
    calculated = "sha256:" + hashlib.sha256(json.dumps(ctx, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    assert claimed == calculated
    tr = load("09_trace/BSD_A1a1_R10_KATZ_AXIS_TRACE_DELTA_20260812.json")
    prev = tr["base_last_event_hash"]
    for event in tr["entries"]:
        assert event["previous_event_hash"] == prev
        core = dict(event)
        got = core.pop("artifact_hash")
        calc = "sha256:" + hashlib.sha256(json.dumps(core, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
        assert got == calc
        assert event["residuals"] == RESIDUALS
        prev = got
    assert tr["terminal_event_hash"] == prev
    assert all("ROOT_CERTIFICATE" not in " ".join(event["outputs"]) for event in tr["entries"])
    assert "not evidence of prospective" in tr["chronology_boundary"]
