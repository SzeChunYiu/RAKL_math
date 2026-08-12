# YM-S1c1a R9 — Part (4) universality vanishing-modulus / path-length audit

**Cycle:** `YM-S1c1a-PART4-UNIVERSALITY-PATH-20260811-R9`  
**Root:** `RAKL_math#5` (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Parent:** `#69`; **active repair issue:** `#166 / YM-S1c1a`  
**Authority:** `PROPOSAL_SHADOW / PRIMARY_SOURCE_PROOF_AUDIT / SAME_CONTEXT_REVIEW_ONLY / NO_THEOREM / NO_ROOT_AUTHORITY`  
**Frozen fibre hash:** `8b1f6276e4b1230d73611b5a47c3fcfb93911604c8ed88e61565b28a401a3527`

## Frozen discriminator

R8 left the smallest source-level objection before constructing a new AF/IR stable-manifold estimate: the detailed Part (4) universality argument might contain a broader, trajectory-aware comparison that repairs the under-typed Section-9-to-Section-10 interface. This cycle audits that detailed proof surface itself.

Primary equation source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026), appended Part (4), corresponding to *Uniqueness and universality of the continuum limit in 4D SU(N) Yang-Mills: Part (4)*, DOI `10.1142/S0219887826501112`. The publisher/metadata source describes a 42-page refereed article and claims universality from single-scale Lipschitz control, OS time-slicing and FRD bounds; the exact equation audit below is bound to the accessible arXiv v1 compilation.

## 1. The detailed Part (4) estimates are stability bounds, not a displayed vanishing scheme modulus

On pp. 568–569, Proposition 4.3 bounds the projector/kernel difference by

`||K_(sigma,nu;B)-K_(sigma',nu';B)||_1 <= C (|sigma-sigma'| + W1(nu,nu'))`

(eq. 4.16). Proposition 4.4 controls blocking changes by `d_blk(B,B')` (eq. 4.18). Lemma 4.5 then telescopes `n` Markov steps with

`||K_theta^(n)-K_theta'^(n)||_1 <= n ||K_theta-K_theta'||_1`

(eq. 4.19).

On this displayed surface there is no factor tending to zero with lattice spacing. The estimates are useful stability controls, but for two fixed distinct scheme points they need not vanish in the continuum limit.

Proposition 4.6 makes this explicit at the cumulant level: at fixed scale,

`|S_(p,c;theta)^(k)-S_(p,c;theta')^(k)| <= C d(theta,theta') exp(-alpha tree(supp O))`

(eq. 4.21), with constants stated independent of volume and `k`.

**Uniformity audit:** volume/scale uniformity of the constant is a positive feature here. But *uniform boundedness in scale is not convergence to zero in scale*. No volume-uniformity failure is diagnosed in this local step.

## 2. Theorem 4.7 proves continuity, not scheme equality

After passing to continuum subsequences, Theorem 4.7 gives

`|S_(p;theta)-S_(p;theta')| <= C d(theta,theta') * support_decay`

(eq. 4.24, p. 570).

This establishes Lipschitz continuity of continuum cumulants with respect to the scheme parameter. It does not imply equality for fixed `theta != theta'`.

The proof then announces a strengthening from continuity to equality. Theorem 4.8 says all continuum Schwinger families coincide. Its proof observes only that the Theorem-4.7 difference is finite and then states that uniformly bounded one-step-kernel differences plus FRD equicontinuity make the limiting one-step kernels coincide (pp. 570–571).

That inference is not supplied by the displayed hypotheses: two equicontinuous, uniformly bounded families can converge to different limits. To apply OS/Markov uniqueness, equality of the limiting one-slice marginal/kernel (or another typed common Markov datum) must be established first; uniqueness then propagates equality rather than creates it.

## 3. Appendix Theorem A.8 exposes an exact path-length obstruction

Appendix Theorem A.8 (p. 588) again proves only

`|S_(p,c;theta)-S_(p,c;theta')| <= C_p d(theta,theta')`

(eq. A.31). It then states that along a polygonal chain in the admissible parameter set of total length at most `epsilon`, the difference is `O(epsilon)`, and concludes equality “by density of small chains.” The following Markov-kernel estimate is

`||K_theta^(n)-K_theta'^(n)||_1 <= n C d(theta,theta')`

(eq. A.33), which is also a stability bound rather than a vanishing bound.

For any metric chain `theta=x_0,...,x_m=theta'`, the triangle inequality gives

`sum_j d(x_(j-1),x_j) >= d(theta,theta')`.

Therefore fixed distinct endpoints cannot in general be joined by chains of arbitrarily small **total** length. Refining a path can make each segment small while leaving total length bounded below by the endpoint distance.

### Exact hostile control

Take `K=[0,1]`, `d(x,y)=|x-y|`, and `S(theta)=theta`.

- `S` is 1-Lipschitz, so it satisfies the abstract form of (A.31).
- The interval admits arbitrarily fine polygonal subdivisions between 0 and 1.
- Every such chain has total length at least 1, and the standard monotone subdivisions have total length exactly 1.
- `S(0) != S(1)`.

Hence **density/fineness of small chain segments plus a Lipschitz estimate does not imply scheme equality**. This falsifies the displayed inference form only; it is not a Yang–Mills countermodel and it does not show that a stronger repair theorem cannot exist.

## 4. Consequence for the AF/IR same-theory bridge

Immediately after the universality section, the weak-coupling section says that the asymptotically-free continuum is identical to the reflection-positive constructed continuum because “uniqueness and universality” were proved earlier (pp. 571–572).

