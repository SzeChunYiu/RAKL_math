# C043 first post-C042 residual split result

**Frozen candidate/evaluator commit:** `f5df31ba1828513b9a86adf5e02943c9355ce891`  
**Receipt:** `05_falsification/C043_FIRST_ROW_SPLIT_RECEIPT_20260812.json`  
**Root:** `OPEN_PROBLEM / NO_SOLUTION_CERTIFICATE`

## Theorem 1 — complete length classification through 30 bits

This theorem concerns the frozen MAGIC/gamma/fixed-width decoder, with repeated
literals allowed.  Put

\[
a=\operatorname{bitlength}(v),\qquad b=\operatorname{bitlength}(m).
\]

Before the optional zero pad, the encoding length is

\[
L_0=8+(2a-1)+(2b-1)+3m(a+1)
   =6+2a+2b+3m(a+1),
\]

and the final even length is \(L=L_0+(L_0\bmod 2)\).

If \(m=1\), then \(b=1\) and

\[
L_0=11+5a.
\]

Thus \(a=3\) gives length 26 and exactly
\((v,m)=(4,1),(5,1),(6,1),(7,1)\).  The adjacent values \(a=2,4\)
give padded length 22 and padded length 32, respectively, so neither raw nor
padded length 28 or 30 arises in this case.  Every one-clause formula is SAT.

If \(m\ge2\) and \(a\ge2\), then \(b\ge2\) and

\[
L_0\ge6+4+4+3\cdot2\cdot3=32.
\]

It remains to take \(a=1\), which forces \(v=1\).  Here

\[
L_0=8+2b+6m.
\]

For \(m=2\) this is 24; for \(m=3\), where \(b=2\), it is 30; and for
\(m\ge4\) it is at least 38.  These values are even.  Consequently:

- length 26 has exactly the four one-clause parameter pairs above and no
  canonical UNSAT word;
- length 28 has no canonical parameter pair;
- length 30 has the unique parameter pair \((v,m)=(1,3)\).

The proof has included the possible odd raw lengths that could acquire the
three target even lengths by padding; none was omitted.

## Theorem 2 — the exact 42-word obstruction and its residual languages

For \(v=1\), ignore the forced variable-index bits and classify the three
signs in a clause by

\[
P=000,\qquad N=111,\qquad T\in\{0,1\}^3\setminus\{P,N\}.
\]

A \(P\)-clause is equivalent to \(x\), an \(N\)-clause to \(\neg x\), and
a mixed clause is a tautology.  Hence a three-clause formula is UNSAT if and
only if its ordered clause list contains both \(P\) and \(N\).  Inclusion-
exclusion gives the exact number

\[
8^3-2\cdot7^3+6^3=42.
\]

At the 15/15 split, the 12-bit header `111001011011` and the first three
payload bits expose the first two signs of clause 1, separated by a forced
variable bit.  The four active rows are therefore

\[
29402,\ 29403,\ 29406,\ 29407,
\]

corresponding in order to first-two-sign patterns \(00,01,10,11\).

For the \(00\) row, if the third sign is 0 then clause 1 is \(P\), and the
last two clauses need at least one \(N\), giving \(8^2-7^2=15\) suffixes.
If the third sign is 1 then clause 1 is mixed, so the last two clauses must be
\(P,N\) in one of two orders.  Thus

\[
|R_{15,29402}|=15+2=17.
\]

The \(11\) row is symmetric, so \(|R_{15,29407}|=17\).  For either mixed
row \(01\) or \(10\), clause 1 remains mixed for both choices of its third
sign.  The last two clauses must again be \(P,N\) in one of two orders, hence

\[
R_{15,29403}=R_{15,29406},\qquad
|R_{15,29403}|=|R_{15,29406}|=2\cdot2=4.
\]

The suffix `22015` lies only in the \(00\) residual, `30037` lies only in the
\(11\) residual, and `21887` lies in all four.  These witnesses prove that
the positive, mixed, and negative residuals are pairwise distinct.  Therefore
the new band has exactly three nonempty row-neighborhood types.

## Theorem 3 — exact new suffix neighborhoods

