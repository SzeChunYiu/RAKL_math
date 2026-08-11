# NS-B1b1 — Pineau–Vicol v2 scenario / transfer audit

**Atom:** `NS-B1b1`  
**Issue:** `#56`  
**Authority:** `SOURCE_BOUND_SCENARIO_CLASSIFICATION / TRANSFER_BLOCKED_SCOPED / NEW_PRIMARY_LITERATURE_MILESTONE / ROOT_AUTHORITY_NONE`  
**Current source version:** Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, arXiv:2607.09619v2, revised 2026-08-06.  
**Framework freshness:** current `SzeChunYiu/RAKL@main` was read at `60a38728d0ebace2fa2312bcad81d1d3f9df757c`. That commit changes pytest root-path behavior only; mathematical-research gate semantics remain those of the application pin `15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`.

This packet is a source audit and method-transfer discriminator. It does **not** claim a new Navier–Stokes theorem, does not certify any singular solution, and cannot contribute root-review credit.

## 1. Exact scenario statements now source-bound

### 1.1 RSS: Pineau–Vicol Theorem 1.4

For a solution on `R^3 x [-1,0)` satisfying the **global pointwise Type-I upper bound**

`|u(x,t)| <= C_{U,0}/(|x| + sqrt(-t))`

and the exact backwards rotated globally self-similar ansatz

`u(x,t)=(-t)^(-1/2) R(alpha s) U(R(-alpha s)x/sqrt(-t)),  s=-log(-t),`

with `U in C^2(R^3)`, there exist thresholds depending on `C_{U,0}` such that `U=0` whenever `|alpha|` is sufficiently small or sufficiently large.

**Residual left by the theorem:** the intermediate `alpha ~ 1` RSS regime is explicitly open.

### 1.2 DSS/RDSS: Theorems 1.6–1.7

For exact DSS with period `S=2 log(lambda)`, Theorem 1.6 excludes the profile when the global pointwise Type-I bound holds and `lambda>1` is sufficiently close to `1`.

For exact `(alpha,lambda)`-RDSS, Theorem 1.7 assumes the same global pointwise Type-I upper bound and exact periodic rotated self-similar ansatz. It proves triviality in two regimes:

1. `|alpha| <= underline(alpha)(C_{U,0})` and `1 < lambda < underline(lambda)(C_{U,0})`;
2. `|alpha| >= overline(alpha)(C_{U,0})` and  
   `1 < lambda < underline(lambda)(C_{U,0})^(1/(1+alpha^2))`.

**Residuals:** moderate rotation and/or periods not sufficiently short remain outside the theorem. Exact RDSS is a special periodic orbit class and cannot represent all finite-`I` ancient dynamics.

### 1.3 Local one-slice criterion: Theorem 1.9 and Remark 1.11

Pineau–Vicol v2 adds a local regularity criterion not present in the v1 abstract/source map used earlier in this workspace.

Let `(u,p)` be smooth on `B_1 x [-1,0)`. Theorem 1.9 assumes:

1. pointwise Type-I velocity:
   `|u(x,t)| <= C_u/(sqrt(-t)+|x|)`;
2. fixed-annulus pressure:
   `|p(x,t)| <= C_p` for `1/2 < |x| < 3/4`;
3. at one sufficiently late time `bar t`, smallness of the self-similar scaling generator
   `sqrt(-bar t) || (-bar t) partial_t u - 1/2 u - 1/2 (x dot grad)u ||_{L^infinity(B_1)} <= delta_0`.

Then `(0,0)` is regular.

In self-similar coordinates `U(y,s)=sqrt(-t)u(x,t)`, the third hypothesis is a one-slice smallness condition on `partial_s U`. Remark 1.11 states that the proof still works under the weaker one-slice Gaussian-weighted condition

`integral |partial_s U(y,bar s)|(1+|y|) exp(-|y|^2/8) dy <= O(delta_0)`

over the expanding self-similar ball.

The source explains the mechanism: localize a weighted Bernoulli/enstrophy estimate, convert the one-slice generator smallness into small local enstrophy, propagate the smallness forward, and finish with Caffarelli–Kohn–Nirenberg epsilon regularity.

## 2. Exact blow-up profile and limit passage relevant to `NS-B1`

The source-bound Type-I route remains Albritton–Barker.

A suitable weak Type-I singularity in their scale-invariant sense yields, after singular rescaling and recentering, a **nontrivial mild bounded ancient solution** `(v,q)` with finite

