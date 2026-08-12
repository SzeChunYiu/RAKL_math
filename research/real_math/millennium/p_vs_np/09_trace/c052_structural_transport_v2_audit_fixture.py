"""Post-merge obligation audit of the existing C052 SEARCH mapping.

This module does not construct or run a classifier.  It re-expresses the
already-frozen SEARCH mapping as the evidence-bound, fail-closed transport-v2
contract introduced at RAKL 496edc.  Unknown future-candidate preservation
facts remain UNKNOWN and therefore yield CANNOT_CHECK.
"""
from __future__ import annotations

from dataclasses import asdict
from enum import Enum
import hashlib
import json
from pathlib import Path

from rakl.framework_candidate_freeze import (
    FrameworkSubjectFreezeBinding,
    FrameworkSubjectRevalidationObservation,
    audit_candidate_freeze_framework_subject,
)
from rakl.structural_types import (
    BoundaryCondition,
    StructuralObject,
    StructuralRelation,
    StructuralRole,
)
from rakl.structural_transport_v2 import (
    ObligationKind,
    ObligationRequirement,
    ObligationStatus,
    StructuralWitnessV2,
    TransferObligation,
    assess_transfer_v2,
)


ATOM = "O9d12a2a1b-C052"
EPISODE = "E-PNP-C052-REPARAMETERIZE-BY-SUPPORT-AND-TOKEN-PHASE"
SEARCH_WITNESS = "W-PNP-C052-SUPPORT-PHASE-SEARCH"
FRAMEWORK_CURRENT_SHA = "a6946c740b50413faf0eee218cc490dd6383e9ab"
FRAMEWORK_PREVIOUS_ACTIVE_SHA = "29d382463eb353696f8ac224dd885bfb2148f55d"
HISTORICAL_CONTEXT_FRAMEWORK_SHA = "62e97d545f93ff604b2db47a7c8d41a59a1c5286"
HISTORICAL_PREACTION_APPLICATION_PIN_SHA = "5dc0627f039e8f3e1cdcb7e05cd7603860afc554"
STRUCTURAL_TRANSPORT_INTRO_SHA = "496edc5ead136980287ac2e72efb486691945366"
STRUCTURAL_TRANSPORT_SHA256 = "f8b03ab9965f04400fac2d74c8c533e2354046025887b6aefd8b79968cf99e87"
QUANTIFIER_RUNTIME_SHA256 = "cbbf7c125a505f4914a2253e75e5a809c67fb74e8193cc31d19ab3019938accc"
QUANTIFIER_SCHEMA_SHA256 = "2874ab098fd28941c1e001abdb90b2a164d0af6fe282bbcbdf68bdb38403917f"
EXACT_QOI = (
    "whether the existing C052 SEARCH mapping licenses only a later target-blind "
    "classifier-and-falsifier identity freeze while preserving its exact mathematical scope"
)
BASE = "research/real_math/millennium/p_vs_np"
PATHS = {
    "context": f"{BASE}/01_frontier/O9d12a2a1b_C052_MATH_CONTEXT_FIBER_20260812.json",
    "memory": f"{BASE}/07_memory/O9d12a2a1b_C052_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "shortcut": f"{BASE}/08_reviews/O9d12a2a1b_C052_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "quantifier": f"{BASE}/08_reviews/O9d12a2a1b_C052_QUANTIFIER_COMPATIBILITY_WITNESS_20260812.json",
    "gate": f"{BASE}/09_trace/O9d12a2a1b_C052_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
    "framework_rebinding": f"{BASE}/09_trace/O9d12a2a1b_C052_FRAMEWORK_SUBJECT_REBINDING_A6946C7_20260812.json",
    "framework_revalidation": f"{BASE}/09_trace/O9d12a2a1b_C052_POSTMERGE_FRAMEWORK_REVALIDATION_A6946C7_20260812.json",
    "receipt": f"{BASE}/08_reviews/O9d12a2a1b_C052_STRUCTURAL_TRANSPORT_V2_AUDIT_20260812.json",
}

ROLES = (
    "explicit parent support cell",
    "explicit current support cell",
    "half-length k",
    "literal-token phase phi",
    "fixed MAGIC comparison coordinates",
    "target-blind symbolic classifier",
    "independent hostile supported-tuple falsifier",
)

