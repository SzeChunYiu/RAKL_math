# BSD-S001c1a — local-correction, extra-zero, and Selmer-local-condition audit

**Date:** 2026-08-11  
**Root control:** RAKL_math issue #7  
**Atom:** `BSD-S001c1a-COMPLEX-UPPER-BOUND`  
**Framework authority observed before this action:** `SzeChunYiu/RAKL@a151d5612709ea0f95c3ea232630f246f722739a`  
**Application branch provenance:** strict S001c1a pre-candidate packet was frozen earlier against the then-current/pinned framework `15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`; this audit does not backfill or rewrite that chronology. The newer RAKL v3 experience substrate is additive/proposal-only and creates no mathematical authority here.  
**Authority:** `PRIMARY_SOURCE_ROUTE_FALSIFIER / REPRESENTATION_REFINEMENT / NO_NEW_THEOREM / ROOT_AUTHORITY_NONE`

## Question executed

The frozen S001c1a packet authorized a correction-normalized source/proof audit before theorem invention. The highest-value falsifier was:

> Can the Mazur–Tate/Kato order coordinate acquire vanishing for reasons not controlled by the complex Taylor order, so that a raw scalar upper bound or equality is not even a well-typed first candidate until every structural correction and no-extra-zero condition is explicit?

This audit uses primary literature only for technical claims. It does not claim a literature-wide impossibility result.

## Same-context expert cell and delegated checks

1. **Arithmetic geometry / Selmer lead** — type-checks Mordell–Weil rank, `p^∞`-Selmer corank, strict Selmer corank, `Sha[p^∞]`, and the all-primes refined BSD factors. **Review outcome:** the newly exposed local-condition loss cannot be silently absorbed into `rank E(Q)`.
2. **Iwasawa / Kato lead** — audits where Kato Euler-system localization lands and what augmentation divisibility actually follows. **Review outcome:** Ota explicitly records a strict-Selmer local condition at `p` as the obstruction to the naively expected exponent.
3. **p-adic / Mazur–Tate lead** — audits split-multiplicative and other extra-vanishing terms in augmentation order. **Review outcome:** the source has both an explicit split-multiplicative correction `sp(S)` and additional extra-zero phenomena beyond it.
4. **Galois-cohomology lead** — checks the local-condition change at `p`. **Review outcome:** the Kato localization need not come from local rational points, hence the ordinary Selmer condition is not automatic in that step.
5. **Adversarial local-global lead** — searches for a counterexample mechanism to naive order identification. **Review outcome:** Ota gives concrete finite-level mechanisms where augmentation order rises independently of Mordell–Weil rank; this is enough to reject an uncorrected scalar-identification candidate, though not enough by itself to refute every possible inequality against complex analytic order.
6. **Formal assurance / novelty lead** — checks implication direction and authority. **Review outcome:** the source result is a representation falsifier/route refinement, not a new theorem, not a BSD-local `FailureExperience` from a failed candidate, and not a root certificate.

Consensus: `REJECT_RAW_ORDER_IDENTIFICATION / REQUIRE_INDEPENDENT_CORRECTION_AND_NO_EXTRA_ZERO CONTRACT / KEEP_CANDIDATE_NONE`.

## Primary source: Ota fixes two distinct loss mechanisms

Primary source: Kazuto Ota, *Kato's Euler system and the Mazur-Tate refined conjecture of BSD type*, arXiv:1509.00682.

### 1. The Mazur–Tate order already contains an explicit local correction

Ota's introduction recalls the Mazur–Tate rank-part in the form

`ord_I(theta_S) >= r_E + sp(S)`,

where `r_E = rank E(Q)` and `sp(S)` is the number of split multiplicative primes of `E` dividing `S`. Thus the finite-level augmentation order is not normalized to Mordell–Weil rank even at the conjectural interface: a local split-multiplicative contribution is part of the order contract.

**Implication for S001c1a:** any proposed comparison

`ord_discrete <= ord_{s=1} L(E,s)`

is ill-typed if `ord_discrete` is a raw Mazur–Tate augmentation order that still contains such local vanishing. The correction must be defined independently from the target rank/order and bound into the statement.

### 2. Subtracting the obvious split-multiplicative count is not a complete no-extra-zero theorem

Ota explicitly warns that a Mazur–Tate element can have an **extra zero**, i.e. lie one augmentation step deeper than the rank-part lower bound. In the simplified discussion with `S` prime to the conductor, he gives a concrete mechanism: if a good prime `ell` satisfies `a_ell=2`, then even when `r_E=0`, the distribution relation can force `theta_ell` into the augmentation ideal. He also notes that the expected leading graded class can itself vanish, motivating derived-height/generalized-regulator refinements.

This yields an exact representation warning stronger than the generic phrase “trivial zeros may occur”:

- the scalar augmentation order can have **structural excess vanishing**;
- that excess need not be exhausted by the explicit `sp(S)` split-multiplicative correction;
- a leading-class/derived-height layer can become necessary when the first predicted graded piece vanishes.

**What this proves:** raw augmentation order is not rigidly identical to arithmetic rank, and the currently frozen correction list is not sufficient by itself to license a universal exact-order candidate.

**What this does not prove:** the cited example alone does not establish a counterexample to every possible inequality against the complex analytic order; no analytic-rank value is imported for that example. A complex-order claim still needs its own source/proof audit.

### 3. Kato's Euler-system route loses a Selmer condition at `p`

Ota's proof discussion records a second, logically independent obstruction. The localization of Heegner points at `p` comes from local rational points, but the localization of Kato's Euler system need not. Consequently the argument naturally controls a **strict Selmer group with zero local condition at `p`**, rather than the usual Selmer group. At the intermediate stage this yields only the weaker augmentation divisibility exponent involving `r_{p^∞}-1`, not the naively expected `r_{p^∞}`. Ota then uses the proved `p`-parity theorem together with the functional equation parity of the Mazur–Tate element to recover the rank-part statement.

