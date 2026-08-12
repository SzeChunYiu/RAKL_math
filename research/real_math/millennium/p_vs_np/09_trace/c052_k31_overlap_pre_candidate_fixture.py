"""Freeze the C052 k=31 actual-overlap context before any candidate or result.

This serializer imports no C041 decoder and has no SAT, formula construction,
overlap comparison, or result capability.  It binds only already-public source
bytes and the public k=31 support/witness summary from the off-window result.
"""

from __future__ import annotations

from dataclasses import asdict, replace
from enum import Enum
import hashlib
import json
from pathlib import Path

from rakl.math_context import AnalogyScanStatus, CrossDomainAnalogy, MathContextFiber, MethodTransfer
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import MemoryQueryStatus, ResearchMemoryReview
from rakl.research_trace import MathResearchTrace, ResearchTraceEntry, ResearchTraceEventType
from rakl.semantic_shortcut import (
    ObstructionFingerprint,
    ObstructionTransformationEpisode,
    ObstructionTransformationReview,
    RouteSearchStatus,
    ShortcutMode,
    TransformationEpisodeAuthority,
    build_transformation_memory,
)


ROOT = Path(__file__).resolve().parents[5]
BASE = "research/real_math/millennium/p_vs_np"
PNP = ROOT / BASE
ATOM = "O9d12a2a1b-C052-K31-OVERLAP"
APPLICATION_BASE_SHA = "686a73336f00ebc9f9441c0c3f64042f5caf046f"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
TIMES = (
    "2026-08-12T14:35:39Z", "2026-08-12T14:35:40Z", "2026-08-12T14:35:41Z",
    "2026-08-12T14:35:42Z", "2026-08-12T14:35:43Z", "2026-08-12T14:35:44Z",
    "2026-08-12T14:35:45Z", "2026-08-12T14:35:46Z",
)

PATHS = {
    "context": f"{BASE}/01_frontier/O9d12a2a1b_C052_K31_OVERLAP_CONTEXT_20260812.json",
    "atomization": f"{BASE}/02_problem_dag/O9d12a2a1b_C052_K31_OVERLAP_ATOMIZATION_20260812.json",
    "memory": f"{BASE}/07_memory/O9d12a2a1b_C052_K31_OVERLAP_RESEARCH_MEMORY_REVIEW_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/O9d12a2a1b_C052_K31_OVERLAP_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/O9d12a2a1b_C052_K31_OVERLAP_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/O9d12a2a1b_C052_K31_OVERLAP_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "firewall": f"{BASE}/09_trace/O9d12a2a1b_C052_K31_OVERLAP_CERTIFICATE_FIREWALL_20260812.json",
    "trace": f"{BASE}/09_trace/O9d12a2a1b_C052_K31_OVERLAP_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": f"{BASE}/09_trace/O9d12a2a1b_C052_K31_OVERLAP_PRE_CANDIDATE_GATE_RECEIPT_20260812.json",
}

