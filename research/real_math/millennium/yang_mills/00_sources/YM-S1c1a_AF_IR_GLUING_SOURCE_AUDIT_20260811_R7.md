# YM-S1c1a — AF/IR continuum-identification summability audit (R7)

**Authority:** `PROPOSAL_SHADOW_SOURCE_AUDIT / NO_THEOREM_PROMOTION / ROOT_AUTHORITY_NONE`  
**Root:** `RAKL_math#5`, still `OPEN_NO_SOLUTION_CERTIFICATE`  
**Parent:** `#69 / YM-S1c1`  
**Prospective repair child:** `#166 / YM-S1c1a`  
**Frozen fibre:** `../10_case_study/YM-S1c1a_FIBRE_RECEIPT_20260811_R7.json`, hash `d6672f16fef8b31e0c419a90eeb0b02f42ce71a56f97092d4cd46fc0fff6a09b`.

This bounded cycle audits the strong/weak-coupling interpolation and same-continuum identification claimed in Section 10 of Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026). Publisher metadata for the April 20, 2026 Fortschritte der Physik article, DOI `10.1002/prop.70097`, confirms the same high-level claim that the strong-coupling and asymptotically-free routes meet in one continuum theory, but the exact equation audit below is bound only to the accessible arXiv v1 text.

The source findings that motivated child #166 were observed before that issue was frozen and therefore receive zero prospective discovery credit. They are retained only as source-proof/gluing evidence.

## 1. Section 10 contains a genuine alternative small-bare-coupling entry lane

The earlier #69 audit isolated a fixed-reference inverse-coupling route whose displayed `beta_K` converges back to a fixed `beta_*`, rather than itself proving the Wilson inverse bare coupling escapes to infinity. Section 10 contains another route that should not be erased by that diagnosis.

Lemma 10.5 introduces the bare Wilson coupling `g_bare` at lattice spacing `a`, performs `k0` coarse-graining steps to a mesoscopic scale, and states an entry theorem for sufficiently small `g_bare`. Its proof gives the schematic quantitative controls

`||K_0|| <= A_b g_bare^2`,

`|g_0-g_bare| <= B_b g_bare^3`,

with constants asserted independent of `a`, followed by entry into a fixed small polydisc after a bounded number of further steps. Thus the source has a distinct weak-bare-coupling entry mechanism. This narrows #69: the live question is not merely whether any weak entry exists, but whether this weak trajectory is consistently oriented and actually identified with the same gapped continuum theory.

**Scoped positive result:** `ALTERNATIVE_SMALL_G_BARE_ENTRY_LANE_PRESENT_IN_SOURCE`.

## 2. The displayed AF scale convention is internally inconsistent, but a later theorem shows the likely intended orientation

Near equations (10.55)–(10.57), the source has `g_{k+1}<g_k` at leading order and sets the continuous scale to `mu_k=mu_0 b^{-k}` while also writing the negative one-loop equation

`mu dg/dmu = - beta_0 g^3 + O(g^5)`.

Those signs do not share one physical orientation: with `mu_{k+1}/mu_k=b^{-1}<1`, a negative beta function makes the coupling grow toward smaller `mu`, not decrease with `k`.

Later Theorem 10.7 instead sets `mu_k=mu_0 b^k` and derives the same negative beta-function sign. This latter convention is compatible with `g_k` decreasing as `k` increases. The audit therefore treats the first `b^{-k}` convention as a **local representation/scale-coordinate inconsistency with an evident later repair candidate**, not as a no-go theorem.

**Scoped result:** `LOCAL_SCALE_ORIENTATION_INCONSISTENCY / LATER_b^k_CONVENTION_IS_REPAIR_CANDIDATE`.

## 3. The source's own asymptotic law defeats the quadratic summability claim used in the AF/IR kernel telescope

The Section-10 identification argument writes a one-step kernel difference bound of the form

`||Delta T_k|| <= L ( |g_k-g'_k| + ||K_k-K'_k|| )`.

It then asserts a coupling-difference estimate

`|g_j-g'_j| <= C (g_j^2 + g_j'^2)`

and an irrelevant-sector recursion forced by the same quadratic terms, and concludes that both contributions are summable in `j`, so `sum_j ||Delta T_j||` converges.

But Theorem 10.7 later gives the precise asymptotic

`g_k = (1+o(1))/sqrt(2 beta_0 k)`

(up to the explicitly discussed `log b` time normalization). Therefore

`g_k^2 = (1+o(1))/(2 beta_0 k)`,

so `sum_k g_k^2` diverges harmonically. The earlier prose on the AF page itself also says the sum of `g_k^2` converges, which is incompatible with Theorem 10.7's later asymptotic.

This does **not** prove that the actual inter-trajectory difference `|g_k-g'_k|` is nonsummable: two trajectories with the same leading beta coefficient could differ at a faster rate. It proves that the displayed `O(g_k^2+g_k'^2)` envelope is not a summable majorant and therefore cannot justify the claimed `l^1` telescope. A sharper difference theorem is required.

The same logical point applies to the displayed `K`-difference recursion. A hostile equality model

`x_k = theta x_{k-1} + c/k`, `0<theta<1`,

satisfies the same contraction-plus-harmonic-forcing shape and has `x_k >= c/k`, hence is not summable. Therefore that recurrence shape alone cannot imply `l^1` control.

**Scoped result:** `DISPLAYED_AF_IR_DIFFERENCE_BOUNDS_DO_NOT_ESTABLISH_SUMMABILITY`.

## 4. Theorem 10.8's final continuum-equality step uses bounded cumulative drift as if it implied vanishing difference

Theorem 10.8 defines the AF and IR Schwinger-function difference at scale `k` and obtains a recursion of the form

