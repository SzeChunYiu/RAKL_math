# RH-ANA-003 primary-source packet — zero-density to exclusion

Evidence cutoff: 2026-08-11. Primary literature only for proof-critical mathematical claims. Numerical work is calibration only.

## Exact target

The root contract remains the classical Riemann Hypothesis: every nontrivial zero `rho` of `zeta(s)` has `Re(rho)=1/2`. This packet studies only one child discriminator from `RH_ANA_003.yaml`: whether current zero-density and zero-free estimates can control an all-height remainder strongly enough to exclude off-critical zeros.

## Current non-explicit zero-density frontier

Larry Guth and James Maynard, **New large value estimates for Dirichlet polynomials**, *Annals of Mathematics* 203 (2026), 623–675, published online 2026-03-01. Primary page: https://annals.math.princeton.edu/2026/203-2/p06 . Author preprint: https://arxiv.org/abs/2405.20552 .

Their paper defines `N(sigma,T)` as the number of zeta zeros with `Re(rho)>=sigma` and `|Im(rho)|<=T` and obtains, after combining the new estimate with Ingham in the stated ranges,

`N(sigma,T) <= T^(30(1-sigma)/13 + o(1))`.

The proof is a genuine advance in density exponents. For the present atom, however, the decisive semantic coordinate is that for every fixed `sigma<1` the displayed exponent `30(1-sigma)/13` is strictly positive. Therefore the right side grows with `T`; it is not an occupancy-zero certificate.

## Explicit log-free density near one

Chiara Bellotti, **An explicit log-free zero density estimate for the Riemann zeta-function**, arXiv:2405.12545 (2024): https://arxiv.org/abs/2405.12545 .

Bellotti studies bounds of the form

`N(sigma,T) <= C T^(B(1-sigma))`.

For one stated uniform regime `3*10^12 < T <= exp(6.7*10^12)` and `sigma>=0.9927`, the paper gives `B=1.448`, `C=1.62*10^11`; sharper interval-dependent constants are tabulated. The paper also states explicitly that the Density Hypothesis `N(sigma,T) << T^(2(1-sigma)+epsilon)` is weaker than RH.

This source is useful as a hostile exact-constant check: even a log-free bound with a small exponent does not become an emptiness theorem merely because it is strong for prime-distribution applications.

## Explicit zero-free boundary

Michael J. Mossinghoff, Timothy S. Trudgian and Andrew Yang, **Explicit zero-free regions for the Riemann zeta-function**, arXiv:2212.06867: https://arxiv.org/abs/2212.06867 .

They prove no zeros in an explicit region adjacent to `Re(s)=1`, including a Vinogradov–Korobov form

`Re(s) >= 1 - 1/(55.241 (log|t|)^(2/3) (log log|t|)^(1/3))`

for the stated height range. The excluded strip narrows toward the line `Re(s)=1` as height increases and therefore does not cover any fixed half-strip `Re(s)>=sigma` with `sigma<1` at all sufficiently large heights.

## Rigorous finite-height calibration

Dave Platt and Tim Trudgian, **The Riemann hypothesis is true up to 3·10^12**, *Bull. Lond. Math. Soc.* 53 (2021), 792–797; arXiv:2004.09765: https://arxiv.org/abs/2004.09765 .

Using rigorous interval arithmetic, they verify that every zero with `0<gamma<=3*10^12` lies on the critical line. In this atom this may close only the bounded-height prefix. It has no authority over the infinite tail.

## Source-bound conversion question

For fixed `sigma>1/2`, an RH-closing tail theorem must exclude every later off-critical zero. Since a zero count is a nonnegative integer, a directly usable local-count upper bound must become `<1` on every block of a cover of the tail (for example every dyadic block), or supply some logically equivalent exact exclusion. A global density estimate whose upper bound grows as a positive power of `T`, or remains a positive constant, does not by itself satisfy that threshold.

This is a route diagnostic, not a theorem that zero-density machinery can never contribute to RH. A future argument could add new zero repulsion, localization, positivity, explicit-formula cancellation, or another mechanism that changes the relevant count from a growing global bound to a zero-occupancy certificate. Any such added mechanism must be stated separately and audited for RH-equivalent assumptions.