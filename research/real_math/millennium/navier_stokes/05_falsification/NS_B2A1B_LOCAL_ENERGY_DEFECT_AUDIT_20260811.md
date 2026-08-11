# NS-B2a1b — local-energy-defect criterion audit

**Atom:** `NS-B2a1b — SIGNED_EULER_FLUX_ENERGY_DEFECT`  
**Parent:** open stacked PR #91 (`NS-B2a1`)  
**Pre-action freeze:** `4baf65cc9fcd146cf9cabd0ff4b4e8d4aafb1500`  
**Framework read:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Current application main observed:** `SzeChunYiu/RAKL_math@6557b1b25fa839fe71aba8047c958d5da892edd8`  
**Authority:** source-bound interface diagnostic only. No Euler theorem candidate, no Navier–Stokes theorem, no Clay/root authority, no independent-review claim.

## Chronology / contamination boundary

The possibility that a local-energy defect obstructs signed-flux telescoping, and a rough scale-critical `O(R)` defect bookkeeping estimate, were already considered before the pre-action freeze. They receive **zero prospective novelty credit**. A broad pre-freeze literature search had also failed to surface a theorem immediately forcing equality. The post-freeze evidence credit is therefore restricted to exact primary-source extraction and hypothesis-by-hypothesis mapping of the bounded source set below.

## Frozen discriminator

Determine whether the exact `F(a)=1` ancient Euler class inherited in Seregin's Theorem 3.1 forces local energy equality under an audited primary-source criterion, or whether the only licensed statement remains a local energy balance with a non-negative defect requiring separate control.

## Bounded primary-source set inspected

1. Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468v1, especially Theorem 3.1, (3.5)–(3.7).  
   https://arxiv.org/abs/2606.29468
2. Jean Duchon and Raoul Robert, *Inertial energy dissipation for weak solutions of incompressible Euler and Navier-Stokes equations*, Nonlinearity 13 (2000), 249–255, Propositions 2–3.  
   https://doi.org/10.1088/0951-7715/13/1/312
3. Peter Constantin, Weinan E and Edriss S. Titi, *Onsager's conjecture on the energy conservation for solutions of Euler's equation*, Comm. Math. Phys. 165 (1994), 207–209.  
   https://doi.org/10.1007/BF02099744
4. Luigi C. Berselli and Stefanos Georgiadis, *Three results on the energy conservation for the 3D Euler equations*, NoDEA 31, 33 (2024), Theorem 2.  
   https://doi.org/10.1007/s00030-024-00924-9

This is a bounded audit, not a completeness claim over all Euler energy-equality literature.

## 1. The inherited limit lies in the Duchon–Robert local-balance class

Seregin obtains, after subsequence extraction, strong convergence on every fixed `Q(a)` in `L_{3ν}` for every `1 <= ν < 10/9`; in particular the limit `u` is locally `L^3`. Theorem 3.1 also keeps the pressure locally in `L^{3/2}` through the scale bound (3.5) and gives the weak Euler equation (3.6) together with the local energy inequality (3.7).

Duchon–Robert Proposition 2 states that an `L^3` weak Euler solution has a distributional local energy balance

`∂_τ(|u|²/2) + div[((|u|²/2)+p)u] + D^u = 0`.

Thus the exact Seregin limit admits a local defect distribution `D^u`. Comparing this equality with Seregin's local energy inequality gives `D^u >= 0` as a distribution. Hence `D^u` is a locally finite positive Radon measure on compact subsets of `Q_-`.

This statement does **not** assert `D^u` is nonzero.

## 2. The audited equality criteria do not match the inherited baseline

### 2.1 Duchon–Robert Proposition 3

A sufficient condition for `D^u=0` is a cubic-increment estimate of the form

`∫ |u(t,x+ξ)-u(t,x)|³ dx <= C(t)|ξ|σ(|ξ|)`, with `σ(r)->0` and `C in L¹_t`.

The inherited `F(a)=1` baseline gives local `u in L∞_t L²_x ∩ L²_t H¹_x`. A direct 3D `H¹` estimate gives, schematically on a compact ball,

`||δ_ξ u(t)||³_3 <= C |ξ|^(3/2) ||u(t)||³_{H¹}`.

The available bound controls the square, not the cube, of the `H¹` norm in time. Therefore this direct inheritance calculation does not verify the `C in L¹_t` requirement of Proposition 3.

### 2.2 Constantin–E–Titi