SOURCE_BINDINGS = {
    "c041_grammar": {
        "path": f"{BASE}/04_candidates/C041_fx_sat_one_sided.py",
        "raw_sha256": "sha256:c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a",
        "git_blob": "fcc4814dd618da96ef9bb8144a4783a0a6e886e1",
    },
    "c048_transfer_condition": {
        "path": f"{BASE}/04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_TRANSFER_CONDITION_FREEZE_20260812.json",
        "raw_sha256": "sha256:e2a924e708c1ab17b78e06a3935fd48772c0c172b9f01b0c756de80f1430908b",
        "artifact_hash": "sha256:b03a1090e7b25222dc2377e309b8600b6e2064d6fc74f702b1f3f984d68cff5e",
        "git_blob": "fed9057163bec46325115e8f6cfbb5c6f3c3d485",
    },
    "c048_proof_certificate": {
        "path": f"{BASE}/04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_PROOF_CERTIFICATE_FREEZE_20260812.json",
        "raw_sha256": "sha256:fd4d478d816c50423f2d6fbd668305bec911bcf3a035a2a5b516eb08796ec16c",
        "artifact_hash": "sha256:84ebf84c9b90a99c3f5e348bacad53ee1d700e2d0c746805cf4b8a0439cd1e33",
        "git_blob": "1283219dec4d6a39cf43d5f2d9a4fafa1883d016",
    },
    "offwindow_proof": {
        "path": f"{BASE}/04_candidates/O9d12a2a1b_C052_V21_OFFWINDOW_SYMBOLIC_HAND_PROOF_20260812.json",
        "raw_sha256": "sha256:28be0eba0d1c4610c07c034911e627d31c276e34474186b70259f4a0480cc494",
        "artifact_hash": "sha256:cd51bbf8ae9acc0a2e2c77f7d8e6c052c3c3a1e9a22b50ddee6271663e6699f7",
        "git_blob": "56255112e4d5a7e3c962c7eb7ffb423fe92c51f6",
    },
    "offwindow_result": {
        "path": f"{BASE}/09_trace/O9d12a2a1b_C052_V21_OFFWINDOW_RESULT_RECEIPT_20260812.json",
        "raw_sha256": "sha256:58d86baf589fa3be1acc8ba599ac4aa0286a152ce4309ddfc1873d0000634b46",
        "artifact_hash": "sha256:c11023a75afaf8128d3b3233cd50eec6de63c762a335adefcece139620ffe42d",
        "git_blob": "d0b7511848924e6ef87fb2b090fab8fd821d6388",
    },
    "offwindow_experience": {
        "path": f"{BASE}/07_memory/O9d12a2a1b_C052_V21_OFFWINDOW_MATHEMATICAL_EXPERIENCE_20260812.json",
        "raw_sha256": "sha256:a6bf9f14a65af46e2c954723e4e0f565fb717aeaecb3191447779bb099672074",
        "artifact_hash": "sha256:df07e8fe9f84c16dc9ecd6dce0adda5d5fac82673f922363764b47f34e1f5ae5",
        "git_blob": "57f2f024c3620c1679b79773fb23a9bf892d4e1d",
    },
}

PARENT_CELL = {"k": 31, "encoded_length": 62, "a": 2, "b": 3, "m": 5, "v_range": [2, 3], "raw_length": 61, "padding": 1}
CURRENT_CELLS = [
    {"encoded_length": 64, "a": 1, "b": 4, "m": 8, "v_range": [1, 1], "raw_length": 64, "padding": 0},
    {"encoded_length": 64, "a": 4, "b": 2, "m": 3, "v_range": [8, 15], "raw_length": 63, "padding": 1},
    {"encoded_length": 64, "a": 6, "b": 2, "m": 2, "v_range": [32, 63], "raw_length": 64, "padding": 0},
]


def _hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _jsonable(value):
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, tuple):
        return [_jsonable(item) for item in value]
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    return value


def _document(value) -> dict:
    return _jsonable(asdict(value))


def _seal(value: dict) -> dict:
    result = dict(value)
    result.pop("artifact_hash", None)
    result["artifact_hash"] = _hash(result)
    return result


def _assert_sources() -> None:
    for binding in SOURCE_BINDINGS.values():
        path = ROOT / binding["path"]
        if "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest() != binding["raw_sha256"]:
            raise RuntimeError(f"source bytes moved: {binding['path']}")
        if path.suffix == ".json" and "artifact_hash" in binding:
            if json.loads(path.read_text(encoding="utf-8"))["artifact_hash"] != binding["artifact_hash"]:
                raise RuntimeError(f"source artifact moved: {binding['path']}")