This is an exact control-theorem/local-condition lesson for the BSD lane:

`Euler-system global class`
`-> localization at p may miss local-rational/crystalline condition`
`-> strict Selmer object`
`-> one rank of divisibility is lost before an independent parity input repairs the stated theorem`.

The parity repair is a parity congruence, not an arbitrary-rank equality between complex Taylor order and the discrete order. It therefore cannot be reused as the missing S001c1a upper/equality bridge.

## Cross-representation exceptional-zero calibration

Mazur–Tate–Teitelbaum's original `p`-adic BSD framework and the Greenberg–Stevens exceptional-zero theorem show the same structural danger in the cyclotomic `p`-adic L-function representation at split multiplicative reduction: interpolation can introduce a central zero that must be measured by an `L`-invariant/derivative formula rather than read as an additional complex zero. Primary anchors:

- B. Mazur, J. Tate, J. Teitelbaum, *On p-adic analogues of the conjectures of Birch and Swinnerton-Dyer*, Invent. Math. 84 (1986), 1–48.
- R. Greenberg, G. Stevens, *p-adic L-functions and p-adic periods of modular forms*, Invent. Math. 111 (1993), 407–447.
- R. Venerucci, *Exceptional zero formulae and a conjecture of Perrin-Riou*, arXiv:1407.1913, for a later primary rank-one exceptional-zero refinement in the split-multiplicative setting.

This calibration is not transferred literally to every Kurihara or Mazur–Tate order. Its role is adversarial: **p-adic/discrete vanishing multiplicity is representation-sensitive and can contain local interpolation/augmentation zeros not present in the complex `s`-order.**

## Exact consequence for the active atom

The active statement must no longer be represented as a single raw inequality. Any candidate family must expose at least the following typed data:

- `O_disc(E,p,S,...)`: independently defined discrete/augmentation order;
- `C_local(E,p,S,...)`: independently defined local/interpolation correction, with every prime/reduction hypothesis explicit;
- `X_extra(E,p,S,...)`: an independently testable no-extra-zero/leading-graded-class condition, or a replacement object that retains information when the first graded class vanishes;
- `r_an(E)=ord_{s=1}L(E,s)`: the complex root coordinate;
- a theorem direction comparing the **normalized** discrete object to `r_an(E)` without using BSD, `rank E(Q)=r_an(E)`, or an equivalent-strength assumption.

A normalization that subtracts `rank E(Q)` or `r_an(E)` is circular for the root bridge. A correction is admissible only if defined from independent local/representation data.

## Exact hypotheses that remain visible

From Ota's theorem interface, any reuse must retain at least the theorem-specific restrictions rather than quote “Mazur–Tate rank-part” generically: non-CM in the stated main setup; the localized coefficient ring obtained by inverting the listed bad primes; the Galois-representation/surjectivity exclusions encoded there; the bound involving `p<r_E`; square-free products of good primes for the main theorem; and the cyclicity condition on `E(F_ell)[p]` for primes not inverted in the coefficient ring. The source also separates ordinary, supersingular, and other prior results rather than giving one uniform control theorem.

No one of these hypotheses supplies the missing complex-order comparison.

## Failure normalization

**Supported route diagnosis:** `REPRESENTATION_ORDER_HAS_INDEPENDENT_LOCAL_OR_EXTRA_VANISHING`.

Sub-causes exposed by this cycle:

- `LOCAL_SPLIT_MULTIPLICATIVE_ORDER_CORRECTION`;
- `FINITE_LEVEL_EXTRA_AUGMENTATION_ZERO`;
- `KATO_LOCAL_CONDITION_TO_STRICT_SELMER_LOSS`;
- `PARITY_REPAIR_DOES_NOT_GLOBALIZE_TO_COMPLEX_ORDER_EQUALITY`.

**Authority boundary:** these are source-supported obstruction mechanisms. They are not promoted to the cross-Millennium `FailureExperienceLattice` as a universal theorem-level blacklist because no S001c1a mathematical candidate was generated and falsified, and no scoped impossibility theorem for every normalized representation was proved.

## Breakthrough-mode output — proposal only

Current RAKL proposal controls support:

- `REFLECTIVE_RESTRUCTURE`: replace a raw scalar order with a typed correction/leading-class interface;
- `CONTRASTIVE_DISCRIMINATION`: compare good-prime finite-level extra zeros, split-multiplicative exceptional zeros, and low-rank no-extra-zero regimes;
- `FIXATION_RESET`: stop accumulating stronger Selmer reconstruction while the complex-order compatibility is unbound;
- `EFFECTUAL_PROBE`: before proving any inequality, test whether its representation can exhibit source-certified excess vanishing under its declared normalization.

No mode creates theorem or evidence authority.

## Residual after the audit

`BSD-S001c1a-COMPLEX-UPPER-BOUND` remains open, but its smallest useful discriminator is now sharper:

> Find a primary-source theorem, or later generate a separately gated candidate, giving an independently normalized discrete/leading-class object with a proved **no-uncontrolled-extra-zero** condition and a non-circular upper/equality comparison to `ord_{s=1}L(E,s)`. If no such scalar normalization survives bounded hostile examples, rotate from scalar order to a richer graded/derived leading object rather than silently absorbing the excess vanishing.

Before any mathematical candidate implementing that discriminator, reopen/freeze context if the chosen normalization or representation adds a structural coordinate not present in the current S001c1a fiber.

Root state remains `OPEN_NO_SOLUTION_CERTIFICATE`.