`I(v,q) = sup_Q [A(Q)+C(Q)+D(Q)+E(Q)]`.

The compactness interface used in that program is local:

- velocity: strong `L^3_loc` after passage to a subsequence;
- pressure: weak `L^(3/2)_loc`, after the source-compatible normalization/decomposition;
- nontriviality: recovered by singularity persistence / epsilon-regularity, not by weak convergence alone.

This passage is enough to preserve the finite-`I` ancient obstruction. It is **not** enough to pass any of the following without a new theorem:

- global pointwise `1/(|x|+sqrt(-t))` decay;
- fixed-annulus `L^infinity` pressure;
- exact RSS/DSS/RDSS symmetry;
- a selected time slice with small `partial_s U`;
- global `L^3` tail tightness.

The pressure distinction is load-bearing. `D` is a critical `L^(3/2)` pressure-oscillation quantity; weak `L^(3/2)_loc` convergence cannot be promoted to an `L^infinity` annular bound by topology alone. Harmonic/far-field pressure pieces must remain explicit.

## 3. Hypothesis-inheritance matrix

| Pineau–Vicol interface coordinate | Available from finite `I` / known AB passage? | Verdict |
|---|---:|---|
| exact RSS ansatz | no | `NOT_INHERITED` |
| exact DSS/RDSS periodicity | no | `NOT_INHERITED` |
| global pointwise Type-I velocity decay | no source-bound implication from `I` | `NOT_INHERITED` |
| local pointwise Type-I velocity bound on the original singular cylinder | no source-bound implication from `I` | `NOT_INHERITED` |
| annular pressure `L^infinity` bound | `D` only gives critical `L^(3/2)` information modulo means | `NOT_INHERITED` |
| one late small self-similar generator slice | no monotone/dissipative extraction theorem is available | `NOT_INHERITED` |
| strong `L^3_loc` velocity compactness | yes, under the AB compactness hypotheses | `SOURCE_BOUND` |
| weak `L^(3/2)_loc` pressure compactness | yes, after source-valid normalization | `SOURCE_BOUND` |
| nontriviality persistence | yes, via AB persistence/epsilon regularity | `SOURCE_BOUND` |
| far-field tightness / global `L^3` trace | no | `OPEN_BRIDGE` |

Therefore none of Theorems 1.4, 1.7, or 1.9 can presently be applied **unchanged** to eliminate the full Albritton–Barker finite-`I` class.

## 4. Critical-element / minimal-counterexample transfer audit

Gallagher–Koch–Planchon and Kenig–Koch provide a solved Navier–Stokes analogue of critical-element logic when the obstruction is measured in a **global critical norm** admitting a profile decomposition and enough decoupling to isolate a minimal blow-up profile.

The finite-`I` class differs in four atomic ways:

1. `I` is a supremum of local cylinder functionals, not a global `L^3`/Besov norm.
2. no source-bound profile decomposition or Pythagorean/orthogonality law is available for `I`;
3. translation/dilation can move concentration between cylinders and allow profile leakage to the far field;
4. pressure contains harmonic/nonlocal pieces for which no `I`-decoupling theorem is available.

Thus a statement such as “choose a minimal finite-`I` counterexample and obtain an almost-periodic orbit modulo symmetries” is **not** licensed. It would require an attainment/Palais–Smale theorem, profile-decoupling/tightness, and nontriviality under the quotient symmetries.

Adversarial model for the logic (not a Navier–Stokes solution): multiple well-separated critical packets can keep a local supremum bounded while defeating a single-profile compactness conclusion. This is precisely the profile-leakage coordinate that a valid finite-`I` critical-element theorem would have to rule out.

## 5. Vorticity stretching and geometric depletion

Pineau–Vicol's 2026 mechanism is valuable because it bypasses a missing Bernoulli maximum principle and works through a weighted `L^2` enstrophy coordinate.

- for small RSS rotation, a positive adjoint weight with Gaussian bounds turns the rotational perturbation into a small weighted-enstrophy estimate;
- for large rotation, the rotation generator forces proximity to an axisymmetric kernel in a weighted norm, which again gives small local enstrophy;
- in Theorem 1.9, one-slice near-stationarity similarly yields small local enstrophy, which is propagated to regularity.

This is a genuine **geometric-depletion/rigidity mechanism**, but its transfer cannot silently replace the pointwise velocity/pressure estimates used to construct and control the weights. The next source audit must identify line by line which estimates in Section 9 require pointwise Type-I and annular pressure `L^infinity`, and whether finite `A,C,D,E` plus suitable-weak structure can substitute.

