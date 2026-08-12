#!/usr/bin/env python3
"""Build the proof/source-bound causal-coordinate feedback proposal.

The synthesis recognizes a shared obstruction morphology, not a shared causal
mechanism.  It grants no theorem or framework authority.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
OUT = ROOT / "research/real_math/millennium/cross_problem/10_case_study/CROSS_FAILURE_CAUSAL_COORDINATE_FEEDBACK_20260812.json"

APPLICATION_SHA = "f0c20a3126c61effc8defbbb66f6e9306f349ad8"
FRAMEWORK_PIN = "7d67a18a96499f5df7bf58bc6b1356d1ce1cafbf"
FRAMEWORK_LIVE = "ea607c8cd8e4fd308ea9a4e024d8c93ff87f5fda"

SOURCES = {
    "pnp_c050": "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C050_K15_MATHEMATICAL_LESSON_20260812.json",
    "pnp_c051": "research/real_math/millennium/p_vs_np/07_memory/O9d12a2a1b_C051_K19_MATHEMATICAL_LESSON_20260812.json",
    "rh_ana003j": "research/real_math/millennium/riemann_hypothesis/08_reviews/RH_ANA_003j_QUANTIFIER_COMPATIBILITY_DISCRIMINATOR_20260812.json",
    "bsd_r16": "research/real_math/millennium/birch_swinnerton_dyer/07_memory/BSD_A1a3_R16_SCOPED_MATHEMATICAL_LESSON_20260812.json",
    "ym_k1": "research/real_math/millennium/yang_mills/07_memory/YM-S1a2i_K1_C001_MATHEMATICAL_LESSON_20260812.json",
}


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def artifact_hash(value: dict) -> str:
    subject = copy.deepcopy(value)
    subject["artifact_hash"] = ""
    return "sha256:" + hashlib.sha256(canonical(subject)).hexdigest()


def source_binding(relative: str) -> dict:
    raw = (ROOT / relative).read_bytes()
    return {"path": relative, "raw_sha256": hashlib.sha256(raw).hexdigest()}


def build() -> dict:
    source_documents = {
        key: json.loads((ROOT / path).read_text(encoding="utf-8"))
        for key, path in SOURCES.items()
    }
    assert source_documents["pnp_c050"]["seven_field_math_lesson"]["exact_result_or_failure"].startswith("It does not: H_15")
    assert source_documents["pnp_c051"]["seven_field_math_lesson"]["exact_result_or_failure"].startswith("It does not: H_19")
    assert source_documents["rh_ana003j"]["mathematical_lesson_boundary"]["supported_mathematical_cause"].startswith("The unbridged coordinate")
    assert source_documents["bsd_r16"]["supported_and_competing_mathematical_causes"]["supported"].startswith("The source theorem asserts")
    assert source_documents["ym_k1"]["supported_and_competing_mathematical_causes"]["supported"].startswith("The missing bridge")

    value = {
        "artifact_hash": "",
        "schema_version": "1.0.0",
        "proposal_id": "CROSS-MILLENNIUM-CAUSAL-COORDINATE-REPARAMETERIZATION-20260812",
        "record_type": "APPLICATION_TO_RAKL_MATHEMATICAL_METHOD_FEEDBACK",
        "status": "QUARANTINED_PROPOSAL",
        "object": "Four proof/source-backed bounded mathematical obstruction diagnoses in P versus NP, RH, BSD, and Yang--Mills",
        "quantity_of_interest": "Whether repeated bounded failures support changing the next mathematical search coordinate before advancing another instance or scale",
        "authority_universe": {
            "application_repository_sha": APPLICATION_SHA,
            "framework_pin_sha": FRAMEWORK_PIN,
            "framework_live_sha": FRAMEWORK_LIVE,
            "framework_pin_to_live_diff_scope": "PAPER3_REGISTRATION_MARKDOWN_ONLY_NO_MATHEMATICAL_GATE_CHANGE",
        },
        "shared_obstruction_morphology": {
            "statement": "An outer index, scale, quotient, or qualitative estimate can change while the desired implication remains controlled by a load-bearing mathematical coordinate that the current representation erases, fixes incompatibly, or leaves quantitatively unbound.",
            "causal_claim_boundary": "This is a shared morphology only. No common cross-domain causal mechanism is proved; each causal coordinate has only its source-scoped status below.",
            "proposed_search_response": "After at least two genuinely distinct proof/source-backed bounded failures expose an explicit actionable coordinate, reparameterize the next discriminator around that coordinate before blind instance progression.",
        },
        "mathematical_witnesses": [
            {
                "problem": "P_VS_NP",
                "source_atoms": ["O9d12a2a1b-C050", "O9d12a2a1b-C051"],
                "attempted_mathematical_implication": "Moving the equal split from k=12 to k=15 and then k=19 might create H_k intersect P_(k+1).",
                "exact_result_or_failure": "H_15 intersect P_16 and H_19 intersect P_20 are both empty: in each frozen world label bit 3 is forced to 1 on H_k and to MAGIC[3]=0 on P_(k+1).",
                "supported_and_competing_mathematical_causes": "Supported bounded cause: suffix-start phase places a forced variable-code bit against a fixed MAGIC coordinate. Nonvacuity and complete frozen branch enumeration reject emptiness or omitted-branch explanations. Universality over later k remains open.",
                "scope": "Exactly the canonical grammar, equal split, C048 swapped reduction, and k=15 or k=19; no cover lower bound or P-vs-NP conclusion.",
                "mathematical_falsifier": "A legal frozen-world label with the opposite bit, a common label, or a later residue class escaping the collision refutes the corresponding scoped or prospective extension.",
                "repair_or_next_discriminator": "Parameterize support by suffix-start residue and literal-code phase; classify forced coordinates before selecting another k.",
                "proof_or_source_evidence": [source_binding(SOURCES["pnp_c050"]), source_binding(SOURCES["pnp_c051"])],
                "load_bearing_coordinate": "suffix-start residue and induced forced-bit/MAGIC alignment",
                "causal_status": "SUPPORTED_BOUNDED_AT_K15_AND_K19",
                "disanalogy": "Unlike the other rows, these are finite exact syntactic separation proofs; C050 and C051 are distinct k-worlds but explicitly related repetitions, not independent cross-domain evidence.",
            },
            {
                "problem": "RIEMANN_HYPOTHESIS",
                "source_atoms": ["RH-ANA-003j"],
                "attempted_mathematical_implication": "Pointwise fixed-n convergence should give E(n,Y_n)<=epsilon_n eventually along a growing diagonal.",
                "exact_result_or_failure": "The source gives a row threshold M(n,epsilon), while the target additionally requires M(n,epsilon_n)<=Y_n eventually; no modulus or comparison is proved.",
                "supported_and_competing_mathematical_causes": "Supported logical gap: unbound n-dependence of the threshold. A useful n-dependent modulus, diagonal compatibility without full uniformity, and endpoint-only control remain competing open possibilities.",
                "scope": "Pre-candidate quantifier/method-transfer diagnosis only; epsilon_n is not frozen, and complement, internal-prefix, and Li/RH obligations remain separate.",
                "mathematical_falsifier": "Derive a valid target-domain M(n,epsilon) and prove the eventual diagonal comparison; the frozen triangular-array world falsifies any generic pointwise-only rule.",
                "repair_or_next_discriminator": "Expose all n-dependent Abel/Laguerre constants and compare the resulting modulus with the prospectively frozen diagonal.",
                "proof_or_source_evidence": [source_binding(SOURCES["rh_ana003j"])],
                "load_bearing_coordinate": "growth of M(n,epsilon_n) relative to Y_n",
                "causal_status": "SUPPORTED_LOGICAL_MISSING_BRIDGE_NO_CANDIDATE_RESULT",
                "disanalogy": "This is not a refuted RH candidate or finite separation proof; it is a pre-candidate quantifier insufficiency diagnosis.",
            },
            {
                "problem": "BIRCH_AND_SWINNERTON_DYER",
                "source_atoms": ["BSD-A1a3-CASSELSTATEDIV-CORANK-GATE"],
                "attempted_mathematical_implication": "Cassels--Tate alternation/nondegeneracy should force the p-primary divisible corank to vanish.",
                "exact_result_or_failure": "The implication from the frozen pairing axioms is impossible: nondegeneracy is on Sha/D and the model (Q_p/Z_p)^r with zero pairing leaves a nondegenerate zero quotient for arbitrary r.",
                "supported_and_competing_mathematical_causes": "Verified scoped cause: quotienting removes the target D. Pairing plus independent D-control remains open; parity and square-order standalone repairs are refuted or reverse premise direction.",
                "scope": "Logical sufficiency of the frozen pairing properties only; the countermodel does not assert arithmetic realizability or refute Cassels--Tate theory.",
                "mathematical_falsifier": "Any derivation from only those axioms forcing D=0 must exclude the explicit divisible-group countermodel.",
                "repair_or_next_discriminator": "Seek independent same-curve control of D or construct two independent rational points; use the pairing only downstream.",
                "proof_or_source_evidence": [source_binding(SOURCES["bsd_r16"])],
                "load_bearing_coordinate": "maximal divisible radical D erased by Sha -> Sha/D",
                "causal_status": "VERIFIED_SCOPED_NONIMPLICATION",
                "disanalogy": "Unlike RH and YM missing-source bridges, a standalone implication is ruled out by an elementary countermodel; this does not rule out adding independent hypotheses.",
            },
            {
                "problem": "YANG_MILLS",
                "source_atoms": ["YM-S1a2i-K1"],
                "attempted_mathematical_implication": "A qualitative contraction plus O(g_k^4) forcing and base flow should fit K_(k+1) into the smaller c_K g_(k+1)^2 ball.",
                "exact_result_or_failure": "The scalar implication holds for each fixed admissible finite constant family, but the acquired source does not bind one k-uniform family or the exact k-to-k+1 norm/graph-ball scope, so the target application is unestablished, not refuted.",
                "supported_and_competing_mathematical_causes": "Supported acquired-evidence gap: uniform quantifiers and norm transport are unbound. The full source or another theorem may supply them; scalar-margin failure is refuted abstractly by continuity.",
                "scope": "Only the K-coordinate one-step radius implication; no lambda, graph-transform, OS, continuum, or mass-gap authority.",
                "mathematical_falsifier": "An exact source passage binding all five constants uniformly in k with the required norm theorem falsifies the missing-bridge diagnosis and reopens composition.",
                "repair_or_next_discriminator": "Acquire exact primary-source ranges for the uniform constants and same-norm theorem before further scalar optimization.",
                "proof_or_source_evidence": [source_binding(SOURCES["ym_k1"])],
                "load_bearing_coordinate": "k-uniform constant family and exact norm transport",
                "causal_status": "SOURCE_SCOPED_INSUFFICIENCY_WITH_ABSTRACT_LEMMA_PROVED",
                "disanalogy": "Unlike BSD, the abstract implication is valid; failure is only to instantiate its hypotheses from acquired target evidence.",
            },
        ],
        "rakl_challenger": {
            "existing_method_surface": "failure-diagnosis residual routing and context reopening",
            "new_method_surface_requested": False,
            "candidate_delta": "Add an activation policy that schedules causal-coordinate reparameterization before another instance/scale progression when the evidence rule is met.",
            "activation_rule": {
                "minimum_genuinely_distinct_bounded_failures": 2,
                "requirements": [
                    "distinct candidate/atom or target-instance identities, not duplicate artifacts of one result",
                    "each failure has proof/source evidence and a scoped supported coordinate",
                    "the coordinate is actionable in a frozen next discriminator",
                    "shared vocabulary alone does not count",
                ],
            },
            "non_activation_worlds": [
                "one material failure only",
                "repeated artifact copies or retrospective restatements of one result",
                "unclassified failures with no supported causal coordinate",
                "the proposed coordinate is already controlled and the residual differs",
                "software, CI, schema, hash, chronology, or repository failures",
            ],
            "fresh_matched_assurance": {
                "required": True,
                "chronology": "Freeze benchmark, evaluator, resource budget, activation labels, and hidden next-action gold before challenger outcomes.",
                "arms": ["INCUMBENT_RAKL", "CAUSAL_COORDINATE_ACTIVATION_POLICY"],
                "worlds": [
                    "activation cases with at least two distinct bounded failures and a useful coordinate",
                    "non-activation cases where continued progression is correct",
                    "planted misleading shared-morphology case",
                    "missing-evidence case requiring CANNOT_CHECK",
                    "fresh mathematical tasks not used to design this proposal",
                ],
                "blocking_metrics": [
                    "valid next-discriminator selection",
                    "repeat-failure avoidance",
                    "viable-route preservation",
                    "correct non-activation",
                    "correct CANNOT_CHECK",
                    "matched mathematical information gain per resource",
                ],
                "falsifier": "Reject or narrow the policy if it fails any protected authority invariant, activates on controls, suppresses a viable route, or does not improve fresh matched mathematical routing at equal resources.",
            },
        },
        "authority_contract": {
            "mathematical_credit_units_created": 0,
            "source_mathematical_units_recounted": False,
            "theorem_authority": False,
            "root_solution_authority": False,
            "framework_evolution_authority": False,
            "method_promotion_authority": False,
            "independent_review_authority": False,
            "framework_mutation_allowed": False,
            "failure_lattice_mutation_allowed": False,
            "research_tool_inventory_mutation_allowed": False,
        },
        "root_states": {
            "P_VS_NP": "OPEN_NO_SOLUTION_CERTIFICATE",
            "RIEMANN_HYPOTHESIS": "OPEN_NO_SOLUTION_CERTIFICATE",
            "BIRCH_AND_SWINNERTON_DYER": "OPEN_NO_SOLUTION_CERTIFICATE",
            "YANG_MILLS": "OPEN_NO_SOLUTION_CERTIFICATE",
        },
    }
    value["artifact_hash"] = artifact_hash(value)
    return value


def main() -> None:
    OUT.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
