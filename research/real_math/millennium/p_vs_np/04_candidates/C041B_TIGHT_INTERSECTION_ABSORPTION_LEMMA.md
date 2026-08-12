# C041B — tight-intersection absorption for even-even off-slice witnesses

**Atom:** `O9d12a2a1b-C041B`  
**Authority:** `PROPOSAL_SHADOW_EXACT_LOCAL_LEMMA / NO_STRICT_RAKL_DISCOVERY_CREDIT / NO_ROOT_AUTHORITY`  
**Framework:** current `SzeChunYiu/RAKL@43897d3afaf0038385102d5acc64793c05ec40f0`, method `3.0.0`

## Chronology boundary

The mathematical idea below was derived before the child verification fibre was persisted. The current-v3 context, dual-memory, obstruction-transformation GLUE review, expert cell and hash-chain therefore govern verification and future routing only. They do not retroactively create strict context-first discovery credit.

## Source-bound setup

Use Cavalar–Oliveira Definition 18–21 exactly. A semi-filter over a complement ground set is a nonempty upward-closed family of subsets that excludes the empty set. A semi-filter above a graph element contains every generator trace through that element. A pair `(E,H)` covers a relevant semi-filter precisely when `E,H` belong to the semi-filter but `E∩H` does not.

Let the parent complement ground set be `U`. Let `i:U -> U0` be the odd-odd embedding into the child ambient square. Let `U'` be a child complement such that its odd-odd part is exactly `U0=i(U)`. Fix a parent feasible C024 dual `y` on relevant parent semi-filters.

For each relevant parent semi-filter `F`, define its cylinder lift

`F^↑ = { X subseteq U' : i^{-1}(X ∩ U0) in F }`.

Give `F^↑` the old weight `y_F`. No fresh child weight is yet added.

Let `w=(r,c)` be a child graph edge with both `r` and `c` even. Put

`S = R_r ∩ U'`, `T = C_c ∩ U'`.

Since `w` is a graph edge, `w notin U'`; hence `S∩T=empty`. Since the old slice is odd-odd while `r,c` are even, `S∩U0=T∩U0=empty`.

Let `K` be any child semi-filter above `w`. Then Definition 19 forces `S,T in K`. In particular, if either `S` or `T` is empty, no such `K` exists because Definition 18 excludes the empty set.

## Lemma: decorated-pair load identity

For any parent pair `(A,B)` with `A,B subseteq U`, define the decorated child pair

`E = S ∪ i(A)`, `H = T ∪ i(B)`.

Then:

1. `E,H in K` by upward closure from `S,T in K`.
2. `E∩H = i(A∩B)`.
3. For every parent semi-filter `F`, the cylinder lift `F^↑` preserves `(E,H)` iff `F` preserves `(A,B)`.
4. Therefore the old lifted dual load on `(E,H)` equals the parent dual load on `(A,B)`.

### Proof

The disjointness relations

`S∩T = S∩U0 = T∩U0 = empty`

imply

`(S∪i(A)) ∩ (T∪i(B)) = i(A)∩i(B) = i(A∩B)`.

Cylinder membership depends only on old-slice projection. Thus

`E in F^↑ iff A in F`,
`H in F^↑ iff B in F`,
`E∩H in F^↑ iff A∩B in F`.

So preservation/non-preservation is identical for the parent and decorated child pair. Summing the same weights `y_F` over the same non-preserving parent filters gives exact equality of pair loads. ∎

## Corollary: tight-intersection absorption is necessary

Call a parent pair `(A,B)` **tight** when its parent dual load is `1`.

If `K` is to receive any positive fresh one-coordinate dual weight while all lifted old weights are kept fixed, then for every tight parent pair `(A,B)`,

`i(A∩B) in K`.

Indeed, if a tight `(A,B)` has `i(A∩B) notin K`, then the decorated child pair `(E,H)` covers `K` because `E,H in K` but `E∩H notin K`. By the load identity, that child pair already has old lifted load `1`. Any positive fresh mass on `K` violates its dual constraint.

Hence a particularly sharp obstruction follows:

> If the fixed parent dual has a tight pair `(A,B)` with `A∩B=empty`, then no child semi-filter above any even-even graph edge can receive positive fresh one-coordinate mass under the unchanged cylinder-lifted old dual.

The reason is Definition 18: `empty notin K`.

## Exact scope and non-claims

This is a **necessary**, not sufficient, criterion. Even if `K` contains every tight parent intersection, some other saturated child pair may cover `K`. The lemma also does not cover mixed-parity child edges, where old/new cross terms can occur. It assumes the old odd-odd complement slice is unchanged, and it keeps the parent dual weights fixed.

Nothing here proves the existence of a useful `K`, the existence of a tight disjoint parent pair for every relevant parent certificate, multi-coordinate augmentation, a uniform recurrence, divergent growth, a source-compatible circuit rate, NP membership/reduction, or `P != NP`.

## RAKL interpretation

The current-v3 semantic shortcut selected a scoped `GLUE`: C024 supplies exact pair-load/tightness semantics; C041A supplies old-slice/cylinder projection. The result compresses one child obstruction into parent data. In RAKL novelty taxonomy this is defensibly **compositional** and **representation** level only; external mathematical novelty is unassessed and protected novelty remains zero until normal gates authorize retention.

## Primary source

Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 (2025), Definitions 18–21. Published version: ACM Transactions on Computation Theory 17(2), Article 13 (2025), DOI 10.1145/3718746.