def context_fiber() -> MathContextFiber:
    anchors = tuple(
        f"git:{APPLICATION_BASE_SHA}:{row['path']}@blob:{row['git_blob']}"
        for row in SOURCE_BINDINGS.values()
    )
    transfer = MethodTransfer(
        source_context="C048 exact literal-transpose collision equivalence plus C052 off-window marginal lemma",
        method="separate local obstruction escape from the exact full-word intersection and require branch-specific certificates",
        shared_structure=(
            "H_31 consists of 1 prepended to a 31-bit suffix of an exact canonical UNSAT length-62 word",
            "P_32 consists of 32-bit prefixes of exact canonical length-64 words",
            "literal-transpose row collision is equivalent to H_31 intersection P_32 nonempty",
            "parent and current support cells are public and finite in parameter coordinates",
        ),
        required_assumptions=(
            "C041 grammar, equal split, MAGIC header, and C048 literal transpose remain byte-identical",
            "positive evidence binds one full 32-bit label to both formula-bound memberships",
            "negative evidence quantifies every H_31 and P_32 member rather than only eight leading coordinates",
            "UNSAT evidence is semantic and cannot be replaced by ambient encoding variability",
        ),
        disanalogies=(
            "the off-window lemma proves coordinate-wise marginals using different formulas, not joint 32-bit coverage",
            "public k31 regression witnesses certify H_31 nonemptiness and marginal variation, not overlap",
            "support-cell exhaustion does not enumerate the word languages inside the cells",
        ),
        repair_question="What candidate-independent positive or negative certificate would decide the exact full-label intersection without reading its result now?",
        source_anchors=anchors,
    )
    analogy = CrossDomainAnalogy(
        source_kind="engineering / protocol handshake",
        source_situation="each endpoint may vary every field marginally while no complete handshake message is shared",
        common_abstraction=("two constrained languages", "marginal field flexibility", "exact whole-message equality"),
        source_to_target_mapping=("endpoint A language -> H_31", "endpoint B language -> P_32", "handshake message -> common 32-bit label"),
        shared_constraints=("membership is endpoint-specific", "success requires one identical full message", "marginals do not compose automatically"),
        disanalogies=("protocol engineering supplies no theorem authority", "H_31 membership additionally requires canonical UNSAT evidence"),
        proposed_principle="freeze whole-object positive and universal negative certificates before choosing a search construction",
        validation_obligation="reject any certificate based only on coordinate-wise marginals, ambient syntax, or a partial prefix match",
        provenance_note="proposal-only ordinary engineering analogy; zero mathematical authority",
    )
    draft = MathContextFiber(
        atom_id=ATOM,
        object_context="The exact fixed-level set intersection H_31 ∩ P_32 under unchanged C041 canonical encoding, equal split, MAGIC header, and C048 literal-transpose definitions.",
        structural_coordinates=(
            "H_31={1||c: exists r such that r||c is an exact canonical length-62 C041 encoding of an UNSAT 3CNF}",
            "P_32={first 32 bits of exact canonical C041 words of length 64}",
            f"exact parent support cell {PARENT_CELL}",
            f"exact exhaustive current support cells {CURRENT_CELLS}",
            "H_31 and P_32 are sets of 32-bit labels; the QoI is full equality, not coordinate marginals",
            "off-window theorem provides forall v forall j forall epsilon exists formula, not exists formula forall coordinates",
            "a positive answer requires one label with both formula-bound memberships",
            "a negative answer requires a universal separation/completeness certificate",
        ),
        equivalent_formulations=(
            "existence of a canonical UNSAT length-62 suffix c equal to the final 31 bits of a canonical length-64 prefix beginning with 1",
            "exact literal-transpose high-row/current-prefix collision at k=31",
            "nonempty intersection of two finite formula-bound code languages",
        ),
        solved_analogues=("C049 k=12, C050 k=15, and C051 k=19 exact empty intersections by bounded forced-coordinate certificates",),
        near_solved_analogues=("C052 off-window theorem removes only the h[0..7] forced-MAGIC obstruction at k=31",),
        method_transfers=(transfer,),
        explicit_disanalogies=(
            "local coordinate escape is not a common full label",
            "one public H_31 witness is not an overlap witness",
            "current support existence is not membership of any chosen H_31 label",
            "computation is not proof; Git, CI, hashes, and trace add zero mathematics",
            "same-context role review is not independent peer review",
        ),
        source_anchors=anchors,
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(analogy,),
        analogy_scan_notes="One whole-message intersection analogy survives only as a certificate-design prompt.",
        frozen_at=TIMES[1],
        first_candidate_at=None,
        packet_hash="",
    )
    return replace(draft, packet_hash=_hash(_document(draft)))


