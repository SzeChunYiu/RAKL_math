# YM-S1a2-C001 — Positive-beta OS/SZZ fixed-lattice transfer-gap composition

**Atom:** `YM-S1a2`  
**Candidate ID:** `YM-S1A2-C001-POSITIVE-BETA-OS-SZZ-FIXED-A-TRANSFER-GAP`  
**Context:** `sha256:89ee3e1d735f6b3e5be46a2acfa1914da01ac3dce52227f2d83cf9d3832f7144`  
**Strict pre-candidate trace head:** `sha256:2bfe124fa78fdd004e7cb72a0647067e14c0e978feb7f3828f9e81f19696440b`  
**Authority:** `SCOPED_COMPOSITION_CANDIDATE / FIXED_LATTICE_ONLY / SAME_CONTEXT_CHECK_REQUIRED / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

## Statement

Fix four-dimensional Wilson lattice Yang–Mills theory with gauge group `SU(N)` and positive inverse-coupling parameter

`0 <= beta < 1/48`,

so that Shen–Zhu–Zhu Assumption 1.1 holds for `d=4`. Let `mu = mu^ym_{N,beta}` be their unique infinite-volume measure on the lattice with unit lattice spacing, and choose one coordinate as Euclidean time.

Let `A_+` be the gauge-invariant local polynomial/smooth-cylinder algebra supported at positive Euclidean times. Reconstruct the Osterwalder–Schrader Hilbert space `H_OS` from `A_+`, with vacuum `Omega=[1]`, and let `T` be one-step positive Euclidean-time translation on that reconstructed physical space.

Then, under the standard Wilson reflection-positive finite-volume realization used in the OS/Lüscher construction,

`Spec(T | Omega^perp) subset [0, exp(-c_N)]`,

where `c_N>0` is the source-independent exponential covariance rate in Shen–Zhu–Zhu Corollary 1.6 for the same `N,beta,d=4`.

Consequently, for physical lattice spacing `a>0`, the fixed-cutoff Hamiltonian `H_a = -(1/a) log T` has excited spectrum bounded below by

`c_N/a`.

This is **not** a continuum Yang–Mills mass-gap theorem. It is a fixed-lattice-spacing, strong-coupling, `SU(N)` transfer-spectrum consequence. `G5` strong-to-weak/RG transport, `G6` physical `a`-scaling, `G7` continuum spectral identification, continuum existence/nontriviality, and the Clay root all remain open.

## Proof decomposition

### Step 1 — finite-volume reflection positivity passes to the exact SZZ limit

For positive Wilson coupling, the standard Wilson lattice action is reflection positive on gauge-invariant positive-time observables. Lüscher constructs the corresponding positive transfer matrix explicitly; Osterwalder–Seiler independently identify physical positivity as the lattice OS condition.

Fix `F in A_+` with finite support and fix the reflection plane. On sufficiently large even periodic lattices, choose the standard reflection geometry so the fixed support does not meet the periodic seam. The finite-volume OS quadratic form is

`Q_L(F) = E_{mu_L}[ overline{F(theta Q)} F(Q) ] >= 0`.

The integrand is a bounded continuous local cylinder function because the gauge group is compact and `F` is local. Shen–Zhu–Zhu Theorem 1.2 states that the whole sequence of finite-volume Yang–Mills measures converges to their unique infinite-volume measure `mu`. Hence, along the reflection-compatible subsequence,

`Q_mu(F) = lim_L Q_L(F) >= 0`.

The full sequence has the same limit, so this defines the same `mu`. Polarization gives the positive semidefinite OS sesquilinear form on `A_+`. Thus the exact SZZ infinite-volume measure inherits the local reflection-positive structure required for OS reconstruction.

No continuum limit is taken in this step.

### Step 2 — the SZZ-controlled source class contains a dense OS generating set

In the OS construction the physical Hilbert space is, by definition, the null quotient and completion of the positive-time gauge-invariant local algebra. Therefore images `[F]`, with `F` ranging over a local gauge-invariant polynomial generating algebra, have dense span in `H_OS`.

These polynomial/Wilson-loop observables are smooth functions of finitely many compact-group edge variables, hence lie in Shen–Zhu–Zhu's `C^infty_cyl(Q)` class. We do **not** assert that every smooth cylinder is gauge invariant; only that the dense physical generating subclass is included in the covariance theorem's larger class.

Let

`psi_F = [F] - <Omega,[F]> Omega`.

Since orthogonal projection onto `Omega^perp` is bounded and the uncentered source span is dense in `H_OS`, the span of the centered `psi_F` is dense in `Omega^perp`.

This closes the source-visibility coordinate that failed in the registered hidden-state world `F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE`.

### Step 3 — Euclidean covariance is the transfer moment

Lüscher's OS construction identifies `T = exp(-a H)` with one-unit positive Euclidean-time translation and reconstructs the Euclidean expectations as transfer-matrix Schwinger functions. For a centered local positive-time source and an integer time translation large enough to separate supports, the same OS identity gives

`<psi_F, T^n psi_F> = Cov_mu(theta F, tau_n F)`

up to a fixed source-dependent shift of the integer separation caused by the finite temporal width of `F`. Equivalently, the support distance satisfies

`d(Lambda_{theta F}, Lambda_{tau_n F}) = n + O_F(1)`.

The fixed offset does not affect nth-root asymptotics.

The one-step transfer operator is positive. This is essential: it makes the moment nonnegative and permits the real logarithmic Hamiltonian functional calculus. If only self-adjointness were available, this candidate would have to fall back to a separately analyzed two-step operator; that fallback is not used here.

### Step 4 — SZZ supplies one common asymptotic rate

Shen–Zhu–Zhu Corollary 1.6 applies to all smooth cylinder functions with disjoint supports and gives

`Cov_mu(f,g) <= C(f,g) exp(-c_N d(Lambda_f,Lambda_g))`,

where the finite prefactor depends on support sizes/norms but the exponent `c_N` depends only on `K_S,N,d`.

Apply it to the reflected and translated centered source above. For each fixed `F`,

`0 <= <psi_F,T^n psi_F> <= C_F exp(-c_N (n-O_F(1)))`.

Therefore

`limsup_{n->infinity} <psi_F,T^n psi_F>^(1/n) <= exp(-c_N) =: q`.

The same `q` works for the dense centered generating family, and `0<q<1` because `c_N>0`. The parent q=0 logarithm failure is therefore out of scope rather than ignored.

### Step 5 — apply the parent dense-source spectral lemma

`YM-S1a1-C001-v2` states that for a positive self-adjoint contraction with vacuum eigenvalue one, a dense excited source family with one common nth-root rate `q<1` forces

`Spec(T|Omega^perp) subset [0,q]`.

With `q=exp(-c_N)` we obtain the stated transfer-spectrum exclusion. Since `T=exp(-aH_a)`, spectral mapping gives

`Spec(H_a|Omega^perp) subset [c_N/a, infinity)`

(with zero transfer spectrum, if present in an infinite-volume completion, corresponding only to infinite energy and not weakening the lower edge).

`QED` at scoped derivation level.

## Hostile scope tests

### F1 — incomplete source family

Drop OS density and reuse only a restricted correlator source. The exact three-state counterexample from the parent route has visible rate `1/4` while an unseen mode has transfer eigenvalue `1/2`. The full-gap inference fails. The candidate therefore genuinely uses Step 2.

### F2 — source-dependent rates

Allow a dense basis with individual rates `q_k<1` but `q_k -> 1`. The full spectrum can accumulate at one and the gap vanishes. SZZ's source-independent `c_N`, not merely sourcewise clustering, is load-bearing.

### F3 — Langevin/physical-generator confusion

SZZ also prove Poincaré/log-Sobolev information for the stochastic Langevin generator. Substituting that generator gap for `H_a` is forbidden. This candidate uses only the spatial Euclidean covariance estimate plus OS Euclidean-time reconstruction.

### F4 — negative beta

SZZ's stochastic bounds are formulated with `|beta|`, but this candidate restricts to positive Wilson coupling. It makes no reflection-positive transfer claim for negative beta.

### F5 — continuum overreach

Even if the fixed-a lower bound is correct, `c_N/a` is not a continuum certificate. The strong-coupling condition is not the asymptotically-free `a->0` path, and no uniform physical-unit lower bound along such a path is proved. `G5-G7` remain explicit residuals.

## Novelty and authority

The argument is intentionally compositional. Its ingredients are published OS/transfer reconstruction, the published SZZ common covariance exponent, the already registered parent spectral lemma, and elementary weak-limit/projection steps. Pending a separate bounded novelty search, the defensible ancestry label is

`PROVISIONAL_RAKL_TRIVIAL`.

That label means zero new problem-solving primitive was required. It is not a publication novelty verdict.

## Result if the derivation survives review

The active spectral route would move from

`G4/source completeness + same-theory covariance-to-transfer binding`

to the sharper residual

`G5 strong-coupling -> continuum/asymptotically-free transport`
`+ G6 physical a-scaling`
`+ G7 continuum spectral identification`.

The Clay root remains `OPEN_NO_SOLUTION_CERTIFICATE`.