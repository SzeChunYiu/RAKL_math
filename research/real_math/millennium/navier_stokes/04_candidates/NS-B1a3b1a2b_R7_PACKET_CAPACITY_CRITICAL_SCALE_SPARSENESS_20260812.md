# NS-B1a3b1a2b R7 — packet capacity versus critical-scale geometric sparseness

**Authority:** proposal/shadow source-bound verification only. No Type-I exclusion, no Clay-root authority, no literature-novelty certificate, and no independent-review credit.

**Cycle:** `NS-B1a3b1a2b-R7-PACKET-SPARSENESS-SCALE-20260812`

**Frozen application base:** `02c5fb7764116cf075d8dd5efd7b6fe835275ab9` / tree `4cd0c3a26dc37400cc1864bb77367b314406c786`.

**Framework subject observed before freeze and revalidated before result materialization:** `SzeChunYiu/RAKL@8db3343dfb764c9a139f9ba76f6f44c76eaf86de`, canonical method `3.0.0`, package `0.1.0`.

**Chronology boundary:** the possible capacity-to-sparseness scale comparison was noticed in automation scratch before issue #336 and the durable packet, so strict prospective hypothesis-generation credit is `RETROSPECTIVE_ONLY`. Issue #336, the pre-candidate packet, the eight-event trace, the source set, exact falsifiers, and the consequential verification target were frozen before this result file.

## Scoped outcome

`CRITICAL_SCALE_VOLUME_FRACTION_FORMULA_IDENTIFIED__DIRECT_GEOMETRIC_CONSUMER_GLUE_OPEN`

The R6 all-center packet-capacity estimate does contain a genuine geometric consequence: at every fixed time, sufficiently large balls see an arbitrarily small **volumetric fraction** of the half-maximal vorticity set. However, when the estimate is written at the scale-invariant vorticity length `Omega(t)^(-1/2)`, the guaranteed smallness is governed by two dimensionless quantities that finite `I` does not make small:

- the Type-I magnitude `I` itself;
- the temporal coherence ratio

`chi(t) = ||partial_t omega(t)||_infinity / ||omega(t)||_infinity^2`.

The exact direct bound therefore does not furnish an `O(1)` critical-scale sparsity certificate for arbitrary finite `I`, and the primary geometric regularity sources audited here do not consume exactly this input anyway: Albritton–Bradshaw's regularity theorem is a velocity-`L^p` sparsity theorem, Grujic's original criterion is local **one-dimensional** sparseness, and Grujic 2026 reaches local 1D sparseness only after additional critical Lorentz-vorticity and vorticity-direction hypotheses. The remaining failure is local-to-global/consumer gluing, not failure of the R6 local ancient-smoothing estimate.

## 1. Starting source-bound capacity law

Let `u` be a nontrivial bounded mild ancient Navier–Stokes solution in the finite-`I` Albritton–Barker class. At a fixed time `t`, write

`Omega = ||omega(t)||_infinity`,

`K = ||partial_t omega(t)||_infinity`.

R6 source-bound ancient smoothing gives `K <= C M^4` with `M=||u||_infinity`. The finite-`I` dissipation coordinate plus temporal persistence gives, for every center `x`, threshold `lambda>0`, and radius `R`,

`|S_lambda(t) cap B(x,R)| <= C I R / [lambda^2 min(R^2, lambda/K)]`,

where `S_lambda(t)={|omega(t)|>=lambda}` and the `K=0` case is interpreted by `lambda/K=+infinity`.

In the large-radius temporal-persistence regime `R^2 >= c lambda/K`, this is the R6 linear packet-capacity law

`|S_lambda(t) cap B(x,R)| <= C I K R lambda^(-3)`.

No pressure term is discarded in deriving a new local-energy identity here: the only mathematical input is the already registered finite-`I` consequence. Pressure/nonlocality remains a separate potential source of a *stronger* future same-theory bridge.

## 2. Exact all-center volume-fraction consequence

Set `lambda=Omega/2` and assume `Omega>0`. Divide by `|B_R|=c_3 R^3`. Then

`sup_x |S_{Omega/2}(t) cap B(x,R)| / |B_R|`

`<= C I / [Omega^2 R^2 min(R^2, Omega/K)]`.

This is already an all-center volumetric-sparseness statement in the sense of the elementary measurable-function definition used by Albritton–Bradshaw: the half-maximum set occupies an arbitrarily small fraction of sufficiently large balls.

Now introduce the scale-invariant temporal-coherence coordinate

