"""Freeze the C053 k=32 structural-phase screen before any overlap candidate.

The fixture may inspect exact public field lengths, headers, token phases and
prior public result receipts.  It cannot decode formulas, call SAT, construct
overlap labels, inspect an overlap result, or freeze a candidate/evaluator.
"""

from __future__ import annotations

from dataclasses import asdict, replace
from enum import Enum
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

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
    StructuralMappingWitness,
    TransformationEpisodeAuthority,
    build_transformation_memory,
)


ROOT = Path(__file__).resolve().parents[5]
BASE = "research/real_math/millennium/p_vs_np"
PNP = ROOT / BASE
SCREEN_PATH = PNP / "03_routes/c053_k32_phase_screen.py"
ATOM = "O9d12a2a1b-C053-K32-PHASE-SCREEN"
APPLICATION_BASE_SHA = "ba9749865e99acf0a9751754cdee3931225804ef"
FRAMEWORK_SHA = "d21592b0ff8da988deabb923fd549891ff8ad9f0"
TIMES = tuple(f"2026-08-12T16:00:0{i}Z" for i in range(8))

PATHS = {
    "context": f"{BASE}/01_frontier/O9d12a2a1b_C053_K32_PHASE_SCREEN_CONTEXT_20260812.json",
    "atomization": f"{BASE}/02_problem_dag/O9d12a2a1b_C053_K32_PHASE_SCREEN_ATOMIZATION_20260812.json",
    "structural_lemma": f"{BASE}/03_routes/O9d12a2a1b_C053_K32_PHASE_SCREEN_STRUCTURAL_LEMMA_20260812.json",
    "memory": f"{BASE}/07_memory/O9d12a2a1b_C053_K32_PHASE_SCREEN_RESEARCH_MEMORY_REVIEW_20260812.json",
    "mathematical_lesson": f"{BASE}/07_memory/O9d12a2a1b_C053_K32_PHASE_SCREEN_MATHEMATICAL_LESSON_20260812.json",
    "transformation_memory": f"{BASE}/07_memory/O9d12a2a1b_C053_K32_PHASE_SCREEN_OBSTRUCTION_TRANSFORMATION_MEMORY_20260812.json",
    "authority_boundary": f"{BASE}/07_memory/O9d12a2a1b_C053_C034_C040_AUTHORITY_BOUNDARY_20260812.json",
    "expert_review": f"{BASE}/08_reviews/O9d12a2a1b_C053_K32_PHASE_SCREEN_EXPERT_CONTEXT_REVIEW_20260812.json",
    "shortcut_review": f"{BASE}/08_reviews/O9d12a2a1b_C053_K32_PHASE_SCREEN_OBSTRUCTION_TRANSFORMATION_REVIEW_20260812.json",
    "discriminator_proposal": f"{BASE}/09_trace/O9d12a2a1b_C053_K32_NEXT_DISCRIMINATOR_PROPOSAL_20260812.json",
    "trace": f"{BASE}/09_trace/O9d12a2a1b_C053_K32_PHASE_SCREEN_PRE_CANDIDATE_TRACE_20260812.json",
    "gate": f"{BASE}/09_trace/O9d12a2a1b_C053_K32_PHASE_SCREEN_PRE_CANDIDATE_GATE_20260812.json",
}

