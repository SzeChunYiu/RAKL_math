from itertools import combinations


def powerset(xs):
    xs = list(xs)
    return [frozenset(c) for r in range(len(xs) + 1) for c in combinations(xs, r)]


def semifilters(universe):
    ps = powerset(universe)
    out = []
    for mask in range(1 << len(ps)):
        fam = {ps[i] for i in range(len(ps)) if (mask >> i) & 1}
        if not fam or frozenset() in fam:
            continue
        if all(not (a <= b) or b in fam for a in fam for b in ps):
            out.append(fam)
    return out


def test_decorated_pair_projection_and_preservation_exhaustive_two_point_parent():
    parent = {0, 1}
    old = {("o", 0), ("o", 1)}
    row_trace = {("s", 0), ("s", 1)}
    col_trace = {("t", 0)}
    child = old | row_trace | col_trace

    def lift(fam):
        return {
            x
            for x in powerset(child)
            if frozenset(v for tag, v in x if tag == "o") in fam
        }

    checks = 0
    for fam in semifilters(parent):
        lifted = lift(fam)
        for a in powerset(parent):
            for b in powerset(parent):
                e = row_trace | {("o", x) for x in a}
                h = col_trace | {("o", x) for x in b}
                assert e & h == {("o", x) for x in (a & b)}
                parent_preserves = not (a in fam and b in fam and (a & b) not in fam)
                child_preserves = not (
                    frozenset(e) in lifted
                    and frozenset(h) in lifted
                    and frozenset(e & h) not in lifted
                )
                assert parent_preserves == child_preserves
                checks += 1
    assert checks == 64


def test_empty_generator_trace_cannot_belong_to_semifilter():
    # This mirrors Definition 18's non-triviality condition: emptyset is excluded.
    for fam in semifilters({0, 1}):
        assert frozenset() not in fam


def test_mixed_old_new_support_breaks_the_simple_intersection_identity():
    old_x = ("o", 0)
    row_trace = {old_x, ("s", 0)}
    col_trace = {("t", 0)}
    a = set()
    b = {old_x}
    e = row_trace | a
    h = col_trace | b
    # The old point in the row trace creates a cross term, which is why C041B is
    # explicitly restricted to even-even witness edges in an odd-odd old slice.
    assert e & h == {old_x}
