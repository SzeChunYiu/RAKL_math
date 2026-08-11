# RH-SPEC-002a source packet — Weil ground-state / prolate-proxy transfer

Date: 2026-08-11. Authority: `PRIMARY_SOURCE_CONTEXT / PRE_CANDIDATE / NO_MATHEMATICAL_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`.

## Refined atomic obstruction

The parent `RH-SPEC-002` calibration showed that generic operator convergence, finite zero prefixes and unspecified joint cutoffs are not sufficient global spectral certificates. This child narrows the next source-side question to the specific Connes–Consani–Moscovici (CCM) route.

`RH-SPEC-002a` asks: **what quantitative, source-defined approximation of the semilocal Weil-form lowest eigenvector `xi_lambda` by a scalar multiple of the explicit prolate proxy `k_lambda` is sufficient to make their Fourier/Mellin transforms converge uniformly on every closed substrip of `|Im z|<1/2`, without fitting the scalar to known zeta zeros?**

The finite-`N` to semilocal limit and the simple/even ground-state requirement remain separate dependencies. This packet does not combine them into a fictitious solved bridge.

## S1 — finite-parameter spectral theorem

**Alain Connes, Caterina Consani, Henri Moscovici, _Zeta Spectral Triples_, arXiv:2511.22755 (2025).**

Theorem 1.1 assumes the smallest eigenvalue of the finite restriction of the Weil quadratic form is simple and its eigenvector is even. Under those hypotheses the paper constructs a self-adjoint rank-one perturbation, identifies its regularized determinant with a scalar/exponential factor times the Fourier transform of that eigenvector, and proves that this entire Fourier transform has only real zeros equal to the approximant spectrum.

**Bound obligation:** finite-stage real-rootedness is conditional on exact source hypotheses. It cannot be inferred from numerical spectra.

## S2 — the target convergence domain is smaller than the whole plane

In Section 7 CCM write the Riemann function in the spectral variable as `Xi(z)=xi(1/2+i z)` and describe the desired determinant limit. The paper states that suitably normalized determinant/ground-state transforms converging toward `Xi` on closed substrips of the open strip `|Im z|<1/2` would entail RH by Hurwitz.

This matters for research economy: the parent calibration used full-plane local-uniform entire convergence as a clean generic sufficient condition. For this source route, **full-plane convergence is stronger than the root requires**. The fresh child must therefore freeze the minimal root-relevant strip rather than inherit a stronger target by inertia.

## S3 — the proxy side of the lambda limit is already rigorous

CCM define an explicit prolate-wave proxy `k_lambda=E(h_lambda)`. Their Lemma 7.2 gives uniform `O(lambda^-2)` approximation of the relevant low prolate modes to the Hermite combination used for Riemann `Xi`. Lemma 7.3 then proves that the Fourier transform of `k_lambda` converges to `Xi` uniformly on every closed substrip of `|Im z|<1/2` as `lambda -> infinity`.

**Bound obligation:** this proves the target transform limit for the proxy `k_lambda`, not for the actual semilocal Weil-form ground state `xi_lambda`.

## S4 — the source itself identifies the missing bridge

Section 8 explicitly lists two essential missing steps for the tentative route:

1. prove that the smallest eigenvalue of the semilocal Weil operator `QW_lambda` is simple and its eigenvector `xi_lambda` is even;
2. prove that `k_lambda` is a sufficiently accurate approximation to a scalar multiple of `xi_lambda` to justify convergence of the zeros of the Fourier transform of `xi_lambda` toward the nontrivial zeta zeros.

The paper describes numerical evidence for the proximity of the two states, but does not promote it to a theorem.

**Bound obligation:** `RH-SPEC-002a` attacks only the second item. The simple/even question stays visible as a sibling dependency.

## S5 — finite-N and lambda limits must not be collapsed

Earlier in Section 7 CCM describe, as part of the proposed strategy, a fixed-`lambda` `N -> infinity` passage from finite-dimensional regularized determinants toward the transform of the semilocal ground state `xi_lambda`, followed by a `lambda -> infinity` passage toward `Xi`.

The parent calibration already demonstrated that a phrase such as `N,lambda -> infinity` is not a mathematical limit by itself. This child therefore treats the `lambda`-stage ground-state/proxy bridge separately. Success here would not discharge finite-`N` spectral/determinant convergence.

## S6 — quantitative eigenvector stability is the likely hidden coordinate

A generic self-adjoint perturbation lesson is relevant only as a method-transfer question: small eigenvalue or residual error need not imply a small eigenvector angle if the distinguished eigenvalue is nearly degenerate. Thus, if the QW/prolate relation is used perturbatively, qualitative simplicity alone is not enough; a quantitative spectral-separation or alternative rigidity mechanism must enter the argument.

This is **not** a claim that the QW ground-state gap vanishes. It is a falsifier-design obligation: expose the separation coordinate before treating small numerical residuals as vector convergence.

## S7 — transform topology must match the root domain

For a Fourier transform in logarithmic coordinate `x`, evaluation at complex `z=t+i eta` weights the integrand by an exponential factor depending on `eta`. Therefore a future candidate should not say merely “`xi_lambda` is close to `k_lambda` in `L2`.” It must identify a source-controlled error norm whose continuity estimate really yields uniform transform error on each closed substrip `|Im z|<=1/2-delta`.

A weighted-`L1` style estimate is an obvious *calibration target* because the triangle inequality directly controls a complex Fourier transform on a fixed strip. Whether the actual QW/prolate machinery can prove such a bound is open and is precisely the point of the next discriminator.

## Expert-cell disposition

The same-context cell used for this atom is deliberately role-separated but not independent:

- **analytic-number-theory / Weil-form lead:** binds `Xi(z)=xi(1/2+iz)`, prime/archimedean source identity and the minimal root-relevant strip;
- **functional-analysis lead:** owns lowest-eigenvalue simplicity, spectral separation, eigenvector stability and finite-`N`/semilocal distinctions;
- **complex-analysis lead:** owns the exact transform topology and domain-local Hurwitz/Rouché implications;
- **prolate / harmonic-analysis lead:** owns the `PW_lambda -> h_lambda -> k_lambda` proxy chain and what is actually proved;
- **adversarial reviewer:** searches for small-residual/large-angle, growing-domain norm-loss and normalization counterexamples;
- **formal/novelty reviewer:** keeps this atom source-bound, preserves all siblings and blocks any claim that restates CCM's missing step as a new theorem.

## Immediate pre-candidate discriminator

Before any theorem candidate, freeze a **norm-and-gap obligation matrix** with three branches:

1. `DIRECT_TRANSFORM`: identify a source-side weighted error functional that directly upper-bounds `sup_K |hat(xi_lambda)-c_lambda hat(k_lambda)|` on each closed substrip;
2. `EIGENVECTOR_STABILITY`: derive ground-state alignment from an exact QW/prolate residual plus a quantitative separation/rigidity estimate;
3. `FALSIFIER`: construct the cheapest structurally matched example showing that the currently available residual/proximity diagnostic can be small while normalized transform error remains order one.

The result of that discriminator will decide whether candidate generation should proceed. Root status remains `OPEN_NO_SOLUTION_CERTIFICATE`.