SOURCE_BINDINGS = {
    "c041_grammar": {
        "path": f"{BASE}/04_candidates/C041_fx_sat_one_sided.py",
        "raw_sha256": "sha256:c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a",
        "git_blob": "fcc4814dd618da96ef9bb8144a4783a0a6e886e1",
    },
    "c048_overlap_equivalence": {
        "path": f"{BASE}/04_candidates/O9d12a2a1b_C048_LITERAL_TRANSPOSE_PROOF_CERTIFICATE_FREEZE_20260812.json",
        "raw_sha256": "sha256:fd4d478d816c50423f2d6fbd668305bec911bcf3a035a2a5b516eb08796ec16c",
        "artifact_hash": "sha256:84ebf84c9b90a99c3f5e348bacad53ee1d700e2d0c746805cf4b8a0439cd1e33",
        "git_blob": "1283219dec4d6a39cf43d5f2d9a4fafa1883d016",
    },
    "k31_negative_certificate": {
        "path": f"{BASE}/04_candidates/O9d12a2a1b_C052_K31_OVERLAP_NEGATIVE_CERTIFICATE_20260812.json",
        "raw_sha256": "sha256:12c0382554081c28121d26f8a422651ea19a0726dbc6f02f50c2fd12ac46e547",
        "artifact_hash": "sha256:b292f34701ba9945f34f9ec5b3adb324c91f075c4339b8b88ced74efac08cd3f",
        "git_blob": "033336e6bbd8ca6ef4d8b97926bdc4905997effd",
    },
    "k31_failure": {
        "path": f"{BASE}/07_memory/O9d12a2a1b_C052_K31_OVERLAP_FAILURE_EXPERIENCE_20260812.json",
        "raw_sha256": "sha256:ed22486cec959bffaa13266572f2d42fd7822d83be4ef30a6c9a371f81cd3c49",
        "artifact_hash": "sha256:80b88bd5fb4cef74c5b1841c7fe1c97adf4086c969af4e0a696602fa266321c1",
        "git_blob": "2431087d68169570e30bd584cec7d1a388206703",
    },
    "k31_lesson": {
        "path": f"{BASE}/07_memory/O9d12a2a1b_C052_K31_OVERLAP_MATHEMATICAL_LESSON_20260812.json",
        "raw_sha256": "sha256:2f93bf9531b12308ac484287f04c80b69626a734bf8c18da30dd5464436a3af0",
        "artifact_hash": "sha256:ce38f59d3efb65e74a23410cbe03108ed768c92034a5d7f4aa4b33dcb516f9c9",
        "git_blob": "9c8acd1d11ee349d96779c36ab50048f76164c80",
    },
    "k31_result": {
        "path": f"{BASE}/09_trace/O9d12a2a1b_C052_K31_OVERLAP_RESULT_RECEIPT_20260812.json",
        "raw_sha256": "sha256:4f3e7b8085e26a7347577ee3614404f59d9b396943af13d8caded98d787f514b",
        "artifact_hash": "sha256:4bc221649f17bb8d8cb168937eb0c855731c404b68431816ad21853cff4bdea3",
        "git_blob": "c782d87d3456ba6603d672f877743a135f361416",
    },
    "external_ledger_assessment": {
        "path": f"{BASE}/08_reviews/C034_C040_EXTERNAL_LEDGER_ASSESSMENT_20260811.json",
        "raw_sha256": "sha256:c64edcf80f2048562182c16a32d5f58416324f3a5c876a430f96902af095cae5",
        "artifact_hash": "sha256:31c75fcccae6866eb0464dbd661b02ad0312f535de4944b2400194ce522ec14b",
        "git_blob": "7ebbbfaa75fd2744a77295a31889edc2c325b8c4",
    },
    "c037_replay": {
        "path": f"{BASE}/05_falsification/C037_EXTERNAL_LEDGER_REPLAY_RECEIPT_20260811.json",
        "raw_sha256": "sha256:602864258fc774724ce2cf50617834e95f93cf60ee34d792cb007157b8ba7514",
        "artifact_hash": "sha256:e0dce5f8dd47c48d7f98e5886019b15f4053c078dcb5399caae3bb05a28be2f8",
        "git_blob": "c0bdaa6c35d6a34ee0e748408c8d91bb65f8b2ab",
    },
    "u8_reconstruction": {
        "path": f"{BASE}/05_falsification/C034B_U8_RETROSPECTIVE_REPLAY_V2_CORRECTION_20260811.json",
        "raw_sha256": "sha256:32e19eb8b4bd0331e29a5b39ddf119c673b990d83996b62d6eed1c5cad314cd0",
        "artifact_hash": "sha256:746b4780cc4908b1afedb300ab9f08914a44b14bedd4dab37dbcf106fb90f2c9",
        "git_blob": "14171984085a519a08c3d1647ccaa0730f47fc23",
    },
}


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