Fix a suffix, hence the third sign of clause 1 and the last two clauses.
If those last clauses contain both \(P\) and \(N\), every one of the four
prefix rows accepts the suffix.  There are two clause orders and two choices
of the third sign, so this common class has four suffixes.

Otherwise a suffix can be accepted only by the \(00\) row, when clause 1 is
\(P\) and the last two clauses contain \(N\) but not \(P\), or only by the
\(11\) row in the polarity-reversed case.  Each one-sided class has

\[
(8^2-7^2)-2=13
\]

suffixes.  A mixed row cannot accept unless the last two clauses already
contain both \(P\) and \(N\), in which case all four rows accept.  Hence no
fourth nonempty neighborhood is possible.  The exact nonempty new column
neighborhoods are

\[
\{29402\},\quad
\{29402,29403,29406,29407\},\quad
\{29407\},
\]

with multiplicities \(13,4,13\).

## Theorem 4 — exact accumulated type counts and finite upper bound

Through \(G_{13}\), C042 proved five row types and five column types.  Parent
levels 13 and 14 have no canonical UNSAT words, while the fallback at parents
13, 14, and 15 only extends the old row-zero complement star by the columns
\(8192,16384,32768\).  Dually, those columns join the existing column class
whose complement neighborhood is \(\{0\}\); they do not create a type.

Before parent 15 the four rows \(29402,29403,29406,29407\) belonged to the
empty row class.  Their new complement neighborhoods lie strictly in the new
column band above 32768.  The three residual classes proved above are mutually
distinct and cannot equal any old nonempty row neighborhood, all of whose
non-fallback canonical support lies below 32768.  Nor are they empty.  Thus
exactly three row types are added.

The three new nonempty column neighborhoods use only the four new rows.  They
are mutually distinct and cannot equal any old nonempty column neighborhood,
which uses only old rows \(0,1,2,3674\).  Nor are they empty.  Thus exactly
three column types are added.  Consequently

\[
t^{\rm row}_{16}=t^{\rm column}_{16}=5+3=8.
\]

The full complement has 62 edges and its exact 8-by-8 twin quotient has ten
complement cells, as listed in the receipt.  No quotient-cover optimum was
computed or claimed.

For completeness, let \(C_1,\dots,C_8\) be the exact row classes and let
\(N_i\) be their common complement neighborhoods.  Each

\[
C_i\times\bigl([2^{16}]\setminus N_i\bigr)
\]

is a graph rectangle, and the eight rectangles cover every graph edge.
Therefore

\[
D_{\cap}(G_{16})\le8,
\qquad
\rho(G_{16})\le D_{\cap}(G_{16})\le8.
\]

This is an upper bound only.  It gives no lower bound and does not say that
\(8\) is optimal.

## Mathematical failure lesson and next discriminator

The candidate successfully found semantic row splitting, but that is not the
load-bearing growth.  Forty-two UNSAT words and four active rows collapse to
three new types on each side, leaving only the finite ceiling
\(\rho(G_{16})\le8\).  The broken mathematical assumption is:

> semantic multiplicity or multi-row support forces coercive cover growth.

It does not.  Exact full-history twins on **both** sides can absorb semantic
multiplicity, and even growth in the number of types would not by itself rule
out a small multiplexed quotient cover.

The reusable transfer condition is narrower: exact bidirectional neighborhood
classification yields

\[
\rho(G_n)\le D_{\cap}(G_n)
\le\min(t_n^{\rm row},t_n^{\rm column}),
\]

provided the classes cover the full accumulated graph, adjacency is constant
on every class product, and the cover polarity is preserved.  This is a cheap
upper-bound falsifier, never a lower-bound mechanism.

The next mathematical discriminator must therefore challenge quotient
multiplexing itself: either construct a uniform small quotient cover, or
exhibit and prove a growing family of quotient semi-filters that cannot be
covered by the same legal pair.  Merely counting formulas, active rows, or
one-sided residuals is insufficient.

Only the length classification, P/N/T lemma, residual identities and witnesses,
exact accumulated type proof, upper-bound construction, broken mathematical
assumption, transfer conditions, and falsifiers earn saturation credit.  Git,
CI, schemas, hashes, serialization, implementation behavior, and runtime are
assurance only and earn zero mathematical saturation credit.