`D_{k+1} <= D_k + C epsilon_k`, with `sum_k epsilon_k < infinity`.

Iteration yields

`D_K <= D_0 + C sum_{k<K} epsilon_k`.

That is a uniform boundedness estimate. It does not imply `D_K -> 0`. The exact hostile control `D_k=1`, `epsilon_k=0` satisfies the hypothesis and never vanishes.

The source then says the initial difference can be absorbed into the same summable error by changing the starting scale or by noting finite Lipschitz distance between initial data, and proceeds to equality of the limiting AF and IR Schwinger families. Finiteness of the initial distance is not a vanishing-tail estimate. A valid repair needs at least one of:

- a contraction factor on `D_k` plus a tail that vanishes;
- a direct estimate `D_k <= r_k` with `r_k -> 0`;
- a genuinely summable AF/IR kernel difference with comparison started at scale `k` and tail sent to infinity; or
- an explicit, type-correct application of Section 9's universality theorem proving that its hypotheses cover these two running trajectories and that its right-hand side tends to zero.

**Scoped result:** `THEOREM_10_8_WRITTEN_RECURSION_GIVES_BOUNDEDNESS_NOT_EQUALITY`.

This is a **local-to-global/same-theory gluing failure in the written proof**, not a local counterexample to Yang–Mills and not a proof that no repair exists.

## 5. Section 9 is a possible repair surface, not an automatically licensed escape hatch

Section 9 Theorem 9.3 states a geometric `a_l`-weighted telescoping estimate for members of an admissible scheme class and concludes scheme-independent continuum limits. Section 10 explicitly invokes that universality theme. The current cycle does not silently identify its scheme parameters with two running AF/IR trajectory states.

A valid repair must bind the exact Section-9 parameter space, single-slice marginals, kernels, OS Hilbert spaces/quotients, and metric `d` to the AF and IR constructions in Theorem 10.8. It must also coexist with the already-open OS quotient/semigroup issues #126/#133, source-family completeness #109, defect budget #73/#158, and weak-RG source binding #159. The existence of a theorem named “universality” does not close those typed interfaces by itself.

## 6. Same-context expert-cell synthesis

1. **Lattice-gauge coupling conventions:** Section 10 provides a real `g_bare` entry lane; #69 should be narrowed rather than read as “no weak entry anywhere.” The early `mu_0 b^{-k}` convention conflicts with the flow sign, while Theorem 10.7's `mu_0 b^k` gives the plausible intended orientation.
2. **RG dynamics / asymptotics:** Theorem 10.7 forces `g_k^2` to harmonic order. An `O(g^2)` difference envelope is therefore not an `l^1` certificate. A sharper stable-manifold/trajectory-difference estimate would be needed.
3. **Constructive continuum QFT:** Equality of two continuum constructions is a gluing statement. A finite cumulative defect and finite initial distance give stability/bounded drift, not equality.
4. **OS/spectral identification:** The mass gap can be transferred from the IR route to the AF route only after equality or an equally strong same-theory identification is actually proved. This cycle gives no independent source-completeness, OS-quotient, or physical-spectrum closure.
5. **Adversarial verification:** Harmonic-series and constant-distance controls falsify the generic inference patterns while respecting their abstract inequalities. They do not purport to be Yang–Mills countermodels.
6. **RAKL v3 assurance/metrology:** Prior #109/#126/#133/#138 and the recently exercised #159/PR#161 routes prevented duplicate work and moved the cycle to the unsaturated strong/weak gluing atom. Same-context agreement earns zero independent-review credit.

## 7. Episode -> diagnosis -> obstruction/lesson separation

- **Episode:** bounded primary-source audit of the Section-10 weak-entry, AF asymptotics, and AF/IR identification chain.
- **Diagnosis:** the source has an alternative weak-bare-coupling entry lane, but the written AF/IR equality proof uses non-summable quadratic envelopes and a non-contracting cumulative-error recursion as if they forced a vanishing difference; an early scale convention also conflicts with the later one.
- **Prospective obstruction/control surface:** issue #166 freezes the next repair question. It is not a promoted RAKL obstruction object.
- **Reusable lesson:** none promoted in this run. The elementary distinction “summable perturbation gives finite drift, not equality” remains proposal/shadow evidence here.

Local mathematical failure: **none in the hostile controls; the controls verify exactly**.  
Local source-proof failure: **the displayed estimates do not support the stated summability/equality inferences**.  
Local-to-global/gluing failure: **the strong-coupling gapped continuum family is not identified with the AF family by the displayed Section-10 inequalities alone**.  
Representation failure: **the Section-10 physical-scale orientation changes from `b^{-k}` to `b^k` without an explicit reindexing at the earlier claim**.

## 8. Residual and next action

Outcome:

`PARTIAL_SUCCESS_SOURCE_ROUTE_REFINED__SMALL_G_BARE_ENTRY_EXISTS__AF_IR_SUMMABILITY_AND_EQUALITY_GLUE_NOT_ESTABLISHED_BY_DISPLAYED_BOUNDS__SCALE_ORIENTATION_LOCALLY_INCONSISTENT`

Next high-information action under #166: audit Section 9 Theorem 9.3/9.4 as a *typed repair candidate*, not by theorem name. Freeze the AF/IR parameter embeddings and show whether the theorem's `a_l`-weighted metric estimate actually applies to two running trajectories on the same regulator/OS spaces. If it does, derive an explicit vanishing bound. If it does not, seek a stronger stable-manifold estimate giving `|g_k-g'_k|=O(k^{-1-\eta})` or another `l^1` kernel difference. Do not spend another cycle merely re-proving that `sum 1/k` diverges.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`. No root/theorem/novelty promotion, no formal proof closure, and no independent mathematical review occurred.
