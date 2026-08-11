from __future__ import annotations

import copy
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CROSS = ROOT / "research/real_math/millennium/cross_problem"


def _load(relative: str) -> dict:
    return json.loads((CROSS / relative).read_text(encoding="utf-8"))


def _canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _assert_self_hash(payload: dict) -> None:
    work = copy.deepcopy(payload)
    observed = work["artifact_hash"]
    work["artifact_hash"] = ""
    assert observed == _canonical_hash(work)


def _powerset(values: set[tuple[int, int]]) -> set[frozenset[tuple[int, int]]]:
    ordered = sorted(values)
    return {
        frozenset(combo)
        for r in range(len(ordered) + 1)
        for combo in itertools.combinations(ordered, r)
    }


def test_xm004_singleton_rectangle_makes_raw_closure_maximal_before_pair_propagation() -> None:
    # This executes only the source-defined set-theoretic part of the falsifier.
    # The source-stated rho(G, R_NN)=0 is bound in the artifact and primary source;
    # it is not re-proved by this finite regression.
    gamma = {(i, j) for i in range(2) for j in range(2)}
    graph = {(0, 0)}
    universe = gamma - graph
    a = (0, 0)

    # R_NN contains every U x V, hence in particular the singleton {a}.
    singleton_rectangle = {a[0]} 
    singleton_column = {a[1]}
    generator = {(i, j) for i in singleton_rectangle for j in singleton_column}
    assert generator == {a}

    trace = generator & universe
    assert trace == set()

    # Theorem-24 base closure includes every superset of the trace inside U.
    closure = {subset for subset in _powerset(universe) if trace <= set(subset)}
    assert closure == _powerset(universe)
    assert len(closure) == 2 ** len(universe)


def test_xm004_records_scoped_failure_not_closure_blacklist() -> None:
    failure = _load("07_memory/XM004_FAILURE_EXPERIENCE_DELTA_20260811.json")["experience"]
    _assert_self_hash(failure)
    assert failure["diagnosis_status"] == "SUPPORTED"
    assert "raw source-native closure volume" in failure["method_family"]
    assert "does not rule out" in failure["scope_conditions"][1]
    assert any("pair-index" in item for item in failure["local_repair_attempts"])

    mapping = _load("07_memory/XM004_TRANSFER_MAPPING_20260811.json")
    _assert_self_hash(mapping)
    assert mapping["status"] == "RETROSPECTIVE_CROSS_PROBLEM_CALIBRATION"
    assert mapping["source_authority_on_current_application_main"] == "VERIFIED_LOCAL"
    assert mapping["target_atom"] == "O9d12a2a1a1"
    assert "NO_MATHEMATICAL_CANDIDATE" in mapping["authority"]


def test_xm004_v3_episode_and_portrait_preserve_authority_boundary() -> None:
    episode = _load("07_memory/XM004_TASK_EPISODE_20260811.json")
    _assert_self_hash(episode)
    assert episode["outcome"] == "PARTIAL_SUCCESS"
    assert any("retrospective" in item for item in episode["residual_signature"])

    memory = _load("07_memory/XM004_RETROSPECTIVE_MEMORY_QUERY_20260811.json")
    _assert_self_hash(memory)
    assert memory["prospective_pre_candidate_gate_credit"] is False
    assert {item["tool_id"] for item in memory["relevant_tools"]} == {
        "T-XM-ROOT-BRIDGE-STABILITY-AUDIT",
        "T-PNP-FRACTIONAL-SEMIFILTER-PACKING",
    }

    portrait = _load("07_memory/XM004_FAILURE_PORTRAIT_20260811.json")
    _assert_self_hash(portrait)
    assert len(portrait["problems"]) == 6
    assert "ROOT_AUTHORITY_NONE" in portrait["authority"]
    pnp = next(item for item in portrait["problems"] if item["problem"] == "P versus NP")
    assert "generator-basis/upward-closure inflation" in pnp["coordinates"]
