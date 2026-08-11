# YM-S1a2-C001-v2 — Positive-beta OS/SZZ fixed-lattice transfer-spectrum composition

**Supersedes:** `YM-S1A2-C001-POSITIVE-BETA-OS-SZZ-FIXED-A-TRANSFER-GAP` (preserved V1; Git blob `5c3fd477ae8c2c6c681eb9b2e7e60cc59358110f`)  
**Atom:** `YM-S1a2`  
**Context:** `sha256:89ee3e1d735f6b3e5be46a2acfa1914da01ac3dce52227f2d83cf9d3832f7144`  
**Authority:** `SCOPED_DERIVATION_RESULT / FIXED_LATTICE_ONLY / SAME_CONTEXT_REVIEW_ONLY / NO_NOVELTY / ROOT_AUTHORITY_NONE`

## Scoped theorem candidate

Consider four-dimensional Wilson lattice Yang–Mills theory with gauge group `SU(N)` and

`0 < beta < 1/48`,

inside Shen–Zhu–Zhu Assumption 1.1 for `d=4`. Let `mu=mu^ym_{N,beta}` be the unique infinite-volume measure from their Theorem 1.2. Choose one lattice direction as Euclidean time.

For the physical Osterwalder–Schrader reconstruction of the gauge-invariant positive-time local algebra, let `Omega=[1]` and let `T` denote one-step Euclidean-time translation. Then the exact source-bound composition below yields

`T >= 0`, `T=T*`, `||T||<=1`, and

`Spec(T | Omega^perp) subset [0, exp(-c_N)]`,

where `c_N>0` is the common covariance exponent of Shen–Zhu–Zhu Corollary 1.6 for this `N,beta,d=4`.

This is a **fixed-lattice physical transfer-spectrum gap** in the strong-coupling `SU(N)` theory. If, in addition, this reconstructed one-step operator is independently identified as an injective `T=exp(-aH_a)` for a self-adjoint lattice Hamiltonian at physical spacing `a`, then spectral mapping gives the conditional bound

`Spec(H_a | Omega^perp) subset [c_N/a, infinity)`.

The transfer-spectrum statement does not depend on the extra injective-logarithm clause.

## Derivation

### 1. Exact infinite-volume measure

SZZ Theorem 1.2 proves that the whole sequence of finite-volume periodic Wilson measures converges to one infinite-volume measure `mu`. Thus any fixed local observable has the same limit along every reflection-compatible even-volume subsequence.

### 2. Reflection positivity survives the local weak limit

For each fixed gauge-invariant positive-time local polynomial/smooth-cylinder source `F`, finite-volume Wilson physical positivity gives

`E_{mu_L}[overline{F(theta Q)}F(Q)] >= 0`.

The integrand is bounded, continuous and local on the compact link-variable space. Passing along a sufficiently large even-volume subsequence and using SZZ convergence gives the same inequality under `mu`. Quotienting null vectors and completing therefore defines the infinite-volume OS Hilbert space.

This uses positive Wilson coupling only. V2 makes no negative-beta claim.

### 3. One-step operator positivity also survives locally

The parent spectral lemma requires a **positive** operator, not merely a self-adjoint one. This is a separate handoff from the OS norm form.

In the finite-volume Lüscher reconstruction, one-step Euclidean translation is represented by a self-adjoint strictly positive transfer matrix `T_L`. Therefore for every fixed local positive-time source image,

`<[F],T_L[F]>_L >= 0`.

By the Euclidean reconstruction identity this matrix element is a bounded local reflected/one-step-translated expectation. Passing that expectation through the same SZZ local weak limit yields

`<[F],T[F]>_mu >= 0`

for the dense local source images in the infinite-volume OS space. Continuity of the bounded time-shift operator extends the quadratic-form inequality to all vectors, hence `T>=0`. Time-translation invariance and OS reflection give self-adjoint contraction semantics.

No strong-operator convergence `T_L -> T` is assumed.

