# C042 activation threshold and quotient result

**Frozen evaluator commit:** `d93ddc0f7c6eaf8d798417568a6db86dbc7c4749`  
**Receipt:** `05_falsification/C042_ACTIVATION_QUOTIENT_RECEIPT_20260812.json`  
**Root:** `OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE`

## Theorem 1 — semantic activation occurs after syntax activation

This theorem is specific to the frozen decoder: (v,m\ge 1), every clause
has exactly three literal slots, and repeated literals are allowed.  It is not
a threshold theorem for a 3CNF convention requiring three distinct variables.

For (v,m\ge1), put

\[
L_0(v,m)=8+g(v)+g(m)+3m(1+w(v)),
\]

where (g(t)=2\lfloor\log_2t\rfloor+1) and
(w(v)=\lfloor\log_2v\rfloor+1).  The frozen decoder pads by one zero exactly
when (L_0) is odd.

The MAGIC prefix first fits an even word of length 8, at parent level (n=4),
but no formula parses.  The shortest canonical formula has length 16, with
equality exactly at ((v,m)=(1,1)), so syntax first activates at (n=8).
Every one-clause CNF is satisfiable.

The one-clause case is satisfiable: choose an assignment satisfying any one of
the three literals in its nonempty clause.  Therefore an UNSAT output needs
(m\ge2).  Hence

\[
L_0\ge8+1+3+3\cdot2\cdot(1+1)=24.
\]

Equality forces (v=1,m=2).  Both equality lengths, 16 and 24, are already
even, so padding does not alter them.  With one variable, a mixed-polarity
clause is a tautology, while the constant-sign clauses are equivalent to
(x) and \(\neg x\).  Every minimum-length canonical UNSAT encoding therefore
has (v=1,m=2), and among those parameter values exactly two ordered sign
payloads are UNSAT, corresponding to the two clause orders.  They are

```text
111001011010010101111111
111001011010111111010101
```

Canonical MAGIC long-form UNSAT therefore first activates at parent level
(n=12), affecting (U_{13}).  Since splitting a (2n)-bit word after bit
(n) is a bijection with ([2^n]^2), the length and parent-level statements
are equivalent.  For clarity, the successive indices are prefix fit at parent
(n=4\to U_5), canonical syntax at (n=8\to U_9), and canonical UNSAT at
(n=12\to U_{13}).

The special all-zero short-code contradiction branch is separate and does not
count as MAGIC semantic activation.  Thus length 24 is not the first UNSAT
decoder word; it is the first canonical MAGIC long-form UNSAT word.  Malformed
nonzero words decode to the tautology branch.

## Theorem 2 — exact early complements

Let (W_n) be the set of UNSAT old-to-new cross offsets.  Then

\[
W_n=\{(0,0)\}\quad(2\le n\le11),
\]

and

\[
W_{12}=\{(0,0),(3674,1407),(3674,4053)\}.
\]

Consequently, for (3\le n\le12),

\[
U_n=U_2\cup\{(0,2^k):2\le k<n\}.
\]

Through (U_{12}), only rows (0,1,2) have nonempty complement stars.  The
associated graph has four row-neighborhood types, giving the explicit
four-rectangle construction

\[
\begin{aligned}
G_n={}&\{0\}\times([2^n]\setminus U_n(0))\\
&\cup\{1\}\times([2^n]\setminus\{2\})\\
&\cup\{2\}\times([2^n]\setminus\{1,2\})\\
&\cup([2^n]\setminus\{0,1,2\})\times[2^n].
\end{aligned}
\]

Therefore (D_{\cap}(G_9)\le4) and, by the registered upper-bound direction,
(\rho(G_9)\le4).

At (U_{13}), the new canonical UNSAT points are

\[
(3674,5503),\qquad(3674,8149),
\]

and the fallback adds ((0,4096)).  Rows (0,1,2,3674) and the remaining
rows are the five exact row types.  Their five row-class rectangles give

\[
D_{\cap}(G_{13})\le5,
\qquad \rho(G_{13})\le5.
\]

Thus the first syntax and first genuine semantic layers are already killed by
a constant source-valid upper construction.  No expensive LP is warranted at
these levels.

## Exact finite quotient certificate

Write

\[
a=(0,0),\quad b=(1,2),\quad c=(2,1),\quad d=(2,2).
\]

For (G_9), let

\[
A_9=\{0,4,8,16,32,64,128,256\}.
\]

