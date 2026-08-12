import hashlib
import json
from pathlib import Path

from rakl.authority_ledger import AuthorityAxis
from rakl.epistemic_sufficiency import (
    AcquisitionKind,
    EpistemicAction,
    EpistemicDecisionCase,
    EpistemicDecisionVerdict,
    EvidenceAcquisitionAction,
    EvidenceObligation,
    ObligationKind,
    recommend_epistemic_action,
)
from rakl.experience_substrate import (
    EpisodeOutcome,
    EpisodeStorageAdmission,
    InventoryAdmissionVerdict,
    TaskEpisode,
    resolve_inventory_admission,
    validate_episode,
)

ROOT = Path(__file__).resolve().parents[2]
CROSS = ROOT / "research/real_math/millennium/cross_problem"
FIBRE = CROSS / "01_frontier/XM023_HODGE_YM_LINEARIZATION_CONSUMER_CONTEXT_FIBRE_20260812.json"
CANDIDATE = CROSS / "04_candidates/XM023_HODGE_YM_LINEARIZATION_CONSUMER_TYPE_SPLIT_20260812.json"
EPISODE = CROSS / "07_memory/XM023_CURRENT_V3_TASK_EPISODE_SHADOW_20260812.taskepisode"


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def test_xm023_fibre_and_candidate_hashes_are_content_bound() -> None:
    fibre = json.loads(FIBRE.read_text())
    expected_fibre = fibre.pop("fibre_snapshot_hash")
    assert "sha256:" + hashlib.sha256(_canonical(fibre)).hexdigest() == expected_fibre

    candidate = json.loads(CANDIDATE.read_text())
    expected_candidate = candidate.pop("artifact_hash")
    assert "sha256:" + hashlib.sha256(_canonical(candidate)).hexdigest() == expected_candidate


def test_xm023_task_episode_is_valid_shadow_and_fails_closed_as_canonical() -> None:
    raw = json.loads(EPISODE.read_text())
    episode = TaskEpisode(
        episode_id=raw["episode_id"],
        task_id=raw["task_id"],
        atom_id=raw["atom_id"],
        context_hash=raw["context_hash"],
        problem_signature=tuple(raw["problem_signature"]),
        fibre_snapshot_hash=raw["fibre_snapshot_hash"],
        operator_ids=tuple(raw["operator_ids"]),
        action_trace=tuple(raw["action_trace"]),
        observation_ids=tuple(raw["observation_ids"]),
        verification_ids=tuple(raw["verification_ids"]),
        outcome=EpisodeOutcome(raw["outcome"]),
        residual_signature=tuple(raw["residual_signature"]),
        evidence_pointers=tuple(raw["evidence_pointers"]),
        artifact_hash=raw["artifact_hash"],
        timestamp=raw["timestamp"],
        cost=raw["cost"],
        storage_admission=EpisodeStorageAdmission(raw["storage_admission"]),
    )
    assert validate_episode(episode) == ()
    report = resolve_inventory_admission(episode, treat_as_canonical=True)
    assert report.verdict is InventoryAdmissionVerdict.SHADOW_REFERENCED_AS_CANONICAL
    assert report.retained_for_search is True
    assert report.counts_toward_canonical_inventory is False


def test_current_v3_sequential_evidence_contract_runs_discriminator_then_refutes_overtransfer() -> None:
    obligation = EvidenceObligation(
        "DISC-XM023-SAME-MAP-SAME-NORM-DERIVATIVE-LIPSCHITZ",
        ObligationKind.DISCRIMINATOR,
        blocking=True,
        satisfied=False,
    )
    acquisition = EvidenceAcquisitionAction(
        "ACT-XM023-RUN-DERIVATIVE-LIPSCHITZ-DISCRIMINATOR",
        AcquisitionKind.RUN_DISCRIMINATOR,
        (obligation.obligation_id,),
        cost=1.0,
    )
    pre = EpistemicDecisionCase(
        case_id="XM023-PRE",
        claim_id="HODGE-RAMIFICATION-EXCUSES-YM-CONTRACTION-COLLISION",
        requested_axis=AuthorityAxis.REPRESENTATION,
        known_answer_validated=True,
        frozen_before_action=True,
        support_sufficient=False,
        refutation_sufficient=False,
        conflict_present=True,
        scope_overbroad=False,
        narrower_scope_available=False,
        obligations=(obligation,),
        acquisition_actions=(acquisition,),
        max_acquisition_cost=1.0,
        terminal_abstention_licensed=False,
    )
    first = recommend_epistemic_action(pre)
    assert first.verdict is EpistemicDecisionVerdict.CORRECT_NEXT_ACTION
    assert first.recommended_action is EpistemicAction.RUN_DISCRIMINATOR
    assert first.grants_scientific_authority is False

    post = EpistemicDecisionCase(
        case_id="XM023-POST",
        claim_id=pre.claim_id,
        requested_axis=AuthorityAxis.REPRESENTATION,
        known_answer_validated=True,
        frozen_before_action=True,
        support_sufficient=False,
        refutation_sufficient=True,
        conflict_present=False,
        scope_overbroad=False,
        narrower_scope_available=False,
        obligations=(),
        acquisition_actions=(),
        max_acquisition_cost=0.0,
        terminal_abstention_licensed=False,
    )
    final = recommend_epistemic_action(post)
    assert final.verdict is EpistemicDecisionVerdict.CORRECT_NEXT_ACTION
    assert final.recommended_action is EpistemicAction.COMMIT_REFUTED
    assert final.grants_scientific_authority is False


def test_xm023_scoped_difference_witness_preserves_target_residuals() -> None:
    candidate = json.loads(CANDIDATE.read_text())
    witness = candidate["transfer"]["DifferenceWitness"]
    assert witness["verdict"] == "METHOD_ANALOGY_RETAINED__TARGET_AUTHORITY_OVERTRANSFER_BLOCKED"
    assert "Lip(F)>=||DF(x)||" in witness["world_B_metric_consumer"]["observation"]
    assert candidate["outcome"] == "PARTIAL_SUCCESS_STRUCTURAL_FAMILY_SPLIT_OVERTRANSFER_BLOCKED"
    assert "regulator/OS glue" in candidate["residual_after"]
