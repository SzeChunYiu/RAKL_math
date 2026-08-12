from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[5]
YM = ROOT / "research/real_math/millennium/yang_mills"

APPLICATION_BASE_SHA = "334c3cf0a405906fe14b07067d6d7f73b6170d4f"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
ATOM = "YM-S1a2i-K1-D001"
PARENT_ATOM = "YM-S1a2i-K1"
HISTORICAL_CANDIDATE = "YM-S1a2i-K1-C001-SYMBOLIC-NEXT-RADIUS-MARGIN"
SOURCE_AUDIT = "research/real_math/millennium/yang_mills/03_sources/YM-S1a2i_K1_D001_WILSON_SOURCE_APPLICABILITY_AUDIT_20260812.json"
CONTEXT = "research/real_math/millennium/yang_mills/01_frontier/YM-S1a2i_K1_D001_CONTEXT_FIBER_20260812.json"
MEMORY = "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_D001_RESEARCH_MEMORY_REVIEW_20260812.json"
TRANSFORMATION_MEMORY = "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_D001_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json"
FAILURE = "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_D001_FAILURE_EXPERIENCE_20260812.json"
LESSON = "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_D001_MATHEMATICAL_LESSON_20260812.json"
EXPERT = "research/real_math/millennium/yang_mills/08_reviews/YM-S1a2i_K1_D001_EXPERT_CONTEXT_REVIEW_20260812.json"
SHORTCUT = "research/real_math/millennium/yang_mills/08_reviews/YM-S1a2i_K1_D001_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json"
TRACE = "research/real_math/millennium/yang_mills/09_trace/YM-S1a2i_K1_D001_PRE_CANDIDATE_TRACE_20260812.json"

PATHS = {
    "source_audit": ROOT / SOURCE_AUDIT,
    "context": ROOT / CONTEXT,
    "failure": ROOT / FAILURE,
    "lesson": ROOT / LESSON,
    "memory": ROOT / MEMORY,
    "transformation_memory": ROOT / TRANSFORMATION_MEMORY,
    "expert_review": ROOT / EXPERT,
    "shortcut_review": ROOT / SHORTCUT,
    "trace": ROOT / TRACE,
}


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def _sha(value: Any, *, prefix: bool = True) -> str:
    digest = hashlib.sha256(_canonical(value)).hexdigest()
    return f"sha256:{digest}" if prefix else digest


def _seal(document: dict[str, Any], field: str = "artifact_hash") -> dict[str, Any]:
    value = dict(document)
    value[field] = ""
    value[field] = _sha(value)
    return value


