"""Frozen evaluator for the C051 exact H_19/P_20 interface.

This file is deliberately not executed in the candidate-freeze round.  Its
future output must be recorded only after the candidate and this evaluator are
publicly frozen.  Enumeration is a discovery/checking aid; any promoted result
must include a direct finite mathematical certificate.
"""

from __future__ import annotations

from itertools import product


MAGIC = "11100101"


def gamma(value: int) -> str:
    bits = f"{value:b}"
    return "0" * (len(bits) - 1) + bits


def token(variable: int, *, negated: bool, width: int) -> str:
    return ("1" if negated else "0") + f"{variable:0{width}b}"


def parent_word(signs: tuple[bool, ...]) -> str:
    """Canonical v=1,m=4 word; signs are the twelve literal signs."""
    if len(signs) != 12:
        raise ValueError("the v=1,m=4 parent has exactly twelve literals")
    return MAGIC + gamma(1) + gamma(4) + "".join(
        token(1, negated=sign, width=1) for sign in signs
    )


def parent_is_unsat(signs: tuple[bool, ...]) -> bool:
    """Exact two-assignment check for the one-variable four-clause formula."""
    clauses = tuple(signs[index : index + 3] for index in range(0, 12, 3))
    for z in (False, True):
        if all(any((not z) if sign else z for sign in clause) for clause in clauses):
            return False
    return True


def current_word(variable_count: int, first_literal: int, first_negated: bool) -> str:
    """One canonical v in 4..7,m=2 completion for a frozen first token."""
    if variable_count not in range(4, 8):
        raise ValueError("length-40 current branches have 4 <= v <= 7")
    if not 1 <= first_literal <= variable_count:
        raise ValueError("first literal index lies outside the declared range")
    first = token(first_literal, negated=first_negated, width=3)
    filler = token(1, negated=False, width=3)
    return MAGIC + gamma(variable_count) + gamma(2) + first + filler * 5


def evaluate() -> dict:
    parent_count = 0
    current_prefixes: dict[str, tuple[int, int, bool, str]] = {}
    for variable_count in range(4, 8):
        for first_literal in range(1, variable_count + 1):
            for first_negated in (False, True):
                word = current_word(variable_count, first_literal, first_negated)
                assert len(word) == 40
                current_prefixes.setdefault(
                    word[:20],
                    (variable_count, first_literal, first_negated, word),
                )

    for signs in product((False, True), repeat=12):
        if not parent_is_unsat(signs):
            continue
        parent_count += 1
        word = parent_word(signs)
        assert len(word) == 38
        label = "1" + word[19:]
        if label in current_prefixes:
            variable_count, first_literal, first_negated, current = current_prefixes[label]
            return {
                "branch": "EXACT_OVERLAP_WITNESS",
                "k": 19,
                "parent_signs": [int(sign) for sign in signs],
                "parent_word": word,
                "parent_unsat": True,
                "current_parameters": {
                    "v": variable_count,
                    "m": 2,
                    "first_literal": first_literal,
                    "first_negated": first_negated,
                },
                "current_word": current,
                "shared_label": label,
                "parent_unsat_words_examined_before_witness": parent_count,
                "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
            }

    return {
        "branch": "SCOPED_OVERLAP_IMPOSSIBILITY",
        "k": 19,
        "parent_unsat_words_examined": parent_count,
        "current_prefixes_examined": len(current_prefixes),
        "scope": "exact frozen C041 canonical grammar, equal split, and C048 swapped interface",
        "root_state": "OPEN_NO_SOLUTION_CERTIFICATE",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(evaluate(), indent=2, sort_keys=True))
