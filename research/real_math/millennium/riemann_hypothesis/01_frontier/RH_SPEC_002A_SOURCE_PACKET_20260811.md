# RH-SPEC-002a source packet — ground-state identification / determinant compactness

**Authority:** source/context packet only. No theorem candidate, no RH evidence, no novelty claim, no root authority.

## Exact source-side residual

The current spectral lane does not need another finite self-adjoint operator. It needs a theorem-quality bridge from the **actual Weil-form ground state** to the already-defined prolate proxy whose transform has the desired Xi limit.

The primary source is Alain Connes, Caterina Consani and Henri Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755v1 (2025).

### What is already rigorous in the source

- `QW_lambda` is treated as a lower-bounded lower-semicontinuous quadratic form; its finite restrictions `QW_lambda^N` live on the Fourier cutoff spaces `E_N`.
- Under the explicit assumption that the smallest eigenvalue of `QW_lambda^N` is simple and its eigenvector is even, Theorem 5.10 constructs the self-adjoint `D_log^(lambda,N)`.
- With the source normalization `delta_N(xi)=1`, the regularized determinant is

  `det_reg(D_log^(lambda,N)-z) = -i lambda^(-iz) \hat xi(z)`.

  The Fourier transform `\hat xi` is entire, all of its zeros are real, and those zeros coincide with the finite/restricted operator spectrum.
- Section 7 constructs a prolate-derived proxy `k_lambda = E(h_lambda)` and proves that `\hat k_lambda` converges to the Riemann Xi function uniformly on every closed substrip of the open strip `|Im z| < 1/2`.

These statements do **not** prove that the true Weil-form ground state has the same limit.

### What the source itself says is missing

Section 8 explicitly isolates two essential missing steps:

1. prove that the smallest eigenvalue of `QW_lambda` is simple and that its corresponding eigenvector `xi_lambda` is even;
2. prove that `k_lambda` approximates a scalar multiple of `xi_lambda` accurately enough to justify convergence of the zeros of `\hat xi_lambda` to the nontrivial zeta zeros.

The paper calls rigorous justification of the `k_lambda` versus `xi_lambda` comparison the main remaining obstacle in its approach. The numerical proximity and the similarity between small Weil eigenvalues and prolate concentration defects are indications only.

## Atomic decomposition used in this cycle

`RH-SPEC-002a` separates six non-compensatory obligations:

1. **GS-SIMPLE-EVEN** — prove or replace simple/even ground-state structure for `QW_lambda` on the intended cofinal family.
2. **N-TRUNCATION** — justify `xi_(lambda,N) -> xi_lambda` at fixed `lambda`, including normalization compatibility.
3. **PROXY-STABILITY** — prove a quantitative relation between the true Weil ground state and the prolate proxy.
4. **TRANSFORM-CONTROL** — show the source-space estimate is strong enough to imply compact-uniform Fourier/Mellin convergence on a root-relevant complex domain.
5. **NORMALIZATION** — freeze the scalar/phase convention independently of known zeta zeros; do not hide a zero-free factor in post-hoc fitting.
6. **COFINAL-LIMIT** — state the `N`/`lambda` limit order or prove the uniformity needed for path independence.

The present cycle selects **PROXY-STABILITY** as the next discriminator but keeps all five dependencies explicit.

## New structural coordinate: residual divided by spectral separation

A key method-transfer lesson from isolated-eigenvalue perturbation theory is that a small approximate-eigenvector error does not by itself identify an eigendirection. The stability denominator is the separation from competing eigenmodes.

For the next calibration, the source-side quantities should be organized before theorem invention around symbols such as:

- `g_lambda`: the gap from the lowest relevant even-sector eigenvalue of the self-adjoint operator associated with `QW_lambda` to the next spectral point in that sector;
- `r_lambda`: a source-computable operator residual or a rigorously justified form/Rayleigh excess of the normalized prolate proxy.

This packet does **not** assert a bound such as `dist(k_lambda, xi_lambda) <= r_lambda/g_lambda`; the exact theorem statement and hypotheses must be frozen only after the current strict packet passes. The point of the coordinate is to prevent the invalid inference “tiny energy/proxy discrepancy ⇒ ground-state identification” when `g_lambda` may be equally tiny or smaller.

## Cheap hostile calibration exposed by the expert cell

Before applying any source-specific perturbation statement, use a two-mode self-adjoint family with a collapsing ground-state separation to check that the proposed certificate refuses to infer vector convergence from a vanishing absolute residual alone. This is a conditioning calibration, not an RH counterexample.

A valid source theorem must then replace the toy denominator with a proved `QW_lambda` spectral-separation statement or a different uniqueness/compactness mechanism.

## Other primary/authoritative anchors

- Alain Connes and Walter D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, Commun. Math. Phys. 406:312 (2025), arXiv:2511.23257 — general quadratic-form/simple-ground-state real-zero mechanism; not a zeta-globalization theorem.
- Tosio Kato, *Perturbation Theory for Linear Operators* — isolated spectral subspace/eigenvalue perturbation background; transfer requires source-domain and gap hypotheses.
- Current RAKL framework at `SzeChunYiu/RAKL` is the assurance authority; this application packet creates no framework authority.

## Explicit exclusions

- no use of low-zero numerical accuracy as proof of convergence;
- no inference from a small lowest eigenvalue to a ground-state gap;
- no unspecified `N,lambda -> infinity` notation as a proof step;
- no de Branges/canonical-system transfer without constructing a source object satisfying the relevant hypotheses;
- no GUE/random-matrix statistics as determinant identification;
- no post-hoc normalization using known zeta zeros;
- no root inference from the retrospective RH-SPEC-002 calibration.

**Current root:** `OPEN_NO_SOLUTION_CERTIFICATE`.