def build_source_audit() -> dict[str, Any]:
    passages = [
        {
            "passage_id": "WILSON-40.1-BETA",
            "pdf_pages": [141],
            "pdf_equations": ["(566)", "(567)"],
            "tex_lines": [9279, 9291],
            "exact_scope": "Theorem 40.1 states g_{k+1}=g_k-b_0 g_k^3+r_k, b_0>0, |r_k|<=C_beta g_k^5, with all constants uniform in volume.",
            "mathematical_use": "Supplies the beta-flow form and volume uniformity; k-uniformity is supplied explicitly by Lemma 40.4 below.",
        },
        {
            "passage_id": "WILSON-40.3-K-CONTRACTION",
            "pdf_pages": [145, 146],
            "pdf_equations": ["(579)"],
            "tex_lines": [9554, 9571],
            "exact_scope": "Lemma 40.3 states the k-to-k+1 estimate only for 0<g_k<=g_star and ||K_k||_k<=C g_k^2: ||KF_k(u_k,K_k)||_{k+1}<=rho||K_k||_k+C g_k^4. It states local Lipschitz constants are bounded uniformly in k on this domain, and the proof attributes k-uniformity to scale-invariant norms and finite-range bounds on C_k.",
            "mathematical_use": "Exposes genuine scale transport and nominal k-uniformity, but the displayed C simultaneously denotes the admissible radius and forcing coefficient.",
        },
        {
            "passage_id": "WILSON-40.4-UNIFORM-RELEVANT-UPDATE",
            "pdf_pages": [146],
            "pdf_equations": ["(580)", "(581)"],
            "tex_lines": [9573, 9584],
            "exact_scope": "Lemma 40.4 repeats the beta flow and states its update constants are uniform in k on the same small domain.",
            "mathematical_use": "Binds b_0 and C_beta into the k-uniform one-step packet, subject to the stated domain.",
        },
        {
            "passage_id": "WILSON-40.5-GRAPH-DOMAIN-AND-CONSTANT-CHOICE",
            "pdf_pages": [146, 147, 148],
            "pdf_equations": ["(582)", "(583)", "(584)", "(585)"],
            "tex_lines": [9595, 9662],
            "exact_scope": "Theorem 40.5 defines D_k using ||K||_k<=c_K g^2, fixes rho,C_K^(0),C_beta from Lemmas 40.3-40.4, requires c_K>=4 C_K^(0)/(1-rho), and says these choices are independent of k and volume. Equation (585) uses the same scale-indexed norms in the graph space.",
            "mathematical_use": "Binds nominal c_K uniformity and exact graph-ball notation, but does not prove that the Lemma 40.3 domain contains this chosen graph ball.",
        },
        {
            "passage_id": "WILSON-40.5-FACTOR-TWO-TRANSPORT",
            "pdf_pages": [147],
            "pdf_equations": ["(586)"],
            "tex_lines": [9665, 9680],
            "exact_scope": "The proof obtains ||K_{k+1}||_{k+1}<=((1+rho)/2)c_K g_k^2, proves only g_k^2<=2g_{k+1}^2, and then asserts ||K_{k+1}||_{k+1}<=c_K g_{k+1}^2.",
            "mathematical_use": "The two displayed inequalities compose only to (1+rho)c_K g_{k+1}^2; because rho>0, they do not imply equation (586).",
        },
        {
            "passage_id": "WILSON-40.5-EXPLICIT-CK",
            "pdf_pages": [148],
            "pdf_equations": ["post-(587) parameter assignment"],
            "tex_lines": [9725, 9750],
            "exact_scope": "The proof explicitly chooses c_K=4 C_K^(0)/(1-rho) and says C_K^(0) and rho are determined in Lemma 40.3.",
            "mathematical_use": "Makes the missing comparison between the chosen c_K and Lemma 40.3's admissible radius load-bearing.",
        },
        {
            "passage_id": "WILSON-A.15-POLYMER-NORM",
            "pdf_pages": [172],
            "pdf_equations": ["Definition A.15.3"],
            "tex_lines": [11481, 11499],
            "exact_scope": "Defines scale-k polymer activities and ||K_k||_k as a supremum over scale-k polymers with e^{mu|X|_k}, field-domain and derivative weights ell_k^{|alpha|+4}.",
            "mathematical_use": "Confirms that the displayed one-step estimate genuinely transports from the k norm to the k+1 norm used by the graph ball.",
        },
    ]
    return _seal(
        {
            "record_type": "YM_K1_D001_PRIMARY_AUTHOR_SOURCE_APPLICABILITY_AUDIT",
            "atom_id": ATOM,
            "parent_atom_id": PARENT_ATOM,
            "application_base_sha": APPLICATION_BASE_SHA,
            "framework_sha": FRAMEWORK_SHA,
            "source_identity": {
                "author": "Jonathan J. Wilson",
                "title": "RIGOROUS CONSTRUCTION OF FOUR-DIMENSIONAL YANG–MILLS QUANTUM FIELD THEORY VIA GRIBOV–ZWANZIGER QUANTIZATION AND RENORMALIZATION GROUP ANALYSIS: MEASURE-THEORETIC FOUNDATIONS, SPECTRAL PROPERTIES, AND THE MASS GAP",
                "publication_date": "2026-04-03",
                "zenodo_version_doi": "10.5281/zenodo.19393832",
                "zenodo_concept_doi": "10.5281/zenodo.19393831",
                "zenodo_record_id": "19393832",
                "record_api": "https://zenodo.org/api/records/19393832",
                "authority": "PRIMARY_AUTHOR_OPEN_ARTIFACT_NOT_INDEPENDENT_PEER_REVIEW",
            },
            "source_files": [
                {
                    "filename": "4D GZ-Yang-Mills.pdf",
                    "download_url": "https://zenodo.org/api/records/19393832/files/4D%20GZ-Yang-Mills.pdf/content",
                    "bytes": 1861857,
                    "sha256": "08013e1ce75c8b2be79c62ba61f70e30024b9bb427c465ceab7ee9266236690d",
                },
                {
                    "filename": "GZYM_submission_final.tex",
                    "download_url": "https://zenodo.org/api/records/19393832/files/GZYM_submission_final.tex/content",
                    "bytes": 787459,
                    "sha256": "ef936e502e84b0cafabc594c9705c16c9c1df29dc95f2a6a679b6b446c526c18",
                },
            ],
            "passage_bindings": passages,
            "uniformity_assessment": {
                "rho": "NAMED_K_UNIFORM_ON_LEMMA_40_3_STATED_DOMAIN",
                "C_force": "NAMED_K_UNIFORM_ON_LEMMA_40_3_STATED_DOMAIN_BUT_NOT_SEPARATED_FROM_DOMAIN_RADIUS_IN_THE_DISPLAYED_STATEMENT",
                "b_0": "NAMED_POSITIVE_FLOW_COEFFICIENT_IN_THEOREM_40_1_AND_LEMMA_40_4",
                "C_beta": "NAMED_K_UNIFORM_REMAINDER_CONSTANT_IN_LEMMA_40_4",
                "c_K": "CHOSEN_INDEPENDENT_OF_K_AND_VOLUME_IN_THEOREM_40_5",
                "norm_transport": "EXPLICIT_K_TO_K_PLUS_1_SCALE_INDEXED_NORM",
                "joint_exact_graph_ball_applicability": "NOT_ESTABLISHED",
            },
            "supported_gaps": [
                {
                    "gap_id": "A-DOMAIN-RADIUS-COMPATIBILITY",
                    "observation": "Lemma 40.3 proves its estimate only on ||K||_k<=C_dom g^2. Theorem 40.5 chooses c_K>=4C_force/(1-rho), but supplies no proof that c_K<=C_dom and no theorem allowing an arbitrary prescribed c_K after shrinking g_star.",
                    "no_reinterpretation_rule": "The displayed Lemma 40.3 uses one symbol C for domain radius and forcing. This audit does not reinterpret that C as two independently adjustable constants; a future upstream proof audit must derive and name C_dom and C_force separately.",
                    "displayed_same_C_consequence": "If the displayed C is used for both roles, the minimum later choice is c_K=4C/(1-rho)>C because 0<rho<1, so the later graph ball is outside the stated Lemma 40.3 domain.",
                    "falsifier": "A source theorem or derivation proving c_K<=C_dom, or proving the one-step contraction on every ||K||_k<=c_K g^2 for the chosen c_K, falsifies this diagnosis.",
                },
                {
                    "gap_id": "B-FACTOR-TWO-FLOW-COMPARISON",
                    "observation": "Theorem 40.5 combines an upper bound ((1+rho)/2)c_K g_k^2 with only g_k^2<=2g_{k+1}^2. These imply at best (1+rho)c_K g_{k+1}^2, not c_K g_{k+1}^2.",
                    "falsifier": "A proved ratio g_k^2/g_{k+1}^2<=2/(1+rho), or the exact lower-flow scalar margin L(g)^2>=rho+(C_force/c_K)g^2 on the frozen interval, falsifies this diagnosis.",
                },
            ],
            "classification": "STRONGER_PREMISE_MISMATCH",
            "supersession": {
                "prior_failure_id": "F-YM-K1-C001-SOURCE-UNIFORMITY-NORM-BRIDGE-UNBOUND",
                "prior_source_exposure_diagnosis": "SUPERSEDED_BY_OPEN_PRIMARY_SOURCE",
                "preserved_residual": "Exact joint applicability of the one-step estimate to the chosen graph ball remains unproved, now for two source-bound mathematical reasons rather than source inaccessibility.",
            },
            "cheapest_future_discriminator": {
                "stage_1": "Audit the upstream proof of Lemma 40.3 without changing its meaning and derive separately justified C_dom and C_force.",
                "stage_1_test": "4*C_force/(1-rho) <= C_dom",
                "stage_2_only_if_stage_1_passes": "On a separately frozen coupling interval, test L(g)^2>=rho+(C_force/c_K)g^2 with L(g)=1-b_0 g^2-C_beta g^4 and L(g)>=0.",
                "not_executed_here": True,
            },
            "bounded_conclusion": "The primary source now exposes nominal k-uniform constants and exact k-to-k+1 norm notation, so source exposure is no longer the gap. The source passages audited here do not establish their joint applicability over the chosen c_K g^2 graph ball, and the displayed factor-two comparison does not establish the next-radius inequality. This is neither a refutation of the scalar lemma nor a proof or refutation of Yang-Mills mass gap.",
            "future_candidate_identity": None,
            "candidate_generation_allowed": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            "audited_at_utc": "2026-08-12T15:00:00Z",
            "artifact_hash": "",
        }
    )


