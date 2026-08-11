from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from rakl.math_context import (
    ContextGateVerdict,
    CrossDomainAnalogy,
    MathContextFiber,
    MethodTransfer,
    audit_math_context_fiber,
)
from rakl.math_research_assurance import MathResearchRecord
from rakl.math_research_runtime import plan_math_research
from rakl.problem_solving_algebra import ProblemSignature
from rakl.research_memory import (
    MemoryQueryStatus,
    ResearchMemoryReview,
    ResearchMemoryVerdict,
    audit_research_memory_review,
)
from rakl.research_trace import (
    MathResearchTrace,
    ResearchTraceEntry,
    ResearchTraceEventType,
    TraceGateVerdict,
    audit_pre_candidate_trace,
)


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/navier_stokes"


def _load(relative: str) -> dict:
    return json.loads((BASE / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


# Polynomial-times-Gaussian exact algebra. A function is (P, alpha), meaning
# P(x,y,z) exp(-alpha |x|^2/2), with P represented by rational coefficients.
def _clean(poly):
    return {key: value for key, value in poly.items() if value}


def _padd(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Fraction(0)) + value
    return _clean(out)


def _pscale(c, a):
    return _clean({key: c * value for key, value in a.items()})


def _pmul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            exponent = tuple(ea[i] + eb[i] for i in range(3))
            out[exponent] = out.get(exponent, Fraction(0)) + ca * cb
    return _clean(out)


def _pder(poly, axis):
    out = {}
    for exponent, coefficient in poly.items():
        power = exponent[axis]
        if power == 0:
            continue
        reduced = list(exponent)
        reduced[axis] -= 1
        key = tuple(reduced)
        out[key] = out.get(key, Fraction(0)) + coefficient * power
    return _clean(out)


def _pmul_x(poly, axis):
    return {
        tuple(exponent[i] + (1 if i == axis else 0) for i in range(3)): coefficient
        for exponent, coefficient in poly.items()
    }


def _fder(function, axis):
    poly, alpha = function
    return (_padd(_pder(poly, axis), _pscale(-alpha, _pmul_x(poly, axis))), alpha)


def _fadd(a, b):
    assert a[1] == b[1]
    return (_padd(a[0], b[0]), a[1])


def _fscale(c, function):
    return (_pscale(c, function[0]), function[1])


def _fmul(a, b):
    return (_pmul(a[0], b[0]), a[1] + b[1])


def _flap(function):
    result = None
    for axis in range(3):
        term = _fder(_fder(function, axis), axis)
        result = term if result is None else _fadd(result, term)
    return result


def _odd_double_factorial(value: int) -> int:
    if value <= 0:
        return 1
    result = 1
    for item in range(1, value + 1, 2):
        result *= item
    return result


def _normalized_gaussian_integral(function) -> Fraction:
    """Integral / (2*pi/alpha)^(3/2), evaluated exactly."""
    poly, alpha = function
    total = Fraction(0)
    for exponent, coefficient in poly.items():
        if any(power % 2 for power in exponent):
            continue
        moment = Fraction(1)
        for power in exponent:
            k = power // 2
            moment *= Fraction(_odd_double_factorial(2 * k - 1), alpha**k)
        total += coefficient * moment
    return total


def _tensor_inner(a, b):
    result = None
    for i in range(3):
        for j in range(3):
            term = _fmul(a[i][j], b[i][j])
            result = term if result is None else _fadd(result, term)
    return result


def _vector_square(vector):
    result = None
    for item in vector:
        term = _fmul(item, item)
        result = term if result is None else _fadd(result, term)
    return result


def _build_seed_objects():
    x = {(1, 0, 0): Fraction(1)}
    y = {(0, 1, 0): Fraction(1)}
    z = {(0, 0, 1): Fraction(1)}
    potential = [
        (_pmul(x, y), Fraction(1)),
        (_pmul(y, z), Fraction(1)),
        (_pmul(x, z), Fraction(1)),
    ]
    velocity = [
        _fadd(_fder(potential[2], 1), _fscale(-1, _fder(potential[1], 2))),
        _fadd(_fder(potential[0], 2), _fscale(-1, _fder(potential[2], 0))),
        _fadd(_fder(potential[1], 0), _fscale(-1, _fder(potential[0], 1))),
    ]
    divergence = _fadd(_fadd(_fder(velocity[0], 0), _fder(velocity[1], 1)), _fder(velocity[2], 2))
    assert divergence[0] == {}

    strain = [
        [
            _fscale(Fraction(1, 2), _fadd(_fder(velocity[i], j), _fder(velocity[j], i)))
            for j in range(3)
        ]
        for i in range(3)
    ]
    vorticity = [
        _fadd(_fder(velocity[2], 1), _fscale(-1, _fder(velocity[1], 2))),
        _fadd(_fder(velocity[0], 2), _fscale(-1, _fder(velocity[2], 0))),
        _fadd(_fder(velocity[1], 0), _fscale(-1, _fder(velocity[0], 1))),
    ]
    dissipation = [[_fscale(-1, _flap(strain[i][j])) for j in range(3)] for i in range(3)]

    advection = [[None] * 3 for _ in range(3)]
    strain_squared = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            adv = None
            square = None
            for k in range(3):
                adv_term = _fmul(velocity[k], _fder(strain[i][j], k))
                sq_term = _fmul(strain[i][k], strain[k][j])
                adv = adv_term if adv is None else _fadd(adv, adv_term)
                square = sq_term if square is None else _fadd(square, sq_term)
            advection[i][j] = adv
            strain_squared[i][j] = square

    full_remainder_before_projection = [
        [
            _fadd(
                _fadd(advection[i][j], strain_squared[i][j]),
                _fscale(Fraction(3, 4), _fmul(vorticity[i], vorticity[j])),
            )
            for j in range(3)
        ]
        for i in range(3)
    ]
    return velocity, dissipation, full_remainder_before_projection


def test_exact_gaussian_seed_moments_and_projection_pairing_are_nonzero() -> None:
    velocity, dissipation, full_remainder = _build_seed_objects()
    energy = _vector_square(velocity)
    dissipation_squared = _tensor_inner(dissipation, dissipation)
    remainder_pairing = _tensor_inner(full_remainder, dissipation)

    assert energy[1] == 2
    assert dissipation_squared[1] == 2
    assert remainder_pairing[1] == 3
    assert _normalized_gaussian_integral(energy) == Fraction(3, 2)
    assert _normalized_gaussian_integral(dissipation_squared) == Fraction(3861, 32)
    assert _normalized_gaussian_integral(remainder_pairing) == Fraction(8, 27)
    assert _normalized_gaussian_integral(remainder_pairing) > 0


def test_fixed_energy_concentration_forces_snapshot_ratio_lower_bound_to_diverge() -> None:
    amplitude = Fraction(3, 2)
    velocity_l2_squared_exponent = 2 * amplitude - 3
    strain_pointwise_exponent = amplitude + 1
    dissipation_pointwise_exponent = strain_pointwise_exponent + 2
    remainder_pointwise_exponent = 2 * amplitude + 2
    dissipation_l2_squared_exponent = 2 * dissipation_pointwise_exponent - 3
    pairing_exponent = remainder_pointwise_exponent + dissipation_pointwise_exponent - 3
    q_lower_bound_exponent = pairing_exponent - dissipation_l2_squared_exponent

    assert velocity_l2_squared_exponent == 0
    assert strain_pointwise_exponent == Fraction(5, 2)
    assert dissipation_pointwise_exponent == Fraction(9, 2)
    assert remainder_pointwise_exponent == 5
    assert dissipation_l2_squared_exponent == 6
    assert pairing_exponent == Fraction(13, 2)
    assert q_lower_bound_exponent == Fraction(1, 2)

    # From the exact seed moments:
    # <F,D> = (16*sqrt(6)/243) pi^(3/2), ||D||_2^2=(3861/32)pi^(3/2).
    assert 243 * 3861 == 938223
    assert 16 * 32 == 512


def _context_from_raw(raw: dict) -> MathContextFiber:
    return MathContextFiber(
        atom_id=raw["atom_id"],
        object_context=raw["object_context"],
        structural_coordinates=tuple(raw["structural_coordinates"]),
        equivalent_formulations=tuple(raw["equivalent_formulations"]),
        solved_analogues=tuple(raw.get("solved_analogues", ())),
        near_solved_analogues=tuple(raw.get("near_solved_analogues", ())),
        method_transfers=tuple(
            MethodTransfer(
                source_context=item["source_context"],
                method=item["method"],
                shared_structure=tuple(item["shared_structure"]),
                required_assumptions=tuple(item["required_assumptions"]),
                disanalogies=tuple(item["disanalogies"]),
                repair_question=item["repair_question"],
                source_anchors=tuple(item["source_anchors"]),
            )
            for item in raw["method_transfers"]
        ),
        explicit_disanalogies=tuple(raw["explicit_disanalogies"]),
        source_anchors=tuple(raw["source_anchors"]),
        analogy_scan_status=raw["analogy_scan_status"],
        cross_domain_analogies=tuple(
            CrossDomainAnalogy(
                source_kind=item["source_kind"],
                source_situation=item["source_situation"],
                common_abstraction=tuple(item["common_abstraction"]),
                source_to_target_mapping=tuple(item["source_to_target_mapping"]),
                shared_constraints=tuple(item["shared_constraints"]),
                disanalogies=tuple(item["disanalogies"]),
                proposed_principle=item["proposed_principle"],
                validation_obligation=item["validation_obligation"],
                provenance_note=item["provenance_note"],
            )
            for item in raw.get("cross_domain_analogies", ())
        ),
        analogy_scan_notes=raw.get("analogy_scan_notes", ""),
        frozen_at=raw["frozen_at"],
        first_candidate_at=raw.get("first_candidate_at"),
        packet_hash=raw["packet_hash"],
    )


def _memory_from_raw(raw: dict) -> ResearchMemoryReview:
    return ResearchMemoryReview(
        target_atom_id=raw["target_atom_id"],
        target_context_hash=raw["target_context_hash"],
        tool_inventory_snapshot_hash=raw["tool_inventory_snapshot_hash"],
        failure_lattice_snapshot_hash=raw["failure_lattice_snapshot_hash"],
        tool_query_status=MemoryQueryStatus(raw["tool_query_status"]),
        failure_query_status=MemoryQueryStatus(raw["failure_query_status"]),
        candidate_method_families=tuple(raw["candidate_method_families"]),
        relevant_tool_ids=tuple(raw.get("relevant_tool_ids", ())),
        relevant_failure_ids=tuple(raw.get("relevant_failure_ids", ())),
        selected_tool_ids=tuple(raw.get("selected_tool_ids", ())),
        tool_applicability_notes=tuple(raw.get("tool_applicability_notes", ())),
        failure_reuse_notes=tuple(raw.get("failure_reuse_notes", ())),
        unresolved_warnings=tuple(raw.get("unresolved_warnings", ())),
        evidence_pointers=tuple(raw.get("evidence_pointers", ())),
        artifact_hash=raw["artifact_hash"],
    )


def _entry_from_raw(raw: dict) -> ResearchTraceEntry:
    return ResearchTraceEntry(
        event_id=raw["event_id"],
        atom_id=raw["atom_id"],
        event_type=ResearchTraceEventType(raw["event_type"]),
        timestamp=raw["timestamp"],
        state_summary=raw["state_summary"],
        action_summary=raw["action_summary"],
        evidence_pointers=tuple(raw["evidence_pointers"]),
        alternatives_considered=tuple(raw.get("alternatives_considered", ())),
        decision_rationale=raw.get("decision_rationale", ""),
        outputs=tuple(raw.get("outputs", ())),
        uncertainties=tuple(raw.get("uncertainties", ())),
        residuals=tuple(raw.get("residuals", ())),
        next_steps=tuple(raw.get("next_steps", ())),
        artifact_hash=raw["artifact_hash"],
        previous_event_hash=raw.get("previous_event_hash", ""),
    )


def test_ns_r001d_strict_packet_and_full_hash_chain_pass_current_rakl_gates() -> None:
    context_raw = _load("01_frontier/NS_R001D_ADVECTION_DEPLETION_CONTEXT_FIBER_20260811.json")
    context_for_hash = copy.deepcopy(context_raw)
    context_for_hash["packet_hash"] = ""
    assert context_raw["packet_hash"] == _canonical_hash(context_for_hash)
    context = _context_from_raw(context_raw)
    assert audit_math_context_fiber(context).verdict is ContextGateVerdict.PASS

    tools_raw = _load("07_memory/NS_R001_RESEARCH_TOOL_INVENTORY_20260811.json")
    failures_raw = _load("07_memory/NS_R001D_FAILURE_EXPERIENCE_LATTICE_20260811.json")
    memory_raw = _load("07_memory/NS_R001D_RESEARCH_MEMORY_REVIEW_20260811.json")
    assert memory_raw["tool_inventory_snapshot_hash"] == _canonical_hash(tools_raw)
    assert memory_raw["failure_lattice_snapshot_hash"] == _canonical_hash(failures_raw)
    memory_for_hash = copy.deepcopy(memory_raw)
    memory_for_hash["artifact_hash"] = ""
    assert memory_raw["artifact_hash"] == _canonical_hash(memory_for_hash)
    memory = _memory_from_raw(memory_raw)
    assert audit_research_memory_review(
        memory, atom_id=context.atom_id, context_hash=context.packet_hash
    ).verdict is ResearchMemoryVerdict.PASS

    pre = _load("09_trace/NS_R001D_ADVECTION_DEPLETION_TRACE_20260811.json")
    continuation = _load("09_trace/NS_R001D_C001_TRACE_CONTINUATION_20260811.json")
    raw_entries = pre["entries"] + continuation["entries"]
    previous = ""
    entries = []
    for raw in raw_entries:
        assert raw["previous_event_hash"] == previous
        payload = copy.deepcopy(raw)
        artifact_hash = payload["artifact_hash"]
        payload["artifact_hash"] = ""
        assert artifact_hash == _canonical_hash(payload)
        previous = artifact_hash
        entries.append(_entry_from_raw(raw))

    trace = MathResearchTrace(trace_id=pre["trace_id"], entries=tuple(entries))
    assert audit_pre_candidate_trace(
        trace, atom_id=context.atom_id, context_packet_hash=context.packet_hash
    ).verdict is TraceGateVerdict.PASS

    plan = plan_math_research(
        signature=ProblemSignature(
            objects=(
                "3D incompressible Navier-Stokes solution",
                "strain tensor",
                "projected nonlinear remainder",
                "finite kinetic energy",
            ),
            relations=(
                "Navier-Stokes scaling",
                "orthogonal strain-space projection",
                "viscous dissipation",
                "advection and quadratic strain production",
            ),
            domain="partial differential equations / mathematical fluid mechanics",
            goal_type="derive or falsify a global-regularity critical-control mechanism",
        ),
        record=MathResearchRecord(claim_id=context.atom_id),
        context_fiber=context,
        memory_review=memory,
        research_trace=trace,
    )
    assert plan.context_gate.verdict is ContextGateVerdict.PASS
    assert plan.memory_gate.verdict is ResearchMemoryVerdict.PASS
    assert plan.trace_gate.verdict is TraceGateVerdict.PASS
    assert plan.candidate_generation_allowed


def test_failure_record_is_hash_bound_scoped_and_nonterminal() -> None:
    raw = _load("07_memory/NS_R001D_C001_FAILURE_EXPERIENCE_DELTA_20260811.json")
    experience = raw["experiences"][0]
    payload = copy.deepcopy(experience)
    artifact_hash = payload["artifact_hash"]
    payload["artifact_hash"] = ""
    assert artifact_hash == _canonical_hash(payload)
    assert experience["diagnosis_status"] == "SUPPORTED"
    assert experience["research_trace_event_id"] == "NS-R001d-E010"
    assert "positive-time" in " ".join(experience["scope_conditions"])
    assert "actual Navier-Stokes evolution" in experience["selected_diagnosis"]
    assert any(link["relation"] == "SAME_METHOD_FAMILY_AS" for link in raw["links"])
    assert any(link["relation"] == "SHARES_BROKEN_ASSUMPTION_WITH" for link in raw["links"])

    candidate = (BASE / "04_candidates/NS_R001D_C001_STATIC_REMAINDER_RATIO_SCREEN_20260811.md").read_text(encoding="utf-8")
    falsifier = (BASE / "05_falsifiers/NS_R001D_C001_EXACT_GAUSSIAN_FALSIFIER_20260811.md").read_text(encoding="utf-8")
    dag = (BASE / "02_problem_dag/NS_R001D_DELTA_20260811.yaml").read_text(encoding="utf-8")
    assert "not the Navier–Stokes solution scaling" in candidate
    assert "does **not** say that `Q(u(t))` becomes large" in falsifier
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in dag
    assert "NS-R001d1" in dag
