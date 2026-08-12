#!/usr/bin/env python3
"""Build the RH ANA003k moving-diagonal pre-candidate packet.

The packet freezes context, accumulated experience, semantic routing, expert
objections, result branches, and a cheap symbolic discriminator specification.
It deliberately selects no epsilon sequence or diagonal constant, materializes
no candidate, runs no discriminator, and records no mathematical result.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE_SHA = "80f8fb5e8c8417bd045cfae9c31df0a19e670eac"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
ATOM = "RH-ANA-003k-JY-MOVING-DIAGONAL"
PARENT = "RH-ANA-003j-D001-JY-C001-DIRECT-ENVELOPE"
BASE = "research/real_math/millennium/riemann_hypothesis"
PATHS = {
    "source": f"{BASE}/01_frontier/RH_ANA_003k_JY_MOVING_DIAGONAL_SOURCE_TRANSFER_20260812.json",
    "atomization": f"{BASE}/02_problem_dag/RH_ANA_003k_JY_MOVING_DIAGONAL_ATOMIZATION_20260812.json",
    "context": f"{BASE}/01_frontier/RH_ANA_003k_JY_MOVING_DIAGONAL_MATH_CONTEXT_FIBER_20260812.json",
    "tool_snapshot": f"{BASE}/07_memory/RH_ANA_003k_JY_MOVING_DIAGONAL_TOOL_SNAPSHOT_20260812.json",
    "failure_snapshot": f"{BASE}/07_memory/RH_ANA_003k_JY_MOVING_DIAGONAL_FAILURE_SNAPSHOT_20260812.json",
    "memory": f"{BASE}/07_memory/RH_ANA_003k_JY_MOVING_DIAGONAL_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/RH_ANA_003k_JY_MOVING_DIAGONAL_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert": f"{BASE}/08_reviews/RH_ANA_003k_JY_MOVING_DIAGONAL_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut": f"{BASE}/08_reviews/RH_ANA_003k_JY_MOVING_DIAGONAL_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "discriminator": f"{BASE}/08_reviews/RH_ANA_003k_JY_MOVING_DIAGONAL_SYMBOLIC_DISCRIMINATOR_FREEZE_20260812.json",
    "trace": f"{BASE}/09_trace/RH_ANA_003k_JY_MOVING_DIAGONAL_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": f"{BASE}/09_trace/RH_ANA_003k_JY_MOVING_DIAGONAL_PRE_CANDIDATE_GATE_20260812.json",
}
EVIDENCE = {
    "jy_result": (f"{BASE}/05_oracles/RH_ANA_003j_D001_JY_C001_PUBLIC_VALIDATION_RESULT_20260812.json", "ee5cb68a30a234b7bf93f6988577bb22d59d41dc82e3678845c6d3dadac3a867"),
    "jy_lesson": (f"{BASE}/07_memory/RH_ANA_003j_D001_JY_C001_MATHEMATICAL_LESSON_20260812.json", "606f33868f5b485eb9f383e5c1cdd8061970d7b0dd58908939f291da04fc1f90"),
    "jy_review": (f"{BASE}/08_reviews/RH_ANA_003j_D001_JY_C001_SAME_CONTEXT_RESULT_REVIEW_20260812.json", "a3923f8a4f5ef134e13c7af1579002bcffa3b1881fad1ac39d98a7f367969204"),
    "prior_context": (f"{BASE}/01_frontier/RH_ANA_003j_MATH_CONTEXT_FIBER_20260812.json", "436c642e0f9764051ee2fcf295577f5b2d8b58282ca9f99e5ffd78f7ae475e31"),
    "prior_memory": (f"{BASE}/07_memory/RH_ANA_003j_RESEARCH_MEMORY_REVIEW_20260812.json", "6214b618fb1ee1333bf2a1023f239b7addb3820b773f1ba43c6a243f5eced43b"),
    "prior_discriminator": (f"{BASE}/08_reviews/RH_ANA_003j_QUANTIFIER_COMPATIBILITY_DISCRIMINATOR_20260812.json", "5c1d32e5b1ce506d265cd0fbf1a564f7a9541c71873c77014d522192caae072b"),
    "c002_result": (f"{BASE}/05_oracles/RH_ANA_003_ABEL_001_C002_PROOF_CHECK_RESULT_20260812.json", "0d1dd6087f752307f4270ce97b1ad4f88d6809037a856c979837b85d94b91b6b"),
}


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def hash_with_blank(value: dict, field: str) -> str:
    subject = copy.deepcopy(value)
    subject[field] = ""
    return "sha256:" + hashlib.sha256(canonical(subject)).hexdigest()


def seal(value: dict) -> dict:
    value["artifact_hash"] = ""
    value["artifact_hash"] = hash_with_blank(value, "artifact_hash")
    return value


def raw_binding(name: str) -> dict:
    path, expected = EVIDENCE[name]
    observed = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
    if observed != expected:
        raise RuntimeError(f"{name}: {observed} != {expected}")
    return {"path": path, "raw_sha256": observed}


def obstruction() -> dict:
    return {
        "obstruction_id": "OBS-RH-ANA003K-JY-SUFFICIENT-MODULUS-VS-MOVING-DIAGONAL",
        "domain": "analytic number theory / asymptotic comparison / quantifier control",
        "roles": ["row n", "tolerance epsilon_n", "sufficient threshold tilde_M_JY", "moving endpoint Y_n", "monotonicity floor U_JY(n)"],
        "relations": [
            "tilde_m_JY(n,epsilon)>=ceil(U_JY(n)) by construction",
            "the inherited proposed diagonal has log Y_n=C n^(5/3)log^2(n+e) for one fixed C>0",
            "diagonal use of the sufficient modulus requires tilde_m_JY(n,epsilon_n)<=log Y_n eventually",
            "epsilon_n and the numerical diagonal constant are not selected in this round",
        ],
        "constraints": ["natural order", "fixed-n result authority only", "endpoint not internal-prefix control", "no outcome-dependent epsilon_n or C", "no discriminator execution in this round"],
        "failure_mechanisms": ["quadratic validity floor outgrows a proposed subquadratic-log diagonal", "tolerance choice makes the threshold larger", "mistaking a sufficient modulus for a necessary convergence threshold", "post-outcome parameter rescue"],
        "invariants_to_preserve": ["exact Johnston--Yang profile", "U_JY including +1.515", "least-M computability CANNOT_CHECK", "separate tilde_M identity", "OPEN root"],
        "desired_transition": ["decide prospectively whether tilde_m_JY(n,epsilon_n)<=log Y_n eventually or the proved sufficient certificate has a scoped growth obstruction"],
        "forbidden_losses": ["drop U_JY without a new proof", "claim failure of all possible remainder methods from failure of this sufficient modulus", "select epsilon_n or C after branch access", "promote endpoint control to Li positivity or RH"],
    }


def source_document() -> dict:
    return seal({
        "schema_version": "1.0.0",
        "record_type": "RH_ANA003K_JY_MOVING_DIAGONAL_SOURCE_AND_METHOD_TRANSFER",
        "packet_id": "RH-ANA-003k-JY-SOURCE-TRANSFER-20260812",
        "atom_id": ATOM,
        "base_sha": BASE_SHA,
        "source_facts": [
            "The proved direct envelope is fixed-n and valid on u>=U_JY(n)=max(log 2,n-1,[2(n-1+1.515)/0.8274]^2).",
            "The computable sufficient tilde_m search begins at ceil(U_JY(n)); it emits no numerical values in the source result.",
            "The frozen least M exists but its least-index computability is CANNOT_CHECK.",
            "The earlier proposed Li-program diagonal form was Y_n=exp(C n^(5/3)log^2(n+e)) with fixed symbolic C>0; no sufficient C was proved.",
        ],
        "context_deductions_to_freeze_not_evaluate": [
            "Writing u_n=log Y_n reduces any threshold comparison to log scale.",
            "The potentially decisive source-independent lower constraint is tilde_m_JY>=ceil(U_JY), before epsilon-dependent growth is considered.",
            "For symbolic comparison the critical ratio is rho_C(n)=C n^(5/3)log^2(n+e)/([2(n-1+1.515)/0.8274]^2).",
            "A later candidate must freeze its exact diagonal/tolerance contract before classifying the asymptotic behavior of rho_C or evaluating any stronger envelope bound.",
        ],
        "method_transfer_matrix": [
            {
                "source_context": "diagonal substitution with a quantitative modulus",
                "method": "compare log threshold against log diagonal under a preregistered tolerance",
                "enabling_assumptions": ["same error family", "valid sufficient modulus", "all parameter dependence explicit"],
                "shared_structure": ["two indices", "row threshold", "moving observation endpoint"],
                "disanalogies": ["tilde_M is sufficient not necessary", "epsilon_n is not yet frozen"],
                "repair_question": "Does the inherited log diagonal log Y_n dominate the built-in U_JY floor, and if not can a separately proved sharper envelope remove that floor?",
            },
            {
                "source_context": "asymptotic scale separation",
                "method": "divide competing log-scales and classify their ratio",
                "enabling_assumptions": ["C is fixed independently of n", "positive terms", "standard logarithm asymptotics"],
                "shared_structure": ["quadratic scale", "n^(5/3) times logarithmic correction"],
                "disanalogies": ["scale comparison alone does not measure the actual remainder", "a failed sufficient certificate is not a theorem of impossibility"],
                "repair_question": "Which conclusion is licensed: certificate incompatibility, sharper-envelope search, or actual remainder obstruction?",
            },
        ],
        "evidence_bindings": {name: raw_binding(name) for name in EVIDENCE},
        "authority": {"mathematical_context_deductions": True, "candidate": False, "evaluation": False, "result": False, "software_credit_units": 0},
    })


def atomization_document(source: dict) -> dict:
    return seal({
        "schema_version": "1.0.0", "atom_id": ATOM, "parent_atom_id": PARENT,
        "object": "The log-scale comparison between the proved sufficient fixed-n Johnston--Yang threshold and a future preregistered Li-program tolerance/diagonal contract.",
        "quantity_of_interest": "Whether tilde_m_JY(n,epsilon_n)<=log Y_n eventually, or whether the current sufficient certificate has a growth obstruction requiring a sharper envelope or larger diagonal.",
        "atomic_obligations": ["freeze epsilon_n later", "freeze diagonal family and C later", "compare built-in U_JY floor", "then compare epsilon-dependent excess", "preserve endpoint-only scope"],
        "candidate_generation_allowed": False,
        "blockers": ["epsilon_n not selected", "diagonal constant C not selected", "symbolic discriminator not executed"],
        "source_hash": source["artifact_hash"],
    })


def context_document(source: dict) -> dict:
    value = {
        "atom_id": ATOM,
        "object_context": "The proved fixed-n sufficient threshold tilde_M_JY(n,epsilon), its mandatory log-floor U_JY(n), a future preregistered positive tolerance sequence epsilon_n, and a future frozen moving diagonal for the Li program; determine only after a later freeze whether certificate compatibility or a growth obstruction occurs.",
        "structural_coordinates": ["outer index n", "log endpoint u", "tolerance epsilon", "quadratic monotonicity floor", "epsilon-dependent strict-search excess", "fixed versus moving quantifiers", "sufficient versus necessary thresholds"],
        "equivalent_formulations": [
            "tilde_M_JY(n,epsilon_n)<=Y_n eventually",
            "tilde_m_JY(n,epsilon_n)<=log Y_n eventually",
            "split comparison: ceil(U_JY(n))<=log Y_n plus epsilon-dependent excess",
            "certificate obstruction: the proved sufficient modulus misses the diagonal",
            "actual remainder obstruction: stronger and not implied by certificate obstruction",
        ],
        "solved_analogues": ["diagonal substitution once an explicit modulus is dominated", "asymptotic comparison by quotient of positive scales"],
        "near_solved_analogues": ["uniform Laguerre estimates below a componentwise monotonicity floor", "sharper nonmonotone direct-envelope analysis", "larger diagonal families under a preregistered resource contract"],
        "method_transfers": [
            {"source_context": "quantitative diagonal lemma", "method": "compare tilde_M_JY with Y_n, equivalently tilde_m_JY with log Y_n", "shared_structure": ["row index", "tolerance", "threshold", "diagonal"], "required_assumptions": ["epsilon_n frozen", "diagonal frozen", "same sufficient modulus"], "disanalogies": ["sufficient modulus failure is not actual remainder failure"], "repair_question": "Can the exact frozen log diagonal log Y_n dominate tilde_m_JY?", "source_anchors": [EVIDENCE["prior_context"][0], EVIDENCE["jy_result"][0]]},
            {"source_context": "scale-ratio test", "method": "reduce to rho_C(n) on log scale", "shared_structure": ["positive asymptotic scales", "fixed constant multiplier"], "required_assumptions": ["C fixed", "n tends to infinity"], "disanalogies": ["epsilon-dependent threshold excess omitted", "actual envelope below U not analyzed"], "repair_question": "Does the floor alone decide certificate incompatibility?", "source_anchors": [PATHS["source"]]},
        ],
        "explicit_disanalogies": ["fixed-n modulus is not an n-uniform rate", "sufficient threshold is not necessary", "endpoint control is not prefix control", "failure of the current certificate is not RH refutation", "a symbolic C>0 is not a selected numerical cutoff"],
        "source_anchors": [PATHS["source"], EVIDENCE["jy_result"][0], EVIDENCE["jy_lesson"][0], EVIDENCE["prior_context"][0]],
        "analogy_scan_status": "BRIDGES_RETAINED",
        "cross_domain_analogies": [
            {"source_kind": "scheduled timeout", "source_situation": "A certified runtime begins with mandatory setup cost before input-dependent work; a deadline below setup can never validate the certificate.", "common_abstraction": ["mandatory floor", "moving deadline", "additional tolerance cost"], "source_to_target_mapping": ["setup cost -> U_JY", "runtime -> tilde_m", "deadline -> log Y_n"], "shared_constraints": ["certificate threshold exceeds its floor", "deadline varies with n"], "disanalogies": ["runtime analogy supplies no number-theoretic bound", "certificate failure need not mean task failure"], "proposed_principle": "test mandatory floor compatibility before optimizing tolerance-dependent excess", "validation_obligation": "classify the exact target ratio only after freezing the diagonal contract", "provenance_note": "proposal-only algorithms analogy"},
        ],
        "analogy_scan_notes": "One analogy survives only as search ordering: test the mandatory floor before expensive epsilon-dependent analysis.",
        "frozen_at": "2026-08-12T16:20:00Z", "first_candidate_at": None, "packet_hash": "",
    }
    value["packet_hash"] = hash_with_blank(value, "packet_hash")
    return value


def memory_documents(context: dict) -> tuple[dict, dict, dict]:
    tools = seal({"snapshot_id": "RH-ANA003K-JY-TOOLS-20260812", "tools": [{"tool_id": "T-RH-JY-C001-FIXED-N-SUFFICIENT-TILDE-M", "applicable": True, "scope": "fixed n and endpoint only", "non_guarantees": ["no diagonal rate", "no necessary threshold", "no prefix control"]}], "source": raw_binding("jy_result")})
    failures = seal({"snapshot_id": "RH-ANA003K-JY-FAILURES-20260812", "failures": [{"failure_id": "F-RH-POINTWISE-TO-DIAGONAL-WITHOUT-MODULUS", "warning": "row-wise convergence cannot be substituted on a moving diagonal"}, {"failure_id": "F-RH-JY-LEAST-INDEX-COMPUTABILITY", "warning": "non-strict computable-real comparison may not decide the least index"}, {"failure_id": "F-RH-SUFFICIENT-CERTIFICATE-NOT-NECESSARY", "warning": "failure of a sufficient threshold does not refute actual convergence"}], "sources": [raw_binding("prior_memory"), raw_binding("jy_lesson")]})
    memory = {
        "target_atom_id": ATOM, "target_context_hash": context["packet_hash"],
        "tool_inventory_snapshot_hash": tools["artifact_hash"], "failure_lattice_snapshot_hash": failures["artifact_hash"],
        "tool_query_status": "MATCHES_FOUND", "failure_query_status": "MATCHES_FOUND",
        "candidate_method_families": ["direct comparison of tilde_m with log diagonal", "mandatory-floor obstruction test", "sharper below-floor envelope", "larger preregistered diagonal family"],
        "relevant_tool_ids": ["T-RH-JY-C001-FIXED-N-SUFFICIENT-TILDE-M"],
        "relevant_failure_ids": ["F-RH-POINTWISE-TO-DIAGONAL-WITHOUT-MODULUS", "F-RH-JY-LEAST-INDEX-COMPUTABILITY", "F-RH-SUFFICIENT-CERTIFICATE-NOT-NECESSARY"],
        "selected_tool_ids": ["T-RH-JY-C001-FIXED-N-SUFFICIENT-TILDE-M"],
        "tool_applicability_notes": ["The tool exposes a sufficient fixed-n threshold and its U_JY floor; it grants no diagonal conclusion."],
        "failure_reuse_notes": ["Keep certificate obstruction distinct from actual remainder obstruction.", "Do not use the noncomputable frozen least index as an executable discriminator."],
        "unresolved_warnings": ["epsilon_n is unfrozen", "diagonal C is unfrozen", "no below-floor envelope is proved", "no discriminator result exists"],
        "evidence_pointers": [PATHS["tool_snapshot"], PATHS["failure_snapshot"], EVIDENCE["jy_result"][0], EVIDENCE["prior_memory"][0]],
        "artifact_hash": "", "cross_problem_coverage_receipt_hash": "",
    }
    memory["artifact_hash"] = hash_with_blank(memory, "artifact_hash")
    return tools, failures, memory


def transformation_documents(context: dict, memory: dict) -> tuple[dict, dict]:
    obs = obstruction()
    episode = {
        "episode_id": "E-ASYMPTOTIC-MANDATORY-FLOOR-FIRST", "source_domain": "asymptotic analysis", "source_context": "sufficient threshold with a parameter-independent mandatory floor",
        "source_obstruction": obs, "transformation_name": "PROJECT_TO_LOG_SCALE_AND_COMPARE_FLOOR_FIRST",
        "operation": "take logarithms, split the sufficient log threshold into mandatory floor plus excess, and compare the floor with log Y_n before tolerance-dependent analysis",
        "preconditions": ["positive thresholds", "same row index", "fixed prospective diagonal contract", "floor is proved for the same sufficient certificate"],
        "resulting_relations": ["floor-compatible, floor-obstructed, or cannot-check branch before excess analysis"],
        "preserved_invariants": obs["invariants_to_preserve"], "relaxed_or_broken_constraints": [],
        "known_breakpoints": ["does not establish necessity", "cannot classify before diagonal contract freeze", "does not control internal prefixes"],
        "evidence_pointers": [PATHS["source"], EVIDENCE["jy_result"][0]], "authority": "SOURCE_EVENT_VERIFIED", "lineage_ids": [], "artifact_hash": "",
    }
    episode["artifact_hash"] = hash_with_blank(episode, "artifact_hash")
    tm = {"memory_id": "RH-ANA003K-JY-TRANSFORMATION-MEMORY-20260812", "source_universe": ["merged RH JY fixed-n result", "elementary asymptotic scale comparison", "prior RH diagonal quantifier packet"], "episodes": [episode], "evidence_pointers": [PATHS["source"], EVIDENCE["prior_discriminator"][0]], "snapshot_hash": ""}
    tm["snapshot_hash"] = hash_with_blank(tm, "snapshot_hash")
    witness = {
        "witness_id": "W-RH-ANA003K-FLOOR-FIRST", "episode_id": episode["episode_id"], "target_obstruction_id": obs["obstruction_id"],
        "role_mapping": [["mandatory source floor", "U_JY(n)"], ["moving deadline", "log Y_n"]],
        "shared_relations": ["sufficient threshold is at least its floor"], "shared_constraints": ["fixed n-indexed scales", "positive thresholds"],
        "precondition_mapping": [["same certificate", "merged tilde_M_JY certificate"], ["fixed diagonal before classification", "required in a later candidate round"]],
        "unmatched_source_preconditions": ["epsilon_n and exact diagonal/C are not frozen"],
        "disanalogies": ["target threshold also has epsilon-dependent excess", "certificate failure is not actual remainder failure"],
        "target_validation_obligations": ["freeze epsilon_n and diagonal contract", "prove ratio limit symbolically", "classify only certificate compatibility"],
        "evidence_pointers": [PATHS["source"], PATHS["discriminator"]], "artifact_hash": "",
    }
    witness["artifact_hash"] = hash_with_blank(witness, "artifact_hash")
    review = {
        "review_id": "RH-ANA003K-JY-OBSTRUCTION-REVIEW-20260812", "target_atom_id": ATOM,
        "target_context_hash": context["packet_hash"], "research_memory_review_hash": memory["artifact_hash"], "episode_memory_snapshot_hash": tm["snapshot_hash"],
        "obstruction": obs, "direct_search_status": "MATCHES_FOUND", "jump_search_status": "NOT_RUN", "glue_search_status": "NOT_RUN", "selected_mode": "SEARCH",
        "direct_candidate_episode_ids": [episode["episode_id"]], "direct_mapping_witnesses": [witness], "jump_mapping_witnesses": [], "glue_witness": None,
        "selected_episode_ids": [episode["episode_id"]], "exhaustion_witness": None, "missing_transformation_specification": None,
        "unresolved_warnings": ["SEARCH selects a discriminator route, not a candidate conclusion", "parameters remain unfrozen", "no LIFT authority"],
        "evidence_pointers": [PATHS["source"], PATHS["memory"], PATHS["transformation_memory"], PATHS["discriminator"]], "artifact_hash": "",
    }
    review["artifact_hash"] = hash_with_blank(review, "artifact_hash")
    return tm, review


def expert_document(context: dict, memory: dict) -> dict:
    return seal({
        "schema_version": "1.0.0", "review_id": "RH-ANA003K-JY-EXPERT-CONTEXT-REVIEW-20260812", "atom_id": ATOM,
        "review_authority": "SAME_CONTEXT_ROLE_SEPARATED_NOT_INDEPENDENT_REVIEW", "context_hash": context["packet_hash"], "memory_hash": memory["artifact_hash"],
        "lenses": [
            {"role": "domain_theory", "finding": "The merged result supplies a sufficient threshold with mandatory U_JY floor.", "objection": "It is not a necessary threshold."},
            {"role": "analogy_method_transfer", "finding": "Floor-first scale comparison is the cheapest same-domain transfer.", "objection": "The timeout analogy gives no arithmetic authority."},
            {"role": "adversarial_falsification", "finding": "A ratio branch can attack the inherited diagonal before epsilon analysis.", "objection": "Do not select C or epsilon after learning the branch."},
            {"role": "formal_methods", "finding": "The ratio limit and quantifier order are formalizable with elementary inequalities.", "objection": "No formal proof or discriminator execution exists now."},
            {"role": "novelty_research_value", "finding": "A certificate-level obstruction would redirect search efficiently.", "objection": "It is not an RH or impossibility result."},
        ],
        "disagreements": ["Whether to enlarge the diagonal or sharpen the envelope cannot be decided before the floor branch and a later frozen Li tolerance contract."],
        "strongest_objection": "The current sufficient modulus can fail while the actual remainder still succeeds below U_JY.",
        "recommendation": "Freeze the symbolic floor-ratio discriminator now; freeze epsilon_n and the diagonal family/constants only in a later candidate round before evaluation.",
        "mathematical_lesson_fields": {
            "attempted_mathematical_implication": "Use the fixed-n sufficient tilde_M_JY to place the natural-order endpoint on a future preregistered Li-program moving diagonal.",
            "exact_mathematical_result_or_failure": "No diagonal result is evaluated here; the exact open obstruction is whether the future log diagonal dominates the mandatory U_JY floor and then the epsilon-dependent strict-search excess.",
            "supported_causes": ["tilde_m_JY is bounded below by ceil(U_JY)", "diagonal compatibility is equivalent to a log-scale threshold comparison"],
            "competing_causes": ["the current sufficient certificate may be too coarse below U_JY", "epsilon-dependent excess may dominate even when the floor is compatible"],
            "scope": "sufficient fixed-n endpoint certificate versus a future moving endpoint only",
            "mathematical_falsifier": "A later proof that the frozen log diagonal log Y_n dominates the complete tilde_m_JY refutes the obstruction branch; a proof that the candidate envelope is valid below U_JY refutes use of U_JY as an unavoidable certificate floor for that successor.",
            "repair_or_new_mathematical_move": "If the current certificate is floor-obstructed, derive a sharper below-floor envelope or prospectively freeze a larger diagonal; do not infer actual remainder failure.",
            "proof_or_source_evidence": [EVIDENCE["jy_result"][0], PATHS["source"], PATHS["discriminator"]],
        },
        "nonmathematical_credit": "ZERO; Git, CI, schemas, hashes, and fixtures are operational only.",
    })


def discriminator_document(source: dict, context: dict) -> dict:
    return seal({
        "schema_version": "1.0.0", "discriminator_id": "RH-ANA003K-JY-CHEAP-SYMBOLIC-SCALE-DISCRIMINATOR-20260812", "atom_id": ATOM,
        "status": "FROZEN_NOT_EXECUTED_NO_BRANCH_SELECTED", "candidate_identity": None,
        "unselected_parameters": {"epsilon_sequence": None, "diagonal_family": None, "diagonal_constant_C": None},
        "symbolic_probe": {
            "prospective_inherited_family": "For a later freeze only: u_n(C)=C n^(5/3)log^2(n+e), with C fixed and positive.",
            "mandatory_floor": "F_n=[2(n-1+1.515)/0.8274]^2=[2(n+0.515)/0.8274]^2.",
            "ratio": "rho_C(n)=u_n(C)/F_n=(C(0.8274)^2/4) n^(5/3)log^2(n+e)/(n+0.515)^2.",
            "future_proof_obligation": "Classify rho_C(n) using exact inequalities/standard log-power asymptotics, then compare ceil(U_JY(n)) with u_n(C); do not numerically fit a finite range.",
            "epsilon_independence": "Because tilde_m_JY>=ceil(U_JY), a floor obstruction branch, if proved, is independent of epsilon_n; a floor-compatible branch still requires epsilon-dependent analysis.",
        },
        "allowed_future_branches": [
            {"branch": "PASS_FLOOR_COMPATIBLE", "condition": "The preregistered log diagonal eventually dominates ceil(U_JY(n)).", "next": "Evaluate epsilon-dependent excess without changing parameters."},
            {"branch": "FAIL_CURRENT_SUFFICIENT_CERTIFICATE_GROWTH", "condition": "ceil(U_JY(n)) exceeds the preregistered log diagonal infinitely often/eventually.", "next": "Reject this sufficient certificate for that diagonal only; do not infer actual remainder failure."},
            {"branch": "PASS_FULL_DIAGONAL_COMPATIBILITY", "condition": "The preregistered log diagonal log Y_n eventually dominates the full computed sufficient tilde_m_JY at the preregistered epsilon_n.", "next": "Record scoped endpoint compatibility only."},
            {"branch": "FAIL_EPSILON_DEPENDENT_EXCESS", "condition": "The floor is compatible but tilde_m-log diagonal remains positive infinitely often/eventually.", "next": "Preserve failure; consider a sharper envelope or larger prospectively frozen diagonal."},
            {"branch": "CANNOT_CHECK", "condition": "epsilon_n, diagonal identity, source bytes, or exact comparison proof is missing.", "next": "Fail closed; do not select replacement parameters after outcome access."},
        ],
        "planted_falsifiers": [
            "Treat tilde_M as a necessary threshold and claim actual remainder impossibility.",
            "Drop +1.515 from U_JY.",
            "Treat C as n-dependent after freezing it as fixed.",
            "Choose epsilon_n or C after inspecting a branch.",
            "Compare M on the original scale while omitting the logarithm.",
            "Promote endpoint compatibility to internal-prefix control, Li positivity, or RH.",
        ],
        "success_contract_for_later_candidate": ["exact epsilon_n identity frozen", "exact diagonal family and constants frozen", "source/result hashes unchanged", "branch conditions unchanged", "symbolic proof before any numerical corroboration"],
        "execution_firewall": {"symbolic_limit_evaluated": False, "branch_selected": False, "epsilon_n_selected": False, "C_selected": False, "numerical_tests_run": False, "result_recorded": False},
        "evidence": [source["artifact_hash"], context["packet_hash"], raw_binding("jy_result")],
        "authority": {"discriminator_specification_only": True, "mathematical_result": False, "candidate": False, "li_or_rh": False},
    })


def trace_document(source: dict, context: dict, memory: dict, expert: dict, shortcut: dict, discriminator: dict) -> dict:
    specs = [
        ("ATOMIZED", "Separate the moving-diagonal comparison from the completed fixed-n result.", [PATHS["atomization"]]),
        ("CONTEXT_FROZEN", "Bind sufficient versus necessary threshold, log scale, U_JY floor, and unfrozen parameters.", [PATHS["context"]]),
        ("ANALOGY_SCAN", "Retain setup-cost versus deadline only as a floor-first search-order analogy.", [PATHS["context"]]),
        ("METHOD_TRANSFER_REVIEW", "Map diagonal-modulus comparison and positive-scale quotient methods with their broken assumptions.", [PATHS["source"], PATHS["context"]]),
        ("EXPERT_CONTEXT_REVIEW", "Preserve the certificate-versus-object objection across five roles.", [PATHS["expert"]]),
        ("EXPERIENCE_MEMORY_REVIEW", "Query the fixed-n sufficient tool and three relevant failure warnings.", [PATHS["memory"]]),
        ("OBSTRUCTION_TRANSFORMATION_REVIEW", "Select same-domain floor-first SEARCH as a future discriminator route only.", [PATHS["shortcut"]]),
        ("NEXT_STEP_PROPOSED", "Later freeze epsilon_n and a diagonal contract, then execute the already-frozen symbolic discriminator without parameter rescue.", [PATHS["discriminator"]]),
    ]
    entries=[]; previous=""
    for i,(kind,action,pointers) in enumerate(specs,1):
        event={"event_id":f"RH-ANA003K-JY-E{i:02d}","atom_id":ATOM,"event_type":kind,"timestamp":f"2026-08-12T16:20:{10+i:02d}Z","state_summary":"The fixed-n JY sufficient modulus is proved, but its compatibility with any Li-program moving diagonal is open and all candidate parameters remain unfrozen.","action_summary":action,"evidence_pointers":pointers,"alternatives_considered":["compare mandatory U_JY floor first","analyze epsilon-dependent excess first","infer actual remainder obstruction","select a larger diagonal now"],"decision_rationale":"Floor-first symbolic comparison has the lowest cost and preserves the distinction between certificate failure and object failure; outcome-bearing parameters must be frozen later.","outputs":["PRE_CANDIDATE_ONLY","NO_EPSILON_SEQUENCE","NO_DIAGONAL_CONSTANT","NO_BRANCH_SELECTED","ZERO_SOFTWARE_MATH_CREDIT"],"uncertainties":["future epsilon_n","future diagonal identity","below-floor envelope possibility"],"residuals":["diagonal compatibility open","actual remainder below U_JY open","Li and RH open"],"next_steps":["publicly freeze this packet","later freeze exact parameters before evaluation","retain any obstruction as certificate-scoped"],"previous_event_hash":previous,"artifact_hash":""}
        event["artifact_hash"]=hash_with_blank(event,"artifact_hash");previous=event["artifact_hash"];entries.append(event)
    return {"trace_id":"RH-ANA003K-JY-MOVING-DIAGONAL-PRE-CANDIDATE-TRACE-20260812","entries":entries}


def gate_document(context: dict, memory: dict, shortcut: dict, trace: dict, discriminator: dict) -> dict:
    return seal({"schema_version":"1.0.0","gate_id":"RH-ANA003K-JY-PRE-CANDIDATE-GATE-20260812","atom_id":ATOM,"application_base_sha":BASE_SHA,"framework_sha":FRAMEWORK_SHA,"context_hash":context["packet_hash"],"memory_hash":memory["artifact_hash"],"shortcut_hash":shortcut["artifact_hash"],"trace_tip":trace["entries"][-1]["artifact_hash"],"discriminator_hash":discriminator["artifact_hash"],"candidate_generation_allowed":False,"pre_candidate_actions":["freeze exact epsilon_n in a later candidate round","freeze exact diagonal family and C in that same later round","bind a successor evaluator to the frozen discriminator before execution"],"chronology":{"candidate_identity":None,"epsilon_sequence_identity":None,"diagonal_constant_identity":None,"discriminator_executed":False,"result_accessed":False},"authority":{"pre_candidate_context_only":True,"mathematical_result":False,"independent_review":False,"li_or_rh":False,"software_credit_units":0}})


def build_all() -> dict[str,dict]:
    source=source_document(); atom=atomization_document(source); context=context_document(source)
    tools,failures,memory=memory_documents(context); tm,shortcut=transformation_documents(context,memory)
    expert=expert_document(context,memory); discriminator=discriminator_document(source,context)
    trace=trace_document(source,context,memory,expert,shortcut,discriminator); gate=gate_document(context,memory,shortcut,trace,discriminator)
    return {PATHS["source"]:source,PATHS["atomization"]:atom,PATHS["context"]:context,PATHS["tool_snapshot"]:tools,PATHS["failure_snapshot"]:failures,PATHS["memory"]:memory,PATHS["transformation_memory"]:tm,PATHS["expert"]:expert,PATHS["shortcut"]:shortcut,PATHS["discriminator"]:discriminator,PATHS["trace"]:trace,PATHS["gate"]:gate}


def main() -> None:
    for relative,value in build_all().items():
        path=ROOT/relative;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,indent=2,sort_keys=True)+"\n")


if __name__ == "__main__":
    main()
