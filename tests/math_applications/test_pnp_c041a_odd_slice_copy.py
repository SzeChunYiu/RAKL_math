"""Finite calibration for C041A.

This test checks a tiny exact instance of the proof interface.  It is not proof,
novelty authority, or independent mathematical review.
"""

from itertools import combinations


def _trace_mask(points, *, row=None, col=None):
    mask = 0
    for j, (r, c) in enumerate(points):
        if (row is not None and r == row) or (col is not None and c == col):
            mask |= 1 << j
    return mask


def _semifilters(k):
    subsets = range(1 << k)
    out = []
    for fam_bits in range(1 << (1 << k)):
        fam = {s for s in subsets if fam_bits & (1 << s)}
        if not fam or 0 in fam:
            continue
        ok = True
        for s in fam:
            for t in subsets:
                if s & ~t == 0 and t not in fam:  # s subset t
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(frozenset(fam))
    return out


def _relevant_semifilters(M, U):
    U_set = set(U)
    G = {(r, c) for r in range(M) for c in range(M)} - U_set
    sfs = _semifilters(len(U))
    rel = []
    for F in sfs:
        witnesses = []
        for r, c in G:
            rt = _trace_mask(U, row=r)
            ct = _trace_mask(U, col=c)
            if rt in F and ct in F:
                witnesses.append((r, c))
        if witnesses:
            rel.append((F, tuple(witnesses)))
    return rel


def _coverage_signature(relevant, k):
    pairs = [(e, h) for e in range(1 << k) for h in range(1 << k)]
    sig = []
    for F, _ in relevant:
        covered_by = tuple(
            p for p, (e, h) in enumerate(pairs) if e in F and h in F and (e & h) not in F
        )
        sig.append((tuple(sorted(F)), covered_by))
    return tuple(sorted(sig))


def _integral_cover_optimum(relevant, k):
    pairs = [(e, h) for e in range(1 << k) for h in range(1 << k)]
    neighborhoods = []
    for e, h in pairs:
        neighborhoods.append({j for j, (F, _) in enumerate(relevant) if e in F and h in F and (e & h) not in F})
    target = set(range(len(relevant)))
    if not target:
        return 0
    for t in range(1, len(pairs) + 1):
        for chosen in combinations(range(len(pairs)), t):
            covered = set()
            for p in chosen:
                covered |= neighborhoods[p]
            if covered == target:
                return t
    raise AssertionError("finite cover not found")


def test_odd_slice_copy_is_exact_non_amplifying_calibration():
    # Parent is the N=2 diagonal-complement (G_NEQ) instance.
    parent_M = 2
    parent_U = [(0, 0), (1, 1)]

    # Zero-based implementation of the paper's one-based odd-odd embedding.
    child_M = 4
    child_U = [(2 * r, 2 * c) for r, c in parent_U]

    # Any child row/column outside the embedded parity slice has empty trace.
    assert _trace_mask(child_U, row=1) == 0
    assert _trace_mask(child_U, row=3) == 0
    assert _trace_mask(child_U, col=1) == 0
    assert _trace_mask(child_U, col=3) == 0

    parent_rel = _relevant_semifilters(parent_M, parent_U)
    child_rel = _relevant_semifilters(child_M, child_U)

    # With the complement points ordered by the embedding, the abstract
    # semi-filter families and their pair-coverage neighborhoods coincide.
    assert {F for F, _ in parent_rel} == {F for F, _ in child_rel}
    assert _coverage_signature(parent_rel, len(parent_U)) == _coverage_signature(child_rel, len(child_U))

    # Tiny exhaustive integral-cover calibration of rho equality.
    assert _integral_cover_optimum(parent_rel, len(parent_U)) == _integral_cover_optimum(child_rel, len(child_U))


def test_task_episode_is_proposal_shadow_and_root_open():
    # Static authority guard: this cycle must remain a local negative result.
    import json
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    episode = json.loads(
        (root / "research/real_math/millennium/p_vs_np/09_trace/O9d12a2a1b_C041A_TASK_EPISODE_20260811.json").read_text()
    )
    result = json.loads(
        (root / "research/real_math/millennium/p_vs_np/05_falsification/C041A_ODD_SLICE_COPY_FALSIFICATION_20260811.json").read_text()
    )

    assert episode["storage_admission"] == "PROPOSAL_SHADOW_STORED"
    assert episode["outcome"] == "FAILURE"
    assert "ZERO_AUGMENTATION" in episode["residual_signature"]
    assert result["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
    assert result["independent_review_credit"] == "0/3"
