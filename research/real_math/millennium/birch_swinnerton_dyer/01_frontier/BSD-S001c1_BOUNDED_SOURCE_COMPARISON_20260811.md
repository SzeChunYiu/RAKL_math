# BSD-S001c1 bounded source comparison — discrete/augmentation order versus complex Taylor order

**Date:** 2026-08-11  
**Root control:** RAKL_math issue #7  
**Parent atom:** `BSD-S001c1-KURIHARA-TAYLOR-COMPARISON`  
**Framework authority checked:** `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`  
**Authority:** `BOUNDED_PRIMARY_SOURCE_AUDIT / ROUTE_REFINEMENT / NO_NEW_THEOREM / ROOT_AUTHORITY_NONE`

## Question executed

The strict S001c1 packet authorized a bounded, notation-normalized primary-source search before theorem invention:

> Is there a proved arbitrary-rank bridge, not assuming BSD or equivalent rank information, that identifies an independently defined Kurihara/Mazur-Tate/Kato order with the complex Taylor order `ord_{s=1} L(E,s)`; or at least supplies enough one-sided inequalities to force equality?

This document records the search result. It is not a literature-wide nonexistence claim.

## Source matrix

| Primary source | Independently defined input | Proved output used here | Root-critical limitation |
|---|---|---|---|
| Kim–Pollack, *The refined Tamagawa number conjectures for GL_2*, arXiv:2505.09121 | Kurihara numbers/Kolyvagin derivatives of special `L`-values | exact Bloch–Kato Selmer rank/module structure under stated large-image/nonvanishing or localized-Iwasawa hypotheses | the paper explicitly presents the result as a discrete BSD/BBK analogue and says the exact Selmer formula is insensitive to analytic rank; the inspected theorem does not identify arbitrary-rank Kurihara order with complex Taylor order |
| Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, arXiv:2203.12159 | modular-symbol/Kurihara data | strong arbitrary-rank `p`-primary Selmer structure, plus rank-zero converse/parity/upper-bound consequences | exact arithmetic structure does not itself supply arbitrary-rank complex analytic-order equality |
| Ota, *Kato's Euler system and the Mazur-Tate refined conjecture of BSD type*, arXiv:1509.00682 | Mazur-Tate elements and derivatives of Kato's Euler system | Mazur-Tate order/divisibility statement comparing augmentation order with Mordell-Weil rank under source hypotheses | the indexing coordinate is algebraic rank; this does not give the missing upper bound by `ord_{s=1}L(E,s)` |
| Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, arXiv:1910.07404 | Darmon-type derivatives of Kato zeta elements/Bockstein structures | arbitrary-rank order-of-vanishing component of the generalized Perrin-Riou framework under hypotheses; connections between IMC and the `p`-part of BSD | general leading-term implications require exact hypothesis-direction audit; algebraic-rank/Sha/BSD-strength inputs cannot be reversed into an unconditional complex-rank theorem |
| Burns–Kurihara–Sano, *On derivatives of Kato's Euler system and the Mazur-Tate Conjecture*, arXiv:2103.11535 | determinantal Kato/Mazur-Tate structures | unconditional positive-rank evidence and conditional/general implication machinery | the source does not provide an arbitrary-rank independent equality between the discrete order and complex Taylor order; general-rank uses must be checked for BSD/GPRC/IMC assumptions |

## Implication separation

The strongest source-bound arithmetic side visible in this search is of the form

`independently defined discrete/Kurihara data`
`-> exact p-primary Selmer structure/corank`

and Mazur-Tate/Kato divisibility results supply arithmetic-rank-indexed augmentation information.

The Clay root still requires the complex coordinate

`r_an = ord_{s=1} L(E,s)`.

The bounded search did **not** source-close either of the following in arbitrary rank without root-strength input:

1. `ord_discrete = r_an`;
2. a correction-normalized upper bound `ord_discrete <= r_an` that can combine with an independent reverse inequality/rigidity statement.

This is a bounded search result, not evidence that no such theorem exists under another vocabulary or restricted family.

## Why the residual is sharper than S001c1

S001c1 asked broadly for a discrete-to-complex compatibility theorem. The source comparison partitions that gap:

- **arithmetic reconstruction is already strong**: spending another cycle improving the Selmer package is low information unless it changes the complex comparison;
- **one-sided/divisibility information is not enough**: an exact root bridge needs the missing implication direction or a rigidity/no-extra-vanishing theorem;
- **correction terms matter**: local Euler factors, exceptional/trivial-zero phenomena, and normalization choices can alter a p-adic/augmentation order and therefore must be explicit before any order inequality is meaningful;
- **root-strength hypotheses are disallowed as proof inputs**: BSD, analytic-rank equality, or equivalent arithmetic-rank assumptions cannot be used to establish the same bridge by reversal.

## New child obstruction

`BSD-S001c1a-COMPLEX-UPPER-BOUND`

Exact question:

> After fixing an independently defined discrete/Mazur-Tate/Kurihara order and all local/trivial-zero corrections, can one source or prove a non-circular upper bound by `ord_{s=1}L(E,s)` (or a direct equality), under hypotheses strictly weaker than BSD/analytic-rank equality? If not for the chosen representation, can one prove a scoped obstruction that forces a representation change?

No candidate is proposed here. The child must pass a fresh context, analogy/method-transfer, expert, dual-memory and hash-chained trace gate before candidate generation.

## Search boundary

The present search inspected the primary sources listed above and targeted arbitrary-rank Mazur-Tate, Kato/GPRC, ETNC-style, Kurihara and modular-symbol language. Search results that merely discuss average analytic rank, rank-zero/rank-one p-converses, or arithmetic Selmer reconstruction without an exact complex-order conclusion were not promoted as bridge theorems.

The search boundary is intentionally recorded because `not found in this bounded search` is not `proved absent from the literature`.

## Authority

`SOURCE_BOUND_REPRESENTATION_REFINEMENT / NO_CANDIDATE / NO_IMPOSSIBILITY / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`.
