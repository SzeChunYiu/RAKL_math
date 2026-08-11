# C041-FX-SAT-ONE-SIDED-v1 — pre-output mathematical freeze

**Status:** candidate definition frozen before native LP output.  This is not a
proof of an increment, recurrence, circuit lower bound, novelty, or P versus NP.

## 1. Exact object and rule

For (n\ge2), set (M_n=2^n), let

\[
U_2=\{(0,0),(2,1),(1,2),(2,2)\}\subset[4]^2,
\qquad G_n=[M_n]^2\setminus U_n.
\]

`C041_fx_sat_one_sided.py` fixes a total decoder
(\operatorname{Dec}:\{0,1\}^{2k}\to 3\mathrm{CNF}).  The all-zero word
decodes to the fixed contradiction
((z\vee z\vee z)\wedge(\neg z\vee\neg z\vee\neg z)).  A word carrying
the eight-bit magic `11100101` is parsed using Elias-gamma codes for the
positive variable and clause counts, followed by three fixed-width signed
literals per clause and, when required, one terminal zero for even parity.
Every other word decodes to the fixed tautology
((z\vee\neg z\vee z)).

Write (s_n(r,c)=1) exactly when
(\operatorname{Dec}(\operatorname{bin}_n(r)\Vert
\operatorname{bin}_n(c))) is satisfiable.  Embed (U_n) in the old-old
block and define the **one-sided** rule

\[
U_{n+1}=U_n\cup
\{(r,M_n+c):0\le r,c<M_n,\ s_n(r,c)=0\}.
\]

There are no new-old or new-new complement points.

## 2. Mathematical statements frozen for proof/falsification

### Lemma A — empty-fibre ambient enlargement

Embedding a complement (U\subset[M]^2) into a larger square while adding
only rows and columns with empty complement stars does not change its relevant
semi-filter family.  Every old relevance witness remains.  A graph edge using
a new row or column has an empty row or column star and therefore cannot create
a relevance witness under Definition 18.  Thus the C037 parent support and its
exact (3/2) certificate may be transported from the (3\times3) ambient
square to this (4\times4) seed, subject to exact recheck after the freeze.

### Lemma B — no-old-edge-deletion cylinder persistence

Suppose an extension embeds (U\) in (U'), deletes no old graph edge, and
every child row/column star restricts under the ground-set projection to its
parent star.  If a parent semi-filter (F) is relevant at the old graph edge
((r,c)), then its cylinder lift is relevant at the same child graph edge:
membership of each child star in the cylinder is equivalent to membership of
its parent restriction in (F).  The C038 pair-projection proof then makes
every feasible supported parent dual feasible after lifting.

The frozen rule satisfies these hypotheses even though it adds complement
points incident to old rows.  Consequently it proves only preservation of old
dual mass, (L_{n+1}\ge L_n); it does **not** prove positive augmentation.

### Lemma C — NP-complete associated graph language

Membership in (U_n) is decidable by recursion and exhaustive assignment
search in (2^{O(n)}=\operatorname{poly}(M_n)).  Membership in (G_n) has an
NP verifier: old-old queries recurse, old-new queries carry a satisfying
assignment for the decoded formula, and new-old/new-new queries are constant
graph edges.  Canonical 3CNF encoding has linear overhead.  Splitting an
encoded formula (x\in\{0,1\}^{2k}) and mapping it to
((0\Vert x_L,1\Vert x_R)) at level (k+1) is a correctly directed
many-one reduction from 3SAT to the associated graph predicate.  Therefore
the direct language is NP-complete.

This repairs the former E-only root-coordinate boundary.  It supplies no
circuit lower bound.

## 3. Difference witnesses and surviving attacks

- **C037:** old graph edges are not deleted and star restriction is exact;
  relevance loss must nevertheless be replayed first.
- **C010:** the complement is not isolated block-diagonal repetition because
  the old-new cross block carries formula-dependent points.  A new one-sided
  multiplexing cover may still refute the route.
- **C013:** the family is not a fixed quotient blow-up.  New rows are twins and
  malformed encodings create large twin classes, so exact neighbourhood
  quotienting remains a mandatory falsifier.
- **C024:** fractional mass can still erase correlation.  No inference from a
  fractional increment to integral/root strength is allowed without the
  registered bridge and rate.

## 4. Frozen discriminator and outcome polarity

The (n=2\to3) child contains at most five complement points by decoder syntax,
so the complete (|U|\le5) exact gate is permitted.  This tiny gate exercises
the all-zero short contradiction rather than the magic-coded asymptotic slice.
It is therefore a **plumbing/conformance discriminator only** and earns no
asymptotic amplification credit.

The evaluation order is fixed:

1. exact square-seed certificate recheck;
2. supported cylinder relevance;
3. lifted pair loads;
4. residual augmentation LP with exact rational primal/dual equality;
5. one-sided multiplexing, quotient/twin, small-intersection, finite-state,
   Hamming/parity/rank, and compiled-cover attacks;
6. a separate first-magic-level structural screen.

Allowed native branches are `SOURCE_DOMAIN_FAILURE`, `DECODER_BRIDGE_FAILURE`,
`RELEVANCE_FAILURE`, `LIFTED_FEASIBILITY_FAILURE`, `ZERO_AUGMENTATION`,
`POSITIVE_FINITE_AUGMENTATION`, and `CANNOT_CHECK`.  Positive finite mass does
not prove a recurrence.  For a superlogarithmic graph checkpoint one must prove

\[
\frac{L_0+\sum_{i<n}d(i)}{n}\longrightarrow\infty.
\]

For a P-versus-NP circuit route one must further prove
(a_n^{\omega(1)}) circuit complexity for this NP language.  The root remains
`OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE`.
