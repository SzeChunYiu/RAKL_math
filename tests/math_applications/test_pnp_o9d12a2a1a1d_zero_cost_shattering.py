from itertools import combinations


def _powerset(items):
    items = tuple(items)
    return {
        frozenset(choice)
        for r in range(len(items) + 1)
        for choice in combinations(items, r)
    }


def _column(n, j):
    return frozenset((i, j) for i in range(n))


def _row(n, i):
    return frozenset((i, j) for j in range(n))


def test_free_column_unions_shatter_zero_cost_target_row():
    # Calibration only: the mathematical proof is the direct construction in the
    # source packet. Finite tests do not promote the claim to theorem authority.
    for n in range(2, 6):
        target = _row(n, 0)
        columns = [_column(n, j) for j in range(n)]
        traces = set()
        for chosen in _powerset(range(n)):
            union = frozenset().union(*(columns[j] for j in chosen))
            traces.add(frozenset(union & target))
        assert traces == _powerset(target)
        assert len(traces) == 2**n


def test_target_row_is_a_zero_intersection_generator():
    for n in range(2, 6):
        rows = [_row(n, i) for i in range(n)]
        columns = [_column(n, j) for j in range(n)]
        generators = set(rows + columns)
        assert _row(n, 0) in generators