def build_context(source_audit: dict[str, Any]) -> dict[str, Any]:
    return _seal(
        {
            "atom_id": ATOM,
            "object_context": "Diagnose whether Wilson's source-uniform one-step K estimate is jointly applicable on the exact c_K g^2 graph ball and whether its displayed flow comparison proves transport to c_K g_{k+1}^2; do not generate a new proof candidate.",
            "structural_coordinates": [
                "Lemma-domain radius C_dom for ||K_k||_k<=C_dom g_k^2",
                "forcing coefficient C_force in rho||K_k||_k+C_force g_k^4",
                "strict contraction 0<rho<1",
                "chosen graph radius c_K>=4C_force/(1-rho)",
                "scale-indexed transport from ||.||_k to ||.||_{k+1}",
                "base lower factor L(g)=1-b_0g^2-C_beta g^4",
                "joint applicability must hold uniformly in k before scalar composition",
                "root status OPEN_NO_SOLUTION_CERTIFICATE",
            ],
            "equivalent_formulations": [
                "Domain inclusion form: require c_K<=C_dom before applying Lemma 40.3 on the full graph ball.",
                "Minimum-radius compatibility form: require 4C_force/(1-rho)<=C_dom for the source's explicit minimum c_K choice.",
                "Exact transport form: require L(g)^2>=rho+(C_force/c_K)g^2 after domain compatibility is established.",
                "Failure-of-displayed-comparison form: ((1+rho)/2)*2=1+rho>1 does not close the next-radius bound.",
            ],
            "solved_analogues": [
                "The prior C001 abstract scalar lemma closes a shrinking O(g^2) radius for a fixed admissible constant family when its estimate is valid on the whole input ball.",
            ],
            "near_solved_analogues": [
                "Wilson Lemma 40.3 and Theorem 40.5 expose the needed scale transport and constants but leave domain-radius compatibility and the exact flow-ratio margin unproved in the cited passage chain.",
            ],
            "method_transfers": [
                {
                    "source_context": "Prior C001 abstract shrinking-radius scalar lemma",
                    "method": "First verify the source estimate on the entire proposed input ball; only then compare the contracted-plus-forced coefficient with a rigorous lower bound for the next radius.",
                    "shared_structure": [
                        "strict contraction rho",
                        "higher-order forcing C_force g^4",
                        "O(g^2) input and target radii",
                        "base-flow lower factor L(g)",
                    ],
                    "required_assumptions": [
                        "C_dom and C_force are separately justified without reinterpreting a source symbol",
                        "c_K<=C_dom",
                        "all constants apply jointly and uniformly in k",
                        "L(g)>=0 and L(g)^2>=rho+(C_force/c_K)g^2 on a frozen interval",
                    ],
                    "disanalogies": [
                        "the abstract lemma begins with an estimate already valid on the full ball, while the source statement does not show that inclusion",
                        "the source proof uses a factor-two comparison rather than the exact scalar margin",
                    ],
                    "repair_question": "Does an upstream derivation produce separately justified C_dom,C_force satisfying 4C_force/(1-rho)<=C_dom before any scalar-margin candidate is frozen?",
                    "source_anchors": [SOURCE_AUDIT, "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_C001_RESULT_20260812.json"],
                }
            ],
            "explicit_disanalogies": [
                "A source statement verified to exist is not thereby mathematically applicable to a larger domain.",
                "Nominal uniformity of each symbol is not joint uniform applicability on the exact graph ball.",
                "A locally valid K-coordinate repair would not establish lambda closure, a stable manifold, continuum construction or mass gap.",
                "This pre-candidate source audit does not assign values to C_dom or C_force and does not execute the scalar lemma.",
            ],
            "source_anchors": [SOURCE_AUDIT, source_audit["artifact_hash"], "10.5281/zenodo.19393832", "10.5281/zenodo.19393831", "RAKL_math@" + APPLICATION_BASE_SHA, "RAKL@" + FRAMEWORK_SHA],
            "analogy_scan_status": "BRIDGES_RETAINED",
            "cross_domain_analogies": [
                {
                    "source_kind": "capacity-control contract",
                    "source_situation": "A controller guarantee is certified only up to an input capacity C_dom, while a downstream planner chooses a larger operating capacity from a separate disturbance budget.",
                    "common_abstraction": ["local guarantee domain", "downstream chosen operating radius", "disturbance-versus-slack budget"],
                    "source_to_target_mapping": ["certified capacity -> C_dom g^2", "planned capacity -> c_K g^2", "disturbance budget -> C_force g^4", "compression -> rho"],
                    "shared_constraints": ["the operating set must lie inside the certified set before the guarantee can be invoked", "a later shrink factor must be compared quantitatively rather than by monotonicity direction alone"],
                    "disanalogies": ["ordinary capacity has no scale-indexed Banach norm", "the analogy supplies no theorem or source authority"],
                    "proposed_principle": "Check domain inclusion before spending contraction slack; then compare the exact multiplicative margins.",
                    "validation_obligation": "Derive source-faithful C_dom,C_force and test 4C_force/(1-rho)<=C_dom; only after a pass, freeze and test the exact L(g)^2 margin.",
                    "provenance_note": "Proposal-only analogy; it does not validate either inequality.",
                }
            ],
            "analogy_scan_notes": "The retained bridge contributes only the domain-inclusion ordering rule; no analogy is treated as mathematical evidence.",
            "frozen_at": "2026-08-12T15:10:00+00:00",
            "first_candidate_at": None,
            "packet_hash": "",
        },
        field="packet_hash",
    )


