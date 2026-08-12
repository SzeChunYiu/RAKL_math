# NS-B1a3b — vorticity-geometry source-family audit

**Authority:** `PRIMARY_SOURCE_BOUND / ROUTING_AND_INTERFACE_ONLY / NO_NEW_NS_THEOREM / ROOT_AUTHORITY_NONE`  
**Bound context:** `sha256:4d62297d17027481b28283c707e69e79544c3866e82e66ff559eb8071af194b7`  
**RAKL main read before mathematics:** `8db3343dfb764c9a139f9ba76f6f44c76eaf86de`, incumbent method `3.0.0`.

## Load-bearing primary sources

### Lei–Ren–Tian: local geometric classifier

Zhen Lei, Xiao Ren, Gang Tian, *A geometric characterization of potential Navier-Stokes singularities*, arXiv:2501.08976 (2025).

Theorem 1.1 is a local suitable-weak criterion on `Q(1)`. If there are a unit vector `e`, `delta>0` and `M>0` such that every regular point satisfies either `|omega|<=M` or

`|xi x e| <= 1-delta`,  where `xi=omega/|omega|`,

then the solution is regular on the smaller cylinder. After rotation this is equivalent to the pointwise one-component domination form `|omega| <= C|omega_3|+M` on regular points.

Corollary 1.5 encodes the contrapositive geometry more sharply: their limiting high-vorticity direction set intersects every great circle on `S^2` iff the origin is singular. Corollary 1.6 gives another local regularity criterion when pairwise vorticity directions remain uniformly separated from orthogonality.

The proof mechanism is not a generic compactness theorem for `xi`. It controls a local absolute-vorticity flux, derives scale-critical Type-I estimates, performs a blow-up, and obtains local decay of that flux for the limiting ancient solution by a De Giorgi argument. This distinction is load-bearing for the present interface audit.

### Albritton–Barker: Type-I producer

Dallas Albritton, Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502 / J. Math. Fluid Mech. 21 (2019), 43.

The source binds a local Type-I singularity to a nontrivial mild bounded ancient solution satisfying finite Type-I control. The previously audited compactness passage used to extract the suitable-weak limit is velocity-strong locally (`L^3` on fixed cylinders after subsequence) with pressure weak locally (`L^{3/2}`), plus local-energy bounds. That output is adequate to pass the velocity nonlinearity and suitable-weak structure; it is not, by itself, a strong compactness statement for `curl u` or for the normalized direction `curl u/|curl u|`.

The Albritton–Barker Liouville theorem based on a backward global-`L^3` sequence remains a separate global consumer. The selected geometry route does not use it.

## Analogue family, not load-bearing transfer

Yoshikazu Giga and Hideyuki Miura, *On vorticity directions near singularities for the Navier-Stokes flows with infinite energy*, Hokkaido University Preprint 956 (2010), later Commun. Math. Phys. 303 (2011). The institutional source abstract states a non-blow-up criterion under a Type-I restriction plus uniform continuity of the vorticity direction where vorticity is large. This confirms the geometry family but supplies an **extra continuity hypothesis**, not an implication from generic finite-I compactness.

Zoran Grujic, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866 (submitted 9 July 2026). Its stated mechanism assumes critical-point singularities with `L^{3/2,infinity}` spatial concentration of vorticity together with local weighted-BMO control of the vorticity direction. Those are additional structural hypotheses, so this very recent route is retained as an orthogonal frontier analogue rather than glued to the active fibre.

## Exact producer / consumer mismatch to test

Producer available from the registered Type-I compactness package:

`u_n -> u strongly in L3_loc`, with local-energy bounds and only weak derivative control absent a stronger theorem.

Geometry consumers require information such as:

`xi_n = curl(u_n)/|curl(u_n)|` lying in a fixed cone on high-vorticity sets, pairwise directional coherence, or another vorticity-direction regularity class.

The map `u -> curl(u)/|curl(u)|` is derivative-taking followed by singular normalization at zero. No cited source licenses continuity of this map under strong `L3_loc` convergence of velocity.

## Adversarial topology calibration

For the smooth divergence-free fields

`u_n(x) = (0, n^{-1} sin(n x_1), 0)`,

one has `u_n -> 0` strongly in `L3_loc`, while

`curl u_n = (0,0,cos(n x_1))`.

Away from its zeros the vorticity direction alternates between `+e_3` and `-e_3` at frequency `n`. Thus the bare topology implication

`strong L3_loc velocity convergence => convergence/stability of vorticity directions`

is false even for smooth divergence-free fields. This is **not** a Navier–Stokes counterexample and says nothing about whether the PDE plus additional estimates can suppress such oscillation. Its sole role is to force any valid inheritance proof to name and use an equation-specific derivative/direction compactness input.

## Source-family disposition

- `SELECT`: Lei–Ren–Tian double-cone and great-circle results as exact local geometry consumers/classifiers.
- `SELECT`: Albritton–Barker compactness as the exact producer topology.
- `DEFER`: Giga–Miura until an exact inherited uniform-continuity hypothesis is proved or theorem text is needed for a candidate.
- `DEFER`: Grujic 2026 until the active fibre independently produces its concentration and weighted-BMO hypotheses.
- `REJECT AS SHORTCUT`: transporting `xi` from velocity `L3_loc` compactness without a derivative-level certificate.
- `REJECT AS SHORTCUT`: reintroducing global-`L3`, far-field pressure, backward uniqueness or stationary Leray-profile assumptions into this local geometry theorem merely to close the interface.

No source in this audit proves that finite Type-I control itself imposes a vorticity-direction cone, coherence modulus, or weighted-BMO condition. The next calculation must therefore audit the transport interface rather than assume it.