def memory_review(context: MathContextFiber) -> ResearchMemoryReview:
    tools = {
        "T-PNP-C048-EXACT-OVERLAP-TRANSFER-CONDITION": "collision iff H_k intersects P_(k+1)",
        "MATH-PNP-C052-OFFWINDOW-UNSAT-ANCHOR-20260812": "scoped marginal escape theorem, not universal tool",
    }
    failures = {
        "F-PNP-C049-K12-EXACT-OVERLAP-EMPTY": "bounded empty intersection",
        "F-PNP-C050-K15-FIXED-VARIABLE-BIT-VERSUS-MAGIC": "bounded forced-coordinate separation",
        "F-PNP-C051-K19-FIXED-VARIABLE-BIT-VERSUS-MAGIC": "bounded forced-coordinate separation",
        "F-PNP-C052-V1-UNSAT-SUBSET-OMISSION": "ambient variation omitted H_k semantics",
        "F-PNP-C052-V2-INVALID-TRAP-DOMAIN-AND-FUTURE-TIMESTAMP": "out-of-domain trap has zero authority",
    }
    draft = ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context.packet_hash,
        tool_inventory_snapshot_hash=_hash(tools),
        failure_lattice_snapshot_hash=_hash(failures),
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=("exact language-intersection certificate", "universal separator", "complete finite formula-bound enumeration"),
        relevant_tool_ids=tuple(tools),
        relevant_failure_ids=tuple(failures),
        selected_tool_ids=("T-PNP-C048-EXACT-OVERLAP-TRANSFER-CONDITION",),
        tool_applicability_notes=(
            "C048 fixes the QoI equivalence but does not decide k31",
            "the off-window result may prune local forced-coordinate arguments only inside its scope",
        ),
        failure_reuse_notes=(
            "k12/k15/k19 warn that support does not imply overlap but cannot be extrapolated to k31",
            "v1 requires formula-bound H_31 evidence; ambient syntax is rejected",
            "the old v2 trap is preserved as zero-authority negative history",
        ),
        unresolved_warnings=(
            "marginal witnesses may differ at all other coordinates",
            "no full-label positive or universal negative certificate is frozen yet",
            "actual overlap result remains inaccessible",
        ),
        evidence_pointers=tuple(row["path"] for row in SOURCE_BINDINGS.values()),
        artifact_hash="",
    )
    return replace(draft, artifact_hash=_hash(_document(draft)))


