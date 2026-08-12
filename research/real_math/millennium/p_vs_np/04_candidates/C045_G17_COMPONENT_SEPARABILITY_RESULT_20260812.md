# C045 G17 component-separability result

**Parallel fibre commit actually used:** `e6d7f886416bf954e368db8edd028f4870fc7a1f`  
**Fibre hash:** `sha256:7c96aab2cbb6bb6151aaa9ae2c34c9259d0964417ce7c9300be9e6d04573f182`  
**Authority:** `RETROSPECTIVE MATHEMATICAL TRUTH CHECK / NO STRICT DISCOVERY CREDIT`  
**Root:** `OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE`

## Chronology boundary

The mathematical result commit `b8f59bca9609d454612e45a8998e584dad7aa043`
was publicly exposed through PR #228 no later than `2026-08-12T01:17:20Z`.
The later merged C045 candidate/evaluator freeze was materialized only after that
exposure. Therefore no later U17 packet can receive prospective, untouched-target,
or strict RAKL discovery authority. The hand arguments below may be checked for
truth retrospectively; the frozen U17 evaluator remains unauthorized and is not
used here. Chronology, Git and CI are assurance metadata and earn zero
mathematical saturation credit.

## Source binding

The cover semantics are bound to Cavalar--Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 (18 March 2025), local pinned source `00_sources/ECCC_TR25_033_20250318.pdf`, blob `8dfe370a6bf687eb33ebf52eaaf9308e1bdf0230`. In Definitions 18--21 a semi-filter is nonempty and upward closed but excludes the empty set; being above a graph element forces the generator traces into the semi-filter; a pair is preserved when membership of both sides forces membership of their intersection; and cover complexity is the minimum number of pairs preventing any above semi-filter from preserving all pairs. Theorem 22 gives `rho <= D_intersection`. These are the only source-level cover facts used here. Primary source: https://eccc.weizmann.ac.il/report/2025/033/ .

The recursive graph/decoder is the frozen application object in `04_candidates/C041_fx_sat_one_sided.py`. C043 supplies the exact canonical length formula and the accumulated G16 fibre facts. C044 supplies the heterogeneous component-multiplexing upper lemma and an explicit three-pair cover of the G16 twin quotient.

## Theorem 1 — exact canonical length-32 UNSAT batch

Write `a=bitlength(v)` and `b=bitlength(m)`. Before optional zero padding,

`L0 = 6 + 2a + 2b + 3m(a+1)`.

A final encoding of length 32 must have `L0` equal to 31 or 32.

For `m=1`, `b=1` and `L0=11+5a`; hence only `a=4` gives raw length 31 and padded length 32, corresponding to `v in {8,...,15}`. Every one-clause CNF is satisfiable.

For `m>=2` and `a=1`, `L0=8+2b+6m` is even and never 32 for a consistent bitlength `b=bitlength(m)`. For `m>=2` and `a>=2`, the minimum is attained at `a=b=m=2`, where `L0=32`; increasing either `a` or `m` makes the length strictly larger. Therefore the only potentially UNSAT length-32 parameter pairs are `(v,m)=(2,2)` and `(3,2)`.

For a non-tautological three-literal clause over `v` variables, if it contains `d` distinct variables then its falsifying set has size `2^(v-d)`, at most `2^(v-1)`, with equality exactly when all three literals are the same signed variable. Two clauses can be jointly UNSAT only if their two falsifying sets cover all `2^v` assignments. The size bound forces both clauses to be repeated unit clauses, and disjointness of their falsifying half-cubes forces opposite signs on the same variable. Conversely such a pair is UNSAT.

Hence there are exactly `2v` ordered UNSAT formulas for each `v`: four for `v=2` and six for `v=3`, ten total.

At the 16/16 split, writing each new complement edge by `(row, fresh-column-offset)`, the ten edges are

```
q0=(58696,37741)   q1=(58698,55881)
q2=(58697, 9654)   q3=(58699,27794)
q4=(58728,37741)   q5=(58730,55881)
q6=(58729, 9654)   q7=(58729,47103)
q8=(58731,27794)   q9=(58731,65243)
```

The actual G17 columns are `65536 + fresh-column-offset`.

## Theorem 2 — the new batch is a disjoint complement block

C043's accumulated G16 complement has nonempty row support only on the previously registered old rows, including the length-30 active rows `29402,29403,29406,29407`; none of the eight new rows `58696,58697,58698,58699,58728,58729,58730,58731` was previously active. Every new G17 column lies in the fresh half and is therefore outside the G16 column projection.

