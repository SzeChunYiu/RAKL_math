from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HODGE = ROOT / "research/real_math/millennium/hodge/deformation"
DIAGNOSIS = HODGE / "07_memory/H4d1c_C004_DIAGNOSIS_20260812.json"
ROUTE = HODGE / "03_routes/H4d1c_C004_TOTAL_WITNESS_BASE_PROJECTION_NOGO_20260812.md"
CASE_STUDY = HODGE / "10_case_study/H4d1c_C004_RAKL_METHOD_CASE_STUDY_20260812.md"
CONTEXT = HODGE / "01_frontier/H4d1c_C004_PROJECTION_FAITHFULNESS_CONTEXT_20260812.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _canonical_hash(value: dict) -> str:
    payload = copy.deepcopy(value)
    payload.pop("artifact_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _image(vectors: tuple[tuple[int, int], ...]) -> set[tuple[int, int]]:
    # The finite coefficient set is sufficient for the displayed basis-image identities.
    return {
        tuple(sum(c * vector[i] for c, vector in zip(coeffs, vectors)) for i in range(2))
        for coeffs in ((a, b) for a in range(-1, 2) for b in range(-1, 2))
    }


def test_diagnosis_uses_non_reserved_episode_pointer_and_self_hashes() -> None:
    diagnosis = _load(DIAGNOSIS)
    assert "episode_id" not in diagnosis
    assert diagnosis["episode_pointer"] == "H4d1c-C004-TOTAL-WITNESS-PROJECTION-FAITHFULNESS"
    assert diagnosis["artifact_hash"] == _canonical_hash(diagnosis)
    assert "NOT A STRICT RAKL CONTEXT_FIRST_DISCOVERY" in diagnosis["chronology_status"]


def test_exact_linear_counterexample_refutes_only_source_to_image_implication() -> None:
    # p(e1)=v1 and p(e2)=0.  A=<e1> is strictly contained in B=<e1,e2>,
    # yet the two sampled linear images agree and omit v2.
    p_e1 = (1, 0)
    p_e2 = (0, 0)
    image_a = _image((p_e1, (0, 0)))
    image_b = _image((p_e1, p_e2))
    assert image_a == image_b
    assert (0, 1) not in image_b

    route = ROUTE.read_text(encoding="utf-8")
    assert "B/A -> H/p(A)" in route
    assert "p(B)=H" in route
    assert "neither follows from `A proper_subset B`" in route


def test_hodge_atlas_warning_and_authority_boundaries_are_preserved() -> None:
    route = ROUTE.read_text(encoding="utf-8")
    case_study = CASE_STUDY.read_text(encoding="utf-8")
    assert "FM-HODGE-REPRESENTATION-EQUIVALENCE-NOT-REDUCTION" in route
    assert "Representation equivalence is not reduction" in route
    assert "representation enlargement is not target-image gain" in route
    assert "does not contain the full pinned-RAKL pre-candidate event sequence" in case_study
    assert "Software tests, CI, hashes, repository growth" in case_study
    assert "zero mathematical or independent-review credit" in case_study
    assert "not** a strict RAKL context-first discovery certificate" in case_study


def test_exact_pinned_framework_and_no_higher_order_or_root_claim() -> None:
    context = _load(CONTEXT)
    assert context["framework"]["live_main_sha"] == "43897d3afaf0038385102d5acc64793c05ec40f0"
    route = ROUTE.read_text(encoding="utf-8")
    assert "NO_HODGE_THEOREM" in route
    assert "NO_ROOT_AUTHORITY" in route
    assert "higher Artin" in route
    assert "root initial-algebraicity" in route