`chi = K / Omega^2`

and write the radius at the critical vorticity length as

`R = a Omega^(-1/2)`.

Because

`Omega^2 R^2 min(R^2,Omega/K) = a^2 min(a^2,1/chi)`,

the bound becomes the dimensionless formula

`sup_x |S_{Omega/2}(t) cap B(x,a Omega^(-1/2))| / |B_{a Omega^(-1/2)}|`

`<= C I / [a^2 min(a^2,1/chi)]`.                         `(R7.1)`

Equivalently, up to harmless constants,

- if `a^2 chi <= 1`, the available bound is `C I a^(-4)`;
- if `a^2 chi >= 1`, the available bound is `C I chi a^(-2)`.

Every factor is dimensionless. Under Navier–Stokes scaling, `Omega` has length dimension `L^-2`, `K` has `L^-4`, so `chi=K/Omega^2` and `a=R sqrt(Omega)` are invariant.

### Consequence for a fixed epsilon

To **guarantee from this bound alone** that the half-maximal vorticity set is `epsilon`-sparse in volume, one can take a scale factor obeying the appropriate branch:

- temporal-persistence branch: `a >= C (I/epsilon)^(1/4)`, provided `a^2 chi <= c`;
- derivative-limited branch: `a >= C (I chi/epsilon)^(1/2)`, with `a^2 chi >= c`.

These are sufficient scales extracted from the registered upper bound, not lower bounds on the actual sparsity scale of the solution.

The key obstruction is therefore precise: **finite `I` means boundedness, not smallness, and ancient local smoothing supplies finiteness of `chi` but no source-bound small universal control of `I`, `chi`, or `I chi`.** Indeed `K<=C M^4` and `Omega<=C M^2` do not upper-bound `chi=K/Omega^2` by a small universal constant because there is no registered lower comparison `Omega >= c M^2`.

Thus `(R7.1)` proves large-scale volumetric sparsity as `a->infinity`, but does not certify small volume fraction at an `O(1)` multiple of the critical vorticity length for arbitrary finite-`I` ancient states.

## 3. Counterexample-first stress semantics

The R6/R5 linearly replicated smooth packet trains show that an `O(R)` capacity and hence `R^-2` volume fraction can be saturated at the level of the magnitude-ledger representation. Current RAKL realization-domain typing is load-bearing:

`AMBIENT_REPRESENTATION -> REPRESENTATION_ONLY`.

Those packet trains are not unforced Navier–Stokes solutions and cannot certify that a genuine finite-`I` ancient NSE state realizes large `I chi`, realizes the worst scale in `(R7.1)`, or violates a geometric regularity criterion. Their legitimate role is only to prevent an algebraic inference that the ledger itself secretly contains radius-free/global or critical-scale geometric control.

A target-domain falsifier would require an actual finite-`I` ancient NSE state or a theorem showing the exact source assumptions allow the bad `I,chi` regime. No such target-domain falsifier is claimed.

## 4. Exact consumer-signature audit

### Albritton–Bradshaw, arXiv:2110.02187

Their Definition 1.1 formalizes all-center **volumetric** `L^p` sparseness, and their Theorem 1.2 is a regularity criterion for velocity data `u_0 in L^p_sigma`, `p>d`, with a particular existence-time and sparse-set/tail signature. The present producer gives a half-maximal **vorticity-superlevel volume fraction** for an ancient finite-`I` state; it does not produce the required velocity `L^p` datum, sparse-set tail norm, or theorem-specific time parameters.

The same paper is nevertheless a strong SEARCH analogue for method diagnosis: it explicitly analyzes how an a-priori sparseness scale can retain energy-level homogeneity rather than closing the critical scaling gap. That is exactly why `(R7.1)` is used as a scale discriminator rather than treated as theorem authority.

**Direct glue verdict:** `SOURCE_PRECONDITION_MISMATCH`.

### Grujic, arXiv:1111.0217

The primary abstract states the regularity condition as local anisotropic geometric control, essentially local **one-dimensional sparseness** of intense regions. A three-dimensional volume-fraction bound on every ball does not automatically imply a one-dimensional sparse line through the relevant point at the same scale: volume can concentrate along a thin set containing that line or around the chosen center.

**Direct glue verdict:** `VOLUMETRIC_TO_LINEAR_SPARSENESS_WITNESS_MISSING`.

### Grujic, arXiv:2607.08866v2