RELATIONS = (
    ("explicit parent support cell", "encoded_length_differs_by_exactly_two_from", "explicit current support cell"),
    ("half-length k", "induces_token_phase_modulo_literal_width", "literal-token phase phi"),
    ("literal-token phase phi", "indexes_suffix_label_against", "fixed MAGIC comparison coordinates"),
    ("target-blind symbolic classifier", "classifies_over", "explicit parent support cell"),
    ("independent hostile supported-tuple falsifier", "tests_totality_of", "target-blind symbolic classifier"),
)

INVARIANTS = (
    "exact C041 length and code grammar",
    "C048 synchronized intersection meaning",
    "C050/C051 bounded scope",
    "target blindness",
    "OPEN_NO_SOLUTION_CERTIFICATE",
)

EPISODE_PRECONDITIONS = (
    "the exact C041 length formula and canonical grammar remain frozen",
    "all parent/current integer, bit-length, parity, phase, and padding quantifiers are explicit",
    "C050 and C051 are reproduced as regression obligations rather than induction premises",
    "escape-admissible, unresolved, and cannot-check outputs remain possible",
    "no target k, decoder, SAT, or overlap result is exposed before candidate/falsifier identity freeze",
)

FORBIDDEN_LOSSES = (
    "new-k enumeration",
    "target k or residue selection",
    "finite-to-universal extrapolation",
    "syntax-to-UNSAT promotion",
    "classifier or falsifier execution",
    "cover or root authority escalation",
)

BOUNDARIES = (
    BoundaryCondition("authority_transition", "identity_freeze_only"),
    BoundaryCondition("evaluation_access", "prohibited"),
    BoundaryCondition("target_k_selection", "prohibited"),
    BoundaryCondition("mathematical_scope", "C041_C048_code_interface_only"),
    BoundaryCondition("root_state", "OPEN_NO_SOLUTION_CERTIFICATE"),
)


def _jsonable(value):
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, tuple):
        return [_jsonable(item) for item in value]
    if isinstance(value, frozenset):
        return sorted(_jsonable(item) for item in value)
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    return value


def _hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _sealed(value: dict) -> dict:
    result = dict(value)
    result["artifact_hash"] = ""
    result["artifact_hash"] = _hash(result)
    return result


def _evidence(*names: str) -> tuple[str, ...]:
    return tuple(PATHS[name] for name in names)


def _structure(structure_id: str, context_id: str, domain: str) -> StructuralObject:
    return StructuralObject(
        structure_id=structure_id,
        domain=domain,
        qoi=EXACT_QOI,
        context_id=context_id,
        roles=tuple(StructuralRole(role, "mapped_C052_SEARCH_role") for role in ROLES),
        relations=tuple(StructuralRelation(source, relation, target) for source, relation, target in RELATIONS),
        invariants=frozenset(INVARIANTS),
        boundaries=BOUNDARIES,
        evidence_ids=_evidence("context", "memory", "shortcut", "quantifier", "gate"),
    )


def _explicit(
    obligation_id: str,
    kind: ObligationKind,
    source_ref: str,
    target_ref: str,
    evidence: tuple[str, ...],
    rationale: str,
) -> TransferObligation:
    return TransferObligation(
        obligation_id,
        kind,
        source_ref,
        target_ref,
        evidence_ids=evidence,
        status=ObligationStatus.SATISFIED,
        rationale_code=rationale,
    )