def build_failure_lattice(context: dict[str, Any], source_audit: dict[str, Any]) -> dict[str, Any]:
    prior_path = YM / "07_memory/YM-S1a2i_K1_C001_FAILURE_EXPERIENCE_20260812.json"
    prior = json.loads(prior_path.read_text())["experiences"][0]
    current = _seal(
        {
            "failure_id": "F-YM-K1-D001-JOINT-DOMAIN-AND-FLOW-TRANSPORT-MISMATCH",
            "atom_id": ATOM,
            "candidate_id": HISTORICAL_CANDIDATE,
            "context_packet_hash": context["packet_hash"],
            "research_trace_event_id": "YM-S1a2i-K1-D001-E00",
            "method_family": "source-scoped strict-contraction margin on a shrinking O(g^2) K graph radius",
            "failure_mode": "The primary source exposes the nominal uniform constants and scale-indexed norm transport, but does not establish contraction on the later chosen graph ball and its displayed factor-two comparison does not prove the next-radius inequality.",
            "residual_signature": [
                "SOURCE_EXPOSURE_GAP_SUPERSEDED",
                "C_DOM_VS_C_FORCE_C_K_JOINT_APPLICABILITY_UNPROVED",
                "FACTOR_TWO_FLOW_COMPARISON_INSUFFICIENT",
                "SCALAR_MARGIN_NOT_EXECUTED_PENDING_DOMAIN_COMPATIBILITY",
                "NO_MASS_GAP_AUTHORITY",
            ],
            "broken_assumptions": [
                "naming k-uniform constants separately suffices to prove they apply jointly on the chosen c_K graph ball",
                "a contraction lemma stated on C_dom g^2 can be invoked on c_K g^2 without proving c_K<=C_dom",
                "the bounds ((1+rho)/2)c_K g_k^2 and g_k^2<=2g_{k+1}^2 imply coefficient one at scale k+1",
            ],
            "scope_conditions": [
                "Wilson Zenodo version DOI 10.5281/zenodo.19393832 with the pinned PDF and TeX hashes",
                "only the Section 40 K-coordinate invariant-region passage chain and Appendix A.15 norm definition",
                "historical candidate identity is referenced only for lineage; no successor candidate is frozen",
                "no claim about lambda, full stable manifold, continuum limit or mass gap",
            ],
            "competing_diagnoses": [
                "the earlier issue was only source inaccessibility",
                "the source's upstream Lemma 40.3 proof contains separately controlled constants satisfying the needed compatibility",
                "a sharper base-flow ratio closes the factor-two step after domain compatibility",
                "the whole stable-manifold or mass-gap claim is refuted",
            ],
            "selected_diagnosis": "SUPPORTED_STRONGER_PREMISE_MISMATCH: source exposure is repaired, but exact graph-ball domain compatibility and the displayed flow comparison remain unproved; root-level refutation is unsupported.",
            "diagnosis_status": "SUPPORTED",
            "evidence_pointers": [SOURCE_AUDIT, source_audit["artifact_hash"], CONTEXT, "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_C001_FAILURE_EXPERIENCE_20260812.json"],
            "falsifier_or_attempt": "Gap A is falsified by a source-faithful proof of c_K<=C_dom or contraction on the chosen c_K ball. Gap B is falsified by a proved ratio g_k^2/g_{k+1}^2<=2/(1+rho), or by the exact L(g)^2 scalar margin after Gap A passes.",
            "observed_result": "Exact primary-source passages show nominal k-uniformity and k-to-k+1 norm transport, superseding the source-exposure diagnosis. They also show two supported local gaps: unproved C_dom/C_force/c_K compatibility and an insufficient factor-two flow comparison. Classification is STRONGER_PREMISE_MISMATCH, not refutation.",
            "local_repair_attempts": [
                "bound exact source version, file hashes, pages, equations and TeX lines",
                "separated source-domain radius from forcing coefficient conceptually without reinterpreting the source constant",
                "computed only the logical consequence of the source's displayed factor-two bounds",
                "froze the cheapest future discriminator without evaluating it",
            ],
            "timestamp": "2026-08-12T15:11:00Z",
            "artifact_hash": "",
        }
    )
    return {
        "experiences": [prior, current],
        "links": [
            {
                "source_id": current["failure_id"],
                "target_id": prior["failure_id"],
                "relation": "SUPERSEDES_DIAGNOSIS",
                "rationale": "The open Zenodo primary-author source contradicts the bounded source-exposure diagnosis while preserving a narrower applicability residual with two exact mathematical gaps.",
                "evidence_pointers": [SOURCE_AUDIT, source_audit["artifact_hash"]],
            }
        ],
    }