def obstruction_bundle(context: MathContextFiber, memory: ResearchMemoryReview):
    source = ObstructionFingerprint(
        obstruction_id="O-PNP-C052-LOCAL-FORCED-COORDINATE",
        domain="fixed-level canonical code language",
        roles=("UNSAT suffix language", "current prefix language"),
        relations=("first eight coordinates compared to MAGIC",),
        constraints=("UNSAT membership", "canonical encoding"),
        failure_mechanisms=("one universally unequal coordinate separates the languages",),
        invariants_to_preserve=("canonicality", "UNSAT", "exact length"),
        desired_transition=("remove the forced-coordinate separator",),
        forbidden_losses=("ambient-only variation",),
    )
    episode_core = {
        "episode_id": "E-PNP-C052-OFFWINDOW-ANCHOR-DECOUPLING",
        "source_domain": "P-vs-NP C041 code language",
        "source_context": "off-window UNSAT anchor marginal theorem",
        "source_obstruction": _document(source),
        "transformation_name": "decouple UNSAT anchor from touched window",
        "operation": "reserve untouched opposite repeated-unit clauses and vary one touched coordinate",
        "preconditions": ["a>=2", "m>=4", "window in unpadded payload", "two untouched clauses"],
        "resulting_relations": ["every h[1..7] coordinate has both H_k marginals", "no local forced-MAGIC coordinate remains"],
        "preserved_invariants": ["canonical encoding", "UNSAT", "exact length"],
        "relaxed_or_broken_constraints": ["fixed local coordinate"],
        "known_breakpoints": ["does not produce joint patterns", "does not prove overlap"],
        "evidence_pointers": [SOURCE_BINDINGS["offwindow_proof"]["path"], SOURCE_BINDINGS["offwindow_result"]["path"]],
        "authority": TransformationEpisodeAuthority.PROOF_BACKED.value,
        "lineage_ids": ["PNP-C052-OFFWINDOW-UNSAT-ANCHOR-MARGINAL-LEMMA-v1"],
    }
    episode = ObstructionTransformationEpisode(
        episode_id=episode_core["episode_id"], source_domain=episode_core["source_domain"], source_context=episode_core["source_context"],
        source_obstruction=source, transformation_name=episode_core["transformation_name"], operation=episode_core["operation"],
        preconditions=tuple(episode_core["preconditions"]), resulting_relations=tuple(episode_core["resulting_relations"]),
        preserved_invariants=tuple(episode_core["preserved_invariants"]), relaxed_or_broken_constraints=tuple(episode_core["relaxed_or_broken_constraints"]),
        known_breakpoints=tuple(episode_core["known_breakpoints"]), evidence_pointers=tuple(episode_core["evidence_pointers"]),
        authority=TransformationEpisodeAuthority.PROOF_BACKED, artifact_hash=_hash(episode_core), lineage_ids=tuple(episode_core["lineage_ids"]),
    )
    transformation_memory = build_transformation_memory(
        memory_id="PNP-C052-K31-OVERLAP-TRANSFORMATION-MEMORY-20260812",
        source_universe=("C048 exact overlap equivalence", "C052 off-window theorem", "C049/C050/C051 empty overlap certificates"),
        episodes=(episode,), evidence_pointers=tuple(row["path"] for row in SOURCE_BINDINGS.values()),
    )
    target = ObstructionFingerprint(
        obstruction_id="O-PNP-C052-K31-FULL-LABEL-INTERSECTION",
        domain="exact finite formula-bound code-language intersection",
        roles=("H_31 member", "P_32 member", "common 32-bit label"),
        relations=("same full label must have both memberships",),
        constraints=("canonical length 62 UNSAT parent", "canonical length 64 current word", "unchanged C048 transpose"),
        failure_mechanisms=("marginal flexibility fails to compose into one common label", "unproved membership or enumeration completeness"),
        invariants_to_preserve=("C041 grammar", "UNSAT semantics", "equal split", "full 32-bit equality"),
        desired_transition=("certify nonempty intersection or certify universal disjointness",),
        forbidden_losses=("ambient-only variation", "partial-prefix match", "marginal-to-joint quantifier swap"),
    )
    draft = ObstructionTransformationReview(
        review_id="PNP-C052-K31-OVERLAP-SHORTCUT-REVIEW-20260812",
        target_atom_id=ATOM, target_context_hash=context.packet_hash, research_memory_review_hash=memory.artifact_hash,
        episode_memory_snapshot_hash=transformation_memory.snapshot_hash, obstruction=target,
        direct_search_status=RouteSearchStatus.NO_VIABLE_MATCH, jump_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        glue_search_status=RouteSearchStatus.NO_VIABLE_MATCH, selected_mode=ShortcutMode.CANNOT_CHECK,
        unresolved_warnings=(
            "off-window transformation breaks only an eight-coordinate separator, not the full-label obstruction",
            "no recorded episode supplies a formula-bound common label or a universal k31 separator",
            "LIFT is not justified because bounded cross-problem coverage and two shared residual failures are not frozen for this exact obstruction",
        ),
        evidence_pointers=(PATHS["context"], PATHS["memory"], SOURCE_BINDINGS["offwindow_result"]["path"]), artifact_hash="",
    )
    review = replace(draft, artifact_hash=_hash(_document(draft)))
    return transformation_memory, review


