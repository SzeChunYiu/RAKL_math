# NS-B1a3b — vorticity-geometry source audit

**Observed:** 2026-08-11  
**Authority:** `PRIMARY_SOURCE_BINDING / PROPOSAL_SHADOW_SEARCH_CONTROL / NO_ROOT_AUTHORITY`

## 1. Albritton–Barker finite-`I` lane

Primary source: Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, `arXiv:1811.00502`, https://arxiv.org/abs/1811.00502.

Bound use in this repository: the active `NS-B1` route uses their equivalence between a registered local Type-I singularity and a nontrivial mild bounded ancient solution satisfying the source Type-I decay/finite-`I` package. This is the source of the `A+C+D+E` information class being audited here.

Transfer boundary: their finite-`I` ancient class is the **input class**. No vorticity-direction modulus or weighted-BMO bound is asserted by this source.

## 2. Giga–Miura direction criterion

Primary source: Yoshikazu Giga and Hideyuki Miura, *On vorticity directions near singularities for the Navier-Stokes flows with infinite energy*, Hokkaido University Preprint Series in Mathematics 956 (2010), published in *Communications in Mathematical Physics* 303 (2011), 289–300, DOI `10.1007/s00220-011-1197-x`; institutional version https://doi.org/10.14943/84103.

Exact theorem calibration from Theorem 1.1 of the institutional version: for a mild solution on `R^3 x (-1,0)` satisfying their Type-I pointwise growth condition `||u||_infinity(t) <= C_0 (-t)^(-1/2)`, if for some `d>0` a common modulus `eta` controls `|zeta(x,t)-zeta(y,t)|` for all points in the high-vorticity region `Omega_d(t)={|omega|>d}`, then the solution does not blow up at `t=0`.

Important DifferenceWitness against the present finite-`I` ancient lane:

- Giga–Miura's registered Type-I hypothesis is a pointwise `L^infinity_x` self-similar growth bound for the original near-blow-up mild solution.
- The current atom starts from the Albritton–Barker finite-`I` ancient information package.
- No direct equivalence between those two hypothesis packages is imported here.

Therefore Giga–Miura is used in `NS-B1a3b-C001` as a **positive geometric-coordinate calibration**: a uniform direction modulus is known to be powerful in a Type-I setting, but it is not silently treated as a Liouville theorem for every finite-`I` ancient solution.

## 3. Grujic 2026 logarithmic-depletion preprint

Primary source: Zoran Grujic, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, `arXiv:2607.08866v2`, submitted 2026-07-09 and revised 2026-07-13, https://arxiv.org/abs/2607.08866.

Exact source coordinates used:

- Definition 2.1 restricts attention to a **critical point singularity** with vorticity magnitude locally scaling like `O(|x|^-2)`, factored as `omega=Phi |x|^-2`, with bounded shape factor and associated high-vorticity superlevel localization at radius `O(lambda^-1/2)`.
- Section 2.3 defines local `bmo_phi` with `phi(r)=1/|log r|` through weighted mean oscillation.
- Theorem 4.1 assumes the critical concentration profile uniformly in time, `omega in L^infinity_t L^{3/2,infinity}_x`, and `xi in L^infinity_t bmo_phi`, and derives a logarithmically decaying localized Lorentz norm for the stretching eigenvalue.

Status boundary: this is a July 2026 arXiv preprint. The present cycle does not independently certify its full proof and does not use it for Clay-root theorem authority. It is used as a current primary-source target exposing a substantially weaker direction-coherence coordinate than uniform continuity.

DifferenceWitness against the present finite-`I` ancient lane:

1. generic finite `I` does not, by the current source contract, imply the critical-point profile `omega=Phi |x|^-2` or its superlevel-set localization;
2. generic finite `I` does not, by the hostile calibration `NS-B1a3b-C001`, imply a uniform `bmo_{1/|log r|}` bound for the vorticity direction;
3. the preprint's theorem is therefore not directly glueable onto the Albritton–Barker finite-`I` ancient class without at least two new inheritance results.

## Negative-history consequence

The source audit rules out two unsafe shortcuts:

- `finite I -> Giga–Miura theorem` without reconciling the distinct Type-I hypothesis packages;
- `finite I -> Grujic 2026 theorem` without proving both the critical-point concentration scenario and the weighted-BMO direction hypothesis.

These are source/transfer interface blocks. They are separate from the local functional derivative-gap obstruction proved by the rotating-vector-potential hostile family.