The left classes are \(\{0\},\{1\},\{2\}\), and the remaining vertices.  The
right classes are (A_9,\{1\},\{2\}\), and the remaining vertices.  Directly
from the displayed formula for (U_n), complement membership is constant on
each class product, all classes are nonempty, and the quotient complement is

\[
\{a,b,c,d\}.
\]

For (G_{13}), let

\[
A_{13}=\{0,4,8,\ldots,4096\},\qquad B=\{5503,8149\}.
\]

Adjoin the left class \(\{3674\}\) and right class (B), removing them from
the corresponding remainder classes.  The quotient complement is then

\[
\{a,b,c,d,e\},\qquad e=(4,4).
\]

These surjective class maps and constant class products prove the exact
nonuniform blow-up identities required by the C013 lift; the truncated class
listings in the receipt are not used as proof.

Twin compression gives a four-type quotient for (G_9) with complement

\[
\{(0,0),(1,2),(2,1),(2,2)\},
\]

and a five-type quotient for (G_{13}) with the additional point ((4,4)).
The mask witnesses in `C042_QUOTIENT_PAIR_WITNESS_RECEIPT_20260812.json`
decode for the four-type quotient to

\[
P_1=(\{a\},\{b,d\}),\qquad
P_2=(\{a,b\},\{c,d\}).
\]

The only quotient graph edges with two nonempty complement stars are

\[
(0,2),(1,0),(0,1),(1,1),(2,0).
\]

The first pair covers the first two and the second pair covers the last three:
the two endpoint stars force the displayed disjoint pair members into every
relevant semi-filter by upward closure, while their empty intersection is not
in a semi-filter.

For the five-type quotient the witnesses decode to

\[
P_1=(\{a,b\},\{c,e\}),\qquad
P_2=(\{b,c,d\},\{a,e\}).
\]

The eleven graph edges with nonempty stars split as

\[
\begin{array}{c|l}
P_1&(0,1),(0,4),(1,1),(1,4),(4,0)\\
P_2&(0,2),(1,0),(2,0),(2,4),(4,1),(4,2).
\end{array}
\]

The same upward-closure argument proves the upper bound.  To prove that one
pair cannot suffice in either quotient, consider the three relevant
semi-filters with minimal generators

\[
\mathcal F_{ab}:\{a\},\{b\},\quad
\mathcal F_{ac}:\{a\},\{c\},\quad
\mathcal F_{bc}:\{b\},\{c\}.
\]

If one pair ((E,H)) covered the first, swap its order so that (a\in E),
(b\in H), (b\notin E), and (a\notin H).  Covering the second then forces
(c\in H) and (c\notin E).  But (E) belongs to neither singleton generator
of \(\mathcal F_{bc}\), a contradiction.  Hence the exact quotient cover number
is two in both cases by a finite mathematical proof, independently of the
exhaustive computation.  C013 quotient lifting therefore gives

\[
\rho(G_9)\le2,
\qquad \rho(G_{13})\le2.
\]

These are finite exact certificates for the quotient and finite upper bounds
for the full graphs, not an asymptotic quotient theorem.  C013 remains
proof-draft authority rather than formal or independent review.

## Mathematical lesson and next discriminator

The failed assumption was that activating a representation activates the
load-bearing obstruction.  The reusable mathematical search heuristic is:
**obstruction activation before amplification, then exact quotient before
lower-bound search**.  Here prefix-fit, valid-syntax, UNSAT-capability, and
quotient-nontriviality are distinct coordinates.  Even the first UNSAT-capable
slice concentrates all canonical variability in one header row and collapses
to one new twin type.

Before later LP work, the next discriminator must track the smaller of the row
and column neighborhood-type counts (t_n).  The elementary type-class
rectangle construction gives

\[
D_{\cap}(G_n)\le\min(t_n^{\rm row},t_n^{\rm column}),
\qquad
\rho(G_n)\le D_{\cap}(G_n).
\]

Superlogarithmic cover growth is impossible at any level where this smaller
type count is (O(\log N_n)).  This transfers only when the neighborhood
quotient is exact, the class maps are surjective and cell-constant, and the
target quantity has the proved upper-bound lift.  Nothing here determines
later levels, where a header or payload may spread across many row labels.

Only the thresholds, equality classification, exact blow-up identities,
explicit cover/counterexample arguments, transfer conditions, and surviving
falsifier earn mathematical saturation credit.  Git state, CI, schemas,
hashes, serialization, solver behavior, and observed runtime are assurance
only.