Their theorem assumes, in the periodic setting, `u in L³_t B^α_{3,∞}`, `α>1/3` (along with the weak-solution/energy-continuity hypotheses in the theorem). From the two inherited energy endpoints alone, interpolation gives locally `u in L³_t H^(2/3)_x`, and the three-dimensional Sobolev/Besov embedding gives only the scale `H^(2/3)_2 -> B^(1/6)_{3,2}`, well below the required spatial `>1/3` Besov regularity. This calculation does not exclude additional hidden regularity; it shows only that (3.5)'s baseline energy class does not supply the Constantin–E–Titi hypothesis by interpolation.

### 2.3 Berselli–Georgiadis Theorem 2

A recent Sobolev sufficient criterion assumes `u in L^r_t W^{1,q}_x`, with `q>2` and `r > 5q/(5q-6)`. The inherited derivative control is only the endpoint `q=2`, `r=2`. It therefore does not enter that theorem.

## 3. What the scale-critical bounds say about the defect

For a non-negative compact spacetime cutoff `φ_R` supported at parabolic scale `R`, with `|∂_τ φ_R| <= C/R²` and `|∇φ_R| <= C/R`, the local balance gives

`<D^u,φ_R> = ∬ (|u|²/2)∂_τφ_R + ((|u|²/2)+p)u·∇φ_R`.

The `F(a)=1` bounds imply the scale estimates

- `sup_τ ∫_{B(R)} |u|² <= C R`,
- `∬_{Q(R)} |∇u|² <= C R`,
- `∬_{Q(R)} |p|^(3/2) <= C R²`.

Local Gagliardo–Nirenberg plus the first two bounds yields `∬_{Q(R)} |u|³ <= C R²`. Consequently the time-cutoff, cubic-flux and pressure-flux contributions are each bounded by `C R`, and `0 <= <D^u,φ_R> <= C R`. Therefore the natural normalized quantity is only bounded, `R^{-1}<D^u,φ_R> = O(1)`, not forced to vanish by (3.5).

This scale calculation is **retrospective calibration now source-checked**, not a newly discovered prospective result.

## 4. Outcome against the preregistered branches

**Observed branch: B — `LOCAL_ENERGY_INEQUALITY_ONLY`, inside the bounded source universe.**

More precisely:

- an explicit local Duchon–Robert defect is licensed and is non-negative under the Seregin local energy inequality;
- none of the audited sufficient equality criteria is implied by the inherited baseline regularity;
- the scale-critical bounds control the defect at the same `O(R)` normalization as the other energy-flux terms but do not make the normalized defect vanish;
- failure to satisfy these sufficient criteria is **not** evidence that `D^u` is nonzero or that local energy equality is impossible.

No branch-C defect-tail theorem was found in the bound source set.

## 5. Exact residual

`O-NS-B2a1b-LOCAL-ENERGY-DEFECT-CONTROL`

Before a signed-flux telescoping route can claim to bypass the parent tail obstruction, one of the following must be source-bound/proved for the exact Seregin class:

1. `D^u = 0` by an applicable local energy-equality criterion;
2. a direct Duchon–Robert increment-flux limit strong enough to show the relevant defect vanishes;
3. a normalized defect-tail/annular estimate forcing the defect contribution to vanish at the large-radius normalization used by the rigidity argument.

Otherwise the signed flux identity contains an interior non-negative term at exactly the same scale as the boundary terms and cannot be telescoped away.

Suggested prospective children:

- `NS-B2a1b1 — DR_INCREMENT_FLUX_VANISHING`
- `NS-B2a1b2 — DEFECT_MEASURE_TAIL_TIGHTNESS`
- `NS-B2a1b3 — IMPROVED_TIME_INTEGRABILITY_FOR_EQUALITY`

Candidate generation remains blocked at the parent Type-II rigidity level.

## 6. Novelty / authority

The source-to-target use of the Duchon–Robert defect is best classified as `TRANSFER_NOVEL` at most: it applies an established local-balance object to this specific Seregin Type-II limit and exposes the exact missing interface. No new Euler operator or theorem is claimed.

**Authority:** `SOURCE_BOUND_INTERFACE_DIAGNOSTIC / BOUNDED_SOURCE_AUDIT / NO_EULER_THEOREM / NO_NAVIER_STOKES_THEOREM / ROOT_AUTHORITY_NONE`.

**Artifact SHA-256:** `sha256:fe7ea09cac4920e0ff610d0a03851e5f9892baadf3dcc5c3f86b288ab8653135`