def build_memory(context: dict[str, Any], failure_lattice: dict[str, Any]) -> dict[str, Any]:
    tool_path = YM / "07_memory/YM-S1A1_RESEARCH_TOOL_INVENTORY_20260811.json"
    tool_hash = _sha(json.loads(tool_path.read_text()))
    return _seal(
        {
            "target_atom_id": ATOM,
            "target_context_hash": context["packet_hash"],
            "tool_inventory_snapshot_hash": tool_hash,
            "failure_lattice_snapshot_hash": _sha(failure_lattice),
            "tool_query_status": "NO_RELEVANT_MATCH",
            "failure_query_status": "MATCHES_FOUND",
            "candidate_method_families": ["source-domain compatibility audit", "strict-contraction scalar margin after source compatibility", "stable-coordinate invariant-region transport"],
            "relevant_tool_ids": [],
            "relevant_failure_ids": ["F-YM-K1-C001-SOURCE-UNIFORMITY-NORM-BRIDGE-UNBOUND", "F-YM-K1-D001-JOINT-DOMAIN-AND-FLOW-TRANSPORT-MISMATCH"],
            "selected_tool_ids": [],
            "tool_applicability_notes": ["No promoted research tool derives Wilson's C_dom and C_force separately or proves that the chosen c_K ball lies inside Lemma 40.3's domain."],
            "failure_reuse_notes": [
                "The prior source-exposure warning is superseded because the Zenodo PDF and TeX are now directly bound.",
                "DifferenceWitness: source visibility changed, but the load-bearing applicability precondition did not become proved merely because the symbols are visible.",
                "The prior abstract scalar lemma remains locally relevant only after the new domain compatibility discriminator passes.",
                "Cheapest repeat-failure test: derive C_dom,C_force from the upstream proof and check 4C_force/(1-rho)<=C_dom before any scalar execution.",
            ],
            "unresolved_warnings": ["Do not reinterpret the source's single C as two adjustable constants.", "Do not compose the abstract scalar lemma before graph-ball domain inclusion is established.", "No local K-coordinate audit licenses a stable-manifold or mass-gap conclusion."],
            "evidence_pointers": [SOURCE_AUDIT, FAILURE, "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_C001_RESULT_20260812.json", "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_C001_FAILURE_EXPERIENCE_20260812.json", "research/real_math/millennium/yang_mills/07_memory/YM-S1A1_RESEARCH_TOOL_INVENTORY_20260811.json"],
            "artifact_hash": "",
            "cross_problem_coverage_receipt_hash": "",
        }
    )


def _obstruction() -> dict[str, Any]:
    return {
        "obstruction_id": "OBS-YM-K1-D001-JOINT-APPLICABILITY",
        "domain": "Yang-Mills polymer RG source applicability",
        "roles": ["Lemma 40.3 admissible K ball", "Lemma 40.3 forcing term", "Theorem 40.5 chosen graph ball", "beta-flow lower factor", "next-scale graph radius"],
        "relations": ["the one-step contraction may be invoked only inside its proved domain", "the contracted-plus-forced upper bound must not exceed the next-scale lower radius"],
        "constraints": ["0<rho<1", "uniformity in k", "exact ||.||_k to ||.||_{k+1} transport", "no reinterpretation of source constants", "future thresholds frozen before evaluation"],
        "failure_mechanisms": ["chosen c_K ball may exceed C_dom ball", "factor-two comparison leaves coefficient 1+rho rather than one"],
        "invariants_to_preserve": ["source theorem quantifiers", "scale-indexed norm scope", "historical candidate chronology", "open root status"],
        "desired_transition": ["establish or reject domain-radius compatibility", "only after compatibility, establish or reject exact scalar flow margin"],
        "forbidden_losses": ["shrinking the graph ball after outcome access", "inventing separate constants without derivation", "claiming mass gap authority"],
    }


def build_transformation_memory(source_audit: dict[str, Any]) -> dict[str, Any]:
    obs = {
        "obstruction_id": "OBS-ABSTRACT-SHRINKING-RADIUS",
        "domain": "elementary invariant-region analysis",
        "roles": ["contracted state", "higher-order forcing", "shrinking target radius"],
        "relations": ["upper state bound must be no larger than target lower radius"],
        "constraints": ["estimate valid on full input ball", "fixed finite constants", "nonnegative lower flow factor"],
        "failure_mechanisms": ["domain exclusion", "insufficient multiplicative margin"],
        "invariants_to_preserve": ["quantifier order", "constant identity", "input domain"],
        "desired_transition": ["replace qualitative monotonicity with exact scalar comparison"],
        "forbidden_losses": ["post-result radius change", "assumption invention"],
    }
    episode = _seal(
        {
            "episode_id": "EP-YM-K1-C001-ABSTRACT-SCALAR-MARGIN",
            "source_domain": "elementary invariant-region analysis",
            "source_context": "Historical C001 abstract scalar implication for one fixed admissible constant family",
            "source_obstruction": obs,
            "transformation_name": "exact lower-radius scalar comparison",
            "operation": "Given an estimate valid on the whole input ball, compare rho+(C_force/c_K)g^2 directly with L(g)^2 instead of relying on monotonicity direction.",
            "preconditions": ["the one-step estimate is proved on the full c_K g^2 input ball", "rho,c_K,C_force,b_0,C_beta are one jointly applicable k-uniform family", "L(g)>=0 on a frozen interval"],
            "resulting_relations": ["a verified scalar margin implies the K upper bound fits the next lower radius"],
            "preserved_invariants": ["k-to-k+1 norm transport", "source constants", "graph radius"],
            "relaxed_or_broken_constraints": ["qualitative old-radius comparison is replaced by an exact coefficient inequality"],
            "known_breakpoints": ["c_K>C_dom", "constants not jointly uniform", "scalar margin not frozen or checked"],
            "evidence_pointers": ["research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_C001_RESULT_20260812.json", SOURCE_AUDIT, source_audit["artifact_hash"]],
            "authority": "VERIFIED_LOCAL",
            "artifact_hash": "",
            "lineage_ids": [HISTORICAL_CANDIDATE],
        }
    )
    out = {
        "memory_id": "OTM-YM-S1a2i-K1-D001-20260812",
        "source_universe": ["historical C001 abstract result on RAKL_math main", "Wilson Zenodo version DOI 10.5281/zenodo.19393832", "current K1 failure lattice"],
        "episodes": [episode],
        "evidence_pointers": [SOURCE_AUDIT, "research/real_math/millennium/yang_mills/05_oracles/YM-S1a2i_K1_C001_RESULT_20260812.json", FAILURE],
        "snapshot_hash": "",
    }
    return _seal(out, field="snapshot_hash")