Under the frozen recursive rule, G17's complement is exactly the embedded top-left copy `U_old=U16` together with the ten length-32 UNSAT cross edges `U_new` above; the remaining two quadrants contribute no complement edges. Consequently

- `U_old` and `U_new` are disjoint ground sets,
- their row projections are disjoint,
- their column projections are disjoint, and
- there is no complement cell coupling the two blocks.

Thus the C044 component-coupling gate does **not** fire at G17. This is a local mathematical negative result, not a statement that coupling can never occur later.

## Theorem 3 — explicit three-pair cover of the new block

Assign the ten new complement edges the following three-bit words, read coordinatewise with `0=E`, `1=H`:

```
q0 000   q1 010   q2 111   q3 100   q4 001
q5 010   q6 011   q7 011   q8 100   q9 101
```

For each coordinate `j=1,2,3`, let `E_j` be the new edges with bit 0 and `H_j` the new edges with bit 1. Each `(E_j,H_j)` is a disjoint partition of `U_new`.

The nonempty row-star signatures are

```
58696 EEE   58697 HHH   58698 EHE   58699 HEE
58728 EEH   58729 EHH   58730 EHE   58731 HEX
```

and the nonempty column-star signatures are

```
 9654 XHH   27794 HEE   37741 EEX
47103 EHH   55881 EHE   65243 HEH
```

For transparency, the following table gives one separating coordinate for every active row/column graph cell; `-` marks a complement edge.

```
          9654 27794 37741 47103 55881 65243
58696       2     1     -     2     2     1
58697       -     2     1     1     1     2
58698       3     1     2     3     -     1
58699       2     -     1     1     1     3
58728       2     1     -     2     2     1
58729       -     1     2     -     3     1
58730       3     1     2     3     -     1
58731       2     -     1     1     1     -
```

At the displayed coordinate the entire row star lies in one side and the entire column star lies in the opposite side. Any semi-filter above that graph edge therefore contains both pair sides by Definition 19 plus upward closure, while their intersection is empty and cannot belong to a semi-filter. Hence the pair covers every above semi-filter. Therefore the new block has a legal three-pair generator-separating cover.

## Theorem 4 — G17 still has a constant four-pair upper cover

Let `(E_j^old,H_j^old)`, `j=1,2,3`, be the C044 three-pair G16 cover lifted from the exact quotient to `U_old`, and let `(E_j^new,H_j^new)` be the three new pairs above. Form three indexwise pairs

`(E_j^old union E_j^new, H_j^old union H_j^new)`.

They are disjoint because the two complement blocks are disjoint, and they cover every relevant graph edge whose two nonempty generator traces lie in the same block. Add the separator pair `(U_old,U_new)`. Any relevant graph edge whose row and column traces lie in different blocks is covered by this separator pair; an edge with an empty trace admits no above semi-filter because that would force the empty set into it.

Thus

`rho(G17) <= sigma(G17) <= 4`.

This is an upper bound only. It does not prove `rho(G17)=4`, does not rule out a different three-pair cover, and gives no asymptotic upper bound without a uniform recurrence proof.

## Diagnosis, obstruction and next action

**Episode outcome.** The prospectively frozen C045 atom asked whether the first untouched length-32 batch creates load-bearing cross-component complement coupling. It does not; exact syntax produces a third block whose row and column projections are disjoint from G16.

**Diagnosis.** The failure is mathematical/representation-local, not retrieval or tooling: fresh semantic UNSAT mass is again noncoercive because the recursive decoder activates it on rows that were previously complement-empty and on necessarily fresh columns.

**Reusable obstruction/lesson.** In this one-sided family, a new semantic batch cannot defeat component multiplexing unless at least one newly UNSAT prefix row already lies in the accumulated old complement row projection. Fresh columns alone never couple backward. The next strict atom should therefore search the canonical length schedule for the **first row-projection collision**, before enumerating cover graphs or LPs.

This is distinct from local-to-global gluing. The local G17 proof closes; the gluing to an asymptotic cover recurrence, to a circuit lower bound, or to `P != NP` is absent and remains open.

## Authority and novelty

The local result is a proposal-only `compositional` mathematical contribution with a `representation` sublemma: exact decoder classification + a new three-bit star code + the prior C044 multiplexing theorem yield the four-pair upper cover. It is proposal/shadow only. Protected retained semantic novelty remains zero on all seven RAKL axes until promotion gates authorize otherwise. Same-context review is not independent review; independent mathematical review count remains `0/3`.
