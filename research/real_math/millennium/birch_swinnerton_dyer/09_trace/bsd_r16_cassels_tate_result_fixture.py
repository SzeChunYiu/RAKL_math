"""Materialize the source-bound BSD R16 Cassels--Tate result.

The result is a narrow logical-sufficiency theorem audit, not a BSD solution:
the Cassels--Tate pairing is nondegenerate only on Sha modulo its maximal
divisible subgroup, so its alternating/nondegenerate consequences do not
control the corank of that subgroup.  A group-theoretic countermodel makes the
non-implication exact.
"""
from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path

from rakl.failure_lattice import FailureDiagnosisStatus, FailureExperience, FailureExperienceLattice, validate_failure_experience
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType, audit_research_trace
from rakl.semantic_shortcut import (
    ObstructionFingerprint,
    ObstructionTransformationEpisode,
    ObstructionTransformationReview,
    RouteSearchStatus,
    ShortcutMode,
    StructuralMappingWitness,
    TransformationEpisodeAuthority,
    audit_obstruction_transformation_review,
    build_transformation_memory,
)


ATOM = "BSD-A1a3-CASSELSTATEDIV-CORANK-GATE"
BASE = "research/real_math/millennium/birch_swinnerton_dyer"
PRE_MERGE_SHA = "d06b0b465a619f19ce0682d8cf964e42b2ee925f"
FRAMEWORK_SHA = "7d67a18a96499f5df7bf58bc6b1356d1ce1cafbf"
PRE_CONTEXT = f"{BASE}/01_frontier/BSD_A1a3_R16_CASSELSTATE_CONTEXT_FIBER_20260812.json"
PRE_TRACE = f"{BASE}/09_trace/BSD_A1a3_R16_PRE_CANDIDATE_TRACE_20260812.json"
PRE_GATE = f"{BASE}/09_trace/BSD_A1a3_R16_SOURCE_DISCRIMINATOR_FREEZE_20260812.json"
PATHS = {
    "source": f"{BASE}/00_sources/BSD_A1a3_R16_CASSELSTATE_SOURCE_AUDIT_20260812.json",
    "lesson": f"{BASE}/07_memory/BSD_A1a3_R16_SCOPED_MATHEMATICAL_LESSON_20260812.json",
    "failure": f"{BASE}/07_memory/BSD_A1a3_R16_FAILURE_EXPERIENCE_DELTA_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/BSD_A1a3_R16_POSTRESULT_TRANSFORMATION_MEMORY_20260812.json",
    "shortcut": f"{BASE}/07_memory/BSD_A1a3_R16_POSTRESULT_SEARCH_REVIEW_20260812.json",
    "trace": f"{BASE}/09_trace/BSD_A1a3_R16_RESULT_TRACE_20260812.json",
    "dag": f"{BASE}/02_problem_dag/BSD_A1a3_R16_CASSELSTATE_DAG_DELTA_20260812.json",
}


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def seal(value: dict) -> dict:
    out = dict(value)
    out["artifact_hash"] = ""
    out["artifact_hash"] = canonical_hash(out)
    return out


def jsonable(value: object) -> object:
    return json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))


