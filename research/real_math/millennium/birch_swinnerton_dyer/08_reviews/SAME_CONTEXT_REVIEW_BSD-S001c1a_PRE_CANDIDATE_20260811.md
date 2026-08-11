# Same-context review — BSD-S001c1a complex upper-bound child

**Date:** 2026-08-11  
**Root control:** RAKL_math issue #7  
**Atom:** `BSD-S001c1a-COMPLEX-UPPER-BOUND`  
**Authority:** `SAME_CONTEXT_PRE_CANDIDATE_REVIEW / NOT_INDEPENDENT / NO_THEOREM_AUTHORITY`

No mathematical upper-bound candidate is proposed in this review.

## Expert cell

### 1. Arithmetic geometry / Selmer lead

**Background:** elliptic curves over `Q`, Mordell-Weil and Bloch–Kato Selmer groups, Tate–Shafarevich groups, descent and BSD arithmetic factors.

**Finding:** the source search strengthens the conclusion that exact `p`-primary Selmer reconstruction is not the missing root step. Even if a discrete order exactly equals `corank Sel_p`, one still needs both the complex-order comparison and the Sha-divisibility/finiteness bridge before obtaining Mordell-Weil rank.

**Strongest objection:** an upper bound for a Selmer/discrete order may still be insufficient if the quantity being bounded includes Sha contribution rather than pure Mordell-Weil rank.

**Delegation:** every future comparison must type the target as complex order, discrete order, Selmer corank, Mordell-Weil rank or Sha term separately.

### 2. Iwasawa / Kato lead

**Background:** Kato Euler systems, Kolyvagin systems, Mazur-Tate elements, cyclotomic Iwasawa theory and characteristic ideals.

**Finding:** Ota and BKS show that Kato derivatives/augmentation filtrations already give strong order/divisibility information. The next useful theorem is not another lower divisibility statement but a comparison controlling the discrete order from the complex side after corrections.

**Strongest objection:** main-conjecture equality or generalized Perrin-Riou input can silently carry arithmetic-rank information strong enough to make the desired conclusion circular.

**Delegation:** annotate every candidate theorem with whether it gives lower bound, upper bound, equality, nonvanishing only, or leading coefficient, and list all rank/Sha/main-conjecture hypotheses.

### 3. Complex ↔ discrete comparison lead

**Background:** complex L-functions, modular symbols, p-adic L-functions, Taylor/augmentation filtrations and explicit reciprocity.

**Finding:** the bounded source set contains exact arithmetic order statements and rank-one complex/arithmetic calibrations, but no source-closed arbitrary-rank upper/equality bridge for the independently defined discrete order.

**Strongest objection:** the correct comparison may require changing the discrete object or subtracting explicit local/trivial-zero contributions before an upper bound can even be true.

**Delegation:** search for correction-normalized order formulas and two-sided inequalities, not raw order equality by notation.

### 4. Adversarial circularity / local-global lead

**Background:** implication audits, exceptional/trivial zeros, local-global failures and hidden-assumption detection.

**Finding:** the main falsifier for the current representation is uncontrolled additional vanishing: if local or structural terms can raise the discrete/p-adic order independently of the complex Taylor order, a universal raw upper bound is false.

**Strongest objection:** calling every excess order an “extra zero” before identifying the exact theorem/object would overstate the literature. The child should therefore ask for a correction-normalized upper bound or a scoped obstruction, not assume a particular failure mechanism.

**Delegation:** for every representation, enumerate correction factors and construct the cheapest family/source example that could violate the proposed inequality.

### 5. Formal assurance lead

**Background:** typed proof DAGs, hypothesis binding, dependency audits and formalization boundaries.

**Finding:** the minimum useful candidate statement must have explicit input/output types and direction, e.g. `normalized_ord_discrete(E,p,...) <= ord_{s=1}L(E,s)`. The normalization and scope are part of the theorem, not prose.

**Strongest objection:** a proof whose premises contain `rank E(Q)=ord L`, BSD, or an equivalent root-strength specialization cannot close the root edge.

**Delegation:** treat each correction term and hypothesis as a child obligation before promotion.

### 6. Novelty / frontier lead

**Background:** primary-source theorem search, notation normalization and rediscovery control.

**Finding:** determinant invention, Kato derivative divisibility and exact discrete Selmer reconstruction are already represented in the literature. The bounded search shifts information value toward the missing inequality direction and representation validity.

**Strongest objection:** an exact theorem may exist under ETNC, special-element, derived-height, Mazur-Tate or equivariant Tamagawa language not captured by the first search.

**Delegation:** run one additional bounded source/proof audit before theorem invention and record both positive and negative matches.

## Consensus

The six roles agree:

1. do not invent another Selmer invariant first;
2. do not treat arithmetic-rank-indexed augmentation divisibility as complex analytic-rank equality;
3. do not reverse BSD/GPRC/ETNC-strength implications;
4. normalize correction terms before comparing orders;
5. attack the missing upper/equality direction directly, with a representation-obstruction branch if the inequality is false.

## Proposal-only modes

- `REFLECTIVE_RESTRUCTURE`: replace “prove BSD from Iwasawa theory” with an exact missing inequality between typed coordinates.
- `CONTRASTIVE_DISCRIMINATION`: compare low-rank solved cases, arbitrary-rank arithmetic theorems and correction-sensitive settings.
- `EFFECTUAL_PROBE`: test whether each candidate representation even admits the desired upper bound before building a proof.
- `FIXATION_RESET`: stop accumulating stronger Selmer reconstructions when they do not move the complex root coordinate.

These recommendations create zero mathematical authority.

## Recommendation

Freeze the child context/memory/trace and machine-audit it. Only then perform the correction-normalized source/proof audit. Candidate generation remains unused in this packet.

Root state: `OPEN_NO_SOLUTION_CERTIFICATE`.
