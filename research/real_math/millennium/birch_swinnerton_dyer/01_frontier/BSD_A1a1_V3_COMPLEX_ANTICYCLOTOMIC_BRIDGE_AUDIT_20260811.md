# BSD-A1a1 v3 bridge audit — complex analytic order versus anticyclotomic arithmetic depth

**Atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`
**Application base:** `SzeChunYiu/RAKL_math@a071ef22d2478b1603567a9e90202ec3ce99fb59`
**Current semantic framework authority inspected:** `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`
**Frozen application execution pin:** `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`
**Authority:** `SOURCE_BOUND_ROUTE_REFINEMENT / V3_SHADOW_TELEMETRY / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`

## Exact question

The current analytic route has two strong local coordinate systems:

1. complex analytic order `ord_{s=1} L(E,s)`;
2. anticyclotomic character-direction order/depth, expressed through `ord_J Theta`, derived p-adic heights, Selmer/Iwasawa filtrations and characteristic ideals.

The audit asks whether current primary sources provide a non-circular theorem that transports **exact complex analytic rank two** to the exact anticyclotomic depth needed by the generalized-Kato route, without importing the desired arithmetic conclusion through Selmer rank, Mordell-Weil rank, p-adic BSD, a main-conjecture equality, or maximal height nondegeneracy.

This is a relation/gluing audit. It does not ask for another local invariant.

## Six-role expert cell

The roles are deliberately separated. These are same-context AI review roles, not independent human peer review.

### 1. Complex L-function / Rankin-Selberg lead

**Evidence inspected:** current `BSD_A1a1_THETA_ORDER_CONTEXT_FIBER_20260811.json`; Castella-Hsieh interpolation/leading-term setup; current BSD root contract.

**Strongest counter-hypothesis:** exact analytic rank two might already force the anticyclotomic order after unpacking the interpolation family carefully.

**Falsifier attempted:** distinguish the complex `s` direction from the anticyclotomic character/J direction and inspect whether the cited interpolation statement contains derivative-order transport rather than only value interpolation/central vanishing.

**Finding:** the audited route keeps the directions distinct. Positive central vanishing and parity constraints do not by themselves give the missing exact upper bound.

**Vote:** `RELATION_GAP_REMAINS`.

### 2. Anticyclotomic Iwasawa / p-adic L-function lead

**Evidence inspected:** Howard `arXiv:1202.6343`; Castella-Hsieh `arXiv:1809.09066`; Castella-Hsu-Kundu-Lee-Liu `arXiv:2308.10474`; Bertolini-Longo-Venerucci `arXiv:2306.17784`.

**Strongest counter-hypothesis:** an anticyclotomic main conjecture or derived-height formula may collapse the order problem automatically.

**Falsifier attempted:** classify whether each order-control statement consumes Selmer/Iwasawa characteristic data, height nondegeneracy, or a p-adic BSD-strength premise.

**Finding:** these sources provide powerful p-adic/arithmetic control, but the audited statements do not derive the required nondegeneracy/order upper bound from bare complex analytic rank two.

**Vote:** `STRONG_LOCAL_MACHINERY / COMPLEX_INPUT_BRIDGE_OPEN`.

### 3. Euler-system / Selmer / Sha lead

**Evidence inspected:** current parallel `BSD-S001c1` memory; Kim-Pollack `arXiv:2505.09121`; Marannino `arXiv:2507.22755`; current root requirement separating Selmer corank, Mordell-Weil rank, and Sha.

**Strongest counter-hypothesis:** sufficiently exact Selmer reconstruction could make the complex bridge redundant.

**Falsifier attempted:** ask whether exact p-primary/discrete reconstruction is itself an arbitrary-rank theorem about `ord_{s=1} L(E,s)`.

**Finding:** exact arithmetic reconstruction remains a different coordinate. The current Kim-Pollack route is especially useful as a near-miss because its strength on Selmer structure does not identify arbitrary complex analytic rank. Recent diagonal-cycle work located in the bounded freshness scan remains rank-one in its stated result.

**Vote:** `NO_ROOT_GLUE_FROM_SELmer_EXACTNESS_ALONE`.

### 4. Height / regulator / leading-term lead

**Evidence inspected:** derived p-adic height and BDP leading-term literature; the refined BSD obligation separating regulator, local factors, torsion and Sha.

**Strongest counter-hypothesis:** the first nonzero derived height is the sought bridge and only needs notation alignment.

**Falsifier attempted:** separate existence of a height/regulator formula from a theorem forcing its required nondegeneracy from complex analytic rank.

**Finding:** nondegeneracy is load-bearing rather than cosmetic. Treating it as automatic would import the missing arithmetic conclusion.

**Vote:** `NONDEGENERACY_IS_AN_OPEN_INTERFACE`.

### 5. Adversarial bridge / gluing lead

**Evidence inspected:** `T-XM-ROOT-BRIDGE-STABILITY-AUDIT`, the current BSD context, and the parallel discrete/Selmer route.

**Strongest counter-hypothesis:** the route is merely suffering from notation complexity and the local statements already imply the root bridge when assembled.

**Falsifier attempted:** enumerate local sections and demand an explicit interface assignment preserving the root-critical coordinate:
`complex s-order -> anticyclotomic J-order/height depth -> Selmer/Mordell-Weil rank`.

**Finding:** each local section can be mathematically useful while the interface remains unverified. This is a genuine local-to-global relation gap, not evidence that any local theorem is false.

**Vote:** `GLUING_BLOCKED`.

### 6. Formal assurance / provenance / v3 telemetry lead

**Evidence inspected:** current RAKL v3 experience/API/evaluation contracts; current RAKL_math execution pin; open PR #41 and its exact-head GitHub Actions run `31481324706`.

**Strongest counter-hypothesis:** updating the application framework pin to the newly merged v3 commit is a harmless way to express current framework authority.

**Falsifier attempted:** inspect exact-head CI after PR #41 changes the execution pin.

**Finding:** the suite reports `219 passed, 5 failed`. Four failures are direct pin/provenance identity conflicts, and another is a diff-check/whitespace failure. Conceptual framework freshness and reproducibility execution identity are therefore separate governance coordinates.

**Vote:** `PROCESS_GAP_CONFIRMED / MATHEMATICS_UNAFFECTED`.

## Fresh primary-source discriminator

The bounded freshness scan was repeated on 11 August 2026 with current primary-source records. The following were retained for exact scope:

- Castella-Hsieh, `arXiv:1809.09066`: generalized Kato classes and anticyclotomic leading-term/derived-height machinery in rank-two settings.
- Howard, `arXiv:1202.6343`: higher p-adic derivatives and derived p-adic heights; degeneracy is tied to Iwasawa non-semisimplicity.
- Castella-Hsu-Kundu-Lee-Liu, `arXiv:2308.10474`: BDP p-adic BSD leading coefficients and maximal anticyclotomic height nondegeneracy in the algebraic analogue.
- Bertolini-Longo-Venerucci, `arXiv:2306.17784`: anticyclotomic main-conjecture results under their stated assumptions.
- Kim-Pollack, `arXiv:2505.09121`: exact p-primary Selmer reconstruction from independently defined discrete/Kolyvagin data; not an arbitrary-rank complex analytic-order theorem.
- Shii, `arXiv:2503.09034`: a weak anticyclotomic Mazur-Tate result in a supersingular inert-prime setting.
- Marannino, `arXiv:2507.22755`: anticyclotomic Euler-system/diagonal-cycle progress with stated analytic-rank-one Bloch-Kato applications.

No audited source in this bounded set was found to prove:

`ord_{s=1} L(E,s)=2`
`=>`
the exact anticyclotomic height nondegeneracy / J-order upper bound needed to rule out higher even order,

under assumptions demonstrably weaker than the arithmetic conclusion being sought.

This is **not** a literature-wide nonexistence or novelty claim.

## Gluing report

### Local section A — complex analytic side

Available information can constrain the order of vanishing in the complex variable and root sign.

### Local section B — anticyclotomic p-adic side

Available information can relate J-adic order, derived heights, characteristic data, and generalized Kato classes under explicit hypotheses.

### Local section C — Selmer/discrete side

Available information can reconstruct strong p-primary arithmetic structure from discrete data under source hypotheses.

### Missing interface

The root-critical interface remains:

> a non-circular theorem showing that the complex analytic rank-two input forces the required anticyclotomic regulator/height nondegeneracy or exact J-order, and then transports that information to the global Mordell-Weil/Sha statement at the exact claimed scope.

Therefore:

`LOCAL_SUCCESS != GLOBAL_BSD_BRIDGE`.

## Saturation update

- `KNOWLEDGE`: `OPEN` — a new source can still change the route.
- `OPERATOR`: `LOCALLY_FLAT` — the audited standard families do not close the bridge by themselves.
- `EXPERIENCE_PATTERN`: `OPEN` — bridge-faithfulness failures are recurring but need prospective accumulation.
- `OBSTRUCTION`: `REOPENED` — sharpened from a generic theta upper bound to nondegeneracy/faithfulness.
- `RELATION`: `REOPENED` — now the primary active axis.
- `PATH`: `REOPENED` — next search should target exact comparison/nondegeneracy rather than another local invariant.
- `META_METHOD`: `REOPENED` — semantic framework authority and frozen execution pin require explicit separation.

## Route decision

Do **not** invent another BSD invariant in this cycle.

The highest-information next mathematical action is to freeze a fresh strict child only after the parent/CI lineage is clean, and make its first discriminator one of:

1. a theorem deriving maximal anticyclotomic derived-height/regulator nondegeneracy from complex analytic rank two without Selmer-rank/main-conjecture/BSD-strength input;
2. a direct complex Rankin-Selberg/automorphic upper bound on J-order with all local corrections explicit;
3. a source-valid proof that a proposed route necessarily imports root-strength arithmetic data, forcing a representation/path change.

No theorem candidate is generated by this audit.

## Authority boundary

`OBSERVED_ROUTE_GAP != IMPOSSIBILITY`
`SOURCE_AUDIT != NOVELTY`
`V3_EPISODE != REUSABLE_LESSON`
`CURRENT_FRAMEWORK_SEMANTICS != FROZEN_EXECUTION_PIN`
`LOCAL_SUCCESS != GLOBAL_SOLUTION`
