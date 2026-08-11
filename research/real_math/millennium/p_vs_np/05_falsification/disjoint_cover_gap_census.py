"""Prospective exact discriminator for essential non-disjoint pair power.

This file is additive and leaves the historical full_cover_oracle.py bytes
unchanged. It reuses that oracle's exact relevant-semi-filter and
Definition-20 pair predicate, changing only the admissible pair family.

Finite outputs are calibration/falsification evidence only.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json

from full_cover_oracle import (
    _maximal_masks,
    _relevant_semifilters,
    c008_gadget_complement,
    exact_full_cover_number,
    pair_covers_semifilter,
)

Edge = tuple[int, int]

SAMPLE_SET_ID = "C026-FRESH-M5-20260811-v1"
SAMPLE_SEED = "C026-FRESH-M5-20260811-v1"
EXPECTED_SAMPLE_MANIFEST_SHA256 = "47b3502c6075d99027c609fbecbc1a637d6650a6c2ba3462cc825fb28337a831"
SAMPLE_COUNT = 64


@dataclass(frozen=True)
class RestrictedCoverResult:
    minimum_pairs: int
    relevant_semifilters: int
    distinct_maximal_pair_masks: int


def exact_disjoint_cover_number(
    n_vertices_per_side: int,
    complement: set[Edge],
) -> RestrictedCoverResult:
    """Exact full-cover optimum using only pairs with E intersection H empty."""
    filters = _relevant_semifilters(n_vertices_per_side, complement)
    if not filters:
        return RestrictedCoverResult(0, 0, 0)

    universe_size = len(complement)
    masks: set[int] = set()
    for e_set in range(1 << universe_size):
        for h_set in range(1 << universe_size):
            if e_set & h_set:
                continue
            mask = 0
            for bit, minimals in enumerate(filters):
                if pair_covers_semifilter(minimals, e_set, h_set):
                    mask |= 1 << bit
            if mask:
                masks.add(mask)

    maximal = _maximal_masks(masks)
    full = (1 << len(filters)) - 1
    queue = deque([0])
    depth = {0: 0}
    while queue:
        current = queue.popleft()
        next_depth = depth[current] + 1
        for pair_mask in maximal:
            nxt = current | pair_mask
            if nxt == full:
                return RestrictedCoverResult(next_depth, len(filters), len(maximal))
            if nxt != current and nxt not in depth:
                depth[nxt] = next_depth
                queue.append(nxt)
    raise RuntimeError("disjoint pair universe failed to cover relevant semi-filters")


def _canonical_complement(complement: tuple[Edge, ...]) -> str:
    return ";".join(f"{u},{v}" for u, v in complement)


def frozen_sample_manifest() -> list[dict[str, object]]:
    edges = tuple((u, v) for u in range(4) for v in range(4))
    ranked: list[tuple[str, tuple[Edge, ...]]] = []
    for complement in combinations(edges, 5):
        digest = sha256(
            (SAMPLE_SEED + "|" + _canonical_complement(complement)).encode("utf-8")
        ).hexdigest()
        ranked.append((digest, complement))
    ranked.sort()
    selected = ranked[:SAMPLE_COUNT]
    manifest = [
        {
            "sample_id": f"C026-M5-{index:03d}",
            "sha256": digest,
            "complement": [list(edge) for edge in complement],
        }
        for index, (digest, complement) in enumerate(selected, 1)
    ]
    manifest_digest = sha256(
        json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    if manifest_digest != EXPECTED_SAMPLE_MANIFEST_SHA256:
        raise RuntimeError(
            "frozen sample manifest mismatch: "
            f"{manifest_digest} != {EXPECTED_SAMPLE_MANIFEST_SHA256}"
        )
    return manifest


def run_census() -> dict[str, object]:
    # Negative control: C008 is known to have unrestricted optimum two and C010
    # supplies a two-pair all-disjoint cover, so both exact optima must be two.
    c008 = c008_gadget_complement()
    c008_unrestricted = exact_full_cover_number(3, c008).minimum_pairs
    c008_disjoint = exact_disjoint_cover_number(3, c008).minimum_pairs
    if (c008_unrestricted, c008_disjoint) != (2, 2):
        raise RuntimeError("C008 restricted/unrestricted negative control failed")

    rows: list[dict[str, object]] = []
    gap_rows: list[dict[str, object]] = []
    distribution: Counter[str] = Counter()

    for item in frozen_sample_manifest():
        complement = {tuple(edge) for edge in item["complement"]}
        unrestricted = exact_full_cover_number(4, complement).minimum_pairs
        disjoint = exact_disjoint_cover_number(4, complement).minimum_pairs
        if disjoint < unrestricted:
            raise RuntimeError("restriction monotonicity violated: rho_disj < rho")
        row = {
            **item,
            "rho": unrestricted,
            "rho_disj": disjoint,
            "strict_gap": disjoint > unrestricted,
        }
        rows.append(row)
        distribution[f"{unrestricted}->{disjoint}"] += 1
        if row["strict_gap"]:
            gap_rows.append(row)

    output = {
        "protocol": "C026-DISJOINT-COVER-GAP-CENSUS-v1",
        "sample_set_id": SAMPLE_SET_ID,
        "sample_manifest_sha256": EXPECTED_SAMPLE_MANIFEST_SHA256,
        "graph_count": len(rows),
        "c008_negative_control": {
            "rho": c008_unrestricted,
            "rho_disj": c008_disjoint,
        },
        "strict_gap_count": len(gap_rows),
        "first_strict_gap": gap_rows[0] if gap_rows else None,
        "distribution": dict(sorted(distribution.items())),
        "rows": rows,
        "authority": (
            "FINITE_EXACT_COMPUTATIONAL_CALIBRATION_ONLY/"
            "NO_ASYMPTOTIC_PROOF/NO_NOVELTY_CLAIM/ROOT_AUTHORITY_NONE"
        ),
    }
    payload = json.dumps(output, sort_keys=True, separators=(",", ":")).encode("utf-8")
    output["output_sha256"] = sha256(payload).hexdigest()
    return output


if __name__ == "__main__":
    print(json.dumps(run_census(), indent=2, sort_keys=True))
