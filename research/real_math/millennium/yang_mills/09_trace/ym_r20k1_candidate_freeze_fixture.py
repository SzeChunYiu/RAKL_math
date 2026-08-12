"""Post-merge durability acknowledgement and result-blind scalar freeze.

The public pre-candidate packet from PR #379 is acknowledged by exact receipt
hash and public Git blob.  Only after that acknowledgement does this fixture
materialize one symbolic scalar candidate and an inert falsifier identity.
Nothing here evaluates source constants, derives a threshold, runs the
falsifier, or classifies a mathematical result.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from rakl.framework_candidate_freeze import (
    CandidateFreezeRevalidationVerdict,
    FrameworkSubjectFreezeBinding,
    FrameworkSubjectRevalidationObservation,
    audit_candidate_freeze_framework_subject,
)
from rakl.pre_action_receipt import (
    PreActionFibreReceipt,
    RejectedRetrieval,
    RetrievalAuthority,
    SelectedRetrieval,
)
from rakl.pre_scratch_fibre_freeze import (
    DurablePersistenceAcknowledgement,
    HookMaterializationStatus,
    run_pre_scratch_fibre_freeze_hook,
)


ATOM = "YM-S1a2i-K1"
CANDIDATE_ID = "YM-S1a2i-K1-C001-SYMBOLIC-NEXT-RADIUS-MARGIN"
APPLICATION_PARENT_SHA = "08c1a790f94c708ed5a463c7a8d6b036fd5828ff"
PUBLIC_RECEIPT_COMMIT = "a5a5bccdb9b308d90ff04a4ab7bdc506e2a18331"
PRE_FRAMEWORK_SHA = "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
STRUCTURAL_TRANSPORT_ANCESTRY_SHA = "496edc5ead136980287ac2e72efb486691945366"
PRE_LATEST_NON_METHOD_SUCCESSOR_SHA = "e3ffc2ceaa71ba9250cf9bab83db9da7266e07e5"
CURRENT_FRAMEWORK_SHA = "29d382463eb353696f8ac224dd885bfb2148f55d"
CONTEXT_HASH = "62b283503fa2f62349dea2b2bb8f67dc65e1b1d944cec01cbd5df8e0bed806ae"
PRE_RECEIPT_CANONICAL_SHA256 = "750361c3807e3f0d7eae34fe52eed45a6411948f0968e80b55a57275ca3039fa"
PRE_RECEIPT_GIT_BLOB = "f83ef82e60bb889290226b86c30f97cf425c3044"
PRE_RECEIPT_RAW_SHA256 = "42330f8a4ebd93ea4c97435ed5d8ffdb81ceef0468a4228b8aca99f1466f2e47"
PRE_RECEIPT_PERSISTED_AT = "2026-08-12T10:54:45Z"
ACK_HOOK_AT = "2026-08-12T10:58:00Z"
CANDIDATE_FROZEN_AT = "2026-08-12T10:59:00Z"
INERT_FALSIFIER_RAW_SHA256 = "65b4a94d78a5c9b718be2c9baa08c52278304b39ee675f02800717d1174d22b5"

BASE = "research/real_math/millennium/yang_mills"
PRE_RECEIPT = f"{BASE}/09_trace/YM-S1a2i_K1_PRE_ACTION_RECEIPT_20260812.json"
PRE_GATE = f"{BASE}/09_trace/YM-S1a2i_K1_PRE_CANDIDATE_GATE_20260812.json"
PRE_TRACE = f"{BASE}/09_trace/YM-S1a2i_K1_PRE_CANDIDATE_TRACE_20260812.json"
PRE_BINDING = f"{BASE}/09_trace/YM-S1a2i_K1_FRAMEWORK_SUBJECT_BINDING_20260812.json"
INERT_FALSIFIER = f"{BASE}/05_oracles/ym_r20k1_inert_scalar_falsifier.py"
PATHS = {
    "durability": f"{BASE}/09_trace/YM-S1a2i_K1_POSTMERGE_DURABILITY_ACK_20260812.json",
    "candidate": f"{BASE}/04_candidates/YM-S1a2i_K1_C001_SCALAR_MARGIN_CANDIDATE_FREEZE_20260812.json",
    "manifest": f"{BASE}/05_oracles/YM-S1a2i_K1_C001_INERT_FALSIFIER_FREEZE_20260812.json",
    "authorization": f"{BASE}/09_trace/YM-S1a2i_K1_C001_EVALUATION_AUTHORIZATION_20260812.json",
    "framework": f"{BASE}/09_trace/YM-S1a2i_K1_C001_FRAMEWORK_REVALIDATION_20260812.json",
    "trace": f"{BASE}/09_trace/YM-S1a2i_K1_C001_CANDIDATE_FREEZE_TRACE_20260812.json",
    "receipt": f"{BASE}/09_trace/YM-S1a2i_K1_C001_CANDIDATE_FREEZE_RECEIPT_20260812.json",
}

NON_METHOD_FRAMEWORK_DIFF = (
    '.github/workflows/paper2-pendulum-microtrial.yml',
    'experiments/paper2/lunarc/build_native_ingest_receipt_v4_4.py',
    'experiments/paper3/build_semantic_descriptor.py',
    'experiments/training_ladder/build_exposure_scaffold.py',
    'publication/papers/paper-01-epistemic-mechanics/main.pdf',
    'publication/papers/paper-02-structural-mechanics/main.pdf',
    'publication/papers/paper-02-structural-mechanics/sections/02b_directionality_evidence.tex',
    'publication/papers/paper-02-structural-mechanics/sections/02c_v3_experience_transfer.tex',
    'publication/papers/paper-03-method-evolution-mechanics/main.pdf',
    'publication/papers/paper-05-verified-discovery-in-mathematics/main.pdf',
    'publication/papers/paper-06-rakl-scientific-research-engine/main.pdf',
    'research/PAPERS_II_III_V_CLAIM_TO_EVIDENCE_MATRIX_20260812.json',
    'research/STRONGEST_VERSION_CAMPAIGN_SCOREBOARD_20260812.json',
    'research/STRONGEST_VERSION_CAMPAIGN_SCOREBOARD_20260812.md',
    'research/fail_closed_framework_closeout_20260812/CLOSEOUT_INDEX.md',
    'research/fail_closed_framework_closeout_20260812/CLOSEOUT_STATUS.json',
    'research/fail_closed_framework_closeout_20260812/ISSUE_478_TERMINAL_RECEIPT.json',
    'research/fail_closed_framework_closeout_20260812/ISSUE_479_TERMINAL_RECEIPT.json',
    'research/glm52_mechanism_suite_v1_1/EMPIRICAL_INSTRUMENT_BINDINGS.json',
    'research/glm52_mechanism_suite_v1_1/NO_NEW_GLM_OUTCOME_RECEIPT.json',
    'research/glm52_mechanism_suite_v1_1/README.md',
    'research/glm52_mechanism_suite_v1_1/WAVE2_FREEZE_RECEIPT.json',
    'research/glm52_mechanism_suite_v1_1/WAVE2_HANDOFF_LANES.md',
    'research/glm52_mechanism_suite_v1_1/offline_selftest.py',
    'research/glm52_mechanism_suite_v1_1/wave2_freeze.py',
    'research/paper2_microtrial_v4_1/PARENT_RUNNER_BINDING_BLOCKER_2834760.json',
    'research/paper2_microtrial_v4_4/NATIVE_EXECUTION_STATUS.json',
    'research/paper2_microtrial_v4_4/NATIVE_INGEST_RECEIPT_3477848.json',
    'research/paper2_microtrial_v4_4/README.md',
    'research/paper2_microtrial_v4_4/native_bundles/PAPER2_V4_4_NATIVE_JOB_3477848.tar.gz',
    'research/paper2_microtrial_v4_4/native_job_3477848/logs/v4_4/p2-pend-v44-3477848.err',
    'research/paper2_microtrial_v4_4/native_job_3477848/logs/v4_4/p2-pend-v44-3477848.out',
    'research/paper2_microtrial_v4_4/native_job_3477848/receipts/v4_4/harvest-3477848.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/receipts/v4_4/job-3477848/allocated_preflight.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/receipts/v4_4/job-3477848/model_snapshot_post.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/receipts/v4_4/job-3477848/model_snapshot_pre.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/receipts/v4_4/sacct-3477848.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/receipts/v4_4/submission-3477848.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/blinded_scores.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/provider_receipts/BLIND_3C791A.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/provider_receipts/BLIND_8E24D5.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/raw_outputs/BLIND_3C791A.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/raw_outputs/BLIND_8E24D5.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/resource_receipts/BLIND_3C791A.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/resource_receipts/BLIND_8E24D5.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/result_receipt.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/run_manifest.json',
    'research/paper2_microtrial_v4_4/native_job_3477848/runs/v4_4/PENDULUM_SEALED_KNOWN_ANSWER_001-seed-17-job-3477848/task_seed_receipt.json',
    'research/paper2_transport_v2/KNOWN_WORLD_ABLATION_RESULT.json',
    'research/paper2_transport_v2/ORACLE_CONFORMANCE_RESULT.json',
    'research/receipts/PUBLICATION_PDF_HARVEST_AFTER_477_20260812.json',
    'schemas/paper2-v4-4-native-ingest-receipt.schema.json',
    'scripts/paper2_known_world_ablation.py',
    'scripts/paper2_transport_oracle_smoke.py',
    'tests/test_cycle_metrics_harvest.py',
    'tests/test_glm52_v1_1_wave2_freeze.py',
    'tests/test_paper2_pendulum_microtrial_v4_lunarc_completeness.py',
    'tests/test_paper3_semantic_descriptor_builder.py',
    'tests/test_training_ladder_phase0_1.py',
)

METHOD_ADJACENT_OPTIONAL_UNWIRED_DIFF = (
    "src/rakl/structural_transport_v2.py",
    "tests/test_structural_transport_v2.py",
)

POST_496_NON_METHOD_FRAMEWORK_DIFF = (
    'publication/papers/paper-02-structural-mechanics/sections/02b_directionality_evidence.tex',
    'research/STRONGEST_VERSION_CAMPAIGN_SCOREBOARD_20260812.json',
    'research/STRONGEST_VERSION_CAMPAIGN_SCOREBOARD_20260812.md',
    'research/empirical_10_of_10_v1/CAPABILITY_QUALIFICATION/README.md',
    'research/empirical_10_of_10_v1/CAPABILITY_QUALIFICATION/STAGE3_4_PROPOSAL_ONLY.json',
    'research/empirical_10_of_10_v1/PAPER3/DOWNSTREAM/PROTOCOL.json',
    'research/empirical_10_of_10_v1/PAPER3/LANE_STATUS.json',
    'research/empirical_10_of_10_v1/PAPER3/NATURAL_DOMAIN_HUMAN/ZERO_LABELS_RECEIPT.json',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/DEGENERACY_AUDIT.json',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/GENERATOR_MANIFEST.json',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/HIDDEN_GOLD_MANIFEST.json',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/MACHINE_WITNESS_OUTPUTS.jsonl',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/MACHINE_WITNESS_PROTOCOL.json',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/OBJECTIVE_TASKS.jsonl',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/POWER_RECEIPT.json',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/PROTOCOL.md',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/SEMANTIC_CONTROL_MANIFEST.json',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/SEMANTIC_CONTROL_SCORES.jsonl',
    'research/empirical_10_of_10_v1/PAPER3/OBJECTIVE/VERIFIER_BINDING.json',
    'research/empirical_10_of_10_v1/PAPER3/PAPER3_CLAIM_TO_RECEIPT_MATRIX.json',
    'research/empirical_10_of_10_v1/PAPER3/README.md',
    'research/training_time_rakl_phase0_1/EXPOSURE_CURVE_HARNESS_SCAFFOLD.json',
    'research/training_time_rakl_phase0_1/README.md',
    'tests/test_paper3_objective_lane_scaffold.py',
    'tests/test_training_ladder_exposure_scaffold_receipt.py',
)


POST_E3FFC_NON_METHOD_FRAMEWORK_DIFF = (
    'research/empirical_10_of_10_v1/CAPABILITY_QUALIFICATION/INTERFACE_CHALLENGER_SPEC.json',
    'research/empirical_10_of_10_v1/CAPABILITY_QUALIFICATION/README.md',
    'research/empirical_10_of_10_v1/CAPABILITY_QUALIFICATION/STAGE2_INTERFACE_CHALLENGER_RECEIPT.json',
    'research/empirical_10_of_10_v1/CAPABILITY_QUALIFICATION/protocol_stage2/RUNNER_INSTRUCTION_BLOCK.txt',
    'research/empirical_10_of_10_v1/CAPABILITY_QUALIFICATION/protocol_stage2/SYSTEM_PROMPT.txt',
    'tests/test_paper2_capability_v3_diagnostic.py',
)

def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def inert_falsifier_raw_sha256(root: Path = Path(".")) -> str:
    return hashlib.sha256((root / INERT_FALSIFIER).read_bytes()).hexdigest()


def seal(value: dict) -> dict:
    document = dict(value)
    document["artifact_hash"] = ""
    document["artifact_hash"] = canonical_hash(document)
    return document


def pre_receipt() -> PreActionFibreReceipt:
    return PreActionFibreReceipt(
        receipt_id="PRE-YM-S1a2i-K1-20260812",
        framework_repository="SzeChunYiu/RAKL",
        framework_commit=PRE_FRAMEWORK_SHA,
        application_repository="SzeChunYiu/RAKL_math",
        application_commit="b7ca6ac51fa8319b559e95402c47959c626f284a",
        task_id="YM-root-5",
        atom_id=ATOM,
        context_hash="sha256:" + CONTEXT_HASH,
        fibre_snapshot_hash="sha256:" + CONTEXT_HASH,
        operator_ids=("SOURCE_SCOPED_SCALAR_INVARIANT_REGION_DISCRIMINATOR",),
        selected_retrievals=(
            SelectedRetrieval("RAKL/main@62e97d54", RetrievalAuthority.CANONICAL, "d05e7e19bb57e43f1fbffb2ccc5bbe8745caa34f8b032fd62e32a08595fc4a89"),
            SelectedRetrieval("YM-R20-lesson", RetrievalAuthority.CANONICAL, "18c39a9a7ea90fede4fb3672d1e777886fea7e88e094f453bb8fada799018a73"),
            SelectedRetrieval("global-failure-atlas", RetrievalAuthority.CANONICAL, "db809b89815e0ca6a58eaa915e531bcd52d127f5449469dd087f349763f69d11"),
        ),
        rejected_retrievals=(
            RejectedRetrieval("Navier-Stokes-B2a1a3", "requires new PDE tail input rather than the selected cheap scalar discriminator"),
            RejectedRetrieval("Hodge-C008", "requires target incidence geometry not present on merged main"),
            RejectedRetrieval("BSD-Sha-finiteness", "deep arithmetic input and no cheap merged-main discriminator"),
        ),
        predeclared_discriminator=(
            "Using only source-bound k-uniform constants, decide whether strict irrelevant contraction plus "
            "higher-order forcing fits the next O(g_{k+1}^2) K radius on one predeclared small-coupling "
            "interval; otherwise return ASSUMPTIONS_INSUFFICIENT or CANNOT_CHECK."
        ),
        allowed_outcome_branches=("SUCCESS", "PARTIAL_SUCCESS", "FAILURE", "BLOCKED", "UNKNOWN"),
        frozen_at_utc="2026-08-12T10:29:00Z",
        sequence_index=21,
    )


def durability_document() -> dict:
    receipt = pre_receipt()
    if receipt.receipt_canonical_sha256 != PRE_RECEIPT_CANONICAL_SHA256:
        raise RuntimeError("public receipt canonical hash mismatch")
    ack = DurablePersistenceAcknowledgement(
        receipt_canonical_sha256=receipt.receipt_canonical_sha256,
        storage_pointer=(
            f"git+https://github.com/SzeChunYiu/RAKL_math.git@{PUBLIC_RECEIPT_COMMIT}"
            f"#blob={PRE_RECEIPT_GIT_BLOB}&path={PRE_RECEIPT}"
        ),
        persisted_at_utc=PRE_RECEIPT_PERSISTED_AT,
    )
    hook = run_pre_scratch_fibre_freeze_hook(
        hook_id="HOOK-YM-S1a2i-K1-POSTMERGE-DURABILITY-20260812",
        hook_invoked_at_utc=ACK_HOOK_AT,
        consequential_turn=True,
        prior_materialized_receipt=receipt,
        persistence_acknowledgement=ack,
    )
    if hook.materialization_status is not HookMaterializationStatus.ALREADY_MATERIALIZED:
        raise RuntimeError(hook.reasons)
    return seal(
        {
            "schema_version": "ym-postmerge-durability-ack-v1",
            "atom_id": ATOM,
            "application_parent_sha": APPLICATION_PARENT_SHA,
            "public_receipt_commit": PUBLIC_RECEIPT_COMMIT,
            "public_reachability_evidence": {
                "pr": 381,
                "url": "https://github.com/SzeChunYiu/RAKL_math/pull/381",
                "github_merged_at": PRE_RECEIPT_PERSISTED_AT,
                "meaning": (
                    "Conservative first public-persistence observation: GitHub reports PR381 merged at this "
                    "time with PUBLIC_RECEIPT_COMMIT reachable from main. The local commit timestamp is not used "
                    "as remote-durability evidence."
                ),
            },
            "public_receipt": {
                "path": PRE_RECEIPT,
                "git_blob": PRE_RECEIPT_GIT_BLOB,
                "raw_sha256": PRE_RECEIPT_RAW_SHA256,
                "receipt_canonical_sha256": receipt.receipt_canonical_sha256,
            },
            "persistence_acknowledgement": {
                "receipt_canonical_sha256": ack.receipt_canonical_sha256,
                "storage_pointer": ack.storage_pointer,
                "persisted_at_utc": ack.persisted_at_utc,
            },
            "hook_result": dict(hook.document()),
            "durable_state": "MATERIALIZED",
            "literal_hook_status": hook.materialization_status.value,
            "semantic_note": (
                "The fixed API reports ALREADY_MATERIALIZED when an exact prior receipt is supplied with a "
                "hash-matching acknowledgement. The operational durable state is MATERIALIZED; no bare in-memory "
                "build is relabelled."
            ),
            "licenses_result_blind_candidate_freeze": True,
            "grants_mathematical_credit": False,
        }
    )


def framework_document() -> dict:
    binding = FrameworkSubjectFreezeBinding(
        binding_id="FSB-YM-S1a2i-K1-C001-CURRENT-20260812",
        authoritative_framework_sha=CURRENT_FRAMEWORK_SHA,
        pre_candidate_packet_hash=CONTEXT_HASH,
        frozen_at_utc=CANDIDATE_FROZEN_AT,
        evidence_pointers=(
            f"git:{APPLICATION_PARENT_SHA}:{PRE_BINDING}",
            f"git:{CURRENT_FRAMEWORK_SHA}:src/rakl/framework_candidate_freeze.py",
            f"git-diff:{PRE_FRAMEWORK_SHA}..{CURRENT_FRAMEWORK_SHA}",
        ),
    )
    observation = FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=CURRENT_FRAMEWORK_SHA,
        intervening_diff=(),
        observation_evidence_pointers=(
            f"git-ls-remote:RAKL/main={CURRENT_FRAMEWORK_SHA}",
            "candidate-freeze binding was created directly against current main after reviewing prior drift",
        ),
    )
    report = audit_candidate_freeze_framework_subject(binding, observation, required=True)
    if report.verdict is not CandidateFreezeRevalidationVerdict.CURRENT_UNCHANGED:
        raise RuntimeError(report.reasons)
    return seal(
        {
            "schema_version": "ym-candidate-framework-revalidation-v1",
            "atom_id": ATOM,
            "freeze_binding": dict(binding.document()),
            "observed_current_main_sha": CURRENT_FRAMEWORK_SHA,
            "pre_candidate_to_current_review": {
                "from_sha": PRE_FRAMEWORK_SHA,
                "to_sha": CURRENT_FRAMEWORK_SHA,
                "pre_to_496_non_method_publication_or_empirical_research_paths": list(NON_METHOD_FRAMEWORK_DIFF),
                "structural_transport_ancestry_sha": STRUCTURAL_TRANSPORT_ANCESTRY_SHA,
                "post_496_non_method_publication_or_empirical_research_paths": list(POST_496_NON_METHOD_FRAMEWORK_DIFF),
                "method_adjacent_optional_unwired_reviewed_paths": list(METHOD_ADJACENT_OPTIONAL_UNWIRED_DIFF),
                "method_adjacent_classification": "METHOD_ADJACENT_OPTIONAL_UNWIRED_REVIEWED",
                "core_pre_candidate_contracts_changed": False,
                "latest_non_method_successor": {
                    "from_sha": PRE_LATEST_NON_METHOD_SUCCESSOR_SHA,
                    "to_sha": CURRENT_FRAMEWORK_SHA,
                    "classification": "NON_METHOD_PAPER2_CAPABILITY_INTERFACE_CHALLENGER_REVIEWED",
                    "changed_paths": list(POST_E3FFC_NON_METHOD_FRAMEWORK_DIFF),
                    "ym_mathematical_gate_changed": False,
                },
                "relevant_unchanged_surfaces": [
                    "src/rakl/math_context.py",
                    "src/rakl/math_research_runtime.py",
                    "src/rakl/research_memory.py",
                    "src/rakl/semantic_shortcut.py",
                    "src/rakl/framework_candidate_freeze.py",
                    "src/rakl/pre_scratch_fibre_freeze.py",
                    "skills/rakl-core/workflows/mathematical-research.md",
                ],
                "method_adjacent_review": (
                    "structural_transport_v2 entered at 496edc5ead136980287ac2e72efb486691945366 as a new optional directional empirical-transport module and is "
                    "method-adjacent, not non-method. It is not imported by the mathematical research runtime, "
                    "candidate-freeze gate, pre-scratch hook, context/memory/shortcut gates, or this YM fixture."
                ),
                "same_domain_scalar_effect": (
                    "Its directional cross-context transport obligations neither prove nor refute the same-domain "
                    "symbolic K-coordinate implication. C001 still requires direct source-uniform constants, exact "
                    "same-norm scope, and the frozen scalar falsifier in a later round."
                ),
            },
            "verdict": report.verdict.value,
            "reasons": list(report.reasons),
            "licenses_candidate_materialization": report.licenses_candidate_materialization,
            "grants_scientific_authority": False,
        }
    )


def candidate_document() -> dict:
    core = {
        "schema_version": "1.0.0",
        "candidate_id": CANDIDATE_ID,
        "atom_id": ATOM,
        "candidate_kind": "SYMBOLIC_SOURCE_SCOPED_K_NEXT_RADIUS_IMPLICATION",
        "frozen_at": CANDIDATE_FROZEN_AT,
        "symbolic_constants": {
            "rho": "real source contraction factor with 0<rho<1, required uniform in k",
            "c_K": "real graph-radius coefficient with c_K>0",
            "C_K": "real coefficient C_K>=0 for the source O(g_k^4) K forcing bound",
            "b_0": "real base-flow cubic coefficient with b_0>0",
            "C_beta": "real coefficient C_beta>=0 for |r_k|<=C_beta g_k^5",
            "epsilon": "existential positive small-coupling radius; no value or formula is frozen",
        },
        "source_bound_hypotheses_to_verify_later": [
            "for every admitted scale k, ||K_k||_k <= c_K g_k^2",
            "for every admitted scale k, ||K_{k+1}||_{k+1} <= rho ||K_k||_k + C_K g_k^4",
            "g_{k+1}=g_k-b_0 g_k^3+r_k with |r_k|<=C_beta g_k^5",
            "rho,c_K,C_K,b_0,C_beta are one finite constant family uniform in k",
            "the K norms and one-step estimate are exactly those of the source-scoped graph ball",
        ],
        "quantifier_order": (
            "FOR_ALL source-bound constants satisfying the displayed signs and k-uniformity; "
            "EXISTS epsilon>0; FOR_ALL admitted k; FOR_ALL 0<g_k<=epsilon; FOR_ALL K_k in the frozen graph ball"
        ),
        "candidate_statement": {
            "lower_base_factor": "L(g)=1-b_0 g^2-C_beta g^4",
            "scalar_margin": "M(g)=L(g)^2-rho-(C_K/c_K)g^2",
            "existence_claim": "there exists epsilon>0 such that L(g)>=0 and M(g)>=0 for every 0<g<=epsilon",
            "conditional_implication": (
                "under the frozen source hypotheses and scalar inequalities, "
                "||K_{k+1}||_{k+1} <= c_K g_{k+1}^2"
            ),
            "derivation_shape_to_check_later": [
                "g_{k+1} >= g_k L(g_k)",
                "c_K g_{k+1}^2 >= c_K g_k^2 L(g_k)^2 when L(g_k)>=0",
                "rho c_K g_k^2+C_K g_k^4 <= c_K g_k^2 L(g_k)^2 when M(g_k)>=0",
            ],
        },
        "proof_obligations": [
            {
                "id": "O1-SOURCE-UNIFORMITY",
                "required_source_constants": ["rho", "c_K", "C_K", "b_0", "C_beta"],
                "obligation": "bind exactly rho,c_K,C_K,b_0,C_beta and the same K norm uniformly in k from the acquired source",
                "status": "FROZEN_UNEVALUATED",
            },
            {"id": "O2-BASE-LOWER-BOUND", "obligation": "derive g_{k+1}>=g_k L(g_k) from the exact signed remainder bound without reversing an inequality", "status": "FROZEN_UNEVALUATED"},
            {"id": "O3-SCALAR-EXISTENCE", "obligation": "prove or refute existence of one epsilon satisfying L>=0 and M>=0; do not choose epsilon after target evaluation", "status": "FROZEN_UNEVALUATED"},
            {"id": "O4-NORM-AND-SCALE-SCOPE", "obligation": "verify the one-step norm and every constant use exactly the source scale indices and graph-ball scope", "status": "FROZEN_UNEVALUATED"},
            {"id": "O5-NEXT-RADIUS-COMPOSITION", "obligation": "compose O1-O4 to the smaller c_K g_{k+1}^2 radius only", "status": "FROZEN_UNEVALUATED"},
        ],
        "allowed_result_branches": [
            "CONDITIONAL_UNIFORM_SCALAR_SLACK_PROVED",
            "SOURCE_UNIFORMITY_OR_NORM_ASSUMPTIONS_INSUFFICIENT",
            "SCALAR_EXISTENCE_OR_COMPOSITION_REFUTED",
            "CANNOT_CHECK",
        ],
        "falsifiers": {
            "source_scope": "one required constant is not source-bound uniformly in k, or the norm changes without a proved bridge",
            "base_lower_bound": "an admissible remainder violates g_{k+1}>=g_k L(g_k)",
            "scalar_existence": "the frozen sign/finite-constant assumptions do not imply any common positive epsilon with L>=0 and M>=0",
            "composition": "the frozen inequalities fail to imply the exact next-radius bound for one admissible symbolic instance",
            "scope": "any step requires lambda control, base injectivity, a full graph transform, OS reconstruction, continuum transport, or mass-gap input",
        },
        "explicit_exclusions": [
            "NO_NUMERICAL_OR_SYMBOLIC_CONSTANT_VALUES_INVENTED",
            "NO_EXPLICIT_EPSILON_OR_THRESHOLD",
            "NO_SOURCE_CONSTANT_EVALUATION",
            "NO_FALSIFIER_EXECUTION",
            "NO_LAMBDA_OR_BASE_INJECTIVITY_CLAIM",
            "NO_FULL_GRAPH_TRANSFORM_CLAIM",
            "NO_CONTINUUM_OR_MASS_GAP_CLAIM",
            "NO_NOVELTY_OR_INDEPENDENT_REVIEW_CLAIM",
        ],
        "target_access": {
            "falsifier_imported_or_executed": False,
            "source_uniformity_checked": False,
            "scalar_existence_checked": False,
            "threshold_derived_or_tested": False,
            "result_accessed": False,
        },
        "future_result_lesson_contract": {
            "current_status": "NO_RESULT_NO_LESSON",
            "required_after_material_result": [
                "attempted_mathematical_implication",
                "exact_mathematical_result_or_failure",
                "supported_and_competing_mathematical_causes",
                "scope",
                "mathematical_falsifier",
                "repair_or_next_discriminator",
                "proof_or_source_evidence",
            ],
            "operational_metadata_zero_math_credit": [
                "Git/branch/PR state", "CI/tests", "schemas/hashes/chronology", "telemetry/repository growth"
            ],
        },
        "authority": {
            "mathematical_proposal": True,
            "mathematical_result_credit": False,
            "proof_authority": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
    }
    identity = {
        "candidate_id": CANDIDATE_ID,
        "canonical_core_sha256": canonical_hash(core),
        "identity_scope": "FULL_CANDIDATE_CORE_BEFORE_IDENTITY_AND_ARTIFACT_HASH",
    }
    return seal({**core, "candidate_identity": identity})


def build_documents() -> dict[str, dict]:
    actual_falsifier_sha256 = inert_falsifier_raw_sha256()
    if actual_falsifier_sha256 != INERT_FALSIFIER_RAW_SHA256:
        raise RuntimeError("inert falsifier byte hash mismatch")
    durability = durability_document()
    framework = framework_document()
    if not durability["licenses_result_blind_candidate_freeze"] or not framework["licenses_candidate_materialization"]:
        raise RuntimeError("operational gate did not license candidate freeze")
    candidate = candidate_document()
    manifest = seal(
        {
            "schema_version": "1.0.0",
            "manifest_id": "YM-S1a2i-K1-C001-INERT-FALSIFIER-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "path": INERT_FALSIFIER,
            "raw_sha256": INERT_FALSIFIER_RAW_SHA256,
            "status": "FROZEN_INERT_NOT_IMPORTED_NOT_EXECUTED",
            "inert_behavior": "Every invocation raises TargetEvaluationNotAuthorized.",
            "current_round_execution_authorized": False,
            "mathematical_result_credit": False,
        }
    )
    authorization = seal(
        {
            "schema_version": "1.0.0",
            "authorization_id": "YM-S1a2i-K1-C001-EVALUATION-AUTHORIZATION-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "falsifier_raw_sha256": INERT_FALSIFIER_RAW_SHA256,
            "current_round_falsifier_execution_authorized": False,
            "source_constant_extraction_authorized": False,
            "symbolic_or_numeric_threshold_derivation_authorized": False,
            "result_classification_authorized": False,
            "allowed_next_action": (
                "COMMIT_THIS_PUBLIC_RESULT_BLIND_CANDIDATE_FREEZE_ONLY; source extraction, scalar evaluation, "
                "falsifier execution, threshold derivation, and result classification remain unauthorized"
            ),
            "future_evaluation_requires_separate_successor_authorization": True,
            "result_state": "UNEVALUATED",
            "mathematical_result_credit": False,
        }
    )
    pre_trace = json.loads(Path(PRE_TRACE).read_text(encoding="utf-8"))
    entries = list(pre_trace["entries"])
    event = {
        "event_id": "YM-S1a2i-K1-E08",
        "atom_id": ATOM,
        "event_type": "CANDIDATE_PROPOSED",
        "timestamp": CANDIDATE_FROZEN_AT,
        "state_summary": "The exact symbolic K-coordinate next-radius implication and inert falsifier identity are frozen after public-receipt durability acknowledgement.",
        "action_summary": "Freeze candidate identity, source obligations, result branches, and falsifiers without evaluation.",
        "evidence_pointers": [PATHS["durability"], PATHS["candidate"], PATHS["manifest"], PATHS["authorization"], PATHS["framework"]],
        "alternatives_considered": ["evaluate source constants now", "invent numerical constants", "freeze a full graph-transform claim", "freeze only the scalar K-coordinate implication"],
        "decision_rationale": "The scalar implication is the smallest result-blind object that discriminates K-coordinate repairability while preserving every deeper Yang-Mills residual.",
        "outputs": [CANDIDATE_ID, candidate["candidate_identity"]["canonical_core_sha256"], "FROZEN_UNEVALUATED", "ZERO_MATHEMATICAL_RESULT_CREDIT"],
        "uncertainties": ["source k-uniformity remains unchecked", "same-norm transport remains unchecked", "the scalar proposition remains unevaluated"],
        "residuals": ["K-coordinate conditional implication open", "lambda/base/full graph/OS/continuum/mass-gap obligations excluded and open", "root OPEN_NO_SOLUTION_CERTIFICATE"],
        "next_steps": ["commit and publish exact freeze before any target evaluation", "obtain separate successor authorization", "evaluate source scope before scalar algebra and preserve any failure"],
        "previous_event_hash": entries[-1]["artifact_hash"],
    }
    event["artifact_hash"] = ""
    event["artifact_hash"] = canonical_hash(event)
    entries.append(event)
    trace = {"trace_id": "TRACE-YM-S1a2i-K1-C001-FREEZE-20260812", "entries": entries}
    documents = {
        "durability": durability,
        "candidate": candidate,
        "manifest": manifest,
        "authorization": authorization,
        "framework": framework,
        "trace": trace,
    }
    integrity = {
        "json_inputs": {name: {"path": PATHS[name], "canonical_sha256": canonical_hash(doc)} for name, doc in sorted(documents.items())},
        "byte_inputs": {
            "public_pre_receipt": {"path": PRE_RECEIPT, "application_commit": PUBLIC_RECEIPT_COMMIT, "git_blob": PRE_RECEIPT_GIT_BLOB, "raw_sha256": PRE_RECEIPT_RAW_SHA256},
            "inert_falsifier": {"path": INERT_FALSIFIER, "raw_sha256": INERT_FALSIFIER_RAW_SHA256},
        },
    }
    documents["receipt"] = seal(
        {
            "schema_version": "1.0.0",
            "receipt_id": "YM-S1a2i-K1-C001-CANDIDATE-FREEZE-20260812",
            "candidate_id": CANDIDATE_ID,
            "candidate_core_sha256": candidate["candidate_identity"]["canonical_core_sha256"],
            "candidate_artifact_hash": candidate["artifact_hash"],
            "frozen_at": CANDIDATE_FROZEN_AT,
            "operational_gates": {
                "public_pre_receipt_durable_state": durability["durable_state"],
                "literal_hook_status": durability["literal_hook_status"],
                "framework_verdict": framework["verdict"],
                "candidate_materialization_licensed": True,
            },
            "chronology": {
                "application_parent_commit": APPLICATION_PARENT_SHA,
                "public_pre_receipt_precedes_candidate": True,
                "candidate_publication_status": "TO_BE_COMMITTED_BEFORE_ANY_EVALUATION",
                "falsifier_imported_or_executed": False,
                "result_accessed": False,
            },
            "full_document_integrity": integrity,
            "full_document_integrity_hash": canonical_hash(integrity),
            "authority": {
                "candidate_is_mathematical_proposal": True,
                "target_truth": False,
                "independent_review": False,
                "mathematical_result_credit": False,
                "mathematical_saturation_credit": False,
                "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            },
            "allowed_next_action": "COMMIT PUBLIC FREEZE ONLY; EVALUATION REQUIRES SEPARATE SUCCESSOR AUTHORIZATION",
        }
    )
    return documents


def write_documents(root: Path = Path(".")) -> None:
    for name, document in build_documents().items():
        path = root / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_documents()
