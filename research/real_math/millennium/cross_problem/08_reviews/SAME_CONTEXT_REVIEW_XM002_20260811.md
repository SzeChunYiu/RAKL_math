# XM002 same-context expert cell — BSD fixed-p projection sufficiency

**Atom:** `XM-ROOT-BRIDGE-002`  
**Target:** BSD-S001 fixed-prime Selmer/Iwasawa → global/complex BSD reconstruction  
**Framework:** `SzeChunYiu/RAKL@dd2c23aaa68819a1c1e24bd95fe4ce5f2568d1db`  
**Authority:** same-context review only; not independent peer review.

## Cell composition

1. **Arithmetic-geometry / BSD lead** — background in elliptic curves, heights, regulators, Tate–Shafarevich groups, local factors, and the exact refined BSD statement. Owns root-object typing and prevents p-adic outputs from being silently identified with complex/global outputs.
2. **Iwasawa / Selmer lead** — background in p-primary Selmer groups, control theorems, p-adic L-functions, characteristic/Fitting/determinant data, and local conditions. Owns the exact observation map `pi_p` and source-theorem hypotheses.
3. **Cross-problem transfer lead** — background in structural analogy and RAKL experience reuse. Owns the DifferenceWitness from C024/XM001 and blocks literal transfer of LP or Yang–Mills mathematics.
4. **Adversarial falsification lead** — background in counterexample construction and identifiability. Owns the cheapest same-observation/different-root calibration and tries to distinguish formal noninjectivity from target realizability.
5. **Formal-methods / logic lead** — background in statement binding, typed maps, dependency DAGs, and executable known-answer tests. Owns the exact factorization claim “does the root functional factor through `pi_p`?” and testable branch logic.
6. **Novelty / metacognition lead** — background in literature-frontier audit and research-policy learning. Owns prior-art caution, fixation detection, and whether this cycle is pruning a weak bridge rather than renaming the BSD problem.

## Joint discussion

### Root typing

The arithmetic-geometry lead requires two distinct outputs to remain separated:

- rank equality: `ord_{s=1} L(E,s) = rank E(Q)`;
- refined leading coefficient, whose official Wiles formulation contains global Tate–Shafarevich order, regulator, archimedean period/local term, finite local factors, and torsion.

The Iwasawa lead agrees that a fixed prime naturally exposes p-primary arithmetic and p-adic analytic objects, but objects absent from the theorem output cannot be assumed reconstructed merely because the theorem is strong at `p`.

### Transfer witness

The transfer lead proposes only the audit pattern from XM001:

`weaker observation/surrogate -> explicit bridge -> root functional`.

The shared structure is “root-critical information may be lost by the weaker representation.” The disanalogies are load-bearing: C024 loses correlation/integrality, XM001 loses continuum scaling, whereas BSD may lose prime-to-p and archimedean coordinates. No source equation is reusable.

The cell therefore refuses to promote `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` as a selected tool because its source PR #95 is still draft. It is used only as a proposal-level search procedure.

### Cheapest falsifier

The adversarial lead rejects three first moves:

- searching for two actual elliptic curves with identical complete fixed-p theorem output — expensive and unnecessary for the first logical discriminator;
- inventing a higher-rank determinant bridge — candidate generation before sufficiency is tested;
- aggregating several primes immediately — changes the observation model instead of testing the stated fixed-p claim.

The recommended first action is a **formal projection-nullspace calibration**. Define a typed global refined-BSD data tuple and an intentionally minimal fixed-p projection. Construct two formal tuples that agree under the projection while their global leading-term functional differs in a coordinate not observed by `pi_p` (for example a prime-to-p Sha/local factor or an archimedean factor). This proves only that the declared projection model is noninjective; it does not assert that both tuples are realized by elliptic curves.

### Formal branch logic

The formal-methods lead requires four branches:

