# NS-B2a1b2 — exact Hill-vortex falsifier for the asymptotic-density bridge

**Authority:** proposal/shadow, source-bound route-pruning only. **Root:** `OPEN_NO_SOLUTION_CERTIFICATE`; independent mathematical review `0/3`.

## Frozen target

Test the successor opened by `NS-B2a1b1`: can Seregin Theorem 3.1 `F(a)=1` Euler-side nontriviality, by itself, force a strictly positive asymptotic linear kinetic-energy density

`Lambda_chi(t) = limsup_{R->infinity} R^-1 int chi_R(x)|u(x,t)|^2 dx`,

where `0 <= chi_R <= 1` is a standard expanding cutoff?

The exact root-facing source remains Seregin arXiv:2606.29468v1 Theorem 3.1: ancient Euler state, displayed scale-weighted bound (3.5), Euler equation (3.6), local-energy inequality (3.7), and unit-scale mixed-norm nontriviality (3.8). Choi arXiv:2011.06808v2 supplies Hill's exact translating Euler vortex and its explicit stream function. Prior proposal/shadow PR #219 was used only to prioritize the exact hostile world and to identify checks to repeat.

## Reverification of the hostile state

For the unit Hill profile, Choi's explicit stream function gives a bounded interior velocity and exterior decay `|V(x)| = O(|x|^-3)`, `|grad V(x)| = O(|x|^-4)`. Hence, directly,

- `V in L2(R^3) intersect L3(R^3)`;
- `grad V in L2(R^3)`.

With nonzero travel velocity `c`, set `U(x,tau)=V(x-c tau)`. Choi's traveling-wave result gives an exact nonzero Euler solution. Normalize pressure by `P=R_i R_j(U_i U_j)`; Calderon-Zygmund boundedness gives `P(tau) in L^(3/2)` uniformly because `U(tau) in L3` uniformly.

The three displayed `F(a)=1` carriers in Seregin (3.5) are finite:

1. kinetic: for `a>=1`, `a^-1 int_{B(a)}|U|^2 <= a^-1 ||V||_2^2`; for `a<=1`, boundedness gives `O(a^2)`;
2. pressure: `a^-2 int_{-a^2}^0 int_{B(a)} |P|^(3/2) <= ||P||_(3/2)^(3/2)`;
3. gradient: the moving-core occupancy estimate
   `int_{-a^2}^0 int_{B(a)} h(x-c tau) dx d tau <= (2a/|c|)||h||_1`
   with `h=|grad V|^2` yields a uniform bound after division by `a`.

The explicit traveling Euler pair satisfies (3.6). Its local Lipschitz regularity and compactly supported testing give local kinetic-energy equality, hence the one-sided interface (3.7). The profile is nonzero and therefore its unit-cylinder mixed-norm functional is strictly positive. This verifies positivity of the same nontriviality *type* as (3.8); it does not identify the value with Seregin's ancestry-specific `epsilon_0` from a hypothetical Navier-Stokes singularity.

## Exact falsifier calculation

Translation preserves total kinetic energy. Therefore, for every fixed `tau<0` and every standard cutoff satisfying `0<=chi_R<=1`,

`0 <= R^-1 int chi_R |U(tau)|^2 <= R^-1 ||V||_2^2 -> 0`.

Thus

`Lambda_chi(tau)=0`

for every time, while `U` is a permanently nonzero exact ancient Euler traveling wave satisfying the displayed `F=1` Euler-side budget and local-energy interface.

No numerics, asymptotic fitting, endpoint interpolation, pressure deletion, derivative bootstrap, or interchange of limits is used.

## Verdict

`HILL_F1_NONZERO_WITH_ZERO_ASYMPTOTIC_LINEAR_DENSITY`.

This **falsifies the bare bridge**

`positive/nonzero unit-scale Euler-side state -> Lambda_chi > 0`

inside the displayed `F=1` Euler-side class. In particular, monotonicity of `Lambda_chi` cannot become a rigidity theorem merely by combining it with qualitative local/spacetime nontriviality.

The result does **not** falsify Seregin Theorem 3.1. Hill has not been shown to lie in the image of Seregin's Navier-Stokes blow-up extraction, and the theorem's particular `epsilon_0` is ancestry-bound. A surviving quantitative bridge could still use a source-inherited relation between nontriviality, the `F=1` budget constant, and large-radius energy growth that explicitly excludes finite-energy traveling states.

## Diagnosis and residual

The failure is not local Euler mathematics: the hostile state is exact and the density limit is elementary. The failure is a local-to-global/observation-map mismatch. `Lambda_chi` has a large kernel containing every finite-energy state, so it cannot identify local nontriviality without an additional source-inherited growth/tightness/no-incoming coordinate.

The sharpened residual is:

`RES-NS-B2a1b2-SOURCE-INHERITED-NONLINEAR-DENSITY-OR-NO-INCOMING-BRIDGE`.

A next candidate must first prove or falsify one of:

- a source-inherited lower linear-energy growth condition excluding finite-energy incoming/traveling cores;
- a no-incoming-flux/tightness/recentering statement with the correct `lim_R limsup_k` quantifiers;
- a different Lyapunov observable whose zero set excludes the exact Hill world;
- a quantitative coupling from Seregin's ancestry-specific nontriviality level and budget constant to a nonzero asymptotic density.

The moving-radius compactness lane remains orthogonal. Root promotion is not attempted.
