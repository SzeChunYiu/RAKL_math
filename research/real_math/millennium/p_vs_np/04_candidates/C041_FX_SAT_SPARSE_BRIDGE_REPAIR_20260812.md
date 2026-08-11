# C041 FX-SAT sparse-support bridge repair

**Status:** mathematical repair after same-context hostile review.  This does
not alter `C041-FX-SAT-ONE-SIDED-v1`, its decoder, its complement sets, or the
post-freeze zero-augmentation result.  It replaces an invalid full-declared-
variable verifier/decider argument by a language-preserving sparse-support
argument.

## 1. Defect exposed by review

A valid canonical word can declare (v=2^t) variables while mentioning only
(x_1).  The word has length (O(t)), but the frozen helper asks for a
length-(v) assignment and enumerates (2^v) assignments.  Thus that helper is
neither polynomially balanced as an NP verifier nor a (2^{O(n)}) complement
decider.  This refutes the displayed algorithm, not the semantic language.

## 2. Direct language

Define

\[
L_G=\{pq\in\{0,1\}^{2n}: n\ge2,
(\operatorname{int}(p),\operatorname{int}(q))\in G_n\}.
\]

Odd-length words and even words shorter than four bits are outside (L_G).
The level is inferred as half the direct input length.

## 3. Sparse-support verifier

For a decoded formula (phi), let

\[
W(\phi)=\{i:x_i\text{ occurs in one of the decoded literal slots}\}.
\]

Order (W(phi)) increasingly and supply one truth bit per occurring variable.
The verifier reconstructs this order, checks the clauses, and never supplies
values for unused declared variables.  Since there are at most three literal
occurrences per clause,

\[
|W(\phi)|\le 3m.
\]

On the canonical magic branch, the literal payload is a substring of the
(2k)-bit cross word, so (3m\le2k).  Each fixed fallback formula has
(|W|=1).  The witness length and verification time are therefore polynomial
in the direct input length.  Old-old inputs recurse by removing one leading bit from
each label; old-new inputs use the sparse witness; new-old and new-new inputs
are constant graph edges; the level-two seed is a finite lookup.  Hence
(L_G\in\mathrm{NP}).

## 4. Sparse explicit complement decider

At an old-new query, enumerate assignments only to (W(phi)).  The cost is

\[
2^{|W(\phi)|}\operatorname{poly}(k)\le2^{O(k)}.
\]

For the canonical branch this is (2^{O(k)}); for either fixed fallback branch
(|W|=1).  There is at most one decoded formula along an old-old recursion, so membership
in (U_n) is decidable in (2^{O(n)}=\operatorname{poly}(M_n)).  This is an
alternative algorithm for the same semantic predicate; no candidate output or
threshold changes.

## 5. Reduction and padding

Bind source 3SAT to clauses with fixed-width binary variable identifiers after
polynomial-time renumbering.  For

\[
h=\mathrm{MAGIC}\Vert\gamma(v)\Vert\gamma(m)\Vert\mathrm{payload},
\]

the canonical word is (h) when (|h|) is even and (h0) when (|h|) is
odd; no other suffix is accepted.  Its length is linear in the registered
source representation.

For an even canonical word (x=x_Lx_R) of length (2k), output

\[
y=(0x_L)(1x_R).
\]

This is a level-(k+1) old-new query and

\[
y\in L_G\iff\operatorname{Dec}(x)\text{ is satisfiable}.
\]

The direction is (3\mathrm{SAT}\le_m^p L_G), and (|y|=|x|+2).  Together
with the sparse verifier, this proves the narrowly stated theorem

\[
\boxed{L_G\text{ is NP-complete}.}
\]

This theorem supplies a language bridge only.  It proves no cover growth,
circuit lower bound, novelty, or P-versus-NP result.
