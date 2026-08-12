from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
RESULT_BASE_SHA = "77b1ca99c1ed6fe8aee5d04a41e42c9bd0051ecb"
ORIGINAL_AUTHORIZATION_MERGE_SHA = "1bf48bf755bb057d822b496fe7b4152c00e3a6bc"
EVALUATOR_IDENTITY_MERGE_SHA = "ff21299ae77dde937e00c5739de3c526a30736d5"
RETROSPECTIVE_AUTHORIZATION_MERGE_SHA = "ba9749865e99acf0a9751754cdee3931225804ef"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
CANDIDATE_ID = "YM-S1a2i-K1-D001-C001-TWO-STAGE-SOURCE-BRIDGE"
SOURCE_TEX_SHA256 = "ef936e502e84b0cafabc594c9705c16c9c1df29dc95f2a6a679b6b446c526c18"
SOURCE_PDF_SHA256 = "08013e1ce75c8b2be79c62ba61f70e30024b9bb427c465ceab7ee9266236690d"

CANDIDATE = "research/real_math/millennium/yang_mills/04_candidates/YM-S1a2i_K1_D001_C001_TWO_STAGE_SOURCE_BRIDGE_FREEZE_20260812.json"
FALSIFIER = "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_D001_C001_INERT_FALSIFIER_FREEZE_20260812.json"
AUTHORIZATION = "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_C001_POSTMERGE_EVALUATION_AUTHORIZATION_20260812.json"
EVALUATOR_FREEZE = "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_D001_C001_EVALUATOR_IDENTITY_FREEZE_20260812.json"
RETROSPECTIVE_AUTHORIZATION = "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_C001_RETROSPECTIVE_REPRODUCTION_AUTHORIZATION_20260812.json"
EVALUATOR = ROOT / "research/real_math/millennium/yang_mills/05_oracles/ym_k1_d001_c001_two_stage_evaluator.py"

OUTPUTS = {
    "source_result": ROOT / "research/real_math/millennium/yang_mills/03_sources/YM-S1a2i_K1_D001_C001_STAGE_A_SOURCE_RESULT_20260812.json",
    "result": ROOT / "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_D001_C001_STAGE_A_RESULT_20260812.json",
    "lesson": ROOT / "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_D001_C001_STAGE_A_MATHEMATICAL_LESSON_20260812.json",
    "failure": ROOT / "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_D001_C001_STAGE_A_FAILURE_EXPERIENCE_LATTICE_DELTA_20260812.json",
    "review": ROOT / "research/real_math/millennium/yang_mills/08_reviews/YM-S1a2i_K1_D001_C001_STAGE_A_SAME_CONTEXT_REVIEW_20260812.json",
    "trace": ROOT / "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_C001_STAGE_A_RESULT_TRACE_20260812.json",
}


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical(value)).hexdigest()


def seal(value: dict[str, Any]) -> dict[str, Any]:
    value["artifact_hash"] = ""
    value["artifact_hash"] = sha(value)
    return value


def historical_binding(path: str, application_commit: str) -> dict[str, Any]:
    raw = (ROOT / path).read_bytes()
    blob = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", f"{application_commit}:{path}"],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    return {
        "path": path,
        "application_commit": application_commit,
        "git_blob": blob,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_sha256": sha(json.loads(raw)),
    }