def trace(context: MathContextFiber, memory: ResearchMemoryReview, shortcut: ObstructionTransformationReview) -> MathResearchTrace:
    types = (
        ResearchTraceEventType.ATOMIZED, ResearchTraceEventType.CONTEXT_FROZEN, ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW, ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW, ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    )
    evidence = (
        (PATHS["atomization"],), (PATHS["context"],), (PATHS["context"],), (PATHS["context"],),
        (PATHS["expert_review"],), (PATHS["memory"],), (PATHS["shortcut_review"],), (PATHS["firewall"], PATHS["gate"]),
    )
    actions = (
        "Freeze the exact H_31 intersection P_32 atom under unchanged C041/C048 definitions.",
        "Freeze exact parent/current support cells, source identities, and full-label QoI.",
        "Retain whole-message handshake analogy only as a certificate-design prompt.",
        "Transfer exact overlap equivalence while rejecting marginal-to-joint inference.",
        "Run role-separated same-context review of positive/negative certificate obligations.",
        "Bind C048 transfer, C052 success, and prior exact empty-overlap failures.",
        "Ask whether recorded transformations break the full-label obstruction; answer CANNOT_CHECK.",
        "Publish candidate-independent certificate requirements and result firewall; do not freeze a candidate.",
    )
    bound_outputs = (
        (), (context.packet_hash,), (context.packet_hash,), (context.packet_hash,), (),
        (memory.artifact_hash,), (shortcut.artifact_hash, shortcut.episode_memory_snapshot_hash), (),
    )
    entries = []
    previous = ""
    for index, (event_type, timestamp, pointers, action, hashes) in enumerate(
        zip(types, TIMES, evidence, actions, bound_outputs), start=1
    ):
        draft = ResearchTraceEntry(
            event_id=f"O9d12a2a1b-C052-K31-OVERLAP-E{index:02d}", atom_id=ATOM, event_type=event_type,
            timestamp=timestamp,
            state_summary="Exact k31 overlap remains unaccessed; only pre-candidate context and certificate requirements are frozen.",
            action_summary=action, evidence_pointers=tuple(pointers),
            alternatives_considered=("infer overlap from marginals", "run SAT/overlap now", "freeze candidate", "freeze result-blind certificate requirements"),
            decision_rationale="The public theorem removes one local obstruction but does not decide the full 32-bit formula-bound language intersection.",
            outputs=tuple(hashes) + ("PRE_CANDIDATE_ONLY", "OVERLAP_RESULT_UNACCESSED", "ZERO_GIT_CI_TRACE_MATH_CREDIT"),
            uncertainties=("no full-label certificate selected", "same-context review is not independent"),
            residuals=("H_31 intersection P_32 unresolved", "P-versus-NP root open"),
            next_steps=("merge this pre-candidate packet", "freeze any later candidate and evaluator only in a separate round"),
            artifact_hash="", previous_event_hash=previous,
        )
        entry = replace(draft, artifact_hash=_hash(_document(draft)))
        entries.append(entry)
        previous = entry.artifact_hash
    return MathResearchTrace(trace_id="PNP-C052-K31-OVERLAP-PRE-CANDIDATE-TRACE-20260812", entries=tuple(entries))


