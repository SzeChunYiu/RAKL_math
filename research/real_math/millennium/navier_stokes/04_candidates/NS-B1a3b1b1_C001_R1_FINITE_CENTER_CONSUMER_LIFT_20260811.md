# NS-B1a3b1b1 C001 — finite-center lift of the logarithmic commutator consumer

Authority: `SCOPED_ANALYTIC_CONTEXT_LIFT / PROPOSAL_SHADOW / NO_ROOT_AUTHORITY`.

## Scoped proposition

Fix `p=3/2`. Assume the unchanged global hypotheses used in Grujić arXiv:2607.08866v2 Theorem 4.1, namely uniform-in-time vorticity control in `L^{3/2,infinity}(R^3)` and uniform-in-time vorticity-direction control in `bmo_{1/|log r|}`. Suppose that for all sufficiently large `lambda` and relevant times,

`A_lambda(t) subset union_{j=1}^{N(t,lambda)} B(x_j(t,lambda), R_j(t,lambda))`,

with `N(t,lambda) <= N0 < infinity` and `R_j(t,lambda) <= C lambda^-1/2`, where `N0,C` are time- and lambda-independent.

Then the localized commutator proof underlying Theorem 4.1 and the finite-union weak-Lorentz inequality give, for sufficiently large `lambda`,

`||alpha(.,t)||_{L^{3/2,infinity}(A_lambda(t))} <= C1 N0^(2/3) / log lambda`,

where `C1` depends on the same global norm suprema, fixed geometric constants and `C`, but not on `t` or `lambda`. Consequently the nonlinear stretching term in equations (23)-(25) is eventually absorbed by viscosity after increasing the truncation threshold by a fixed amount depending on `N0`. Thus **one-center containment is stronger than required at this specific restricted-Lorentz/De Giorgi interface**; a uniformly bounded finite-center cover suffices.

This is not a generalization of the full paper and not a theorem that finite-`I` Type-I solutions possess such a cover.

## Step 1 — translated local commutator estimate

Grujić Theorem 4.1 is stated for a ball centered at the critical point, taken to be the origin. Inspecting its proof shows that its analytic localized estimate is translation-covariant. For a ball `B(x0,R)`, translate coordinates by `z=x-x0`. The near-field cutoff becomes `B(x0,2R)`, local BMO means translate, the Calderón–Zygmund kernel depends on differences, and the global weak-Lorentz and `bmo_phi` norms are translation invariant. The same argument therefore gives

`||alpha||_{L^{3/2,infinity}(B(x0,R))} <= C0/|log R|`

with the same uniform `C0`, provided `R` is sufficiently small.

No producer or critical-profile statement is inferred from translation covariance; this is only a local estimate extracted from the source proof.

## Step 2 — finite-union weak-Lorentz bound

Use the standard distribution quasi-norm

`||f||_{p,infinity,dist} = sup_{s>0} s |{|f|>s}|^(1/p)`,

which is the standard weak-`L^p` form equivalent to the rearrangement convention. Let `E_j=B(x_j,R_j)` and `E=union_j E_j`. If each restriction obeys `||alpha 1_{E_j}||_{p,infinity,dist} <= A_j`, then for every `s>0`,

`|{x in E: |alpha(x)|>s}| <= sum_j |{x in E_j: |alpha(x)|>s}| <= s^-p sum_j A_j^p`.

Therefore

`||alpha 1_E||_{p,infinity,dist} <= (sum_j A_j^p)^(1/p) <= N^(1/p) max_j A_j`.

At `p=3/2`, `1/p=2/3`. With `A_j <= C0/|log R_j|` and `R_j <= C lambda^-1/2`, for sufficiently large `lambda` monotonicity of `1/|log r|` on small scales gives

`max_j A_j <= C2/log lambda`.

Since `A_lambda subset E` and `N<=N0`,

`||alpha||_{L^{3/2,infinity}(A_lambda)} <= C3 N0^(2/3)/log lambda`.

All fixed norm-convention equivalence factors are absorbed into `C3`.

## Step 3 — absorption in the source energy inequality

Grujić equation (24) gives

`integral_{A_lambda} alpha omega_lambda^2 <= ||alpha||_{L^{3/2,infinity}(A_lambda)} ||omega_lambda||_{L^{6,2}}^2`.

The Lorentz-Sobolev estimate bounds the second factor by `C_S^2 ||grad omega_lambda||_2^2`. Thus it suffices that

`C_S^2 C3 N0^(2/3)/log lambda <= nu/2`.

For fixed `N0`, the left side tends to zero as `lambda -> infinity`, so a time-independent truncation level exists. The one-center argument of source equation (25) is therefore replaced, at this interface, by the finite-cover inequality above.

The linear-source estimate in source equation (27) begins with the same restricted `alpha` norm. Replacing `2C0/log lambda` by `C3 N0^(2/3)/log lambda` changes fixed constants (after Young's inequality the multiplicity dependence is correspondingly raised) but preserves the logarithmic asymptotic through the displayed energy inequality. This observation is scoped to that energy segment; later geometric inversion/harmonic-measure stages are not promoted by this file.

## Counterexample-first multiplicity audit

An `N`-independent union constant is not admissible. Take `N` disjoint translated copies of a fixed weak-`L^p` profile at equal strength. Their distribution functions add on levels where the copies share the same distribution, producing the `N^(1/p)` scaling. Hence the safe multiplicity loss at `p=3/2` is `N^(2/3)` up to norm-convention constants.

If the number of balls is allowed to depend on threshold, `N=N(lambda)`, fixed-multiplicity reasoning fails. A sufficient condition for the same absorption mechanism is

`N(lambda)^(2/3)/log lambda -> 0`.

No such growth bound is supplied here by Navier–Stokes dynamics.

## Producer and gluing residuals

### Local mathematical residual

The scoped consumer lemma is closed at the restricted-Lorentz interface, but no equation-specific theorem has been proved that maps Albritton–Barker finite `I` to:

- a bounded-multiplicity `O(lambda^-1/2)` cover of high-vorticity sets;
- global uniform vorticity `L^{3/2,infinity}`;
- global uniform direction `bmo_{1/|log r|}`.

### Local-to-global / state-space gluing residual

A local blow-up/ancient object must still glue to the same pre-singularity theory and to the global Lorentz/far-field hypotheses consumed by the commutator proof. Moving centers, secondary profiles, far-field strain, pressure/local-energy compactness, and the ancient-versus-pre-singularity interface remain separate obligations.

Barker arXiv:2111.14776v2 gives a finite-singular-point result under a different global velocity `L^{3,infinity}` hypothesis. Its DifferenceWitness prevents direct theorem transfer; it is only a structural hint that a bounded-multiplicity PDE target is less rigid than unique-core selection.

## Outcome

`PARTIAL_SUCCESS / SCOPED_CONTEXT_LIFT`.

Residual before: continuation of the selected consumer appeared to require an equation-specific **unique one-center** morphology producer.

Residual after: unique-center selection is not required for the localized commutator/De Giorgi restricted-norm interface. The morphology obligation is narrowed to a **bounded-multiplicity shrinking cover**, while the amplitude, direction, producer and state-space gluing obligations remain open.

Novelty classification: `REPRESENTATION_NOVEL_SHADOW` (RAKL case-study class only; no claim of novelty in the mathematical literature).
