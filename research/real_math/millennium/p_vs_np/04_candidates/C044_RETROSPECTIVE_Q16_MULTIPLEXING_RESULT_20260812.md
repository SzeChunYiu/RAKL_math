# C044 retrospective Q16 multiplexing result

**Parent:** C043 exact eight-type quotient  
**Receipt:** `05_falsification/C044_RETROSPECTIVE_Q16_MULTIPLEXING_RECEIPT_20260812.json`  
**Chronology:** `RETROSPECTIVE / RESULT EXPOSED BEFORE CANDIDATE FREEZE`  
**Root:** `OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE`

## Chronology and authority boundary

A parallel read-only search exposed the three-pair quotient witness before a
strict C044 pre-candidate packet and evaluator were frozen.  Therefore this
round does **not** receive strict context-first RAKL discovery authority.  The
result may still be checked for mathematical truth, because discovery
chronology and truth are separate gates.  Nothing below backfills or rewrites
the chronology.

The hand argument proves an upper bound.  A retrospective exhaustive canonical
oracle also returned value three, but computation is not proof; no exact lower
bound is promoted here.  The reviews are same-context hostile checks, not
independent peer review.

## Frozen parent object

The C043 quotient complement is

\[
\begin{aligned}
U_Q=\{&a=(0,0),\ b=(1,2),\ c=(2,1),\ d=(2,2),\ e=(4,4),\\
      &f=(5,5),\ g=(5,6),\ h=(6,5),\ i=(7,5),\ j=(7,7)\}.
\end{aligned}
\]

It is the disjoint union

\[
U_A=\{a,b,c,d,e\},\qquad U_B=\{f,g,h,i,j\}.
\]

No complement cell has one endpoint in the active label set
\(A=\{0,1,2,4\}\) and the other in \(B=\{5,6,7\}\).  Label 3 has an empty
complement row and column fibre.  Thus every active cross-component cell is a
graph edge, while a cell incident to an empty fibre admits no semi-filter above
it under the registered source definition.

## Lemma 1 — heterogeneous block multiplexing

Let a bipartite complement be the disjoint union of \(t\) diagonal component
ground sets \(U_1,\ldots,U_t\), with no cross-component complement cell.  If
component \(r\) has a disjoint generator-separating family of size \(k_r\),
then

\[
\sigma(G)\le \max_r k_r+\lceil\log_2t\rceil.
\]

### Proof

Put \(k=\max_r k_r\), pad each local family to length \(k\) with empty pairs,
and for each index take the union of its left members over all components and,
separately, the union of its right members.  Each global pair remains disjoint:
local members are disjoint inside one component and different component ground
sets are disjoint.  A within-component relevant graph edge is separated by the
index that separated it locally.

Give the components distinct binary labels.  For every label bit, put the whole
of each 0-component complement on one side and the whole of each 1-component
complement on the other.  Any relevant cross-component graph edge has nonempty
row and column fibres in different components, so some bit places the two
fibres on opposite sides.  These pairs are disjoint because the component
ground sets are disjoint.

Every relevant graph edge is therefore generator-separated.  C010-L1 gives
\(\rho(G)\le\sigma(G)\), proving the lemma.  Identical components were not
load-bearing; disjoint component grounds and component-wise local families
were.

## Theorem 2 — an explicit three-pair cover of Q16

Consider the three disjoint full partitions of \(U_Q\):

\[
\begin{aligned}
P_1&=(\{a,b,c,d,e\},\{f,g,h,i,j\}),\\
P_2&=(\{a,e,f,g,h\},\{b,c,d,i,j\}),\\
P_3&=(\{a,b,d,f,g\},\{c,e,h,i,j\}).
\end{aligned}
\]

For a complement row or column star, record `E` if the star is contained in
the first member of a pair, `H` if it is contained in the second, and `X` if
it is mixed.  Across \(P_1,P_2,P_3\), the nonempty stars have signatures

\[
\begin{array}{c|ccccccc}
\text{row label}&0&1&2&4&5&6&7\\\hline
\text{signature}&EEE&EHE&EHX&EEH&HEE&HEH&HHH
\end{array}
\]

and

\[
\begin{array}{c|ccccccc}
\text{column label}&0&1&2&4&5&6&7\\\hline
\text{signature}&EEE&EHH&EHE&EEH&HXX&HEE&HHH.
\end{array}
\]

The receipt lists all 39 relevant quotient graph cells and, for each one, a
coordinate in which the row and column stars are `E/H` opposites.  This table
is finite corroboration; the structural reason is clearer:

- \(P_1=(U_A,U_B)\) separates every active cross-component graph edge;
- the restrictions of \(P_2,P_3\) to \(U_A\) generator-separate every
  relevant old-component graph edge;
- their restrictions to \(U_B\) generator-separate every relevant
  new-component graph edge.

For a relevant graph edge separated by \((E,H)\), every semi-filter above that
edge contains the row and column fibres and therefore contains \(E,H\) by
upward closure.  Since \(E\cap H=\varnothing\), it cannot preserve the pair.
Thus the three pairs cover every relevant full semi-filter, and

\[
\rho(Q_{16})\le\sigma(Q_{16})\le3.
\]

C013 applies because C043 proved the exact surjective twin quotient and
cell-constant adjacency.  It gives only the upper-bound direction

\[
\boxed{\rho(G_{16})\le\rho(Q_{16})\le3}.
\]

This sharpens C043's eight-rectangle ceiling.  It does not prove equality for
\(G_{16}\), and it does not imply \(D_{\cap}(G_{16})\le3\).

## Retrospective canonical computation — not promoted as proof

The bounded canonical oracle enumerated arbitrary overlapping pairs over the
ten complement cells and reported:

\[
39\ \text{canonical filters},\qquad
63\ \text{maximal pair masks},\qquad
\rho_{\rm can}^{\rm computed}(Q_{16})=3.
\]

This supports the conjectural exact sandwich
\(3\le\rho(Q_{16})\le3\), but no transparent hand case proof or formally
checked exhaustive certificate is present.  Therefore this round records only
the proved upper bound.  The lower-bound residual remains open rather than
converting enumeration into theorem authority.

## Mathematical failure lesson

C043 showed real semantic and twin-type growth.  C044 shows why that growth was
still noncoercive: the ten quotient-complement cells split into two disjoint
active components, local pairs can be reused indexwise, and one additional
component bit covers all cross-component obligations.  The failed assumption
is sharper than “type count implies cover growth”:

> Adding new exact types forces new cover resources even when the new
> complement structure is component-separable.

It does not.  For heterogeneous block-diagonal complements, the local cover
cost accumulates by a **maximum**, not a sum, plus only logarithmic component
separation.

The transfer condition is exact: the ceiling applies only when complement
components have disjoint ground sets, there are no cross-component complement
cells, every local family is disjoint generator-separating, and the target uses
the same full-cover polarity.  A single cross-component complement cell can
change endpoint fibres and falsify the construction.

The next fresh strict atom must use an untouched target and ask when later
canonical layers first introduce load-bearing cross-component complement
coupling that defeats the inherited three-pair code.  Counting more formulas,
rows, or types is not enough.

Only the component decomposition, heterogeneous multiplexing lemma, explicit
pairs, fibre-containment proof, broken mathematical assumption, transfer
conditions, and falsifiers earn mathematical saturation credit.  Chronology,
Git, PRs, CI, schemas, hashes, implementation behavior, solver behavior, and
runtime are assurance-only with zero mathematical credit.