def _load_screen():
    spec = importlib.util.spec_from_file_location("c053_phase_screen_runtime", SCREEN_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _assert_sources() -> None:
    for binding in SOURCE_BINDINGS.values():
        path = ROOT / binding["path"]
        if "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest() != binding["raw_sha256"]:
            raise RuntimeError(f"source bytes moved: {binding['path']}")
        if "artifact_hash" in binding and json.loads(path.read_text())["artifact_hash"] != binding["artifact_hash"]:
            raise RuntimeError(f"source artifact moved: {binding['path']}")


def structural_lemma(screen: dict) -> dict:
    return _seal({
        "schema_version": "1.0.0",
        "lemma_id": "PNP-C053-K32-BOUNDARY-TOKEN-PHASE-SCREEN-LEMMA-20260812",
        "atom_id": ATOM,
        "source_binding": SOURCE_BINDINGS["c041_grammar"],
        "screen_implementation_raw_sha256": "sha256:" + hashlib.sha256(SCREEN_PATH.read_bytes()).hexdigest(),
        "statement": "Within the checked set {k=31,k=32}, k=32 is the least checked k surviving both known k31 syntax screens. At k32 the endpoint screen rejects no parameter pair; fixed-current-header tokens reject 17668 of 42148 pairs; 24480 pairs survive the two-family screen.",
        "support_equations": {
            "header": "H(a,m)=6+2a+2 bit_length(m)",
            "raw_length": "R(a,m)=H(a,m)+3m(a+1)",
            "encoded_length": "E(a,m)=R(a,m)+(R(a,m) mod 2)",
            "split_map": "h[0]=1 and h[j]=x[k+j-1] for 1<=j<=k",
            "mapped_parent_token_start": "j=H_parent+t(a_parent+1)-k+1",
        },
        "bounded_classification": _jsonable(screen),
        "clean_all_parameter_phases": [
            {"k": 32, "parent_cell": [4, 3], "current_cell": [3, 4], "surviving_pairs": 32},
            {"k": 32, "parent_cell": [6, 2], "current_cell": [3, 4], "surviving_pairs": 128},
        ],
        "partial_phase": {"k": 32, "parent_cell": [6, 2], "current_cell": [11, 1], "surviving_pairs": 24320, "total_pairs": 32768},
        "hand_count_certificate": {
            "support_derivation": "With H=6+2a+2 bit_length(m), R=H+3m(a+1), and E=R+(R mod 2), exact E=64 parent support (m>=2) is (1,8),(4,3),(6,2), while exact E=66 current support is (3,4),(11,1).",
            "cell_pair_sizes": [4, 1024, 32, 8192, 128, 32768],
            "endpoint_derivation": "For current (3,4), (32-18) mod 4=2 and legal variables attain both endpoint bits; for current (11,1), (32-30) mod 12=2 and legal variables likewise attain both bits. Hence no k32 endpoint is forced to one.",
            "case_derivations": [
                "(1,8)->(3,4) and (1,8)->(11,1): a complete mapped token has variable code 0, so all 4 and 1024 pairs reject.",
                "(4,3)->(3,4): mapped starts 2,7,12 have only legal parent codes, so all 32 pairs survive.",
                "(4,3)->(11,1): the complete start 12 lies in the leading-zero gamma(v_current) run and has code 0, so all 8192 pairs reject.",
                "(6,2)->(3,4): the only complete start 5 has code 18 or 19, legal for every parent p in {32,...,63}, so all 128 pairs survive.",
                "(6,2)->(11,1): starts 5,12,19 have codes 16,1,r; the residue count below gives 8448 rejected and 24320 surviving pairs.",
            ],
            "partial_phase": "(a_parent,m_parent)=(6,2) to (a_current,m_current)=(11,1)",
            "parent_parameter_range": "p=v_parent in {32,...,63}",
            "mapped_token_starts": [5, 12, 19],
            "mapped_variable_codes": ["16", "1", "r=((v_current-1024)>>3)&63"],
            "residue_multiplicity": "Each r in {0,...,63} occurs for exactly 16 of the 1024 current parameters v_current in {1024,...,2047}.",
            "illegality_condition": "The fixed codes 16 and 1 are legal for every p>=32, so rejection occurs exactly when r=0 or r>p.",
            "rejected_pair_derivation": "16*sum_{p=32}^{63}(64-p)=16*(1+...+32)=8448",
            "partial_phase_survivor_derivation": "32*1024-8448=32768-8448=24320",
            "other_rejected_phase_counts": [4, 1024, 8192],
            "all_phase_totals": "rejected=4+1024+8192+8448=17668; survivors=32+128+24320=24480",
            "computation_role": "The source-bound program corroborates these hand counts only; it is not the proof.",
        },
        "proof_outline": [
            "Exact support equations give the unique k31 parent cell and three current cells, and at k32 give parent cells (1,8),(4,3),(6,2) and current cells (3,4),(11,1).",
            "The k31 result proves all 82 parameter pairs are removed by the pad endpoint or fixed illegal-token separator.",
            "At k32, current p[32] varies over {0,1} inside a legal payload index for every current parameter, so no pad-versus-forced-one endpoint conflict remains.",
            "Map every complete parent token lying in the fixed current header using j=H_parent+t w_parent-k+1 and decode its variable code against the exact parent v.",
            "For the only nontrivial partial phase (6,2)->(11,1), the complete mapped tokens start at h[5], h[12], h[19] and have variable codes 16, 1, and r=((v_current-1024)>>3)&63. Each r in {0,...,63} occurs 16 times. For p=v_parent in {32,...,63}, rejection is exactly r=0 or r>p, hence 16*sum_{p=32}^{63}(64-p)=16*(1+...+32)=8448 rejected and 32768-8448=24320 surviving pairs.",
            "The other three rejected phases contribute 4, 1024, and 8192 pairs, while the two current (3,4) clean phases contribute 32 and 128 survivors. Thus rejected=4+1024+8192+8448=17668 and survivors=32+128+24320=24480. The program only corroborates these hand counts.",
        ],
        "authority": "SOURCE_BOUND_EXACT_STRUCTURAL_LEMMA_FOR_TWO_SEPARATOR_FAMILIES_ONLY",
        "non_guarantees": ["no canonical word compatibility", "no UNSAT membership", "no H_32/P_33 overlap", "no collision", "no cover or circuit result", "no P-versus-NP result"],
        "overlap_or_sat_accessed": False,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def context_fiber(screen: dict, lemma: dict) -> MathContextFiber:
    anchors = tuple(f"git:{APPLICATION_BASE_SHA}:{row['path']}@blob:{row['git_blob']}" for row in SOURCE_BINDINGS.values())
    transfer = MethodTransfer(
        source_context="C052 exact k31 empty-overlap proof and its boundary/token mathematical lesson",
        method="solve support equations, map split coordinates into field/token phases, and remove phases killed by syntax before any word or SAT search",
        shared_structure=("adjacent even-length support cells", "equal split h[j]=x[k+j-1]", "fixed current header mapped into parent token phases", "screen survival is weaker than overlap"),
        required_assumptions=("unchanged C041 encoding", "all support cells are solved exactly", "only complete fixed-header parent tokens authorize token rejection", "survival never becomes a positive certificate"),
        disanalogies=("k31 has one parent cell whereas k32 has three", "k31 endpoint is fixed in one current cell whereas k32 endpoints vary", "a k31 impossibility proof cannot be transported as k32 disjointness"),
        repair_question="Which exact k32 cell/parameter phases are not universally separated by either known k31 syntax family?",
        source_anchors=anchors,
    )
    analogy = CrossDomainAnalogy(
        source_kind="engineering / binary protocol parser",
        source_situation="a message revision may remove one field mismatch while a later alignment makes another field invalid",
        common_abstraction=("two constrained bit languages", "field boundaries", "block legality", "version-to-version phase change"),
        source_to_target_mapping=("old message format -> parent canonical word", "new message format -> current prefix", "invalid field code -> illegal parent variable token", "version -> k"),
        shared_constraints=("full-message validity is block-structured", "boundary phase changes with total length", "one removed mismatch does not remove every mismatch"),
        disanalogies=("protocol validity has no UNSAT semantics", "engineering examples supply no theorem authority"),
        proposed_principle="screen boundary and block phases before attempting expensive whole-object compatibility",
        validation_obligation="derive exact C041 support and coordinate maps; reject any inference from analogy alone",
        provenance_note="proposal-only cross-domain analogy with zero mathematical authority",
    )
    draft = MathContextFiber(
        atom_id=ATOM,
        object_context="The exact k=32 parent/current support-cell and field-phase screen for the two proved k31 separator families, before any H_32 intersection P_33 candidate or result.",
        structural_coordinates=(
            "E(a,m)=6+2a+2 bit_length(m)+3m(a+1)+parity padding",
            "parent length 2k and current length 2(k+1)",
            "h[0]=1 and h[j]=x[k+j-1]",
            "parent endpoint is fixed zero only when raw parent length is 2k-1",
            "a fixed-header token obstruction exists only when a complete mapped parent token decodes outside 1..v_parent",
            f"k31 survivors={screen['k31']['surviving_parameter_pair_count']}",
            f"k32 survivors={screen['k32']['surviving_parameter_pair_count']} of {screen['k32']['parameter_pair_count']}",
            f"structural lemma artifact {lemma['artifact_hash']}",
        ),
        equivalent_formulations=("finite support-cell phase compatibility", "boundary-pad and fixed-header-token necessary-condition screen", "least member of the checked set {31,32} not decided by the two known syntax separators"),
        solved_analogues=("C052 k31 exact disjointness by endpoint/token dichotomy",),
        near_solved_analogues=("C049/C050/C051 bounded forced-coordinate screens", "C037 exact finite nonmonotonicity warns that extension does not preserve constraints"),
        method_transfers=(transfer,),
        explicit_disanalogies=("phase survival is not word-language intersection", "ambient legal syntax is not UNSAT membership", "finite k32 classification is not general k", "C034-C040 missing certificates remain CANNOT_CHECK", "same-context review is not independent peer review"),
        source_anchors=anchors + (f"{PATHS['structural_lemma']}#{lemma['artifact_hash']}",),
        analogy_scan_status=AnalogyScanStatus.BRIDGES_RETAINED.value,
        cross_domain_analogies=(analogy,),
        analogy_scan_notes="The parser analogy survives only as a search-order proposal.",
        frozen_at=TIMES[1],
        first_candidate_at=None,
        packet_hash="",
    )
    return replace(draft, packet_hash=_hash(_document(draft)))


def memory_review(context: MathContextFiber) -> ResearchMemoryReview:
    tools = {
        "T-PNP-C048-EXACT-OVERLAP-EQUIVALENCE": "full collision iff H_k intersects P_(k+1); does not decide the intersection",
        "MATH-PNP-C052-K31-FULL-WORD-SEPARATOR": "proof-backed boundary/token phase screen in exact k31 scope",
        "C034B-U8-RECONSTRUCTED-FULL-UNION-LP": "retrospective exact finite reconstruction only; no direct phase applicability",
    }
    failures = {
        "F-PNP-C052-K31-ACTUAL-OVERLAP-EMPTY-BY-SYNTAX-DICHOTOMY": "local marginal escape left later whole-word separators",
        "F-C037-ARBITRARY-EXTENSION-NONMONOTONE": "exact finite replay warns extension changes active constraints",
        "F-C034-FINITE-OVERGENERALIZATION": "small finite behavior never licenses a universal claim",
        "F-C034-C040-MISSING-CERTIFICATES": "C035/C036/C039/C040 and strict-v3 history fail closed",
    }
    draft = ResearchMemoryReview(
        target_atom_id=ATOM,
        target_context_hash=context.packet_hash,
        tool_inventory_snapshot_hash=_hash(tools),
        failure_lattice_snapshot_hash=_hash(failures),
        tool_query_status=MemoryQueryStatus.MATCHES_FOUND,
        failure_query_status=MemoryQueryStatus.MATCHES_FOUND,
        candidate_method_families=("support Diophantine classification", "split-coordinate phase map", "fixed-header parent-token legality screen"),
        relevant_tool_ids=tuple(tools),
        relevant_failure_ids=tuple(failures),
        selected_tool_ids=("MATH-PNP-C052-K31-FULL-WORD-SEPARATOR",),
        tool_applicability_notes=("the same two separator families can be rederived at k32 only after exact phase remapping", "C048 fixes the downstream QoI but is not used to infer overlap", "U8 reconstruction is retained only as exact finite-method experience"),
        failure_reuse_notes=("k31 is a warning not a blacklist; k32 changes parent/current support and token phase", "C037 blocks monotonic extension reasoning", "missing C034-C040 certificates are not promoted"),
        unresolved_warnings=("other syntax separators may remain", "phase survival does not supply a formula-bound witness", "the partial (6,2)->(11,1) phase has parameter-dependent legality", "no overlap candidate or evaluator is frozen"),
        evidence_pointers=tuple(row["path"] for row in SOURCE_BINDINGS.values()),
        artifact_hash="",
    )
    return replace(draft, artifact_hash=_hash(_document(draft)))


def obstruction_bundle(context: MathContextFiber, memory: ResearchMemoryReview):
    shared_relations = ("adjacent even-length support cells are compared by split-coordinate phase", "fixed current header blocks map into parent payload-token phases")
    shared_constraints = ("unchanged C041 grammar", "exact support equations", "no overlap or SAT access")
    source_obstruction = ObstructionFingerprint(
        obstruction_id="O-PNP-C052-K31-POST-MARGINAL-SYNTAX-SCREEN",
        domain="canonical binary formula languages",
        roles=("parent support cell", "current support cell", "boundary/token screen"),
        relations=shared_relations,
        constraints=shared_constraints,
        failure_mechanisms=("survival of a local marginal screen can conceal later syntax separators",),
        invariants_to_preserve=("canonical encoding", "equal split", "formula-bound downstream QoI"),
        desired_transition=("classify exact phase pairs before word search",),
        forbidden_losses=("marginal-to-overlap inference",),
    )
    episode_core = {
        "episode_id": "E-PNP-C052-K31-FULL-WORD-SCREEN",
        "source_domain": "canonical binary formula languages",
        "source_context": "C052 exact k31 boundary/token separator",
        "source_obstruction": _document(source_obstruction),
        "transformation_name": "lift coordinate screening to boundary and complete-token phase screening",
        "operation": "solve support equations, map split indices, and test endpoint/fixed-header token legality before overlap",
        "preconditions": list(shared_constraints),
        "resulting_relations": ["classify exact phase pairs before word search", "all k31 parameter phases classified by two separator families", "full-word search avoided when a universal syntax separator exists"],
        "preserved_invariants": ["canonical C041 encoding", "exact level", "UNSAT remains required downstream"],
        "relaxed_or_broken_constraints": ["first-eight-coordinate-only screening"],
        "known_breakpoints": ["screen survival is inconclusive", "changed k requires complete remapping"],
        "evidence_pointers": [SOURCE_BINDINGS["k31_negative_certificate"]["path"], SOURCE_BINDINGS["k31_lesson"]["path"]],
        "authority": TransformationEpisodeAuthority.PROOF_BACKED.value,
        "lineage_ids": ["PNP-C052-K31-UNIVERSAL-SYNTAX-SEPARATOR-v1"],
    }
    episode = ObstructionTransformationEpisode(
        episode_id=episode_core["episode_id"], source_domain=episode_core["source_domain"], source_context=episode_core["source_context"],
        source_obstruction=source_obstruction, transformation_name=episode_core["transformation_name"], operation=episode_core["operation"],
        preconditions=tuple(episode_core["preconditions"]), resulting_relations=tuple(episode_core["resulting_relations"]),
        preserved_invariants=tuple(episode_core["preserved_invariants"]), relaxed_or_broken_constraints=tuple(episode_core["relaxed_or_broken_constraints"]),
        known_breakpoints=tuple(episode_core["known_breakpoints"]), evidence_pointers=tuple(episode_core["evidence_pointers"]),
        authority=TransformationEpisodeAuthority.PROOF_BACKED, artifact_hash=_hash(episode_core), lineage_ids=tuple(episode_core["lineage_ids"]),
    )
    transformation_memory = build_transformation_memory(
        memory_id="PNP-C053-K32-PHASE-SCREEN-TRANSFORMATION-MEMORY-20260812",
        source_universe=("C052 k31 proof", "C052 mathematical lesson", "C037 exact finite extension counterexample", "C034b U8 retrospective reconstruction"),
        episodes=(episode,),
        evidence_pointers=tuple(row["path"] for row in SOURCE_BINDINGS.values()),
    )
    target = ObstructionFingerprint(
        obstruction_id="O-PNP-C053-K32-FIND-UNSCREENED-PHASE",
        domain="canonical binary formula languages",
        roles=("parent support cell", "current support cell", "boundary/token screen"),
        relations=shared_relations,
        constraints=shared_constraints,
        failure_mechanisms=("survival of a local marginal screen can conceal later syntax separators",),
        invariants_to_preserve=("canonical encoding", "equal split", "formula-bound downstream QoI"),
        desired_transition=("classify exact phase pairs before word search",),
        forbidden_losses=("screen survival promoted to overlap", "missing support cells"),
    )
    mapping_core = {
        "witness_id": "W-PNP-C053-K31-TO-K32-PHASE-SCREEN",
        "episode_id": episode.episode_id,
        "target_obstruction_id": target.obstruction_id,
        "role_mapping": [[role, role] for role in source_obstruction.roles],
        "shared_relations": list(shared_relations),
        "shared_constraints": list(shared_constraints),
        "precondition_mapping": [[item, f"rederived at k32: {item}"] for item in episode.preconditions],
        "unmatched_source_preconditions": [],
        "disanalogies": ["k31 has one parent support cell while k32 has three", "k31 proves disjointness while k32 screen survival is only a necessary-condition result"],
        "target_validation_obligations": ["solve all k32 parent/current support cells", "map every complete fixed-header parent token", "preserve CANNOT_CHECK outside the two-family screen"],
        "evidence_pointers": [PATHS["structural_lemma"], SOURCE_BINDINGS["k31_result"]["path"]],
    }
    mapping = StructuralMappingWitness(
        witness_id=mapping_core["witness_id"], episode_id=episode.episode_id, target_obstruction_id=target.obstruction_id,
        role_mapping=tuple(tuple(row) for row in mapping_core["role_mapping"]), shared_relations=shared_relations,
        shared_constraints=shared_constraints, precondition_mapping=tuple(tuple(row) for row in mapping_core["precondition_mapping"]),
        unmatched_source_preconditions=(), disanalogies=tuple(mapping_core["disanalogies"]),
        target_validation_obligations=tuple(mapping_core["target_validation_obligations"]), evidence_pointers=tuple(mapping_core["evidence_pointers"]),
        artifact_hash=_hash(mapping_core),
    )
    draft = ObstructionTransformationReview(
        review_id="PNP-C053-K32-PHASE-SCREEN-SHORTCUT-REVIEW-20260812",
        target_atom_id=ATOM,
        target_context_hash=context.packet_hash,
        research_memory_review_hash=memory.artifact_hash,
        episode_memory_snapshot_hash=transformation_memory.snapshot_hash,
        obstruction=target,
        direct_search_status=RouteSearchStatus.MATCHES_FOUND,
        jump_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        glue_search_status=RouteSearchStatus.NO_VIABLE_MATCH,
        selected_mode=ShortcutMode.SEARCH,
        direct_candidate_episode_ids=(episode.episode_id,),
        direct_mapping_witnesses=(mapping,),
        selected_episode_ids=(episode.episode_id,),
        unresolved_warnings=("SEARCH reuses only screening order, not the k31 conclusion", "k32 survivors remain open to other syntax and semantic obstructions", "C037/U8 evidence supplies warnings only and no phase theorem"),
        evidence_pointers=(PATHS["context"], PATHS["memory"], PATHS["structural_lemma"]),
        artifact_hash="",
    )
    return transformation_memory, replace(draft, artifact_hash=_hash(_document(draft)))


def authority_boundary() -> dict:
    return _seal({
        "schema_version": "1.0.0",
        "boundary_id": "PNP-C053-C034-C040-AUTHORITY-BOUNDARY-20260812",
        "assessment_binding": SOURCE_BINDINGS["external_ledger_assessment"],
        "promotable_external_results": ["C037 exact finite strict-decrease replay", "U8 reconstructed full-union LP value 49/24"],
        "promotable_scope_notes": {
            "C037": "exact finite computational replay only; no asymptotic, novelty, or root authority",
            "U8": "retrospective reconstruction of the finite full-union LP with a different matching certificate, not recovery of the missing original certificate and not automatic all-rule authority",
        },
        "desk_checked_only": {"C034a": "proof authority none", "C038": "conditional statement binding missing"},
        "missing_certificate_claims": {"C035/C036/C039/C040": "CANNOT_CHECK", "strict_v3_chronology": "CANNOT_CHECK"},
        "use_in_c053": "warnings against monotonic extension and finite overgeneralization only; no direct phase-screen authority",
        "external_packet_root_authority": "NONE",
    })


def mathematical_lesson(lemma: dict) -> dict:
    return _seal({
        "schema_version": "1.0.0",
        "lesson_id": "MATH-PNP-C053-K32-PHASE-SCREEN-20260812",
        "structural_lemma_artifact_hash": lemma["artifact_hash"],
        "seven_field_mathematical_lesson": {
            "attempted_implication": "Moving from k=31 to the next adjacent-supported level might remove the parent-pad endpoint conflict and the mapped illegal-parent-token conflict simultaneously.",
            "exact_theorem_or_failure": "Within the checked set {31,32}, k=32 is the least checked k with parameter phases surviving both separator families. At k=32 the endpoint screen excludes none; fixed-current-header token illegality excludes 17668 of 42148 parameter pairs; 24480 survive this two-family screen.",
            "supported_and_competing_mathematical_causes": "Supported cause is a changed split/field phase: p[32] is variable rather than forced one, and only some complete current-header blocks map to illegal parent tokens. Competing causes still open include a different fixed coordinate, a different multi-bit legality constraint, full-word incompatibility, and absence of any UNSAT parent in a surviving syntax phase.",
            "scope": "Exact C041 encoding, k=31 and k=32 only, all exact parent/current support cells and parameter pairs, and only the two separator families proved at k=31. No statement about overlap, general k, collision, covers, circuits, or P versus NP.",
            "mathematical_falsifier": "A missed exact support cell, an incorrect split-coordinate map, a k32 current endpoint forced to one in a claimed survivor, an illegal complete fixed-header parent token in a claimed clean phase, or a recomputation count different from 0/82 and 24480/42148 refutes the corresponding lemma component.",
            "repair_or_next_mathematical_move": "Analyze full-word compatibility first in the smallest clean phase (parent a,m)=(4,3) and current a+,m+=(3,4), while screening every other complete mapped block before constructing formulas; retain the larger clean and partial phases as alternatives.",
            "proof_and_source_evidence": "Hand derivation: H=6+2a+2 bit_length(m), R=H+3m(a+1), and E=R+(R mod 2) give exact E=64 parent cells (1,8),(4,3),(6,2) and exact E=66 current cells (3,4),(11,1). The split map h[j]=x[k+j-1] gives complete token start j=H+t(a+1)-k+1 with j>=1. Endpoint phases are variable in both current cells. The six cell-pair cases respectively reject/survive 4/0, 1024/0, 0/32, 8192/0, 0/128, and 8448/24320 pairs. In the partial (6,2)->(11,1) case, starts 5,12,19 have codes 16,1,r with r=((v_current-1024)>>3)&63; each r in {0,...,63} occurs 16 times. For p=v_parent in {32,...,63}, only r=0 or r>p is illegal, so 16*sum_{p=32}^{63}(64-p)=16*(1+...+32)=8448 reject and 32768-8448=24320 survive. Thus 4+1024+8192+8448=17668 reject and 32+128+24320=24480 survive. The source-bound program corroborates these hand derivations only and receives no proof authority.",
        },
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })


def custom_documents(context: MathContextFiber, memory: ResearchMemoryReview, shortcut: ObstructionTransformationReview, lemma: dict) -> dict:
    atomization = _seal({
        "schema_version": "1.0.0", "atom_id": ATOM, "parent_atom_id": "O9d12a2a1b-C052-K31-OVERLAP",
        "object": "exact field phases at the checked levels k in {31,32} surviving the k31 endpoint and mapped-illegal-token screens",
        "qoi": "EXACT_PHASE_CLASSIFICATION_ONLY",
        "atomic_obstruction": "a later k can change padding, endpoint and token alignment, so k31 separation cannot be extrapolated",
        "application_base_sha": APPLICATION_BASE_SHA, "candidate_identity": None, "overlap_result_accessed": False,
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    expert = _seal({
        "schema_version": "1.0.0", "review_id": "PNP-C053-K32-PHASE-SCREEN-EXPERT-CONTEXT-REVIEW-20260812", "atom_id": ATOM,
        "context_hash": context.packet_hash, "memory_hash": memory.artifact_hash, "structural_lemma_hash": lemma["artifact_hash"],
        "role_reviews": [
            {"role": "domain_theory_lead", "finding": "The support equations and exact split map prove k32 is the first of {31,32} with surviving phases; this says nothing about overlap."},
            {"role": "analogy_method_transfer_lead", "finding": "Transfer the phase-screening order from k31; protocol analogies have zero authority."},
            {"role": "adversarial_falsification_lead", "finding": "The cheapest refuters are a missed support cell, an off-by-one token start, or a supposedly legal fixed code outside 1..v_parent."},
            {"role": "formal_methods_lead", "finding": "Bind C041 bytes and express each rejection as an endpoint set or complete-token legality predicate; do not inspect formula semantics."},
            {"role": "novelty_research_value_lead", "finding": "The bounded phase lemma improves search information only; novelty, general k and root relevance are unresolved."},
        ],
        "strongest_objection": "A surviving phase may still have no common full word and no UNSAT parent; the packet explicitly makes no overlap claim.",
        "disagreement": "Whether to select the smaller clean all-parameter phase (4,3)->(3,4) or the much larger partial survivor (6,2)->(11,1) for the next atom remains open; information gain favors the clean phase, breadth favors the partial survivor.",
        "blocking_concerns": [],
        "recommendation": "Freeze only the next discriminator proposal for the clean k32 phases; no candidate/evaluator/result this round.",
        "review_authority": "ROLE_SEPARATED_SAME_CONTEXT_NOT_INDEPENDENT_PEER_REVIEW",
    })
    proposal = _seal({
        "schema_version": "1.0.0", "proposal_id": "PNP-C053-K32-NEXT-DISCRIMINATOR-PROPOSAL-20260812", "atom_id": ATOM,
        "candidate_identity": None, "evaluator_identity": None, "implementation": None,
        "proposed_next_atom": "exact formula-bound compatibility inside the clean k32 (parent a,m)=(4,3), (current a+,m+)=(3,4) phase",
        "selection_rationale": "all 32 parameter pairs survive both known screens, the phase is smaller than the other clean/partial phases, and parent padding makes the changed endpoint obligation explicit",
        "alternatives": ["clean (6,2)->(3,4) phase with 128 parameter pairs", "partial (6,2)->(11,1) phase with 24320 survivors", "global H_32 intersection P_33 search"],
        "future_discriminator_requirements": ["freeze exact phase membership and full-word QoI", "freeze positive/negative/CANNOT_CHECK certificates before construction", "run counterexample-first symbolic screen for other complete blocks", "prove UNSAT for any positive parent", "do not infer from phase survival"],
        "expected_information_gain": "decide whether a clean syntax-surviving phase reaches a new full-word obstruction before any broader k32 search",
        "falsifiers": ["missed support cell", "endpoint p32 actually forced one", "mapped complete header token illegal for some claimed clean parameter", "source-binding mismatch"],
        "overlap_result_accessed": False, "sat_executed": False, "hidden_or_native_executed": False,
        "authority": "NEXT_ACTION_PROPOSAL_ONLY_NOT_CANDIDATE_NOT_EVALUATOR_NOT_RESULT",
    })
    gate = _seal({
        "schema_version": "1.0.0", "gate_id": "PNP-C053-K32-PHASE-SCREEN-PRE-CANDIDATE-GATE-20260812", "atom_id": ATOM,
        "application_base_sha": APPLICATION_BASE_SHA, "framework_pin": FRAMEWORK_SHA,
        "context_hash": context.packet_hash, "memory_hash": memory.artifact_hash, "shortcut_review_hash": shortcut.artifact_hash,
        "structural_lemma_hash": lemma["artifact_hash"], "licensed_action": "PUBLISH_PRE_CANDIDATE_PHASE_CLASSIFICATION_AND_NEXT_ACTION_PROPOSAL_ONLY",
        "candidate_generation_in_this_round": False, "candidate_or_evaluator_identity_frozen": False, "overlap_or_sat_result_accessed": False,
        "mathematical_credit": ["exact source-bound k31/k32 two-family structural phase lemma"],
        "zero_mathematical_credit": ["Git", "CI", "schemas", "hashes", "trace", "same-context review", "external missing-certificate claims"],
        "git_ci_schema_hash_mathematical_credit": 0,
        "next_round_requirement": "fresh public candidate/falsifier identity freeze after this packet merges; no backfill",
        "root_status": "OPEN_NO_SOLUTION_CERTIFICATE",
    })
    return {"atomization": atomization, "expert_review": expert, "discriminator_proposal": proposal, "gate": gate, "authority_boundary": authority_boundary(), "mathematical_lesson": mathematical_lesson(lemma)}


def trace(context: MathContextFiber, memory: ResearchMemoryReview, shortcut: ObstructionTransformationReview, lemma: dict) -> MathResearchTrace:
    types = (
        ResearchTraceEventType.ATOMIZED, ResearchTraceEventType.CONTEXT_FROZEN, ResearchTraceEventType.ANALOGY_SCAN,
        ResearchTraceEventType.METHOD_TRANSFER_REVIEW, ResearchTraceEventType.EXPERT_CONTEXT_REVIEW,
        ResearchTraceEventType.EXPERIENCE_MEMORY_REVIEW, ResearchTraceEventType.OBSTRUCTION_TRANSFORMATION_REVIEW,
        ResearchTraceEventType.NEXT_STEP_PROPOSED,
    )
    pointers = (
        (PATHS["atomization"],), (PATHS["context"], PATHS["structural_lemma"]), (PATHS["context"],),
        (PATHS["context"], PATHS["structural_lemma"]), (PATHS["expert_review"],),
        (PATHS["memory"], PATHS["authority_boundary"]), (PATHS["shortcut_review"],), (PATHS["discriminator_proposal"], PATHS["gate"]),
    )
    actions = (
        "Freeze the syntax-only k31/k32 phase-classification atom.",
        "Freeze exact support equations, field phases and source-bound structural lemma.",
        "Retain protocol-parser alignment only as proposal guidance.",
        "Transfer the proved k31 screen by complete k32 coordinate remapping.",
        "Run role-separated review of support completeness, off-by-one and authority boundaries.",
        "Query k31 success/failure plus bounded C037/U8 experience; preserve missing-certificate CANNOT_CHECK claims.",
        "Select SEARCH using the proof-backed k31 screening episode and exact mapping witness.",
        "Freeze the next discriminator proposal only; do not freeze a candidate, evaluator or result.",
    )
    outputs = (
        (), (context.packet_hash, lemma["artifact_hash"]), (context.packet_hash,), (lemma["artifact_hash"],), (),
        (memory.artifact_hash,), (shortcut.artifact_hash, shortcut.episode_memory_snapshot_hash), (),
    )
    entries = []
    previous = ""
    for index, (event_type, timestamp, evidence, action, bound) in enumerate(zip(types, TIMES, pointers, actions, outputs), start=1):
        draft = ResearchTraceEntry(
            event_id=f"O9d12a2a1b-C053-K32-PHASE-SCREEN-E{index:02d}", atom_id=ATOM, event_type=event_type,
            timestamp=timestamp, state_summary="Only public structural fields are classified; no overlap/SAT/candidate/evaluator result is accessed.",
            action_summary=action, evidence_pointers=tuple(evidence),
            alternatives_considered=("extrapolate k31 emptiness", "scan full labels", "run SAT", "classify exact support and field phases"),
            decision_rationale="The k31 lesson identifies boundary and token phase as the cheapest source-bound discriminator before any expensive or semantic search.",
            outputs=tuple(bound) + ("PRE_CANDIDATE_ONLY", "NO_OVERLAP_OR_SAT_ACCESS", "ROOT_OPEN"),
            uncertainties=("other syntax separators remain possible", "phase survival is not overlap", "same-context review is not independent"),
            residuals=("exact clean-phase word compatibility unresolved", "H_32 intersection P_33 unresolved", "P-versus-NP root open"),
            next_steps=("merge this packet", "freeze a separate candidate/falsifier identity only in a later round"),
            artifact_hash="", previous_event_hash=previous,
        )
        entry = replace(draft, artifact_hash=_hash(_document(draft)))
        entries.append(entry)
        previous = entry.artifact_hash
    return MathResearchTrace(trace_id="PNP-C053-K32-PHASE-SCREEN-PRE-CANDIDATE-TRACE-20260812", entries=tuple(entries))


def build_objects():
    _assert_sources()
    screen = _load_screen().classify()
    lemma = structural_lemma(screen)
    context = context_fiber(screen, lemma)
    memory = memory_review(context)
    transformation_memory, shortcut = obstruction_bundle(context, memory)
    research_trace = trace(context, memory, shortcut, lemma)
    return screen, lemma, context, memory, transformation_memory, shortcut, research_trace


def build_plan():
    _, _, context, memory, transformation_memory, shortcut, research_trace = build_objects()
    return plan_math_research(
        signature=ProblemSignature(
            objects=("k31/k32 support cells", "boundary endpoint", "mapped parent tokens"),
            relations=("adjacent-length support", "split-coordinate phase", "token legality"),
            quantifiers=("all exact support cells", "all parameter pairs"),
            domain="finite canonical C041 structural syntax",
            goal_type="classify phases surviving two proved separator families",
            constraints=("unchanged C041", "no overlap/SAT access", "survival not overlap"),
        ),
        record=MathResearchRecord(claim_id=ATOM), context_fiber=context, memory_review=memory,
        transformation_memory=transformation_memory, shortcut_review=shortcut, research_trace=research_trace,
    )


def build_documents() -> dict:
    _, lemma, context, memory, transformation_memory, shortcut, research_trace = build_objects()
    documents = {
        "context": _document(context), "structural_lemma": lemma, "memory": _document(memory),
        "transformation_memory": _document(transformation_memory), "shortcut_review": _document(shortcut),
        "trace": _document(research_trace),
    }
    documents.update(custom_documents(context, memory, shortcut, lemma))
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
