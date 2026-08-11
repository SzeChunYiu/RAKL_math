"""Frozen C041 one-sided SAT/UNSAT cross-extension rule.

This module specifies a mathematical candidate before native evaluation.  It
does not establish an LP increment, a recurrence, a circuit lower bound, or a
P-versus-NP result.  Exhaustive satisfiability is used only to decide the
complement predicate in time exponential in the label length, hence polynomial
in the graph side length.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


Edge = tuple[int, int]
Literal = tuple[int, bool]  # (one-based variable index, is_negated)
Clause = tuple[Literal, Literal, Literal]

MAGIC = "11100101"
SEED_LEVEL = 2
SEED_COMPLEMENT: frozenset[Edge] = frozenset(
    {(0, 0), (2, 1), (1, 2), (2, 2)}
)


@dataclass(frozen=True)
class Formula3CNF:
    variable_count: int
    clauses: tuple[Clause, ...]
    decoder_branch: str


TAUTOLOGY = Formula3CNF(
    1,
    ((((1, False), (1, True), (1, False))),),
    "MALFORMED_TO_TAUTOLOGY",
)
CONTRADICTION = Formula3CNF(
    1,
    (
        ((1, False), (1, False), (1, False)),
        ((1, True), (1, True), (1, True)),
    ),
    "ALL_ZERO_SHORT_CONTRADICTION",
)


def _gamma(value: int) -> str:
    if value < 1:
        raise ValueError("gamma code is defined here only for positive integers")
    bits = f"{value:b}"
    return "0" * (len(bits) - 1) + bits


def _read_gamma(bits: str, start: int) -> tuple[int, int] | None:
    zeros = 0
    cursor = start
    while cursor < len(bits) and bits[cursor] == "0":
        zeros += 1
        cursor += 1
    if cursor >= len(bits):
        return None
    end = cursor + zeros + 1
    if end > len(bits):
        return None
    return int(bits[cursor:end], 2), end


def encode_formula(formula: Formula3CNF) -> str:
    """Return the frozen even-length canonical encoding of a nonempty 3CNF."""
    v = formula.variable_count
    m = len(formula.clauses)
    if v < 1 or m < 1:
        raise ValueError("the canonical long form requires positive v and m")
    width = v.bit_length()
    payload: list[str] = []
    for clause in formula.clauses:
        if len(clause) != 3:
            raise ValueError("every clause must contain exactly three literals")
        for variable, negated in clause:
            if not 1 <= variable <= v:
                raise ValueError("literal variable is outside the declared range")
            payload.append("1" if negated else "0")
            payload.append(f"{variable:0{width}b}")
    answer = MAGIC + _gamma(v) + _gamma(m) + "".join(payload)
    if len(answer) % 2:
        answer += "0"
    return answer


def decode_formula(bits: str) -> Formula3CNF:
    """Decode every even binary word; malformed words map to a tautology."""
    if not bits or len(bits) % 2 or set(bits) - {"0", "1"}:
        return TAUTOLOGY
    if bits == "0" * len(bits):
        return CONTRADICTION
    if not bits.startswith(MAGIC):
        return TAUTOLOGY

    first = _read_gamma(bits, len(MAGIC))
    if first is None:
        return TAUTOLOGY
    v, cursor = first
    second = _read_gamma(bits, cursor)
    if second is None:
        return TAUTOLOGY
    m, cursor = second
    width = v.bit_length()
    payload_length = 3 * m * (1 + width)
    expected_end = cursor + payload_length
    if len(bits) not in {expected_end, expected_end + 1}:
        return TAUTOLOGY
    if len(bits) == expected_end + 1 and bits[-1] != "0":
        return TAUTOLOGY

    clauses: list[Clause] = []
    for _ in range(m):
        literals: list[Literal] = []
        for _ in range(3):
            negated = bits[cursor] == "1"
            cursor += 1
            variable = int(bits[cursor : cursor + width], 2)
            cursor += width
            if not 1 <= variable <= v:
                return TAUTOLOGY
            literals.append((variable, negated))
        clauses.append(tuple(literals))  # type: ignore[arg-type]
    return Formula3CNF(v, tuple(clauses), "CANONICAL_MAGIC_LONG_FORM")


def assignment_satisfies(formula: Formula3CNF, assignment: tuple[bool, ...]) -> bool:
    if len(assignment) != formula.variable_count:
        return False
    for clause in formula.clauses:
        if not any(
            (not assignment[variable - 1]) if negated else assignment[variable - 1]
            for variable, negated in clause
        ):
            return False
    return True


def is_satisfiable(formula: Formula3CNF) -> bool:
    return any(
        assignment_satisfies(formula, assignment)
        for assignment in product((False, True), repeat=formula.variable_count)
    )


def cross_word(level: int, row: int, fresh_column_offset: int) -> str:
    side = 1 << level
    if not (0 <= row < side and 0 <= fresh_column_offset < side):
        raise ValueError("cross-layer labels lie outside the level-n old blocks")
    return f"{row:0{level}b}{fresh_column_offset:0{level}b}"


def complement_contains(level: int, row: int, column: int) -> bool:
    """Membership in U_level under the frozen recursive rule."""
    if level < SEED_LEVEL:
        raise ValueError("the family starts at level 2")
    side = 1 << level
    if not (0 <= row < side and 0 <= column < side):
        raise ValueError("vertex label lies outside the square domain")
    if level == SEED_LEVEL:
        return (row, column) in SEED_COMPLEMENT

    half = side >> 1
    if row < half and column < half:
        return complement_contains(level - 1, row, column)
    if row < half <= column:
        formula = decode_formula(cross_word(level - 1, row, column - half))
        return not is_satisfiable(formula)
    return False


def graph_edge_has_np_witness(
    level: int,
    row: int,
    column: int,
    assignment: tuple[bool, ...] | None = None,
) -> bool:
    """Polynomial verifier relation for the associated graph predicate."""
    if level < SEED_LEVEL:
        return False
    side = 1 << level
    if not (0 <= row < side and 0 <= column < side):
        return False
    if level == SEED_LEVEL:
        return (row, column) not in SEED_COMPLEMENT
    half = side >> 1
    if row < half and column < half:
        return graph_edge_has_np_witness(level - 1, row, column, assignment)
    if row < half <= column:
        formula = decode_formula(cross_word(level - 1, row, column - half))
        return assignment is not None and assignment_satisfies(formula, assignment)
    return True


def sat_reduction(formula: Formula3CNF) -> tuple[int, int, int]:
    """Map a 3CNF to an old-new graph query: (level,row,column)."""
    encoded = encode_formula(formula)
    half_length = len(encoded) // 2
    old_side = 1 << half_length
    row = int(encoded[:half_length], 2)
    fresh_column = old_side + int(encoded[half_length:], 2)
    return half_length + 1, row, fresh_column


def materialize_complement(level: int, *, maximum_level: int = 4) -> set[Edge]:
    """Materialize only tiny instances; this is not an asymptotic oracle."""
    if level > maximum_level:
        raise ValueError("finite materialization guard exceeded")
    side = 1 << level
    return {
        (row, column)
        for row in range(side)
        for column in range(side)
        if complement_contains(level, row, column)
    }