R8 had classified the Section-9-to-Section-10 interface as `MISSING_TYPED_APPLICABILITY_WITNESS`, with a live objection that the more detailed Part (4) source might contain the needed broadened metric. R9 closes **that objection on the inspected proof surface**: Part (4) supplies Lipschitz/bounded/equicontinuous stability, but the displayed equality argument still lacks a vanishing endpoint comparison.

This remains a **source-proof and local-to-global same-theory gluing obstruction**, not a theorem that the two continuum limits differ. A repair could still be obtained by any of the following:

1. prove `d_k(theta_k,theta'_k) -> 0` for the paired schemes/trajectories in the actual comparison metric;
2. prove direct convergence of one-slice marginals and one-step kernels to common limits in a norm strong enough for OS time-slicing;
3. show that the two parameterizations have zero pseudodistance because they represent the same regulator/theory object, with a typed identity witness;
4. prove a direct AF/IR stable-manifold or inter-trajectory estimate whose tail tends to zero.

Until one of these is source-bound or proved, the mass gap of the IR/strong construction cannot be transferred merely by invoking this universality equality step.

## 5. Spectral / lattice / RG scope audit

- **Finite-lattice gap:** not re-litigated here; no local finite-lattice spectral counterexample is claimed.
- **Volume uniformity:** the inspected Part (4) source explicitly claims constants independent of volume; no failure found at this coordinate.
- **Lattice-spacing uniformity:** bounds uniform in `k` are present, but the required *vanishing in the comparison* is absent from the displayed Part (4) formulas audited here.
- **Physical spectral identification:** remains downstream. A gap can be called the same physical gap across AF/IR constructions only after the continuum theories/states are actually identified.
- **Decay -> gap:** not newly closed or refuted in this cycle.
- **OS source/semigroup gluing:** Theorem 4.8 appeals to Markov uniqueness only after asserting common limiting data; the displayed stability estimates do not establish that common data.
- **Numerics:** none used. The hostile control is exact.

## 6. Same-context expert cell

1. **Rigorous lattice/RG analyst:** checked which Part (4) parameters actually enter the single-scale kernel and whether the bounds decay with scale. Finding: displayed bounds are `O(d(theta,theta'))`, uniform but not vanishing.
2. **Metric/functional analyst:** reduced the “small polygonal chain” step to the metric triangle inequality. Finding: fine segments do not imply arbitrarily small total endpoint path length.
3. **Constructive QFT / OS analyst:** separated stability of Markov data from equality of limiting Markov data. Finding: OS uniqueness propagates common data; it does not manufacture common data from bounded differences.
4. **Spectral/transfer-matrix analyst:** audited downstream consequence. Finding: no direct finite-lattice gap result is falsified; only the same-theory transfer of the gap remains unlicensed.
5. **Adversarial source/provenance analyst:** cross-checked Part (4) Propositions 4.3–4.6, Theorems 4.7–4.8, Appendix A.8 and the weak-coupling handoff. A visual PDF screenshot of the p. 570 theorem transition was inspected earlier in this run; later screenshot retries for pp. 570/588 cache-missed, so exact line selectors from the primary PDF are retained as the reproducible source surface.
6. **RAKL v3 assurance/metrology analyst:** kept this as a proposal/shadow TaskEpisode, separated episode -> diagnosis -> proposed obstruction/lesson, assigned zero independent-review credit and zero retained semantic novelty pending protected gates.

Same-context consensus is not an independent mathematical review.

## 7. Episode -> diagnosis -> obstruction/lesson separation

- **Episode:** `EP-YM-S1c1a-R9-20260811`: bounded audit of detailed Part (4) universality equality and its AF/IR handoff.
- **Diagnosis:** `DG-YM-S1c1a-R9-PATH-LENGTH-EQUALITY-SHADOW`: the displayed source proves Lipschitz stability/continuity but infers equality using bounded/equicontinuous kernels and “small chains” without a vanishing endpoint modulus.
- **Proposed obstruction:** `OBS-YM-S1c1a-R9-NONVANISHING-UNIVERSALITY-SHADOW`; proposal/shadow only, not a protected RAKL obstruction.
- **Proposed reusable lesson:** `LESSON-YM-S1c1a-R9-LIPSCHITZ-NEQ-EQUALITY-SHADOW`: a Lipschitz comparison plus arbitrarily fine path subdivision does not imply equality at distinct endpoints; a vanishing comparison or identity witness is required. Proposal/shadow only.
- **Failure signature:** `FS-YM-S1c1a-R9-SMALL-CHAIN-LENGTH-FALLACY-SHADOW`.

Local mathematical verification: **the path-length hostile control is exact**.  
Local source-proof failure: **the displayed proof interface does not justify the equality inference from the stability bounds**.  
Local-to-global/gluing failure: **the AF and IR continuum constructions are still not identified as the same OS theory by this argument**.

## 8. Outcome and next discriminator

**Outcome:** `PARTIAL_SUCCESS__PART4_UNIVERSALITY_EQUALITY_INFERENCE_FAILS_PATH_LENGTH_FALSIFIER__AFIR_SAME_THEORY_GLUE_STILL_OPEN`

**Residual:** `RES-YM-S1c1a-R9-VANISHING-SCHEME-OR-AFIR-COMPARISON-WITNESS`

Next action: rotate from source-completeness prose to a constructive discriminator. Freeze the smallest same-theory comparison problem: either derive a source-valid `d_k -> 0`/common-Markov-data estimate for the actual AF/IR pair, or derive a stable-manifold/inter-trajectory bound strong enough to force the Schwinger-function difference to zero. Reject any argument that supplies only boundedness, equicontinuity, Cauchy control of each family separately, or fine partitions with non-vanishing endpoint distance.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`. No theorem/root/novelty/scientific-authority promotion and no independent mathematical review occurred.