1. `NULLSPACE_WITNESS`: same fixed-p observation, different root functional. Weak projection-only inference is rejected; open a child obligation for a reconstruction theorem that kills the kernel on the actual elliptic-curve image.
2. `FACTORIZATION_THEOREM_FOUND`: a source-bound theorem proves the root output factors through the exact fixed-p output under explicit hypotheses. Audit the theorem and its dependencies instead of inventing a new bridge.
3. `PROJECTION_UNDERSPECIFIED`: the target lane has not defined what the fixed-p theorem actually returns. Remain pre-candidate and refine the interface.
4. `ROOT_OUTPUT_SPLITS`: rank equality may factor through a weaker object while the refined leading term does not. Split the atom rather than averaging authority.

## Cross-problem failure portrait

| Problem/lane | Current typed issue | Authority in this review |
|---|---|---|
| P vs NP C024 | fractional surrogate loses cross-fusion integrality/correlation | merged `SUPPORTED` failure; exact source-specific mechanism |
| Yang–Mills XM001/YM-S1 | pointwise finite-cutoff positivity can collapse after physical normalization | draft `SUPPORTED` inference calibration; mechanism not arithmetic |
| Navier–Stokes NS-R001 | energy norms can stay fixed while critical concentration-sensitive norms grow on arbitrary divergence-free histories | active exact scaling calibration; not a solution-space impossibility |
| RH analytic/spectral | finite/restricted/coarse evidence must not be promoted to exact global zero/arithmetic bridge | pre-candidate warning only |
| Hodge deformation/motives | target-side Hodge/motivated labels are not source algebraic-cycle witnesses | pre-candidate warning only |
| BSD-S001 | fixed-p arithmetic is explicitly a projection of a richer global/complex target | active target obstruction; no failure recorded yet |

The recurring **candidate family** is `ROOT_CRITICAL_INFORMATION_LOSS_UNDER_PROJECTION_OR_LIMIT`. The cell does not promote that family to a universal cause. Each instance keeps a distinct mechanism and target-specific falsifier.

## Breakthrough-learning decision

- **Mode:** `REFLECTIVE_RESTRUCTURE + CONTRASTIVE_DISCRIMINATION + EFFECTUAL_PROBE`.
- **Why:** the current bottleneck is not lack of candidate formulas; it is failure to type the observation-to-root map. A small nullspace probe has higher partition power than another higher-rank construction.
- **Fixation warning:** “Iwasawa data are rich, therefore globally sufficient” is a representation-level intuition, not an implication.
- **Contrastive rehearsal:** compare rank-one closed bridges, where an explicit complex/arithmetic identity supplies the missing coupling, against arbitrary-rank fixed-p structure lacking a registered global complex reconstruction.
- **Learning-policy observation:** cross-problem reuse is most valuable when it transfers a falsifier shape and forces a missing map to be typed; it is dangerous when it transfers the source formula.

## Votes

- Arithmetic-geometry / BSD lead: **ACCEPT** the projection-sufficiency falsifier; **BLOCK** any global BSD inference from unspecified fixed-p data.
- Iwasawa / Selmer lead: **ACCEPT WITH SCOPE**; exact theorem output and hypotheses must be frozen before interpreting a failure.
- Cross-problem transfer lead: **ACCEPT** the DifferenceWitness; **REJECT** literal C024/XM001 method transfer.
- Adversarial falsification lead: **ACCEPT** formal nullspace calibration as cheapest discriminator; insists on a separate realizability label.
- Formal-methods / logic lead: **ACCEPT** only with explicit `pi_p`, root functional, and four result branches.
- Novelty / metacognition lead: **ACCEPT** as route-pruning research; **NO NOVELTY CLAIM** and no theorem authority.

## Selected next action

Execute `XM002-BSD-FIXED-P-PROJECTION-NULLSPACE` only after the pre-candidate context, dual-memory review, and trace are frozen. The expected information gain is to distinguish:

- a merely underdetermined fixed-p representation;
- an actual source-bound reconstruction theorem;
- or a need to split rank equality from refined leading-term reconstruction.