def build_expert_review(context: dict[str, Any], source_audit: dict[str, Any]) -> dict[str, Any]:
    return _seal(
        {
            "record_type": "YM_K1_D001_ROLE_SEPARATED_SAME_CONTEXT_EXPERT_REVIEW",
            "review_id": "REVIEW-YM-S1a2i-K1-D001-20260812",
            "atom_id": ATOM,
            "target_context_hash": context["packet_hash"],
            "review_independence": "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW",
            "roles": [
                {"role": "domain_theory_lead", "finding": "Wilson Lemmas 40.3-40.4 expose scale-indexed transport and nominal k-uniform constants, but Lemma 40.3's admitted K radius is not shown to contain Theorem 40.5's chosen c_K graph ball.", "strongest_objection": "The same symbol C is used for domain radius and forcing in the lemma, while the later minimum c_K=4C/(1-rho) is strictly larger than C; splitting the symbol post hoc is not allowed."},
                {"role": "analogy_method_transfer_lead", "finding": "The prior abstract scalar-margin method transfers only conditionally.", "strongest_objection": "Its enabling precondition is estimate validity on the whole input ball; that is exactly the unresolved source premise, so the method cannot yet be composed."},
                {"role": "adversarial_falsification_lead", "finding": "The displayed factor-two step is arithmetically insufficient: ((1+rho)/2)*2=1+rho>1.", "strongest_objection": "Any closure argument must replace the coarse factor two by a sharp enough ratio or the exact L(g)^2 margin."},
                {"role": "formal_methods_lead", "finding": "The exact proof obligations are domain inclusion c_K<=C_dom followed by L(g)^2>=rho+(C_force/c_K)g^2 with L(g)>=0.", "strongest_objection": "Neither obligation may be marked discharged by naming constants, a big-O statement, or a source theorem label."},
                {"role": "novelty_research_value_lead", "finding": "The retained value is a precise source-applicability diagnosis and cheapest discriminator, not a new Yang-Mills theorem.", "strongest_objection": "No source audit of one K-coordinate passage can support novelty, stable-manifold closure, continuum construction or mass-gap authority."},
            ],
            "disagreements": ["The source text calls the Section 40 treatment fully closed, while the passage-level implication audit finds two local obligations not discharged by the displayed inequalities."],
            "strongest_overall_objection": "Even perfect scalar algebra is inapplicable until the source one-step estimate is proved on the selected graph ball; after that, the factor-two comparison still needs a sharper scalar margin.",
            "unresolved_uncertainties": ["The upstream proof may contain separately controllable C_dom and C_force, but the audited passage chain does not expose their compatibility.", "A later source version or independent derivation may repair either local gap."],
            "classification": "STRONGER_PREMISE_MISMATCH",
            "recommendation": "Block candidate generation. Audit Lemma 40.3 upstream constants and test 4C_force/(1-rho)<=C_dom; only on a pass should a later, separately frozen scalar-margin evaluation occur.",
            "evidence_pointers": [SOURCE_AUDIT, source_audit["artifact_hash"], CONTEXT],
            "future_candidate_identity": None,
            "candidate_generation_allowed": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            "reviewed_at_utc": "2026-08-12T15:14:00Z",
            "artifact_hash": "",
        }
    )


def build_shortcut(context: dict[str, Any], memory: dict[str, Any], tm: dict[str, Any], source_audit: dict[str, Any]) -> dict[str, Any]:
    witness = _seal(
        {
            "witness_id": "MAP-YM-K1-D001-ABSTRACT-MARGIN",
            "episode_id": "EP-YM-K1-C001-ABSTRACT-SCALAR-MARGIN",
            "target_obstruction_id": _obstruction()["obstruction_id"],
            "role_mapping": [["abstract input ball", "Wilson Lemma 40.3 admitted ball"], ["abstract graph radius", "Theorem 40.5 c_K graph radius"], ["abstract lower flow factor", "L(g)=1-b_0g^2-C_beta g^4"]],
            "shared_relations": ["the one-step upper bound must be valid on the entire input ball before it can be compared with the next lower radius"],
            "shared_constraints": ["0<rho<1", "fixed constants", "same k-to-k+1 norm transport"],
            "precondition_mapping": [["estimate valid on full input ball", "UNPROVED: c_K<=C_dom"], ["jointly applicable constants", "PARTIAL: named but not jointly applicable on chosen ball"], ["nonnegative lower factor", "DEFERRED: not evaluated in this packet"]],
            "unmatched_source_preconditions": ["proof that c_K<=C_dom or equivalent contraction validity on the chosen graph ball"],
            "disanalogies": ["the abstract episode assumes its domain premise; the source application is precisely missing that premise"],
            "target_validation_obligations": ["derive C_dom and C_force separately without reinterpretation", "test 4C_force/(1-rho)<=C_dom", "only after a pass, freeze and test the exact L(g)^2 margin"],
            "evidence_pointers": [SOURCE_AUDIT, source_audit["artifact_hash"], tm["snapshot_hash"]],
            "artifact_hash": "",
        }
    )
    return _seal(
        {
            "review_id": "OTR-YM-S1a2i-K1-D001-20260812",
            "target_atom_id": ATOM,
            "target_context_hash": context["packet_hash"],
            "research_memory_review_hash": memory["artifact_hash"],
            "episode_memory_snapshot_hash": tm["snapshot_hash"],
            "obstruction": _obstruction(),
            "direct_search_status": "NO_VIABLE_MATCH",
            "jump_search_status": "NO_VIABLE_MATCH",
            "glue_search_status": "NO_VIABLE_MATCH",
            "selected_mode": "CANNOT_CHECK",
            "direct_candidate_episode_ids": ["EP-YM-K1-C001-ABSTRACT-SCALAR-MARGIN"],
            "direct_mapping_witnesses": [witness],
            "jump_mapping_witnesses": [],
            "glue_witness": None,
            "selected_episode_ids": [],
            "exhaustion_witness": None,
            "missing_transformation_specification": None,
            "unresolved_warnings": ["SEARCH is blocked by the unmatched graph-ball domain precondition.", "JUMP and GLUE add no authority over the exact source constants.", "LIFT is forbidden because a single source-applicability residual and no bounded cross-problem coverage cannot justify invention."],
            "evidence_pointers": [SOURCE_AUDIT, MEMORY, TRANSFORMATION_MEMORY, EXPERT],
            "artifact_hash": "",
        }
    )


