"""Source-bound C053 structural phase screen; no SAT or overlap access.

This module classifies only two already-public canonical syntax separators:

1. a parent parity pad forcing ``h[k]=0`` against a current endpoint forced to 1;
2. a complete parent payload-token phase lying inside the fixed current header
   and decoding to an illegal parent variable index.

Survival means only that these two separator families do not decide the pair.
It is not evidence that the corresponding word languages intersect.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
C041 = ROOT / "research/real_math/millennium/p_vs_np/04_candidates/C041_fx_sat_one_sided.py"
C041_RAW_SHA256 = "c0caca2fe7244c3d847de8b59473cec72132ec04ad3e9fab668f5cd95a2bd75a"
MAGIC = "11100101"


def gamma(value: int) -> str:
    bits = f"{value:b}"
    return "0" * (len(bits) - 1) + bits


def cell(a: int, m: int) -> dict:
    b = m.bit_length()
    header = 6 + 2 * a + 2 * b
    width = 1 + a
    raw = header + 3 * m * width
    padding = raw & 1
    return {
        "a": a,
        "b": b,
        "m": m,
        "header": header,
        "width": width,
        "raw": raw,
        "padding": padding,
        "encoded": raw + padding,
        "v_min": 1 << (a - 1),
        "v_max": (1 << a) - 1,
    }


def support_cells(encoded_length: int, *, parent: bool) -> list[dict]:
    minimum_m = 2 if parent else 1
    return [
        row
        for a in range(1, encoded_length + 1)
        for m in range(minimum_m, encoded_length + 1)
        if (row := cell(a, m))["encoded"] == encoded_length
    ]


def fixed_header(v: int, m: int) -> str:
    return MAGIC + gamma(v) + gamma(m)


def current_endpoint_values(v: int, m: int, k: int) -> set[str]:
    """Possible values of p[k] over legal current payload literals."""
    header = fixed_header(v, m)
    if k < len(header):
        return {header[k]}
    width = 1 + v.bit_length()
    phase = (k - len(header)) % width
    if phase == 0:
        return {"0", "1"}
    return {
        f"{variable:0{v.bit_length()}b}"[phase - 1]
        for variable in range(1, v + 1)
    }


def mapped_fixed_header_tokens(parent: dict, current_v: int, current_m: int, k: int) -> list[dict]:
    """Return complete parent tokens whose h positions lie in the current header."""
    header = fixed_header(current_v, current_m)
    rows = []
    for token in range(3 * parent["m"]):
        # h[j]=x[k+j-1], so x[H+t*w] maps to j=H+t*w-k+1.
        start = parent["header"] + token * parent["width"] - k + 1
        end = start + parent["width"]
        # h[0] is the prepended 1 and is not x[k-1]; only h[j], j>=1,
        # participates in the parent-word coordinate map.
        if 1 <= start and end <= min(k + 1, len(header)):
            bits = header[start:end]
            rows.append(
                {
                    "parent_token": token,
                    "h_start": start,
                    "bits": bits,
                    "variable_code": int(bits[1:], 2),
                }
            )
    return rows


def parameter_pair_status(parent: dict, parent_v: int, current: dict, current_v: int, k: int) -> dict:
    endpoint_values = current_endpoint_values(current_v, current["m"], k)
    endpoint_conflict = parent["padding"] == 1 and endpoint_values == {"1"}
    mapped = mapped_fixed_header_tokens(parent, current_v, current["m"], k)
    illegal = [row for row in mapped if not 1 <= row["variable_code"] <= parent_v]
    return {
        "endpoint_values": sorted(endpoint_values),
        "endpoint_forced_conflict": endpoint_conflict,
        "mapped_fixed_header_tokens": mapped,
        "mapped_illegal_tokens": illegal,
        "survives_known_screen": not endpoint_conflict and not illegal,
    }


def classify_k(k: int) -> dict:
    parents = support_cells(2 * k, parent=True)
    currents = support_cells(2 * (k + 1), parent=False)
    matrix = []
    endpoint_count = illegal_count = survivor_count = total = 0
    for parent in parents:
        for current in currents:
            local_endpoint = local_illegal = local_survivor = local_total = 0
            example_survivor = None
            for parent_v in range(parent["v_min"], parent["v_max"] + 1):
                for current_v in range(current["v_min"], current["v_max"] + 1):
                    status = parameter_pair_status(parent, parent_v, current, current_v, k)
                    local_total += 1
                    local_endpoint += int(status["endpoint_forced_conflict"])
                    local_illegal += int(bool(status["mapped_illegal_tokens"]))
                    local_survivor += int(status["survives_known_screen"])
                    if status["survives_known_screen"] and example_survivor is None:
                        example_survivor = {
                            "parent_v": parent_v,
                            "current_v": current_v,
                            "endpoint_values": status["endpoint_values"],
                            "mapped_fixed_header_tokens": status["mapped_fixed_header_tokens"],
                        }
            matrix.append(
                {
                    "parent_cell": (parent["a"], parent["m"]),
                    "current_cell": (current["a"], current["m"]),
                    "parameter_pair_count": local_total,
                    "endpoint_forced_conflict_count": local_endpoint,
                    "mapped_illegal_token_count": local_illegal,
                    "surviving_parameter_pair_count": local_survivor,
                    "example_survivor": example_survivor,
                }
            )
            total += local_total
            endpoint_count += local_endpoint
            illegal_count += local_illegal
            survivor_count += local_survivor
    return {
        "k": k,
        "parent_support_cells": parents,
        "current_support_cells": currents,
        "cell_phase_matrix": matrix,
        "parameter_pair_count": total,
        "endpoint_forced_conflict_count": endpoint_count,
        "mapped_illegal_token_count": illegal_count,
        "surviving_parameter_pair_count": survivor_count,
    }


def classify() -> dict:
    if hashlib.sha256(C041.read_bytes()).hexdigest() != C041_RAW_SHA256:
        raise RuntimeError("frozen C041 source moved")
    k31 = classify_k(31)
    k32 = classify_k(32)
    return {
        "screen_id": "PNP-C053-K32-BOUNDARY-TOKEN-PHASE-SCREEN-v1",
        "bounded_k_values": [31, 32],
        "k31": k31,
        "k32": k32,
        "least_surviving_k": 32 if not k31["surviving_parameter_pair_count"] and k32["surviving_parameter_pair_count"] else None,
        "proved_scope": "only the two k31 separator families over exact C041 support and fixed-header token phases",
        "non_guarantee": "screen survival does not imply canonical word compatibility, UNSAT parent membership, overlap, collision, cover growth, circuit lower bounds, or P versus NP",
        "overlap_or_sat_accessed": False,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(classify(), indent=2, sort_keys=True))
