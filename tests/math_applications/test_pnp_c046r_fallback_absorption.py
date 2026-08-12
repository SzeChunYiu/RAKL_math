"""Calibration/falsification checks for the C046R fallback-aware four-pair witness.

This finite check is not a proof and grants no mathematical or root authority.
The hand case proof is recorded in C046R_FALLBACK_ABSORPTION_RESULT_20260812.md.
"""


def test_c046r_repaired_four_pairs_separate_bound_active_quotient_cells() -> None:
    old_edges = {
        "a": ("oR0", "oC0"),
        "b": ("oR1", "oC2"),
        "c": ("oR2", "oC1"),
        "d": ("oR2", "oC2"),
        "e": ("oR4", "oC4"),
        "f": ("oR5", "oC5"),
        "g": ("oR5", "oC6"),
        "h": ("oR6", "oC5"),
        "i": ("oR7", "oC5"),
        "j": ("oR7", "oC7"),
    }
    new_data = [
        ("q0", 58696, 37741, "000"),
        ("q1", 58698, 55881, "010"),
        ("q2", 58697, 9654, "111"),
        ("q3", 58699, 27794, "100"),
        ("q4", 58728, 37741, "001"),
        ("q5", 58730, 55881, "010"),
        ("q6", 58729, 9654, "011"),
        ("q7", 58729, 47103, "011"),
        ("q8", 58731, 27794, "100"),
        ("q9", 58731, 65243, "101"),
    ]
    coords = dict(old_edges)
    for edge, row, col, _ in new_data:
        coords[edge] = (f"nR{row}", f"nC{col}")
    coords["qf"] = ("oR0", "fC0")

    old_pairs = [
        (set("abcde"), set("fghij")),
        (set("aefgh"), set("bcdij")),
        (set("abdfg"), set("cehij")),
    ]
    codes = {edge: bits for edge, _, _, bits in new_data}
    pairs = []
    for index in range(3):
        new_e = {edge for edge, bits in codes.items() if bits[index] == "0"}
        new_h = {edge for edge, bits in codes.items() if bits[index] == "1"}
        pairs.append((old_pairs[index][0] | new_e | {"qf"}, old_pairs[index][1] | new_h))
    pairs.append((set(old_edges) | {"qf"}, set(codes)))

    assert all(not (e & h) for e, h in pairs)

    rows: dict[str, set[str]] = {}
    cols: dict[str, set[str]] = {}
    for edge, (row, col) in coords.items():
        rows.setdefault(row, set()).add(edge)
        cols.setdefault(col, set()).add(edge)

    complement_cells = set(coords.values())
    checked = 0
    for row, row_star in rows.items():
        for col, col_star in cols.items():
            if (row, col) in complement_cells:
                continue
            checked += 1
            separated = False
            for e, h in pairs:
                row_side = 0 if row_star <= e else 1 if row_star <= h else None
                col_side = 0 if col_star <= e else 1 if col_star <= h else None
                if row_side is not None and col_side is not None and row_side != col_side:
                    separated = True
                    break
            assert separated, (row, col, row_star, col_star)

    assert checked == 189