def evaluator_module():
    spec = importlib.util.spec_from_file_location("ym_k1_d001_c001_two_stage_evaluator", EVALUATOR)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def evaluator_receipt() -> dict[str, Any]:
    m = evaluator_module()
    worlds = [
        (
            "WORLD-A-B-PASS-SEPARATE-CONSTANTS-EXACT-MARGIN",
            m.EvaluationWorld(m.StageADerivation.SEPARATE_CONSTANTS, True, True, m.StageBProof.EXACT_INTERVAL_MARGIN),
            "APPLICABLE_BRIDGE",
        ),
        (
            "WORLD-A-FAIL-CONFLATED-C-TRAP",
            m.EvaluationWorld(m.StageADerivation.CONFLATED_SOURCE_CONSTANT, False, False, m.StageBProof.NOT_ENTERED),
            "STRONGER_PREMISE_MISMATCH_A",
        ),
        (
            "WORLD-B-FAIL-FACTOR-TWO-TRAP",
            m.EvaluationWorld(m.StageADerivation.SEPARATE_CONSTANTS, True, True, m.StageBProof.FACTOR_TWO_ONLY),
            "FLOW_MARGIN_FAIL_B",
        ),
        (
            "WORLD-CANNOT-CHECK-UPSTREAM-CONSTANTS",
            m.EvaluationWorld(m.StageADerivation.INSUFFICIENT, None, False, m.StageBProof.NOT_ENTERED),
            "CANNOT_CHECK",
        ),
    ]
    rows = []
    for world_id, world, expected in worlds:
        observed = m.evaluate(world)
        rows.append(
            {
                "world_id": world_id,
                "expected_branch": expected,
                "observed_branch": observed.branch.value,
                "match": observed.branch.value == expected,
            }
        )
    return {
        "evaluator_id": "YM-S1a2i-K1-D001-C001-TWO-STAGE-EVALUATOR-v1",
        "path": str(EVALUATOR.relative_to(ROOT)),
        "raw_sha256": hashlib.sha256(EVALUATOR.read_bytes()).hexdigest(),
        "planted_world_results": rows,
        "all_planted_worlds_match": all(row["match"] for row in rows),
    }