def custom_documents(context: MathContextFiber, memory: ResearchMemoryReview, shortcut: ObstructionTransformationReview) -> dict:
    positive = [
        "one exact 32-bit label h",
        "one exact canonical length-62 parent word r||c from the frozen parent cell with h=1||c",
        "formula-bound proof that the parent 3CNF is UNSAT, hence h is in H_31",
        "one exact canonical length-64 current word from one frozen current cell whose first 32 bits equal h",
        "byte-for-byte full-label equality and unchanged C048 literal-transpose binding",
    ]
    negative = [
        "a universal invariant separating every formula-bound H_31 member from every P_32 member, or an exhaustive enumeration with a proof of completeness",
        "complete coverage of v in {2,3}, every canonical parent formula, and semantic UNSAT membership",
        "complete coverage of all three current support cells and every canonical current formula",
        "a checked argument that no identical 32-bit label has both memberships",
        "fail closed if canonicality, UNSAT, source identity, or enumeration completeness is missing",
    ]
    atomization = _seal({
        "schema_version": "1.0.0", "atom_id": ATOM, "parent_atom_id": "O9d12a2a1b-C052-V2.1",
        "object": "exact H_31 intersection P_32", "qoi": "NONEMPTY_OR_EMPTY_OR_CANNOT_CHECK",
        "atomic_obstruction": "coordinate-wise H_31 marginals do not decide existence of one common full 32-bit label",
        "application_base_sha": APPLICATION_BASE_SHA, "target_result_accessed": False, "candidate_identity": None,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    expert = _seal({
        "schema_version": "1.0.0", "review_id": "PNP-C052-K31-OVERLAP-EXPERT-CONTEXT-REVIEW-20260812", "atom_id": ATOM,
        "context_hash": context.packet_hash, "memory_hash": memory.artifact_hash,
        "role_reviews": [
            {"role": "domain_theory_lead", "finding": "C048 makes full language intersection the exact QoI; off-window marginals are insufficient."},
            {"role": "analogy_method_transfer_lead", "finding": "Transfer whole-message certificate design, not protocol authority."},
            {"role": "adversarial_falsification_lead", "finding": "Reject partial prefixes, ambient words, non-formula-bound UNSAT claims, and quantifier swaps."},
            {"role": "formal_methods_lead", "finding": "Positive and negative branches need exact source, membership, full equality, and checker boundaries."},
            {"role": "novelty_research_value_lead", "finding": "A bounded k31 answer would be scoped mathematics, not a circuit lower bound or P-vs-NP result."},
        ],
        "strongest_objection": "The 28 public regression witnesses were chosen separately for marginal obligations and cannot be treated as overlap candidates without a new public candidate freeze.",
        "disagreement": "Whether universal separation or complete enumeration is cheaper is unresolved; neither is selected here.",
        "recommendation": "Freeze candidate-independent certificates and firewall, then stop before candidate generation.",
        "review_authority": "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW",
    })
    firewall = _seal({
        "schema_version": "1.0.0", "firewall_id": "PNP-C052-K31-OVERLAP-CERTIFICATE-FIREWALL-20260812", "atom_id": ATOM,
        "source_bindings": SOURCE_BINDINGS, "parent_support_cell": PARENT_CELL, "exhaustive_current_support_cells": CURRENT_CELLS,
        "candidate_independent_positive_certificate_requirements": positive,
        "candidate_independent_negative_certificate_requirements": negative,
        "allowed_future_branches": ["NONEMPTY_WITH_EXACT_POSITIVE_CERTIFICATE", "EMPTY_WITH_EXACT_NEGATIVE_CERTIFICATE", "CANNOT_CHECK"],
        "chronology_firewall": {
            "formula_constructed_beyond_already_public_regression_witnesses": False,
            "public_regression_witness_bits_or_labels_compared": False,
            "SAT_or_UNSAT_executed": False, "overlap_executed_or_label_accessed": False,
            "candidate_or_evaluator_identity_frozen": False, "hidden_or_native_result_accessed": False,
        },
        "forbidden_in_this_round": ["construct a new formula or label", "compare any H_31 and P_32 labels", "run SAT, decoder, or overlap", "propose or freeze a candidate identity", "access an overlap result"],
        "zero_mathematical_credit": ["Git", "CI", "hashes", "schemas", "trace chronology", "same-context review"],
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    gate = _seal({
        "schema_version": "1.0.0", "gate_id": "PNP-C052-K31-OVERLAP-PRE-CANDIDATE-GATE-20260812", "atom_id": ATOM,
        "application_base_sha": APPLICATION_BASE_SHA, "framework_pin": FRAMEWORK_SHA,
        "context_hash": context.packet_hash, "memory_hash": memory.artifact_hash, "shortcut_review_hash": shortcut.artifact_hash,
        "licensed_action": "PUBLIC_MERGE_OF_PRE_CANDIDATE_PACKET_ONLY", "candidate_generation_in_this_round": False,
        "overlap_result_accessed": False, "mathematical_result_credit": 0, "git_ci_trace_mathematical_credit": 0,
        "next_round_requirement": "separate public candidate and falsifier freeze before any construction or comparison",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    return {"atomization": atomization, "expert_review": expert, "firewall": firewall, "gate": gate}


def build_objects():
    _assert_sources()
    context = context_fiber()
    memory = memory_review(context)
    transformation_memory, shortcut = obstruction_bundle(context, memory)
    research_trace = trace(context, memory, shortcut)
    return context, memory, transformation_memory, shortcut, research_trace


def build_plan():
    context, memory, transformation_memory, shortcut, research_trace = build_objects()
    return plan_math_research(
        signature=ProblemSignature(
            objects=("H_31", "P_32"), relations=("set intersection", "formula-bound membership", "full-label equality"),
            quantifiers=("exists common label for positive branch", "forall members for negative branch"),
            domain="finite canonical C041 code languages", goal_type="decide exact intersection",
            constraints=("unchanged C041/C048", "result blind", "candidate independent"),
        ),
        record=MathResearchRecord(claim_id=ATOM), context_fiber=context, memory_review=memory,
        transformation_memory=transformation_memory, shortcut_review=shortcut, research_trace=research_trace,
    )


def build_documents() -> dict:
    context, memory, transformation_memory, shortcut, research_trace = build_objects()
    documents = {
        "context": _document(context), "memory": _document(memory),
        "transformation_memory": _document(transformation_memory), "shortcut_review": _document(shortcut),
        "trace": _document(research_trace),
    }
    documents.update(custom_documents(context, memory, shortcut))
    return documents


def write() -> dict:
    documents = build_documents()
    for name, document in documents.items():
        path = ROOT / PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return documents


if __name__ == "__main__":
    write()