def build_lesson(context: dict[str, Any], source_audit: dict[str, Any], failure: dict[str, Any]) -> dict[str, Any]:
    return _seal(
        {
            "record_type": "YM_K1_D001_SEVEN_FIELD_MATHEMATICAL_LESSON",
            "atom_id": ATOM,
            "historical_candidate_id": HISTORICAL_CANDIDATE,
            "classification": "STRONGER_PREMISE_MISMATCH",
            "attempted_mathematical_implication": "Use Wilson's nominally k-uniform rho,C_K^(0),b_0,C_beta and k-to-k+1 norm estimate on the Theorem 40.5 graph ball to invoke the historical scalar lemma and prove ||K_{k+1}||_{k+1}<=c_K g_{k+1}^2.",
            "exact_mathematical_result_or_failure": "The primary source now binds the named constants and exact scale transport, superseding the source-exposure gap. It does not prove that Lemma 40.3's admitted radius C_dom contains the chosen c_K radius, and its displayed factor-two flow comparison yields at best coefficient 1+rho at scale k+1 rather than one. Exact target applicability therefore remains unproved; this is not a refutation.",
            "supported_and_competing_mathematical_causes": {
                "supported": [
                    {"gap_id": "A-DOMAIN-RADIUS-COMPATIBILITY", "cause": "The one-step estimate is stated only on C_dom g^2, while c_K is selected from C_force and rho without a proved c_K<=C_dom relation.", "falsifier": "Prove c_K<=C_dom or contraction on the chosen c_K ball."},
                    {"gap_id": "B-FACTOR-TWO-FLOW-COMPARISON", "cause": "The proof's two inequalities compose to coefficient 1+rho, not one.", "falsifier": "Prove g_k^2/g_{k+1}^2<=2/(1+rho), or after Gap A passes prove the exact L(g)^2 margin."},
                ],
                "competing": [
                    {"cause": "The constants or scale-indexed norms are unavailable.", "status": "REFUTED_BY_PINNED_PRIMARY_SOURCE_PASSAGES"},
                    {"cause": "The abstract scalar margin is impossible near zero.", "status": "NOT_SUPPORTED_BY_HISTORICAL_C001_CONTINUITY_RESULT"},
                    {"cause": "An upstream proof separates C_dom and C_force compatibly.", "status": "OPEN_CHEAPEST_DISCRIMINATOR"},
                    {"cause": "The full Yang-Mills mass-gap programme is refuted.", "status": "UNSUPPORTED_SCOPE_LEAP"},
                ],
            },
            "scope": "Only the Section 40 irrelevant K-coordinate invariant-region passage chain in Wilson Zenodo version 10.5281/zenodo.19393832. Excludes lambda, base inversion, full graph transform, continuum limit, OS reconstruction and mass gap.",
            "mathematical_falsifier": "Gap A is falsified by a source-faithful compatibility proof for the chosen graph ball. Gap B is independently falsified by a sharp enough flow-ratio proof or the exact scalar margin after Gap A passes. Neither falsifier is executed here.",
            "repair_or_next_discriminator": "First derive separately justified C_dom and C_force from the upstream Lemma 40.3 proof, without reinterpreting its displayed C, and freeze the test 4C_force/(1-rho)<=C_dom. Only if it passes, in a later candidate/result round freeze an interval and test L(g)^2>=rho+(C_force/c_K)g^2 with L(g)=1-b_0g^2-C_beta g^4 and L(g)>=0.",
            "proof_or_source_evidence": [SOURCE_AUDIT, source_audit["artifact_hash"], "Wilson PDF pp.141,145-148,172; equations (566)-(586); Lemmas 40.3-40.4; Theorem 40.5; Definition A.15.3", "Wilson TeX lines 9279-9291,9554-9584,9595-9680,9725-9750,11481-11499", FAILURE, _sha(failure)],
            "zero_mathematical_credit": ["Git/branch/PR state", "CI/tests", "schemas/hashes/chronology", "telemetry/repository growth", "file download mechanics"],
            "future_candidate_identity": None,
            "candidate_generation_allowed": False,
            "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            "artifact_hash": "",
        }
    )