### 4. Dense centered source class is already inside SZZ's class

The OS physical Hilbert space is the null quotient/completion of the gauge-invariant positive-time local algebra, so its local source images have dense span by construction. Gauge-invariant local polynomials and Wilson-loop functions are smooth cylinder functions of finitely many compact-group edge variables and hence are included in SZZ's larger `C^infty_cyl(Q)` class.

Center the source vector by

`psi_F=[F]-<Omega,[F]>Omega`.

The bounded projection onto `Omega^perp` maps the dense source span to a dense span in `Omega^perp`. Thus the registered hidden-source failure cannot occur inside this chosen OS generating family.

### 5. Exact covariance-to-transfer moment

For a fixed centered real/self-adjoint local source and sufficiently large integer translation `n`, OS reconstruction identifies

`<psi_F,T^n psi_F>`

with the reflected Euclidean connected two-point function, i.e. the covariance of the reflected source and its translated copy. The temporal support width of a fixed `F` changes the nearest-support distance only by a source-dependent additive constant:

`d(Lambda_{theta F},Lambda_{tau_nF}) = n + O_F(1)`.

Because `T>=0`, these diagonal moments are nonnegative.

### 6. SZZ supplies the required common q

SZZ Corollary 1.6 gives, for disjoint smooth-cylinder supports,

`Cov_mu(f,g) <= C(f,g) exp(-c_N d(Lambda_f,Lambda_g))`,

with one `c_N>0` depending on `K_S,N,d` but not on source identity. Applying the bound to the reflected/translated centered OS sources gives

`0 <= <psi_F,T^n psi_F> <= C_F exp(-c_N(n-O_F(1)))`.

Therefore, for every source in the dense centered generating family,

`limsup_n <psi_F,T^n psi_F>^(1/n) <= q := exp(-c_N) < 1`.

The source-dependent prefactor and additive distance offset disappear under nth roots. The same `q` applies to every source.

### 7. Full excited transfer-spectrum exclusion

`YM-S1a1-C001-v2` proves that a positive self-adjoint contraction with vacuum eigenvalue one and a dense excited source family satisfying one common nth-root rate `q<1` has

`Spec(T|Omega^perp) subset [0,q]`.

Substituting `q=exp(-c_N)` yields the theorem.

## Hostile controls retained

- **incomplete sources:** the exact three-state hidden-mode world refutes full-gap inference without density;
- **nonuniform rates:** dense `q_k<1` with `q_k->1` refute sourcewise-only decay;
- **wrong generator:** SZZ Langevin Poincaré/log-Sobolev gaps are not substituted for the physical transfer spectrum;
- **negative beta:** excluded from this reflection-positive route;
- **beta=0:** excluded from the ordinary finite-energy Hamiltonian interpretation after V1 review;
- **continuum overreach:** no inference across the strong-to-weak or `a->0` interfaces.

## Exact remaining Yang–Mills obligations

This local composition closes only the `YM-S1a2` same-theory fixed-cutoff/infinite-volume source-to-transfer interface for the stated `SU(N)` strong-coupling scope. It leaves:

- `G5`: a rigorous route from the controlled strong-coupling lattice region toward the asymptotically-free continuum trajectory while retaining a useful spectral statement;
- `G6`: the physical lattice-spacing dependence needed for a nonzero dimensionful lower bound as `a->0`;
- `G7`: continuum reconstruction and identification of the limiting physical spectrum;
- continuum existence/nontriviality and all other Clay axioms;
- extension from this `SU(N)` scope to the official all-compact-simple-group statement.

## Novelty / authority

All mathematical ingredients are source-bound or previously registered and the new work is an explicit composition plus scope repair. The defensible ancestry label is

`PROVISIONAL_RAKL_TRIVIAL`.

No bounded novelty search, formal proof assistant check, independent mathematical review, continuum theorem, or root certificate exists. The Clay Yang–Mills issue remains `OPEN_NO_SOLUTION_CERTIFICATE`.