def build_source_result() -> dict[str, Any]:
    return seal(
        {
            "schema_version": "1.0.0",
            "record_type": "YM_K1_D001_C001_STAGE_A_SOURCE_DERIVATION_RESULT",
            "atom_id": "YM-S1a2i-K1-D001",
            "candidate_id": CANDIDATE_ID,
            "result_base_sha": RESULT_BASE_SHA,
            "run_type": "RETROSPECTIVE_REPRODUCTION_NOT_PROSPECTIVE_DISCOVERY",
            "strict_rakl_discovery_chronology": False,
            "framework_sha": FRAMEWORK_SHA,
            "source_identity": {
                "author": "Jonathan J. Wilson",
                "zenodo_version_doi": "10.5281/zenodo.19393832",
                "zenodo_concept_doi": "10.5281/zenodo.19393831",
                "tex_sha256": SOURCE_TEX_SHA256,
                "pdf_sha256": SOURCE_PDF_SHA256,
                "authority": "PRIMARY_AUTHOR_OPEN_ARTIFACT_NOT_INDEPENDENT_PEER_REVIEW",
            },
            "audit_boundary": {
                "full_bound_tex_searched": True,
                "primary_passages_read_in_context": [
                    "TeX 7491-7566: symbolic two-step constants and an absolute contraction ball r",
                    "TeX 7653-7681: stable-manifold hypotheses and freely chosen r under separate variables",
                    "TeX 9551-9571: complete statement and proof of Lemma 40.3",
                    "TeX 9615-9643,9665-9680,9725-9750: Theorem 40.5 constants and graph ball",
                    "TeX 11588-11625,11674-11686: cumulant/extraction inputs and qualitative Lipschitz proof",
                    "TeX 12027-12040: separate multiscale quadratic contraction estimate",
                ],
                "search_terms": [
                    "lem:UVR3_irrelevant_contraction",
                    "C_K^{(0)}",
                    "sec:rg_two_steps_constants",
                    "sufficiently small ball",
                    "strict contraction factor",
                ],
            },
            "lemma_40_3_quantifier_audit": {
                "quantified_statement": (
                    "exists rho in (0,1), C>0, g_star>0 such that forall admitted k,g_k,K_k, "
                    "||KF_k(u_k,K_k)||_(k+1)<=rho||K_k||_k+C g_k^4 on ||K_k||_k<=C g_k^2"
                ),
                "exact_tex_lines": "9554-9571",
                "same_symbol_roles": {
                    "C_dom": "C in ||K_k||_k<=C g_k^2",
                    "C_force": "the same C in +C g_k^4",
                },
                "proof_content": [
                    "bounded extraction plus multilinear cumulant bounds are cited",
                    "rescaling is said to contribute a strict contraction factor",
                    "gluing is said to be quadratic and hence O(g_k^4) on the displayed C g_k^2 domain",
                    "scale-uniformity is attributed to scale-invariant norms and finite-range covariance bounds",
                ],
                "not_derived": [
                    "no formula or numerical bound for rho",
                    "no independently named C_dom and C_force",
                    "no inequality relating a later c_K to the displayed domain coefficient C",
                ],
            },
            "upstream_transfer_attempts": [
                {
                    "passage": "TeX 7510-7532",
                    "available_structure": "kappa_0 and A_0 are symbolically named for ||K_1||<=kappa_0||K_0||+A_0|c_0|^2, uniformly on an undefined D_0",
                    "broken_transfer": "the source does not identify |c_k|^2 with g_k^4, D_0 with ||K||<=C_dom g^2, or A with C_force in Lemma 40.3",
                },
                {
                    "passage": "TeX 7551-7566 and 7653-7681",
                    "available_structure": "an absolute ball radius r and smallness epsilon_* may be chosen so a sequence-space map contracts",
                    "broken_transfer": "no proof maps that absolute r-ball and its full-state norm to the later scale-dependent c_K g^2 graph ball or to Lemma 40.3's same-C statement",
                },
                {
                    "passage": "TeX 11588-11625 and 11674-11686",
                    "available_structure": "cumulants converge for a sufficiently small norm, with implicit constants C and C_n; the RG Lipschitz proof is qualitative",
                    "broken_transfer": "the convergence radius and forcing coefficient are not assembled into separately justified C_dom,C_force,rho",
                },
                {
                    "passage": "TeX 12027-12040",
                    "available_structure": "a different estimate ||K_(k+1)||<=A||K_k||^2+B exp(-cM^2/g^2) on ||K_k||<=epsilon_*",
                    "broken_transfer": "this additive tail estimate is not mapped to rho||K||+C_force g^4 on a C_dom g^2 domain and depends on an M chosen for fixed g",
                },
            ],
            "stage_a_derivation": {
                "separate_constant_derivation_status": "NOT_ESTABLISHED",
                "literal_source_binding": "C_dom=C_force=C",
                "rho_status": "EXISTENTIAL_WITH_0<rho<1_NOT_NUMERIC",
                "chosen_radius": "c_K=4*C_force/(1-rho)",
                "exact_symbolic_comparison": "c_K/C_dom=4/(1-rho)>4>1",
                "comparison_uses_no_numeric_constant_assignment": True,
                "classification": "STRONGER_PREMISE_MISMATCH_A",
                "stage_b_authorized_after_result": False,
            },
            "competing_mathematical_diagnoses": [
                {
                    "diagnosis": "NOTATION_OVERLOAD_HIDES_SEPARATE_COMPATIBLE_CONSTANTS",
                    "status": "UNSUPPORTED_BY_BOUND_SOURCE",
                    "reopen_falsifier": "Supply a derivation that names both roles and proves 4*C_force/(1-rho)<=C_dom.",
                },
                {
                    "diagnosis": "ADJUSTABLE_ABSOLUTE_BALL_OR_NORM_RESCALING_REPAIRS_DOMAIN",
                    "status": "NOT_MAPPED_TO_LEMMA_40_3_GRAPH_BALL",
                    "reopen_falsifier": "Prove that the r-ball contains every chosen-graph input with the exact estimate; a uniform scalar norm rescaling alone cannot work because it multiplies C_dom and C_force by the same factor and preserves their ratio.",
                },
                {
                    "diagnosis": "LATER_SOURCE_LEMMA_PROVES_THE_MISSING_COMPARISON",
                    "status": "NOT_FOUND_IN_FULL_BOUND_TEX_SEARCH",
                    "reopen_falsifier": "Bind an exact passage or stronger source version proving the compatibility inequality.",
                },
                {
                    "diagnosis": "SHRINKING_G_STAR_ALONE_REPAIRS_A_PROPORTIONAL_RADIUS_MISMATCH",
                    "status": "REFUTED_FOR_THE_DISPLAYED_C_DOM_G_SQUARED_DOMAIN",
                    "reason": "Both radii scale as g^2, so their coefficient ratio is independent of g_star.",
                },
            ],
            "bounded_conclusion": (
                "The Stage-A source audit is checkable in the literal quantified world exposed by Lemma 40.3: "
                "the same existential C is the admitted-radius coefficient and forcing coefficient.  The later minimum "
                "choice c_K=4C/(1-rho) lies strictly outside that displayed C g^2 domain for every 0<rho<1.  The "
                "upstream passages do not derive a separate compatible pair.  This blocks only the local K-coordinate "
                "bridge; it neither refutes Lemma 40.3 nor reaches the stable manifold or Yang-Mills mass gap."
            ),
            "authority": {
                "mathematical_credit": "SCOPED_SYMBOLIC_SOURCE_APPLICABILITY_FAILURE",
                "proof_authority": False,
                "independent_review": False,
                "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            },
            "artifact_hash": "",
        }
    )


def build_result(source_result: dict[str, Any]) -> dict[str, Any]:
    m = evaluator_module()
    target = m.evaluate(
        m.EvaluationWorld(
            m.StageADerivation.CONFLATED_SOURCE_CONSTANT,
            False,
            False,
            m.StageBProof.NOT_ENTERED,
        )
    )
    return seal(
        {
            "schema_version": "1.0.0",
            "record_type": "YM_K1_D001_C001_TWO_STAGE_SOURCE_BRIDGE_RESULT",
            "atom_id": "YM-S1a2i-K1-D001",
            "candidate_id": CANDIDATE_ID,
            "result_base_sha": RESULT_BASE_SHA,
            "run_type": "RETROSPECTIVE_REPRODUCTION_NOT_PROSPECTIVE_DISCOVERY",
            "strict_rakl_discovery_chronology": False,
            "framework_sha": FRAMEWORK_SHA,
            "frozen_identity_bindings": {
                "candidate": historical_binding(CANDIDATE, ORIGINAL_AUTHORIZATION_MERGE_SHA),
                "declarative_falsifier": historical_binding(FALSIFIER, ORIGINAL_AUTHORIZATION_MERGE_SHA),
                "original_authorization": historical_binding(AUTHORIZATION, ORIGINAL_AUTHORIZATION_MERGE_SHA),
                "evaluator_identity_freeze": historical_binding(EVALUATOR_FREEZE, EVALUATOR_IDENTITY_MERGE_SHA),
                "retrospective_authorization": historical_binding(RETROSPECTIVE_AUTHORIZATION, RETROSPECTIVE_AUTHORIZATION_MERGE_SHA),
            },
            "source_result": {
                "path": str(OUTPUTS["source_result"].relative_to(ROOT)),
                "artifact_hash": source_result["artifact_hash"],
            },
            "evaluator_receipt": evaluator_receipt(),
            "stage_a": {
                "status": target.stage_a_status,
                "source_derivation_status": "ONLY_LITERAL_CONFLATED_C_IS_JUSTIFIED",
                "literal_source_binding": "C_dom=C_force=C",
                "chosen_radius": "c_K=4*C/(1-rho)",
                "symbolic_ratio": "c_K/C_dom=4/(1-rho)>4>1",
                "numeric_constants_invented": False,
                "result_reason": target.reason,
            },
            "classified_branch": target.branch.value,
            "stage_b": {
                "entered": False,
                "reason": "Frozen branch precedence forbids Stage B after Stage-A failure.",
                "g_star_selected": False,
                "margin_result_accessed": False,
            },
            "result_scope": "Local applicability of the Section 40 K-coordinate one-step estimate to the chosen graph radius only.",
            "not_claimed": [
                "Lemma 40.3 is false",
                "no reformulation can repair the domain mismatch",
                "the full graph transform is refuted",
                "Yang-Mills existence or mass gap is proved or refuted",
                "same-context review is independent peer review",
            ],
            "authority": {
                "mathematical_result_credit": "SCOPED_STAGE_A_SOURCE_PREMISE_MISMATCH",
                "strict_rakl_discovery_authority": False,
                "retrospective_reproduction_only": True,
                "target_truth": False,
                "proof_authority": False,
                "independent_review": False,
                "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            },
            "artifact_hash": "",
        }
    )


def build_lesson(source_result: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    return seal(
        {
            "schema_version": "1.0.0",
            "record_type": "YM_K1_D001_C001_STAGE_A_SEVEN_FIELD_MATHEMATICAL_LESSON",
            "atom_id": "YM-S1a2i-K1-D001",
            "candidate_id": CANDIDATE_ID,
            "classification": "STRONGER_PREMISE_MISMATCH_A",
            "run_type": "RETROSPECTIVE_REPRODUCTION_NOT_PROSPECTIVE_DISCOVERY",
            "attempted_mathematical_implication": (
                "Derive source-faithful C_dom,C_force,rho for Wilson Lemma 40.3 and prove that the Theorem 40.5 "
                "choice c_K=4C_force/(1-rho) satisfies c_K<=C_dom, so the one-step contraction can legally be "
                "applied on the entire chosen K graph ball."
            ),
            "exact_mathematical_result_or_failure": (
                "The complete Lemma 40.3 proof provides only one existential C in both roles and no derivation "
                "of a separate compatible pair.  Under the literal source binding C_dom=C_force=C and 0<rho<1, "
                "c_K/C_dom=4/(1-rho)>4, so the chosen graph ball exceeds the displayed contraction domain."
            ),
            "supported_and_competing_mathematical_causes": {
                "supported": [
                    "same-symbol coupling of the domain radius and forcing coefficient",
                "absence of a source derivation connecting upstream absolute r/epsilon_* balls to the proportional C_dom g^2 ball",
                "shrinking g_star cannot change the ratio of two radii both proportional to g^2",
                    "uniform scalar norm rescaling preserves C_force/C_dom and therefore preserves the mismatch",
                ],
                "competing": [
                    "the notation suppresses two independently derived compatible constants",
                    "a rescaled norm or absolute small ball contains the chosen graph ball with the same contraction estimate",
                    "a later or stronger primary-source version supplies the missing comparison",
                ],
                "cause_status": "SUPPORTED_BOUNDED_SOURCE_APPLICABILITY_DIAGNOSIS_NOT_GLOBAL_IMPOSSIBILITY",
            },
            "scope": (
                "Only the Lemma 40.3/Theorem 40.5 K-coordinate domain inclusion in Wilson Zenodo version "
                "10.5281/zenodo.19393832.  Stage B, lambda, base inversion, the full stable manifold, continuum/OS "
                "construction and mass gap are excluded."
            ),
            "mathematical_falsifier": (
                "A source-faithful derivation of separate C_dom,C_force,rho together with "
                "4*C_force/(1-rho)<=C_dom, or a theorem proving the one-step estimate directly on every "
                "||K||<=c_K g^2 input for the chosen c_K, falsifies this diagnosis."
            ),
            "repair_or_next_discriminator": (
                "Do not enter Stage B.  Search a stronger source or reconstruct the one-step estimate with explicit "
                "domain bookkeeping; the cheapest repair must expose how the contraction domain changes when the "
                "forcing bound and norm normalization change, then re-run the frozen compatibility inequality."
            ),
            "proof_or_source_evidence": [
                str(OUTPUTS["source_result"].relative_to(ROOT)),
                source_result["artifact_hash"],
                str(OUTPUTS["result"].relative_to(ROOT)),
                result["artifact_hash"],
                "Wilson TeX 9554-9571,9615-9643,9725-9750",
                "Wilson upstream TeX 7491-7566,7653-7681,11588-11625,11674-11686,12027-12040",
            ],
            "framework_method_implication_proposal": {
                "status": "QUARANTINED_PROPOSAL_ONLY",
                "mathematical_research_lesson": (
                    "When transferring an estimate with existential constants, preserve co-witness structure and "
                    "same-symbol role coupling.  A later proof may not treat a domain constant and a forcing constant "
                    "as independently tunable unless the source derivation supplies a witness and compatibility map."
                ),
                "proposed_gate_question": (
                    "Are all constants used by the target theorem jointly witnessed under the source quantifiers, "
                    "and does the target's parameter choice remain inside the exact source domain?"
                ),
                "authority": "APPLICATION_LESSON_NOT_FRAMEWORK_PROMOTION",
            },
            "zero_mathematical_credit": [
                "Git/branch/PR state",
                "CI/tests",
                "schemas/hashes/chronology",
                "telemetry/repository growth",
                "file download mechanics",
            ],
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            "strict_rakl_discovery_chronology": False,
            "artifact_hash": "",
        }
    )


def build_failure(source_result: dict[str, Any], result: dict[str, Any], lesson: dict[str, Any]) -> dict[str, Any]:
    experience = seal(
        {
            "failure_id": "F-YM-K1-D001-C001-CONFLATED-CONSTANT-DOMAIN-MISMATCH",
            "atom_id": "YM-S1a2i-K1-D001",
            "candidate_id": CANDIDATE_ID,
            "context_packet_hash": "sha256:35b646d79a98d7255b0c2a9f60bfb582e1f8dbeaae3218f9c7225cd902b2aec0",
            "research_trace_event_id": "YM-S1a2i-K1-D001-C001-E09",
            "method_family": "source-scoped strict contraction on a shrinking O(g^2) graph radius",
            "failure_mode": "the target graph radius is chosen from the forcing role of a source constant but exceeds the same constant's admitted-domain role",
            "residual_signature": [
                "EXISTENTIAL_CONSTANT_CO_WITNESS_NOT_SEPARABLE",
                "C_DOM_EQUALS_C_FORCE_IN_DISPLAYED_SOURCE",
                "C_K_OVER_C_DOM_EQUALS_4_OVER_1_MINUS_RHO_GREATER_THAN_ONE",
                "STAGE_B_NOT_ENTERED",
            ],
            "broken_assumptions": [
                "one overloaded source symbol can be split into independently adjustable constants without a derivation",
                "shrinking g_star repairs a coefficient mismatch between two g^2-scaled radii",
                "qualitative upstream small-ball control automatically maps to the later proportional graph ball",
            ],
            "scope_conditions": [
                "Wilson Zenodo 10.5281/zenodo.19393832 at the bound PDF/TeX hashes",
                "only the Section 40 K-coordinate domain inclusion",
                "reusable warning rather than a blacklist if a future source supplies separate compatible witnesses",
            ],
            "competing_diagnoses": [
                "hidden compatible constants intended by notation",
                "absolute r-ball or norm rescaling supplies an unrecorded bridge",
                "later source theorem supplies domain containment",
            ],
            "selected_diagnosis": "SUPPORTED_CONFLATED_CONSTANT_DOMAIN_MISMATCH_IN_THE_DISPLAYED_SOURCE_STATEMENT",
            "diagnosis_status": "SUPPORTED",
            "evidence_pointers": [
                str(OUTPUTS["source_result"].relative_to(ROOT)),
                source_result["artifact_hash"],
                str(OUTPUTS["result"].relative_to(ROOT)),
                result["artifact_hash"],
                str(OUTPUTS["lesson"].relative_to(ROOT)),
                lesson["artifact_hash"],
            ],
            "falsifier_or_attempt": lesson["mathematical_falsifier"],
            "observed_result": lesson["exact_mathematical_result_or_failure"],
            "local_repair_attempts": [
                "read the complete lemma proof rather than only the display",
                "searched full bound TeX for separate constant derivations and later repairs",
                "tested the literal symbolic world without inventing numeric constants",
                "preserved alternate repair routes as reopen conditions",
            ],
            "timestamp": "2026-08-12T16:15:00Z",
            "artifact_hash": "",
        }
    )
    return {
        "schema_version": "1.0.0",
        "record_type": "NONCANONICAL_FAILURE_LINEAGE_PATCH_WITH_EMBEDDED_CANONICAL_DELTA",
        "canonical_contract_scope": "Only the experiences and links fields form the schema-valid canonical lattice delta; external lineage metadata is proposal-only.",
        "supersedes_external_failure_id": "F-YM-K1-D001-JOINT-DOMAIN-AND-FLOW-TRANSPORT-MISMATCH",
        "experiences": [experience],
        "links": [],
        "external_link_proposal": {
            "source_id": experience["failure_id"],
            "target_id": "F-YM-K1-D001-JOINT-DOMAIN-AND-FLOW-TRANSPORT-MISMATCH",
            "relation": "SUPERSEDES_DIAGNOSIS",
            "status": "NOT_REGISTERED_HERE_BECAUSE_CANONICAL_LINK_ENDPOINTS_MUST_BE_LOCAL",
            "rationale": "A later canonical combined lattice may register this relation after both experiences are present in one artifact.",
        },
        "artifact_hash": "",
    }


def build_review(source_result: dict[str, Any], result: dict[str, Any], lesson: dict[str, Any]) -> dict[str, Any]:
    return seal(
        {
            "schema_version": "1.0.0",
            "record_type": "ROLE_SEPARATED_SAME_CONTEXT_MATHEMATICAL_REVIEW",
            "atom_id": "YM-S1a2i-K1-D001",
            "candidate_id": CANDIDATE_ID,
            "review_independence": "SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW",
            "run_type": "RETROSPECTIVE_REPRODUCTION_NOT_PROSPECTIVE_DISCOVERY",
            "reviewed_artifacts": [
                {"path": str(OUTPUTS["source_result"].relative_to(ROOT)), "artifact_hash": source_result["artifact_hash"]},
                {"path": str(OUTPUTS["result"].relative_to(ROOT)), "artifact_hash": result["artifact_hash"]},
                {"path": str(OUTPUTS["lesson"].relative_to(ROOT)), "artifact_hash": lesson["artifact_hash"]},
            ],
            "role_reviews": [
                {
                    "role": "DOMAIN_THEORY_LEAD",
                    "verdict": "PASS_SCOPED",
                    "strongest_objection": "The existential Lemma 40.3 constant need not be a maximal domain radius, so the calculation cannot prove that every possible reformulation fails.",
                    "resolution": "The result is limited to non-applicability of the displayed same-C theorem to the later c_K ball; it makes no maximality or impossibility claim.",
                },
                {
                    "role": "ANALOGY_METHOD_TRANSFER_LEAD",
                    "verdict": "PASS_SCOPED",
                    "strongest_objection": "The earlier absolute r-ball might support a repaired derivation after shrinking g_star.",
                    "resolution": "That is preserved as a repair route, but the source never maps its variables, norm, and forcing term to Lemma 40.3 or proves containment of the later graph ball.",
                },
                {
                    "role": "ADVERSARIAL_FALSIFICATION_LEAD",
                    "verdict": "PASS",
                    "strongest_objection": "Could shrinking g_star or uniformly rescaling the K norm reverse the domain comparison?",
                    "resolution": "No: shrinking g_star cancels from two g^2 radii, while scalar norm rescaling multiplies both C_dom and C_force equally and leaves 4C_force/((1-rho)C_dom) invariant.",
                },
                {
                    "role": "FORMAL_METHODS_LEAD",
                    "verdict": "PASS_ELEMENTARY_SYMBOLIC",
                    "strongest_objection": "The result must not rely on unrecorded numeric constants.",
                    "resolution": "Only 0<rho<1 and the exact source co-witness C are used to prove 4/(1-rho)>4>1; no numeric assignment or Stage-B access occurs.",
                },
                {
                    "role": "NOVELTY_RESEARCH_VALUE_LEAD",
                    "verdict": "PASS_DIAGNOSTIC_VALUE_ONLY",
                    "strongest_objection": "A source audit is not new mathematics or a Yang-Mills result.",
                    "resolution": "No novelty is claimed; value is confined to local proof-obligation diagnosis and a reusable constant-role transfer warning.",
                },
            ],
            "disagreements": [
                "An absolute r-ball may enable a future repaired proof, but it does not repair the displayed Lemma 40.3 invocation without an explicit transfer derivation."
            ],
            "blocking_concerns": [],
            "verdict": "INTERNALLY_READY_FOR_SCOPED_STAGE_A_RESULT_PR",
            "next_action": "Merge the scoped failure result; do not enter Stage B. Reopen only on a stronger source or explicit one-step re-derivation.",
            "artifact_hash": "",
        }
    )


def trace_event(
    event_id: str,
    event_type: str,
    previous_event_hash: str,
    state_summary: str,
    action_summary: str,
    evidence_pointers: list[str],
    outputs: list[str],
    residuals: list[str],
    next_steps: list[str],
    timestamp: str,
) -> dict[str, Any]:
    return seal(
        {
            "event_id": event_id,
            "atom_id": "YM-S1a2i-K1-D001",
            "event_type": event_type,
            "timestamp": timestamp,
            "state_summary": state_summary,
            "action_summary": action_summary,
            "evidence_pointers": evidence_pointers,
            "alternatives_considered": [],
            "decision_rationale": "",
            "outputs": outputs,
            "uncertainties": [],
            "residuals": residuals,
            "next_steps": next_steps,
            "previous_event_hash": previous_event_hash,
            "artifact_hash": "",
        }
    )


def build_trace(
    source_result: dict[str, Any],
    result: dict[str, Any],
    lesson: dict[str, Any],
    failure: dict[str, Any],
    review: dict[str, Any],
) -> dict[str, Any]:
    e08 = trace_event(
        "YM-S1a2i-K1-D001-C001-E08",
        "FALSIFIER_RUN",
        "sha256:c71a13ac9370968d892ea60aa7b0e303a383a609d8cba100d584a895354ebada",
        "The retrospective authorization is active and the exact two-stage evaluator is bound; strict discovery chronology is irrecoverably false for this generation.",
        "Reproduce the four frozen planted worlds and Stage A from the bound public source without entering Stage B.",
        [str(EVALUATOR.relative_to(ROOT)), historical_binding(RETROSPECTIVE_AUTHORIZATION, RETROSPECTIVE_AUTHORIZATION_MERGE_SHA)["raw_sha256"]],
        ["FOUR_OF_FOUR_PLANTED_WORLDS_MATCH", source_result["artifact_hash"]],
        [],
        [],
        "2026-08-12T16:13:00Z",
    )
    e09 = trace_event(
        "YM-S1a2i-K1-D001-C001-E09",
        "RESULT_RECORDED",
        e08["artifact_hash"],
        "The literal source co-witness C serves both domain and forcing roles.",
        "Classify Stage A by the frozen symbolic compatibility predicate.",
        [str(OUTPUTS["source_result"].relative_to(ROOT)), source_result["artifact_hash"]],
        ["STRONGER_PREMISE_MISMATCH_A", result["artifact_hash"]],
        ["c_K/C_dom=4/(1-rho)>4>1", "Stage B is forbidden"],
        [],
        "2026-08-12T16:14:00Z",
    )
    e10 = trace_event(
        "YM-S1a2i-K1-D001-C001-E10",
        "RESIDUAL_OPENED",
        e09["artifact_hash"],
        "The displayed source route fails, but a stronger source or explicit re-derivation could still repair the local bridge.",
        "Record the seven-field mathematical lesson and conditional failure-memory warning.",
        [str(OUTPUTS["lesson"].relative_to(ROOT)), lesson["artifact_hash"]],
        [lesson["artifact_hash"], failure["experiences"][0]["artifact_hash"]],
        ["Need separately witnessed compatible constants or a direct chosen-ball contraction theorem"],
        ["Do not enter Stage B", "Reopen source/derivation search only on new mathematical evidence"],
        "2026-08-12T16:15:00Z",
    )
    e11 = trace_event(
        "YM-S1a2i-K1-D001-C001-E11",
        "REVIEWED",
        e10["artifact_hash"],
        "Five same-context mathematical roles reviewed the source quantifiers, transfer gap, symbolic falsifier, scope, and research value.",
        "Resolve the strongest objections without widening the claim or entering Stage B.",
        [str(OUTPUTS["review"].relative_to(ROOT)), review["artifact_hash"]],
        ["INTERNALLY_READY_FOR_SCOPED_STAGE_A_RESULT_PR", review["artifact_hash"]],
        [],
        ["Merge scoped Stage-A result", "Reopen only on new mathematical evidence"],
        "2026-08-12T16:16:00Z",
    )
    return seal(
        {
            "schema_version": "1.0.0",
            "record_type": "MATH_RESEARCH_TRACE_SUCCESSOR",
            "atom_id": "YM-S1a2i-K1-D001",
            "candidate_id": CANDIDATE_ID,
            "run_type": "RETROSPECTIVE_REPRODUCTION_NOT_PROSPECTIVE_DISCOVERY",
            "strict_rakl_discovery_chronology": False,
            "prior_local_non_strict_result_commit": "25c0271d6a0f379cad4dab3c2a4be56d732f5a00",
            "parent_trace_terminal_event_hash": "sha256:c71a13ac9370968d892ea60aa7b0e303a383a609d8cba100d584a895354ebada",
            "events": [e08, e09, e10, e11],
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            "artifact_hash": "",
        }
    )


def build_documents() -> dict[str, dict[str, Any]]:
    source_result = build_source_result()
    result = build_result(source_result)
    lesson = build_lesson(source_result, result)
    failure = build_failure(source_result, result, lesson)
    failure = seal(failure)
    review = build_review(source_result, result, lesson)
    trace = build_trace(source_result, result, lesson, failure, review)
    return {
        "source_result": source_result,
        "result": result,
        "lesson": lesson,
        "failure": failure,
        "review": review,
        "trace": trace,
    }


def write_documents() -> None:
    for key, value in build_documents().items():
        OUTPUTS[key].parent.mkdir(parents=True, exist_ok=True)
        OUTPUTS[key].write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    write_documents()
