# BSD-S001c1 — discrete Kurihara order versus complex Taylor order source audit

**Date:** 2026-08-11  
**Root control:** RAKL_math issue #7  
**Parent:** `BSD-S001c`  
**Authority:** `SOURCE_BOUND_ROUTE_REFINEMENT / NO_NEW_THEOREM / ROOT_AUTHORITY_NONE`

## Atomic question

Can the strongest independently defined `p`-adic/discrete arithmetic order invariant currently visible in the Kato/Kurihara literature be compared, without assuming BSD or analytic-rank equality, to

`ord_{s=1} L(E,s)`

strongly enough to close arbitrary-rank BSD rank equality?

This audit is a source classification, not a theorem candidate and not an impossibility claim.

## Primary-source implication audit

### P1 — Kim–Pollack, refined Tamagawa number conjectures for GL_2

Chan-Ho Kim and Robert Pollack, *The refined Tamagawa number conjectures for GL_2*, arXiv:2505.09121 (current manuscript dated 22 March 2026).

The source defines a collection of Kurihara numbers from modular symbols and describes them as **Kolyvagin derivatives of special L-values**, a discrete variation of those values. It explicitly sets up an analogy between this collection and the Taylor expansion of the complex `L`-function.

Under large image and nonvanishing of the Kurihara collection, Main Theorem I proves:

- Kato's Kolyvagin system is non-trivial;
- the exact Bloch–Kato Selmer module structure is determined by the Kurihara collection;
- in particular,
  `corank Sel = ord(Kurihara collection)`,
  together with an exact finite-module length formula.

The source describes these formulas as corresponding to the rank part and the `p`-part of BSD. Its abstract and introduction also emphasize that the exact Selmer structure formula is **insensitive to analytic rank** and is a **discrete analogue** rather than a theorem obtained from arbitrary complex derivatives.

Main Theorem II proves Kurihara nonvanishing under several alternative inputs, including complex analytic rank zero, analytic rank one plus extra hypotheses, localized Iwasawa-main-conjecture input, or a good-ordinary/p-distinguished setting. These inputs establish nonvanishing, not an arbitrary-rank equality

`ord(Kurihara collection) = ord_{s=1} L(E,s)`.

**Audit result:** Kim–Pollack supply an independently defined arithmetic/discrete order that can exactly recover the `p`-primary Selmer corank. The inspected main theorems do not identify that discrete order with arbitrary complex analytic rank. This is a sharper comparison target than a vaguely specified higher-rank determinant.

### P2 — Kim, arbitrary-rank Selmer structure

Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, arXiv:2203.12159, final version 14 May 2025.

The source determines substantial arbitrary-rank `p`-primary Selmer structure from modular-symbol/Kurihara data for a large class of curves and obtains a rank-zero `p`-converse, parity, and upper bounds on Mordell–Weil rank.

**Audit result:** this is strong arithmetic reconstruction but does not itself state the arbitrary-rank complex equality required by the Clay root contract. The distinction between exact arithmetic structure and complex analytic order persists.

### P3 — Burns–Kurihara–Sano higher-rank Kato/Bockstein interface

David Burns, Masato Kurihara, Takamichi Sano, *On derivatives of Kato's Euler system for elliptic curves*, arXiv:1910.07404.

The Generalized Perrin–Riou Conjecture relates Darmon-type derivatives of Kato zeta elements to higher derivatives of the complex `L`-function, and the authors prove its order-of-vanishing part in arbitrary rank under hypotheses. They also establish an arbitrary-rank connection between the `p`-part of BSD and Iwasawa main conjectures.

However, in the finite-level leading-term formulation used in the existing BSD projection audit, the canonical `eta^BSD` is defined from the complex BSD leading term. Therefore that object cannot be used backwards as an independent reconstruction of the same complex leading term without a separately defined arithmetic element and an independent comparison theorem.

**Audit result:** determinant/Bockstein representation is not missing; independence and implication direction remain missing.

### P4 — Kato's Euler-system source

Kazuya Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), 117–290.

Kato constructs Euler-system/zeta-element machinery linking modular-form zeta values, Iwasawa theory and Selmer groups. This supplies the upstream cohomological source of the Kato/Kolyvagin pipeline but does not by itself identify the arbitrary complex Taylor order with the exact discrete Kurihara order.

### P5 — low-rank comparison calibration

Ashay Burungale, Christopher Skinner, Ye Tian, Xin Wan, *Zeta elements for elliptic curves and applications*, arXiv:2409.01350, proves strong zeta-element/main-conjecture applications including `p`-part BSD consequences for analytic rank zero or one and new `p`-converse cases.

**Audit result:** low-rank complex↔arithmetic closure remains an important solved/near-solved calibration, but it does not remove the arbitrary-rank compatibility edge.

## Typed implication graph

The source-bound arrows currently supported by the inspected material are:

`Kurihara collection nonzero`
→ **proved under Kim–Pollack hypotheses**
`exact p-primary Bloch–Kato Selmer structure`

and, in particular,

`ord(Kurihara)`
→ **exact arithmetic formula**
`corank Sel_p`.

Separate source theorems can establish Kurihara nonvanishing from localized IMC or ordinary hypotheses. In low analytic rank, complex rank-zero/rank-one assumptions can also imply nonvanishing under additional conditions.

The root-critical arrows remain distinct:

1. `ord_{s=1} L(E,s)` ↔ `ord(Kurihara)` in arbitrary rank;
2. `corank Sel_p` → `rank E(Q)` after controlling the relevant divisible Sha contribution;
3. `p`-primary refined factors → the all-primes plus archimedean complex BSD leading coefficient.

The first arrow is now the **highest-information active comparison coordinate**. The present audit found no theorem in the inspected primary sources that supplies arbitrary-rank equality of the first pair without a root-strength assumption. This is a bounded source statement, not a literature-wide nonexistence claim.

## Strongest falsifier for an overclaim

Any proposed route saying “Kurihara/Kato/Iwasawa theory determines BSD rank” must provide a source theorem with:

- input that does not assume BSD, analytic-rank equality, or an equivalent root-strength statement;
- an independently defined discrete/p-adic object;
- conclusion explicitly involving the complex order `ord_{s=1}L(E,s)`;
- exact prime/reduction/residual/local hypotheses;
- an order-preserving, not merely nonvanishing, comparison.

If the route proves only `corank Sel_p = ord(Kurihara)`, it is arithmetic progress but does not close the complex BSD rank edge.

## Failure-cause normalization

**Supported route diagnosis:** `EXACT_ARITHMETIC_RECONSTRUCTION_WITH_UNBOUND_COMPLEX_ORDER_COORDINATE`.

This diagnosis is **not** a `FailureExperience` from a failed RAKL mathematical candidate and is **not** a verified impossibility. It records only that the strongest inspected discrete Selmer reconstruction theorem leaves the complex Taylor-order comparison as a separate source obligation.

## Next atom

`BSD-S001c1-KURIHARA-TAYLOR-COMPARISON`

Before candidate invention:

1. freeze the child context, expert review, dual-memory review and hash-chained trace;
2. search primary ETNC/Mazur–Tate/derived-height/special-element literature for an exact discrete-order ↔ complex-order theorem or one-sided inequalities;
3. classify every result by assumptions and implication direction;
4. generate a mathematical candidate only if a precise missing comparison remains after this normalized search.

No root authority changes in this audit.