The current 2026 route assumes critical `L^{3/2,infinity}` vorticity concentration and local logarithmically weighted BMO control of vorticity direction, derives logarithmic vortex-stretching depletion and a subcritical Lorentz–Zygmund gain, then transfers that gain to local 1D sparseness below a uniform analyticity radius. R6/R7 does not supply the global Lorentz amplitude or direction hypothesis; the current consumer therefore remains source-incomplete even before the scale comparison.

**Direct glue verdict:** `CRITICAL_AMPLITUDE_AND_DIRECTION_PRECONDITIONS_UNMAPPED`.

### Gallagher–Koch–Planchon, arXiv:1012.0145

The critical-element/profile-decomposition route works in global critical Lebesgue/Besov spaces and, in particular, is tied to bounded global `L^3`/critical-space structure. Finite `I` plus `(R7.1)` does not supply that global critical norm or profile-tightness premise.

**Direct glue verdict:** `GLOBAL_CRITICAL_SPACE_PRECONDITION_UNMAPPED`.

## 5. Scaling, units, endpoint, pressure, derivative-loss and circularity audit

- **Scaling:** `a=R sqrt(Omega)` and `chi=K/Omega^2` are invariant. `(R7.1)` is dimensionless.
- **Units:** the pre-normalized measure bound has units `L^3`; after division by ball volume there is no residual physical unit.
- **Constants:** all conclusions are inequality-shape statements up to universal/source constants. No numerical threshold is used as theorem authority.
- **Endpoint:** `Omega=0` is excluded from the normalization; that case has no half-maximal vorticity geometry to diagnose. No terminal value at `t=0` is imported.
- **Pressure/nonlocality:** pressure is not proven irrelevant to the target problem. It is absent only because R7 audits what follows from the already-derived capacity law. A future pressure cancellation/no-incoming theorem remains an allowed repair.
- **Derivative loss:** `K=||partial_t omega||_infinity` is source-bound by ancient mild smoothing; no further derivative is introduced.
- **Circular bootstrap:** no regularity criterion is assumed to derive `(R7.1)`. Existing criteria are used only as downstream signature checks.
- **One-dimensional versus volumetric:** no Fubini/averaging shortcut is used to claim the exact line-through-point condition from ball volume fraction.
- **Critical elements:** no profile compactness is inferred without its global critical-space premise.

## 6. Episode -> diagnosis -> failure -> obstruction/lesson

- **Episode:** freeze R6 capacity law; translate it into all-center half-maximal volume fraction; normalize at `Omega^-1/2`; audit exact same-domain geometric consumers and a critical-element analogue.
- **Diagnosis:** the capacity law contains real large-scale volumetric geometry but its critical-scale guarantee depends on the dimensionless coordinates `I` and `chi`; the retained source consumers also require different geometry/state signatures.
- **Failure:** `finite-I packet capacity -> existing geometric regularity theorem` is not source-licensed from the current fibre.
- **Local mathematical status:** success — equation/source-class capacity algebra and scale normalization close exactly.
- **Local-to-global/consumer gluing status:** open — no exact existing consumer is fed by `(R7.1)` alone.
- **Obstruction:** `O-NS-B1a3b1a2b-CRITICAL-SCALE-TEMPORAL-COHERENCE-OR-CONSUMER-TYPE`.
- **Candidate lesson:** after obtaining an all-center growth law, normalize it at the target's critical physical scale before celebrating geometric sparsity; expose every surviving dimensionless factor and type-check the consumer (volume/line, velocity/vorticity, time-lag, tail norm) separately.

## 7. Next strict atom

`NS-B1a3b1a2c` should search actual finite-`I` ancient NSE dynamics for one of three source-valid repairs:

1. a dimensionless temporal-coherence/cascade relation controlling `I chi` (or a stronger scale-aligned replacement) near half-maximal vorticity;
2. a same-theory transformation from all-center volumetric vorticity sparsity to the exact local one-dimensional/analyticity consumer while preserving center/time quantifiers;
3. a different source-complete consumer that directly accepts the finite-`I` Morrey/capacity geometry without importing global critical `L^3`/Lorentz or direction control.

A pressure/no-incoming/tail mechanism remains an orthogonal repair route and should be preferred over another local smoothing derivative if it changes one of those dimensionless or consumer-interface coordinates.

The Clay root remains `OPEN_NO_SOLUTION_CERTIFICATE`; proof DAG remains open; verifier/dependency/axiom closure is not triggered; genuinely independent mathematical review remains `0/3`.