def build_assessment():
    source = _structure(
        "PNP-C052-RECORDED-SUPPORT-PHASE-EPISODE",
        "C041-C048-C050-C051-EPISODE-CONTEXT",
        "mathematics / recorded variable-width code synchronization episode",
    )
    target = _structure(
        "PNP-C052-CURRENT-SEARCH-MAPPING",
        "O9d12a2a1b-C052-FROZEN-CONTEXT",
        "mathematics / C052 prospective support-phase routing",
    )
    obligations: list[TransferObligation] = [
        TransferObligation(
            "QOI-EXACT",
            ObligationKind.QOI,
            EXACT_QOI,
            EXACT_QOI,
            evidence_ids=_evidence("shortcut", "gate"),
        )
    ]
    obligations.extend(
        TransferObligation(
            f"ROLE-{index:02d}",
            ObligationKind.ROLE,
            role,
            role,
            evidence_ids=_evidence("shortcut"),
        )
        for index, role in enumerate(ROLES, 1)
    )
    obligations.extend(
        TransferObligation(
            f"RELATION-{index:02d}",
            ObligationKind.RELATION,
            "|".join((source_role, relation, target_role, "1")),
            "|".join((source_role, relation, target_role, "1")),
            evidence_ids=_evidence("context", "shortcut"),
        )
        for index, (source_role, relation, target_role) in enumerate(RELATIONS, 1)
    )
    obligations.extend(
        TransferObligation(
            f"INVARIANT-{index:02d}",
            ObligationKind.INVARIANT,
            invariant,
            invariant,
            evidence_ids=_evidence("context", "shortcut", "gate"),
        )
        for index, invariant in enumerate(INVARIANTS, 1)
    )
    obligations.extend(
        (
            _explicit("PRE-GRAMMAR-FROZEN", ObligationKind.PRECONDITION, EPISODE_PRECONDITIONS[0], EPISODE_PRECONDITIONS[0], _evidence("context", "memory"), "frozen_context_and_episode"),
            _explicit("PRE-QUANTIFIER-DOMAIN", ObligationKind.PRECONDITION, EPISODE_PRECONDITIONS[1], EPISODE_PRECONDITIONS[1], _evidence("context", "quantifier"), "explicit_conditional_quantifier_witness"),
            _explicit("PRE-REGRESSION-OBLIGATIONS", ObligationKind.PRECONDITION, EPISODE_PRECONDITIONS[2], EPISODE_PRECONDITIONS[2], _evidence("context", "shortcut", "gate"), "bounded_regressions_recorded_not_universalized"),
            TransferObligation(
                "PRE-ESCAPE-OUTPUTS-PRESERVED",
                ObligationKind.PRECONDITION,
                EPISODE_PRECONDITIONS[3],
                EPISODE_PRECONDITIONS[3],
                evidence_ids=_evidence("shortcut", "gate"),
                status=ObligationStatus.UNKNOWN,
                rationale_code="future_classifier_identity_absent",
            ),
            _explicit("PRE-NO-RESULT-ACCESS", ObligationKind.PRECONDITION, EPISODE_PRECONDITIONS[4], EPISODE_PRECONDITIONS[4], _evidence("gate"), "current_gate_records_no_target_or_result_access"),
            TransferObligation(
                "PRE-FUTURE-IDENTITIES-TARGET-BLIND",
                ObligationKind.PRECONDITION,
                "later classifier and falsifier identities preserve target blindness",
                "later classifier and falsifier identities preserve target blindness",
                evidence_ids=_evidence("shortcut", "gate"),
                status=ObligationStatus.UNKNOWN,
                rationale_code="future_classifier_identity_absent",
            ),
        )
    )
    obligations.extend(
        TransferObligation(
            f"BOUNDARY-{index:02d}",
            ObligationKind.BOUNDARY,
            boundary.key,
            boundary.value,
            evidence_ids=_evidence("context", "shortcut", "gate"),
        )
        for index, boundary in enumerate(BOUNDARIES, 1)
    )
    obligations.extend(
        TransferObligation(
            f"LOSS-{index:02d}",
            ObligationKind.FORBIDDEN_LOSS,
            loss,
            "",
            requirement=ObligationRequirement.FORBIDDEN,
            evidence_ids=_evidence("shortcut", "gate"),
        )
        for index, loss in enumerate(FORBIDDEN_LOSSES, 1)
    )
    witness = StructuralWitnessV2(
        witness_id="W-PNP-C052-SUPPORT-PHASE-SEARCH-V2-AUDIT",
        source_structure_id=source.structure_id,
        target_structure_id=target.structure_id,
        source_context_id=source.context_id,
        target_context_id=target.context_id,
        qoi=EXACT_QOI,
        role_mapping=tuple((role, role) for role in ROLES),
        obligations=tuple(obligations),
        permitted_losses=frozenset(),
        forbidden_losses=frozenset(FORBIDDEN_LOSSES),
        uncertainty_note=(
            "The already-frozen mapping names future validation obligations, but no classifier or falsifier "
            "identity exists yet; target-side preservation and forbidden-loss facts therefore remain unknown."
        ),
    )
    return source, target, witness, assess_transfer_v2(source, target, witness)


def _raw_input_hash(path: str, root: Path) -> str:
    return hashlib.sha256((root / path).read_bytes()).hexdigest()