def _trace_entry(index: int, event_type: str, previous: str, state: str, action: str, evidence: list[str], **extra: Any) -> dict[str, Any]:
    entry = {
        "event_id": f"YM-S1a2i-K1-D001-E{index:02d}",
        "atom_id": ATOM,
        "event_type": event_type,
        "timestamp": f"2026-08-12T15:{10+index:02d}:00+00:00",
        "state_summary": state,
        "action_summary": action,
        "evidence_pointers": evidence,
        "alternatives_considered": extra.get("alternatives_considered", []),
        "decision_rationale": extra.get("decision_rationale", ""),
        "outputs": extra.get("outputs", []),
        "uncertainties": extra.get("uncertainties", []),
        "residuals": extra.get("residuals", []),
        "next_steps": extra.get("next_steps", []),
        "artifact_hash": "",
        "previous_event_hash": previous,
    }
    return _seal(entry)


def build_trace(context: dict[str, Any], source_audit: dict[str, Any], memory: dict[str, Any], expert: dict[str, Any], shortcut: dict[str, Any], lesson: dict[str, Any]) -> dict[str, Any]:
    specs = [
        ("ATOMIZED", "The newly accessible Wilson primary-author source supersedes the earlier exposure gap but reveals two narrower K-coordinate applicability gaps.", "Open a diagnostic child atom; preserve the historical candidate and root as open.", [SOURCE_AUDIT, source_audit["artifact_hash"]], {"outputs": [ATOM], "residuals": ["A-DOMAIN-RADIUS-COMPATIBILITY", "B-FACTOR-TWO-FLOW-COMPARISON"]}),
        ("CONTEXT_FROZEN", "The active object is only joint applicability of the one-step K estimate and exact next-radius transport.", "Freeze source version, constants, norm scope, disanalogies and two-stage discriminator before any successor candidate.", [CONTEXT, context["packet_hash"]], {"outputs": [context["packet_hash"]]}),
        ("ANALOGY_SCAN", "One capacity-domain analogy survives only as a proposal to check inclusion before margin spending.", "Retain the bridge with explicit disanalogies and no theorem authority.", [context["packet_hash"]], {}),
        ("METHOD_TRANSFER_REVIEW", "The historical abstract scalar lemma is conditionally relevant but assumes validity on the full input ball.", "Block transfer until C_dom versus C_force/c_K compatibility is established.", [context["packet_hash"], SOURCE_AUDIT], {"alternatives_considered": ["apply the scalar lemma immediately", "reinterpret the source's C as adjustable constants"], "decision_rationale": "Both alternatives silently assume the exact premise under audit."}),
        ("EXPERT_CONTEXT_REVIEW", "Five same-context roles agree on stronger-premise mismatch and preserve two separate falsifiers.", "Freeze the strongest objection and block candidate generation.", [EXPERT, expert["artifact_hash"]], {"outputs": [expert["artifact_hash"]], "uncertainties": expert["unresolved_uncertainties"]}),
        ("EXPERIENCE_MEMORY_REVIEW", "The prior exposure diagnosis is superseded; the abstract scalar tool remains inapplicable until domain inclusion passes.", "Freeze dual-memory scope and the DifferenceWitness.", [MEMORY, memory["artifact_hash"], FAILURE, LESSON], {"outputs": [memory["artifact_hash"], lesson["artifact_hash"]], "uncertainties": memory["unresolved_warnings"]}),
        ("OBSTRUCTION_TRANSFORMATION_REVIEW", "The exact-margin episode is retrieved but its full-input-ball precondition is unmatched; no SEARCH/JUMP/GLUE route is viable and LIFT is not licensed.", "Return CANNOT_CHECK rather than inventing constants or a candidate.", [SHORTCUT, shortcut["artifact_hash"]], {"outputs": [shortcut["artifact_hash"], "CANNOT_CHECK"], "residuals": shortcut["unresolved_warnings"]}),
        ("NEXT_STEP_PROPOSED", "The packet is result-aware only about the source audit and remains pre-candidate for any successor mathematical action.", "Audit the upstream proof for separately justified C_dom,C_force and freeze 4C_force/(1-rho)<=C_dom as the cheapest future discriminator; defer scalar-margin evaluation.", [SOURCE_AUDIT, CONTEXT, MEMORY, SHORTCUT, LESSON], {"alternatives_considered": ["freeze a scalar candidate now", "claim Theorem 40.5 refuted", "continue to mass-gap consequences"], "decision_rationale": "Domain compatibility is cheaper and logically prior; all broader alternatives exceed the evidence scope.", "uncertainties": ["The upstream proof may or may not supply compatible constants."], "outputs": ["NO_SUCCESSOR_CANDIDATE_IDENTITY", "CANDIDATE_GENERATION_BLOCKED"], "next_steps": ["Derive C_dom and C_force separately from the upstream proof.", "Freeze and run 4C_force/(1-rho)<=C_dom in a later round.", "Only on a pass, freeze the exact L(g)^2 scalar-margin evaluation."]}),
    ]
    entries: list[dict[str, Any]] = []
    previous = ""
    for index, (event_type, state, action, evidence, extra) in enumerate(specs):
        entry = _trace_entry(index, event_type, previous, state, action, evidence, **extra)
        entries.append(entry)
        previous = entry["artifact_hash"]
    return {"trace_id": "TRACE-YM-S1a2i-K1-D001-PRE-20260812", "entries": entries}


def build_documents() -> dict[str, dict[str, Any]]:
    source = build_source_audit()
    context = build_context(source)
    failure = build_failure_lattice(context, source)
    memory = build_memory(context, failure)
    tm = build_transformation_memory(source)
    expert = build_expert_review(context, source)
    shortcut = build_shortcut(context, memory, tm, source)
    lesson = build_lesson(context, source, failure)
    trace = build_trace(context, source, memory, expert, shortcut, lesson)
    return {
        "source_audit": source,
        "context": context,
        "failure": failure,
        "lesson": lesson,
        "memory": memory,
        "transformation_memory": tm,
        "expert_review": expert,
        "shortcut_review": shortcut,
        "trace": trace,
    }


def write_documents() -> None:
    for name, document in build_documents().items():
        path = PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    write_documents()