def load(root: Path, relative: str) -> dict:
    value = json.loads((root / relative).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def source_document(pre_gate: dict) -> dict:
    return seal({
        "record_type": "BSD_R16_PRIMARY_SOURCE_DIRECTION_AND_LOGICAL_SUFFICIENCY_AUDIT",
        "cycle_id": "BSD-A1A3-CASSELSTATE-DIVISIBLE-CORANK-20260812-R16",
        "atom_id": ATOM,
        "framework_main_sha_at_result": FRAMEWORK_SHA,
        "framework_drift_review": "a6946c..7d67a18 adds Paper3 objective artifacts and an optional objective-transfer benchmark module/tests; it is not imported by the mandatory mathematical research runtime or gates",
        "pre_result_freeze": {"merge_commit": PRE_MERGE_SHA, "gate_path": PRE_GATE, "gate_artifact_hash": pre_gate["artifact_hash"]},
        "source": {
            "authors": ["Bjorn Poonen", "Michael Stoll"],
            "title": "The Cassels-Tate pairing on polarized abelian varieties",
            "publication": "Annals of Mathematics 150 (1999), 1109-1149",
            "arxiv_id": "math/9911267v1",
            "url": "https://arxiv.org/pdf/math/9911267",
            "downloaded_at_utc": "2026-08-12T11:42:00Z",
            "pdf_bytes": 399391,
            "pdf_sha256": "a7f6b91f8dbc38d8c061fc8aa2c2848a1ed503cb0dbe91c5bd1a6f6ef9dff804",
            "selectors": [
                "abstract, Annals p.1109: definition of Sha_nd and nondegenerate quotient pairing; elliptic-curve alternation",
                "introduction, Annals pp.1110-1111: pairing on Sha(E), quotient by maximal divisible subgroup, alternation, and square-order consequence conditional on finiteness",
                "Section 2, Annals p.1112: M_div, M_nd=M/M_div, p-primary notation, and alternating versus antisymmetric distinction",
                "Corollary 12 remarks, Annals p.1126: recovery of Cassels alternation theorem for elliptic curves",
            ],
            "underlying_cassels_reference": "J. W. S. Cassels, Arithmetic on curves of genus 1, IV, J. reine angew. Math. 211 (1962), 95-112",
        },
        "source_bound_statements": [
            "In general the Cassels--Tate pairing is Sha(A) x Sha(A^vee) -> Q/Z; for an elliptic curve, the canonical principal polarization identifies E with E^vee and gives the self-pairing used here.",
            "For an elliptic curve E over a global field, the Cassels--Tate pairing on Sha(E) becomes nondegenerate after quotienting Sha(E) by its maximal divisible subgroup D.",
            "For elliptic curves the pairing is alternating, including the 2-primary part; the source separately warns that antisymmetric alone implies alternating automatically only at odd p.",
            "If Sha(E) is finite, alternation and nondegeneracy force its order to be a square; finiteness is a premise of this consequence, not an output of the pairing theorem.",
        ],
        "p_primary_specialization_proof": [
            "Sha(E) is torsion and decomposes into primary components; its maximal divisible subgroup decomposes similarly.",
            "A bilinear Q/Z-valued pairing between p-primary and q-primary elements is zero for p different from q because its value is killed by powers of both primes.",
            "Therefore the quotient pairing splits by prime and is nondegenerate on Sha(E)[p^infinity]/D[p^infinity], but D[p^infinity] has already been removed.",
        ],
        "exact_group_countermodel": {
            "group": "M=(Q_p/Z_p)^r for any integer r>=0",
            "pairing": "the zero bilinear pairing M x M -> Q/Z",
            "maximal_divisible_subgroup": "M_div=M",
            "quotient": "M_nd=M/M_div=0",
            "checks": ["the full pairing is alternating", "the induced pairing on the zero quotient is nondegenerate", "corank_Zp M_div=r is arbitrary, including r=1"],
            "conclusion": "The abstract Cassels--Tate pairing properties alone imply neither corank D=0 nor even parity of corank D.",
            "realizability_boundary": "This is a logical countermodel to the inference from pairing axioms alone; it does not assert that every r occurs as the divisible Sha corank of an elliptic curve.",
        },
        "classified_branch": "PAIRING_DESCENDS_ONLY_TO_QUOTIENT_NO_DIVISIBLE_CORANK_CONTROL",
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        "authority": {"source_theorem": "STORED_PRIMARY_SOURCE", "countermodel": "ELEMENTARY_GROUP_THEORETIC_PROOF", "formal_proof": False, "independent_review": False, "novelty_claim": False, "root_promotion": False},
    })


def lesson_document(source: dict) -> dict:
    return seal({
        "record_type": "BSD_R16_SEVEN_FIELD_MATHEMATICAL_LESSON",
        "atom_id": ATOM,
        "attempted_mathematical_implication": "Cassels--Tate alternation/nondegeneracy -> corank_Zp Sha(E/Q)[p^infinity]=0 ->, after exact Selmer corank two, rank E(Q)=2.",
        "exact_mathematical_result_or_failure": "The route fails as a standalone implication: nondegeneracy is on Sha/D, where D is the maximal divisible subgroup. The theorem controls the nondivisible quotient, not corank D. The explicit divisible-group countermodel shows it implies neither D=0 nor parity of corank D.",
        "supported_and_competing_mathematical_causes": {
            "supported": "The source theorem asserts nondegeneracy only after quotienting by D, so it supplies no control on the size or corank of the removed divisible subgroup.",
            "competing": [
                {"cause": "alternation forces D to have even corank", "status": "REFUTED_BY_r_EQUALS_1_COUNTERMODEL"},
                {"cause": "square order of finite Sha forces finiteness", "status": "REVERSED_DIRECTION_FINITE_IS_A_PREMISE"},
                {"cause": "the pairing plus an additional theorem controlling D may still prove finiteness", "status": "OPEN_NOT_REFUTED"},
            ],
        },
        "scope": "Logical sufficiency of the exact Poonen--Stoll/Cassels pairing properties for the R15 p-primary divisible-corank slack, for the same E/Q and p. This is not an existence claim for infinite Sha, not a refutation of Cassels--Tate theory, and not a blacklist on pairing methods combined with independent input.",
        "mathematical_falsifier": "A theorem derived solely from the frozen pairing properties that forces corank D=0 would have to exclude M=(Q_p/Z_p, zero pairing), whose quotient is zero with nondegenerate alternating induced pairing. Thus that implication is impossible without an additional hypothesis not present in the pairing properties.",
        "repair_or_next_discriminator": "Seek an independent same-E/Q theorem forcing D=0 (equivalently p-primary Sha finiteness in the R15 cofinite scope) from input no stronger than the active analytic/arithmetic data, or construct two independent rational points. Use Cassels--Tate only downstream to constrain the finite quotient/order; do not use it to prove its own radical vanishes.",
        "proof_or_source_evidence": [PATHS["source"], "Poonen--Stoll arXiv:math/9911267v1, abstract/introduction/Section 2", "elementary countermodel M=(Q_p/Z_p)^r with zero pairing"],
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        "zero_math_credit": ["Git/branch/PR state", "CI/tests", "schemas/hashes/chronology", "telemetry/repository growth"],
    })


def obstruction() -> ObstructionFingerprint:
    return ObstructionFingerprint(
        obstruction_id="O-BSD-R16-DIVISIBLE-RADICAL-SLACK", domain="arithmetic_geometry",
        roles=("exact_selmer_corank", "mordell_weil_rank", "divisible_sha_slack", "pairing", "pairing_radical_or_quotient"),
        relations=("selmer_corank_equals_rank_plus_sha_corank", "pairing_structure_may_apply_only_after_quotient"),
        constraints=("same_E_Q_and_p", "no_Sha_finiteness_premise", "exact_pairing_hypotheses", "p_equals_2_scope_explicit"),
        failure_mechanisms=("radical_is_invisible_to_pairing", "finite_quotient_parity_misapplied_to_divisible_corank", "target_assumed_as_hypothesis"),
        invariants_to_preserve=("R15_exact_corank_identity", "same_curve_and_prime", "proof_direction", "root_remains_open"),
        desired_transition=("determine_exact_pairing_implication_for_corank_of_maximal_divisible_sha_subgroup",),
        forbidden_losses=("replace_D_by_Sha_mod_D", "assume_D_zero", "infer_zero_from_even_parity", "ignore_2_primary_scope"),
    )


def postresult_memory(source: dict):
    obs = obstruction()
    episode_core = ObstructionTransformationEpisode(
        episode_id="OTEP-BSD-R16-CASSELSTATE-RADICAL-QUOTIENT", source_domain="arithmetic_geometry",
        source_context="Cassels--Tate pairing for elliptic curves over global fields, as stated by Poonen--Stoll",
        source_obstruction=obs, transformation_name="quotient by the maximal divisible subgroup before invoking nondegeneracy",
        operation="replace Sha by Sha_nd=Sha/D before invoking nondegeneracy; retain D as an independent uncontrolled coordinate",
        preconditions=("E is an elliptic curve over a global field", "D is the maximal divisible subgroup of Sha(E)", "use the Cassels--Tate pairing and its elliptic-curve alternation theorem"),
        resulting_relations=("determine_exact_pairing_implication_for_corank_of_maximal_divisible_sha_subgroup", "nondegenerate_alternating_pairing_on_Sha_mod_D", "D_corank_remains_uncontrolled"),
        preserved_invariants=("same E and p", "R15 corank identity", "pairing theorem direction", "finite Sha remains an extra hypothesis"),
        relaxed_or_broken_constraints=("nondegeneracy_on_full_Sha",),
        known_breakpoints=("cannot infer D=0", "cannot infer parity of corank D", "finite-order square consequence assumes finiteness"),
        evidence_pointers=(PATHS["source"], source["source"]["url"]), authority=TransformationEpisodeAuthority.SOURCE_EVENT_VERIFIED,
        artifact_hash="", lineage_ids=("LEM-BSD-R15-KUMMER-SHA-CORANK-DECOMPOSITION",),
    )
    episode = replace(episode_core, artifact_hash=canonical_hash(asdict(episode_core)))
    return build_transformation_memory(
        memory_id="OTM-BSD-R16-POSTRESULT-20260812", source_universe=("Poonen--Stoll arXiv:math/9911267v1", "merged BSD R15 result"),
        episodes=(episode,), evidence_pointers=(PATHS["source"], PRE_GATE),
    )


def postresult_review(context_hash: str, pre_memory_hash: str, memory):
    episode = memory.episodes[0]
    preconditions = tuple((item, "verified by Poonen--Stoll source scope and target specialization E/Q") for item in episode.preconditions)
    witness_core = StructuralMappingWitness(
        witness_id="SMW-BSD-R16-CASSELSTATE-SAME-DOMAIN", episode_id=episode.episode_id,
        target_obstruction_id=obstruction().obstruction_id,
        role_mapping=tuple((role, role) for role in obstruction().roles),
        shared_relations=obstruction().relations,
        shared_constraints=obstruction().constraints,
        precondition_mapping=preconditions, unmatched_source_preconditions=(),
        disanalogies=("Poonen--Stoll treats the full global Sha while R15 targets one p-primary component; primary decomposition supplies the specialization.",),
        target_validation_obligations=("keep D distinct from Sha/D", "do not convert conditional finite-order consequences into finiteness"),
        evidence_pointers=(PATHS["source"], PATHS["lesson"]), artifact_hash="",
    )
    witness = replace(witness_core, artifact_hash=canonical_hash(asdict(witness_core)))
    review_core = ObstructionTransformationReview(
        review_id="OTR-BSD-R16-POSTRESULT-SEARCH-20260812", target_atom_id=ATOM,
        target_context_hash=context_hash, research_memory_review_hash=pre_memory_hash,
        episode_memory_snapshot_hash=memory.snapshot_hash, obstruction=obstruction(),
        direct_search_status=RouteSearchStatus.MATCHES_FOUND, jump_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        glue_search_status=RouteSearchStatus.NO_VIABLE_MATCH, selected_mode=ShortcutMode.SEARCH,
        direct_candidate_episode_ids=(episode.episode_id,), direct_mapping_witnesses=(witness,), selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=("This post-result assimilation does not retroactively authorize candidate generation or claim discovery chronology.",),
        evidence_pointers=(PATHS["source"], PATHS["lesson"], PATHS["transformation_memory"]), artifact_hash="",
    )
    return replace(review_core, artifact_hash=canonical_hash(asdict(review_core)))


def failure_document(context_hash: str, lesson: dict) -> dict:
    core = FailureExperience(
        failure_id="F-BSD-R16-PAIRING-QUOTIENT-BLIND-TO-DIVISIBLE-CORANK", atom_id=ATOM,
        candidate_id="NO_MATHEMATICAL_CANDIDATE_R16_PREDECLARED_SOURCE_DISCRIMINATOR",
        context_packet_hash=context_hash, research_trace_event_id="BSD-R16-E10",
        method_family="Cassels--Tate alternating/nondegenerate pairing as a repair for p-primary divisible Sha corank slack",
        failure_mode="The pairing becomes nondegenerate only after quotienting by the maximal divisible subgroup whose corank is the target.",
        residual_signature=("EXACT_SELMER_CORANK_TWO_TO_P_PRIMARY_SHA_FINITE_OR_INDEPENDENT_MW_RANK_TWO", "PAIRING_CONTROLS_ONLY_NONDIVISIBLE_QUOTIENT"),
        broken_assumptions=("nondegeneracy applies to the full Sha including D", "alternation forces D=0 or even corank", "square order consequence proves finiteness"),
        scope_conditions=("same elliptic curve E/Q and prime p", "only exact Cassels--Tate pairing properties plus R15 corank decomposition", "countermodel is logical and does not assert arithmetic realizability", "reuse remains allowed with independent D-control input"),
        competing_diagnoses=("pairing forces zero divisible corank", "pairing forces even divisible corank", "pairing controls only Sha/D", "p=2 invalidates elliptic alternation"),
        selected_diagnosis="VERIFIED_SCOPED_NONIMPLICATION: the quotient pairing is blind to D; the r=1 divisible countermodel refutes both zero and parity inferences from these axioms alone.",
        diagnosis_status=FailureDiagnosisStatus.VERIFIED_IMPOSSIBILITY,
        evidence_pointers=(PATHS["source"], PATHS["lesson"]),
        falsifier_or_attempt=lesson["mathematical_falsifier"], observed_result=lesson["exact_mathematical_result_or_failure"],
        artifact_hash="", timestamp="2026-08-12T11:45:00Z",
        local_repair_attempts=("restricted pairing by primary decomposition", "separated D from Sha/D", "tested r=1 and arbitrary-r divisible countermodels"),
    )
    experience = replace(core, artifact_hash=canonical_hash(asdict(core)))
    assert not validate_failure_experience(experience)
    return jsonable(asdict(FailureExperienceLattice(experiences=(experience,), links=())))


def append_trace(pre_trace: dict, source: dict, lesson: dict, failure: dict, shortcut) -> MathResearchTrace:
    old = []
    for item in pre_trace["entries"]:
        old.append(ResearchTraceEntry(
            event_id=item["event_id"], atom_id=item["atom_id"], event_type=ResearchTraceEventType(item["event_type"]),
            timestamp=item["timestamp"], state_summary=item["state_summary"], action_summary=item["action_summary"],
            evidence_pointers=tuple(item["evidence_pointers"]), alternatives_considered=tuple(item.get("alternatives_considered", [])),
            decision_rationale=item.get("decision_rationale", ""), outputs=tuple(item.get("outputs", [])),
            uncertainties=tuple(item.get("uncertainties", [])), residuals=tuple(item.get("residuals", [])),
            next_steps=tuple(item.get("next_steps", [])), artifact_hash=item["artifact_hash"], previous_event_hash=item.get("previous_event_hash", ""),
        ))
    specs = (
        (ResearchTraceEventType.FALSIFIER_RUN, "Public pre-result freeze is durable; source access authorized.", "Check exact pairing domain/radical/quotient and run the divisible-group countermodel.", (PATHS["source"],), (source["classified_branch"],), (), ()),
        (ResearchTraceEventType.RESULT_RECORDED, "Cassels--Tate is nondegenerate on Sha/D, not on D.", "Classify the frozen result branch and retain the seven-field lesson.", (PATHS["source"], PATHS["lesson"]), (lesson["exact_mathematical_result_or_failure"],), ("No arithmetic example with infinite D is claimed or needed for the logical nonimplication.",), ()),
        (ResearchTraceEventType.RESIDUAL_OPENED, "Pairing-only repair is refuted in its exact standalone scope.", "Open independent D=0 or rational-point construction residual.", (PATHS["failure"],), (), (), (lesson["repair_or_next_discriminator"],)),
        (ResearchTraceEventType.REVIEWED, "Role-separated same-context review accepts only the scoped nonimplication.", "Assimilate the verified source episode without calling the review independent.", (shortcut.artifact_hash, PATHS["lesson"]), ("domain: quotient theorem is exact", "transfer: p-primary decomposition is valid", "falsification: r=1 refutes parity", "formal: countermodel proves logical insufficiency", "novelty: stored theorem plus new local routing diagnosis only"), ("No formal proof or independent external mathematical review.",), (lesson["repair_or_next_discriminator"],)),
    )
    entries = list(old)
    for offset, spec in enumerate(specs, 9):
        core = ResearchTraceEntry(
            event_id=f"BSD-R16-E{offset:02d}", atom_id=ATOM, event_type=spec[0], timestamp=f"2026-08-12T11:{35 + offset:02d}:00Z",
            state_summary=spec[1], action_summary=spec[2], evidence_pointers=spec[3],
            outputs=spec[4], uncertainties=spec[5], residuals=("PAIRING_BLIND_TO_D",) if spec[0] is ResearchTraceEventType.RESIDUAL_OPENED else (),
            next_steps=spec[6], artifact_hash="", previous_event_hash=entries[-1].artifact_hash,
        )
        entries.append(replace(core, artifact_hash=canonical_hash(asdict(core))))
    return MathResearchTrace(trace_id="TRACE-BSD-R16-RESULT-20260812", entries=tuple(entries))


def dag_document(lesson: dict) -> dict:
    return seal({
        "record_type": "BSD_R16_PROOF_DAG_DELTA", "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
        "parent_atom": "BSD-A1a3-COMPLEX-RANK-TWO-TO-P-PRIMARY-SHA-FINITENESS-OR-INDEPENDENT-MW-RANK-TWO",
        "refuted_route": {"id": "BSD-A1a3-CASSELSTATE-PAIRING-ALONE-FORCES-D-ZERO", "scope": "Cassels--Tate alternation/nondegeneracy without independent D-control", "proof": "divisible-group countermodel", "pointer": PATHS["lesson"]},
        "retained_downstream_use": "After an independent theorem proves D=0/finite Sha, Cassels--Tate alternation constrains the finite nondivisible quotient/order; it does not provide that independent theorem.",
        "open_children": ["same-E/Q theorem forcing p-primary Sha finiteness from admissible upstream data", "independent construction of two rational points", "separate refined Sha-order/regulator/local-factor/period leading-term obligations"],
        "next_discriminator": lesson["repair_or_next_discriminator"],
    })


def build_documents(root: Path = Path(".")) -> dict[str, dict]:
    pre_gate, pre_trace, context = load(root, PRE_GATE), load(root, PRE_TRACE), load(root, PRE_CONTEXT)
    source = source_document(pre_gate)
    lesson = lesson_document(source)
    memory = postresult_memory(source)
    shortcut = postresult_review(context["packet_hash"], pre_gate["document_hashes"]["memory"], memory)
    shortcut_report = audit_obstruction_transformation_review(
        shortcut, atom_id=ATOM, context_hash=context["packet_hash"],
        research_memory_review_hash=pre_gate["document_hashes"]["memory"], transformation_memory=memory,
    )
    if shortcut_report.verdict.value != "PASS":
        raise RuntimeError(shortcut_report.reasons)
    failure = failure_document(context["packet_hash"], lesson)
    trace = append_trace(pre_trace, source, lesson, failure, shortcut)
    trace_report = audit_research_trace(trace)
    if trace_report.verdict.value != "PASS":
        raise RuntimeError(trace_report.reasons)
    return {
        "source": source, "lesson": lesson, "failure": failure,
        "transformation_memory": jsonable(asdict(memory)), "shortcut": jsonable(asdict(shortcut)),
        "trace": jsonable(asdict(trace)), "dag": dag_document(lesson),
    }


def write(root: Path = Path(".")) -> None:
    for key, value in build_documents(root).items():
        path = root / PATHS[key]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write()