def framework_rebinding_documents(root: Path) -> tuple[dict, dict]:
    context = json.loads((root / PATHS["context"]).read_text(encoding="utf-8"))
    binding = FrameworkSubjectFreezeBinding(
        binding_id="PNP-C052-FRAMEWORK-SUBJECT-REBIND-A6946C7-20260812",
        authoritative_framework_sha=FRAMEWORK_CURRENT_SHA,
        pre_candidate_packet_hash=context["packet_hash"].removeprefix("sha256:"),
        frozen_at_utc="2026-08-12T11:18:00Z",
        evidence_pointers=(
            f"git:{FRAMEWORK_CURRENT_SHA}:RAKL_VERSION.json",
            f"git:{FRAMEWORK_CURRENT_SHA}:skills/rakl-core/workflows/mathematical-research.md",
            f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/structural_transport_v2.py@sha256:{STRUCTURAL_TRANSPORT_SHA256}",
            f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/quantifier_compatibility.py@sha256:{QUANTIFIER_RUNTIME_SHA256}",
            f"git:{FRAMEWORK_CURRENT_SHA}:schemas/quantifier-compatibility-witness-v1.schema.json@sha256:{QUANTIFIER_SCHEMA_SHA256}",
            PATHS["context"],
        ),
    )
    observation = FrameworkSubjectRevalidationObservation(
        observed_current_main_sha=FRAMEWORK_CURRENT_SHA,
        intervening_diff=(),
        observation_evidence_pointers=(
            f"git-ls-remote:SzeChunYiu/RAKL:refs/heads/main:{FRAMEWORK_CURRENT_SHA}",
            f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/structural_transport_v2.py@sha256:{STRUCTURAL_TRANSPORT_SHA256}",
            f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/quantifier_compatibility.py@sha256:{QUANTIFIER_RUNTIME_SHA256}",
        ),
    )
    report = audit_candidate_freeze_framework_subject(binding, observation, required=True)
    rebinding = _sealed({
        **dict(binding.document()),
        "rebind_chronology": {
            "historical_context_framework_binding_sha": HISTORICAL_CONTEXT_FRAMEWORK_SHA,
            "historical_context_binding_preserved_not_rewritten": True,
            "historical_preaction_application_pin": HISTORICAL_PREACTION_APPLICATION_PIN_SHA,
            "historical_preaction_pin_is_provenance_only": True,
            "current_rebind_frozen_after_framework_tip_observation": True,
            "candidate_or_falsifier_identity_existed_at_rebind": False,
            "historical_identity_only_license_status_before_revalidation": "STALE_FOR_ANY_FUTURE_CLASSIFIER_FREEZE",
            "historical_identity_only_license_superseded_by": "PNP-C052-POSTMERGE-FRAMEWORK-REVALIDATION-A6946C7-20260812",
        },
        "rebind_reason": (
            "The historical 62e97d context binding remains chronologically valid, but 496edc added the "
            "protected structural_transport_v2 runtime.  Rebind the unchanged mathematical packet to "
            "current a6946c7 before any later candidate identity; do not backdate or overwrite history."
        ),
        "intervening_surface_classification": {
            "protected_added_at_496edc": ["src/rakl/structural_transport_v2.py"],
            "unchanged_quantifier_runtime_sha256": QUANTIFIER_RUNTIME_SHA256,
            "unchanged_quantifier_schema_sha256": QUANTIFIER_SCHEMA_SHA256,
            "previous_active_framework_sha": FRAMEWORK_PREVIOUS_ACTIVE_SHA,
            "predecessor_to_current_diff": {
                "classification": "NON_CORE_PUBLICATION_RESEARCH_SCOREBOARD_AND_TEST_ONLY",
                "insertions": 374,
                "deletions": 18,
                "paths": [
                    "research/STRONGEST_VERSION_CAMPAIGN_SCOREBOARD_20260812.json",
                    "research/STRONGEST_VERSION_CAMPAIGN_SCOREBOARD_20260812.md",
                    "research/paper1_adversarial_epistemic_benchmark_v1/COMPARATOR_MODELS.md",
                    "research/paper1_adversarial_epistemic_benchmark_v1/DESIGN_FREEZE.json",
                    "research/paper1_adversarial_epistemic_benchmark_v1/EPISODE_FAMILIES.md",
                    "research/paper1_adversarial_epistemic_benchmark_v1/METRICS.md",
                    "research/paper1_adversarial_epistemic_benchmark_v1/PROTOCOL.md",
                    "research/paper1_adversarial_epistemic_benchmark_v1/README.md",
                    "research/paper2_nearest_work_2026/AUDIT_STATUS.json",
                    "research/paper2_nearest_work_2026/BIBLIOGRAPHY_PATCH.tex",
                    "research/paper2_nearest_work_2026/CLAIM_MATRIX.md",
                    "research/paper2_nearest_work_2026/COMPARATOR_REQUIREMENTS.md",
                    "research/paper2_nearest_work_2026/MANUSCRIPT_DIFF_PLAN.md",
                    "research/paper2_nearest_work_2026/NOVELTY_THREAT_RANKING.md",
                    "research/paper2_nearest_work_2026/README.md",
                    "research/paper2_nmi_flagship_gate_v1/DESIGN_GATE_FREEZE.json",
                    "research/paper2_nmi_flagship_gate_v1/README.md",
                    "tests/test_paper1_adversarial_epistemic_scaffold.py",
                    "tests/test_paper2_nearest_work_2026_scaffold.py",
                ],
                "protected_math_gate_paths_changed": [],
            },
            "post_496_to_current_core_method_diff": [],
            "post_496_to_current_scope": "publication, empirical research, scoreboards, capability freezes, and paper tests only",
        },
        "authority": {
            "process_rebinding_only": True,
            "mathematical_result_credit": 0,
            "proof_authority": False,
            "independent_review_credit": 0,
        },
    })
    revalidation = _sealed({
        "schema_version": "framework-subject-revalidation-observation-v1",
        "observation_id": "PNP-C052-POSTMERGE-FRAMEWORK-REVALIDATION-A6946C7-20260812",
        "active_binding_id": binding.binding_id,
        "active_binding_canonical_sha256": binding.binding_canonical_sha256,
        "observed_current_main_sha": observation.observed_current_main_sha,
        "intervening_diff": [],
        "observation_evidence_pointers": list(observation.observation_evidence_pointers),
        "verdict": report.verdict.value,
        "reasons": list(report.reasons),
        "licenses_candidate_materialization": report.licenses_candidate_materialization,
        "licensed_action": "PRESERVE_PRIOR_IDENTITY_FREEZE_ONLY_LICENSE",
        "supersession": {
            "historical_62e97d_identity_only_license": "STALE_FOR_FUTURE_USE",
            "current_a6946c7_mandatory_gate_revalidation": "SUPERSEDES_HISTORICAL_LICENSE_FOR_FUTURE_CLASSIFIER_FREEZE",
            "current_license_scope": "FREEZE_TARGET_BLIND_CLASSIFIER_AND_INDEPENDENT_FALSIFIER_IDENTITIES_ONLY",
        },
        "optional_transport_v2_disposition": {
            "wired_into_mandatory_C052_gate": False,
            "audit_verdict": "CANNOT_CHECK",
            "blocks_already_supported_same_domain_identity_freeze_route": False,
            "blocks_transport_v2_certified_mapping_claim": True,
            "blocks_theorem_or_mathematical_result_claim": True,
            "reason": (
                "The optional v2 audit cannot verify properties of identities that do not yet exist.  This "
                "advisory abstention neither weakens nor replaces the unchanged mandatory context/memory/shortcut/"
                "trace/quantifier gates, but it forbids claiming that transport-v2 already certifies the mapping."
            ),
        },
        "classifier_or_falsifier_identity_created": False,
        "classifier_or_falsifier_execution_authorized": False,
        "new_k_enumeration_authorized": False,
        "target_selection_authorized": False,
        "decoder_sat_overlap_access_authorized": False,
        "mathematical_result_credit": 0,
        "grants_scientific_authority": report.grants_scientific_authority,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    return rebinding, revalidation


def build_document(root: str | Path | None = None) -> dict:
    base = Path(root) if root is not None else Path(__file__).resolve().parents[5]
    source, target, witness, assessment = build_assessment()
    input_names = ("context", "memory", "shortcut", "quantifier", "gate")
    return _sealed({
        "schema_version": "1.0.0",
        "audit_id": "PNP-C052-STRUCTURAL-TRANSPORT-V2-AUDIT-20260812",
        "atom_id": ATOM,
        "audited_episode_id": EPISODE,
        "audited_search_witness_id": SEARCH_WITNESS,
        "audit_scope": (
            "post-merge obligation-level audit of the existing SEARCH mapping only; no classifier candidate, "
            "falsifier identity, target cell, evaluated result, or theorem is created"
        ),
        "framework_binding": {
            "current_runtime_sha": FRAMEWORK_CURRENT_SHA,
            "structural_transport_v2_introduction_sha": STRUCTURAL_TRANSPORT_INTRO_SHA,
            "structural_transport_v2_sha256": STRUCTURAL_TRANSPORT_SHA256,
            "quantifier_runtime_sha256": QUANTIFIER_RUNTIME_SHA256,
            "quantifier_schema_sha256": QUANTIFIER_SCHEMA_SHA256,
        },
        "input_artifacts": {
            name: {"path": PATHS[name], "raw_sha256": _raw_input_hash(PATHS[name], base)}
            for name in input_names
        },
        "source_structure": _jsonable(asdict(source)),
        "target_structure": _jsonable(asdict(target)),
        "witness": _jsonable(witness.canonical_payload()),
        "assessment": {
            "decision": assessment.decision.value,
            "reasons": list(assessment.reasons),
            "witness_hash": assessment.witness_hash,
            "traces": _jsonable([asdict(item) for item in assessment.traces]),
        },
        "unknown_load_bearing_facts": [
            "whether the future total classifier identity retains ESCAPE_ADMISSIBLE, UNRESOLVED, and CANNOT_CHECK branches",
            "whether the future classifier and hostile falsifier identities remain target-blind",
            "whether each forbidden loss remains absent in those as-yet nonexistent identities",
        ],
        "seven_field_mathematical_lesson": {
            "attempted_implication": (
                "The existing role/relation mapping for the bounded C050/C051 phase obstruction is sufficient "
                "to license safe transport to a parametric support-phase classifier-identity freeze."
            ),
            "exact_result_or_failure": (
                "CANNOT_CHECK: the recorded structures, relations, bounded invariants, exact quantifier witness, "
                "and current no-result boundary are evidenced, but future classifier/falsifier preservation and "
                "all six forbidden-loss obligations are not yet mathematically inspectable because those identities do not exist."
            ),
            "supported_and_competing_causes": {
                "supported": [
                    "the SEARCH mapping records semantic correspondences but not evidence about an unmaterialized target operator",
                    "bounded k=15 and k=19 conflicts cannot certify universal output completeness or absence of forbidden extrapolation",
                ],
                "competing_not_established": [
                    "the transport is false",
                    "a supported escape cell exists",
                    "a universal forced-conflict class exists",
                ],
            },
            "scope": (
                "Only the C052 mapping from the C041/C048 code interface and bounded C050/C051 lessons to a "
                "future identity-freeze action; no syntax, UNSAT, overlap, cover, circuit, or P-versus-NP conclusion."
            ),
            "mathematical_falsifier": (
                "A frozen target-blind total classifier/falsifier pair whose formal domain covers every declared "
                "support tuple, retains ESCAPE_ADMISSIBLE/UNRESOLVED/CANNOT_CHECK, reproduces both bounded regressions, "
                "and proves preservation of every forbidden-loss obligation would falsify this present CANNOT_CHECK diagnosis."
            ),
            "repair_or_next_discriminator": (
                "Freeze, without executing, exact target-blind classifier and hostile-falsifier identities; then rerun "
                "this obligation audit against their formal domain, branches, quantifiers, and authority boundary."
            ),
            "proof_and_source_evidence": [
                PATHS["context"],
                PATHS["memory"],
                PATHS["shortcut"],
                PATHS["quantifier"],
                PATHS["gate"],
                f"git:{FRAMEWORK_CURRENT_SHA}:src/rakl/structural_transport_v2.py@sha256:{STRUCTURAL_TRANSPORT_SHA256}",
            ],
        },
        "authority": {
            "audit_decision": assessment.decision.value,
            "transport_v2_certified_candidate_generation_authority": False,
            "mandatory_same_domain_identity_freeze_route_blocked": False,
            "classifier_or_falsifier_identity_created": False,
            "execution_authority": False,
            "mathematical_result_credit": 0,
            "proof_authority": False,
            "independent_review_credit": 0,
            "git_ci_schema_hash_chronology_credit": 0,
            "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
        "explicit_non_actions": {
            "new_k_enumeration_authorized": False,
            "target_k_selected": False,
            "decoder_sat_overlap_accessed": False,
            "classifier_identity_created": False,
            "falsifier_identity_created": False,
            "classifier_or_falsifier_executed": False,
            "parametric_theorem_proposed": False,
        },
    })


def build_documents(root: str | Path | None = None) -> dict[str, dict]:
    base = Path(root) if root is not None else Path(__file__).resolve().parents[5]
    rebinding, revalidation = framework_rebinding_documents(base)
    return {
        "framework_rebinding": rebinding,
        "framework_revalidation": revalidation,
        "receipt": build_document(base),
    }


def write_documents(root: str | Path = ".") -> None:
    base = Path(root)
    for name, document in build_documents(base).items():
        path = base / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_documents()