## 6. Compactness, pressure, decay, far field, backward uniqueness audit

**Weak limits.** Strong `L^3_loc` velocity is adequate for the local cubic nonlinearity and suitable-limit passage; weak pressure convergence is adequate only in the source's local topology. Neither yields pointwise derivative estimates.

**Pressure localization.** The required annular pressure condition in Theorem 1.9 is not a corollary of `D`. Calderón–Zygmund near-field control and harmonic far-field control must be separated, with pressure gauges fixed explicitly.

**Decay/far field.** The global RSS/RDSS theorems use the global pointwise Type-I profile decay. Finite `I` does not give global tail tightness or global `L^3`. Moving-center/profile leakage remains live.

**Time-slice compactness.** Space-time compactness does not supply convergence of `partial_s U` at a selected slice, much less smallness. A separate derivative estimate plus a selection principle would be needed.

**Backward uniqueness.** It remains a terminal rigidity tool only after exact terminal vanishing/integrability/decay hypotheses are produced. It cannot create exact symmetry, far-field tightness, or a near-stationary self-similar slice.

## 7. Exact rigidity theorem / bridge that would be sufficient

Two stages are required for the Pineau–Vicol route.

### Stage A — finite-`I` localization theorem

A source-valid replacement for Theorem 1.9 of the form:

> For every `M<infinity` there is `delta(M)>0` such that a suitable/smooth Navier–Stokes solution on a unit parabolic cylinder with `A+C+D+E <= M` (with an explicitly stated pressure gauge/localization hypothesis no stronger than what the blow-up passage preserves) is regular at the top center whenever, at one sufficiently late self-similar time, the Gaussian-weighted norm  
> `integral |partial_s U|(1+|y|)exp(-|y|^2/8)`  
> is at most `delta(M)`.

This is **not known here**; it is the exact method-transfer theorem whose proof obligations can be audited against Pineau–Vicol Section 9.

### Stage B — near-stationary-slice extraction theorem

Even if Stage A succeeds, one still needs:

> Every finite-`I` Type-I singular trajectory has a sequence of singular rescalings and late self-similar times for which the Stage-A weighted self-similar generator norm tends to zero, with nontriviality and pressure normalization preserved.

No such theorem follows from current compactness. Periodic/RDSS and rotating renormalized motion are direct hostile cases. A valid proof would need a signed/monotone or genuinely integrable self-similar-time dissipation, or a different compactness-rigidity mechanism that rules out recurrence.

The previous PR #54 failure matters here: absolute critical local-energy shell costs are `O(1)` per scale and do not supply a finite currency across infinite scale descent. Therefore Stage B must not be justified by rebranding that absolute shell accounting.

## 8. Breakthrough/metacognitive controls

Proposal-only modes retained for search:

- `REFLECTIVE_RESTRUCTURE`: replace “terminate infinitely many scales” by “extract one near-stationary renormalized slice”;
- `CONTRASTIVE_DISCRIMINATION`: compare exact RSS/RDSS, moderate-period recurrent motion, and genuinely nonperiodic ancient orbits to expose which derivative/tightness coordinate separates them.

No mode creates method authority. The observed residuals are already classified (`pressure topology`, `noncompact symmetry`, `profile leakage`, `near-stationary-slice extraction`), so there is no evidence here for a new framework ontology or method-basis defect.

## 9. Verdict and next atom

**Verdict:** `TRANSFER_BLOCKED_SCOPED`.

The v2 Pineau–Vicol results are a materially important 2026 update because they:

- eliminate extreme-rotation global RSS under the exact pointwise Type-I hypothesis;
- eliminate corresponding short-period RDSS regimes;
- add a local one-slice approximate-self-similarity regularity criterion.

But they do **not** close the general Type-I finite-`I` ancient class, do not force exact/approximate self-similarity, and do not touch Type-II.

**Narrow residual:** `NS-B1b1a — finite-I localization audit of the Pineau–Vicol weighted-enstrophy criterion.` Before any theorem candidate, freeze a fresh context and test whether the pointwise velocity and annular pressure hypotheses are genuinely load-bearing or can be replaced by the exact `A,C,D,E` controls inherited in the Albritton–Barker blow-up passage.

No root certificate, proof DAG, verifier receipt, novelty certificate, or isolated mathematical review is claimed.
