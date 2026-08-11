# C026 — source-native semi-filter closure has unbounded one-pair cascade sensitivity

**Atom:** `O9d12a2a1a1`  
**Candidate:** `C026`  
**Authority:** `SCOPED_ROUTE_PRUNING / SOURCE-COMPATIBLE_GENERIC_DISCRETE_SPACE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`  
**Framework bound at candidate freeze:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`

## Question

C025 showed that a first-order common signature repairs C024's lost compatibility but returns to the canonical `O(log N)` representation class. The source paper already supplies a genuinely noncanonical state: the least semi-filter closure obtained by starting from the traces required above a witness and repeatedly applying the selected preservation pairs.

The next lower-bound question is not whether that state is expressive. It is whether a quantitative coordinate extracted from it can obey a bounded **one-new-pair** accounting law. C026 attacks the cheapest candidates first: raw closure volume, its logarithm, raw number of newly forced intersections, and raw propagation depth.

## Source semantics

For a finite set `U`, a semi-filter is upward closed, nonempty, and excludes `∅`. A pair `(E,H)` is preserved when membership of both endpoints forces membership of `E∩H`. A semi-filter is above a witness `w` when it contains the required generator traces `B∩U` for generators containing `w`. These are the exact source-native ingredients of Cavalar–Oliveira's cover-complexity construction.

Nothing below changes those definitions. The construction is deliberately generic in discrete complexity; it is **not** asserted to come from the row/column generators of an explicit graph.

## Proposition

For every integer `m >= 3` there is a finite discrete space and a target witness `w` with an old family of preservation pairs `Λ_old` and one additional pair `p` such that:

1. a semi-filter above `w` preserving every pair in `Λ_old` exists;
2. all old pairs are dormant in the least such closure;
3. after adding only `p`, preservation forces a chain of `m-1` intersections ending at `∅`;
4. the least upward closure changes from `m+1` sets to all `2^m` subsets of `U`.

Hence the one-pair marginal changes in raw closure cardinality, `log_2` closure cardinality, number of newly forced intersection conclusions, and propagation depth are unbounded as `m` grows.

## Construction

Let

\[
U=[m],\qquad \Gamma=U\cup\{w\},\qquad A=\{w\}.
\]

For `i in [m]`, define

\[
D_i=U\setminus\{i\},\qquad B_i=D_i\cup\{w\}.
\]

Because `w∈B_i` for every `i`, every semi-filter above `w` must contain all `D_i`.

For `2 <= j <= m`, define

\[
C_j=U\setminus\{1,\ldots,j\}.
\]

Take the old pair family

\[
\Lambda_{\rm old}
=\{(C_j,D_{j+1}):2\le j\le m-1\},
\]

and the single new pair

\[
p=(D_1,D_2).
\]

## Proof

Let `F_0` be the upward closure of `D_1,...,D_m`.

Every `D_i` has size `m-1`. Its only supersets inside `U` are itself and `U`. Therefore

\[
F_0=\{U,D_1,\ldots,D_m\},
\qquad |F_0|=m+1,
\qquad \varnothing\notin F_0.
\]

For every `j>=2`, the set `C_j` has size at most `m-2`, so `C_j` is not a superset of any `D_i` and hence `C_j\notin F_0`. Consequently the antecedent of every old pair `(C_j,D_{j+1})` is false in `F_0`; `F_0` preserves `Λ_old` vacuously. This proves that the old family alone does not eliminate the witness.

Now add `p=(D_1,D_2)`. Since both endpoints are already in every semi-filter above `w`, preservation of `p` forces

\[
C_2=D_1\cap D_2.
\]

Once `C_2` is present, the previously dormant old pair `(C_2,D_3)` forces

\[
C_3=C_2\cap D_3.
\]

Inductively, if `C_j` has been forced for some `2<=j<m`, the old pair `(C_j,D_{j+1})` forces

\[
C_{j+1}=C_j\cap D_{j+1}.
\]

Thus one new pair awakens the entire old chain

\[
C_2,C_3,\ldots,C_m,
\]

and

\[
C_m=U\setminus [m]=\varnothing.
\]

An upward-closed family containing `∅` contains every subset of `U`, so the least fixed-point closure after adding `p` is `P(U)` and has cardinality `2^m`.

The new pair therefore causes `m-1` newly forced intersection conclusions and changes raw closure cardinality from `m+1` to `2^m`. It also changes `log_2` closure cardinality by

\[
m-\log_2(m+1),
\]

which is unbounded. Any raw propagation-depth definition that counts these dependency levels likewise grows at least linearly in this construction.

## What this falsifies

C026 falsifies the following **universal** candidate accounting rules over source-compatible finite discrete spaces:

- `potential = |least closure|` with an `O(1)` marginal bound per newly added pair;
- `potential = log_2 |least closure|` with an `O(1)` marginal bound;
- raw count of newly forced intersections with an `O(1)` marginal bound;
- raw dependency/propagation depth with an `O(1)` marginal bound.

The result is an amortization warning: one new fusion pair can unlock work encoded in many older pairs.

## What this does not falsify

C026 does **not** falsify:

- the source-native closure representation itself;
- a quotient, rank, certificate, or amortized charge that assigns responsibility differently;
- graph-specific potentials exploiting row/column geometry;
- a potential whose local law is proved only on a restricted target family;
- a super-log cover-complexity route;
- P versus NP.

The most important unresolved discriminator is now:

> Does row/column graph geometry forbid or control the generic cascade, or must a valid lower-bound invariant explicitly quotient/amortize closure cascades?

## Method consequence

The representation axis has advanced: the source-native least fixed point is a precise noncanonical state not covered by C025's first-order signature ceiling. The **accounting/relation** axis is reopened. Before searching for a hard target, the next method should either:

1. prove a graph-specific suppression theorem for cascade sensitivity; or
2. define a quotient/amortized closure charge and immediately re-run C010, C021, C024, C025, and the C026 cascade family.

No novelty claim is made for the elementary closure-system phenomenon. Its value here is source-bound route pruning and localization of the next atomic obstruction.
