# NS-B1a3b1b-C001 — standard enstrophy endpoint audit

**Authority:** PROSPECTIVE_PROOF_ARCHITECTURE_ROUTE_PRUNING / NO_NAVIER_STOKES_COUNTEREXAMPLE / NO_ROOT_AUTHORITY
**Atom:** `NS-B1a3b1b` / issue #137
**Framework subject:** `SzeChunYiu/RAKL@812e9cf18345ef430f0a4cc3ff78f93d7f18ed22` (`method_version=3.0.0`)
**Pre-action application head:** `158ac7fcf75848fa2cf4b52f442c29c1e00d4b21`
**Pre-action receipt:** `pre_action_receipt:37f81faa2acfd4d753d94d4bd762dc098d75cf51d9820344871d44bc0ad740aa`

## Exact question
Can the standard Navier–Stokes vorticity/enstrophy energy method, added to finite energy dissipation or finite Type-I spacetime gradient control, by itself produce a uniformly bounded or sufficiently small critical time-slice vorticity/enstrophy trace?

The registered test starts in the whole-space smooth rapidly decaying setting. This is favorable: localizing adds cutoff, transport, and pressure/localization obligations. Failure already in the global scalar closure is therefore a local proof-architecture endpoint, not a local-to-global gluing failure.

## Source-bound downstream calibration
Albritton–Barker `arXiv:1811.00502v2` provides the Type-I/ancient-solution framework and a global-`L^3` backward-sequence Liouville trigger. Pineau–Vicol `arXiv:2607.09619v2` (revised 2026-08-06) provides a different local one-slice route: Theorem 1.9 assumes a local pointwise Type-I velocity bound plus annular pressure control and a sufficiently small self-similar-time derivative on one late slice; Proposition 9.5 isolates sufficiently small one-time rescaled local enstrophy as a regularity trigger. These are consumers, not producer assumptions.

## Standard equation-specific derivation
For a smooth rapidly decaying solution,
`∂t ω - Δω + (u·∇)ω = (ω·∇)u`.
Set `y(t)=||ω(t)||_2^2`, `X(t)=||∇ω(t)||_2`. Testing by `ω` and using incompressibility gives
`(1/2)y'(t)+X(t)^2 = ∫(ω·∇u)·ω`.
Whole-space div–curl gives `||∇u||_2=||ω||_2` (a universal inequality is enough), hence
`|stretching| <= ||∇u||_2 ||ω||_4^2`.
In 3D, `||ω||_4 <= C_GN ||ω||_2^(1/4)||∇ω||_2^(3/4)`, so
`|stretching| <= C y^(3/4) X^(3/2)`.
Young with exponents `4/3` and `4` absorbs part of `X^2`, yielding for some finite universal `C0>0`
`y'(t) <= C0 y(t)^3`.  (E)
The kinetic-energy identity supplies `∫_0^T y(t)dt<∞` on every smooth interval before a putative first singular time. The standard route therefore retains only `y>=0`, `y∈L^1_t`, `y'<=C0 y^3`.

No pressure term was discarded in this global vorticity identity: curl eliminates pressure. Pressure/local harmonic pieces re-enter upon localization and remain separate.

## Counterexample-first scalar falsifier
Let `s=T-t` and `y_a(t)=a s^(-1/2)`, `a>0`. Then
`∫_(T-ε)^T y_a(t)dt = 2a sqrt(ε)<∞`, while `sup y_a=∞`, and the scale-invariant rescaled enstrophy is constant: `s^(1/2)y_a(t)=a`.
Moreover, `y_a'(t)=(a/2)s^(-3/2)` and `y_a(t)^3=a^3s^(-3/2)`. Thus (E) is satisfied whenever `a^2>=1/(2C0)`.

So the exact scalar consequences of finite dissipation plus the standard enstrophy estimate admit the Type-I endpoint exponent with no decay of scale-invariant enstrophy. Grönwall/Osgood cannot turn these data alone into either a uniform enstrophy trace or a small late rescaled-enstrophy slice.

This scalar profile is **not** asserted to come from a Navier–Stokes solution. It falsifies only the registered proof architecture. Any successful equation-specific upgrade must use information lost before (E), such as sign/coherence in vortex stretching, frequency/scale localization, a monotone or finite-variation self-similar defect, no-recurrence, or a different source-valid consumer.

## Scaling and endpoint audit
Under `u_λ(x,t)=λu(λx,λ^2t)`, `ω_λ=λ^2ω(λx,λ^2t)` and `y_λ=λy`. Hence `(T-t)^(1/2)y(t)` is dimensionless. The hostile exponent `1/2` is exactly scale-critical for enstrophy. Its time integral is finite because `1/2<1`.

The failure is not a missing-constant issue: for every finite `C0>0`, choosing `a >= (2C0)^(-1/2)` satisfies the scalar differential inequality. Finite total dissipation alone does not repair it.

## Failure separation
**Local mathematical/proof-architecture failure:** `finite dissipation + standard absolute vortex-stretching estimate -> bounded/small critical time trace` fails at the scalar endpoint. New scoped failure: `F-NS-B1a3b1b-STANDARD-ENSTROPHY-ENDPOINT`.

**Localization/gluing failure:** not newly established. Local cutoffs add transport/pressure terms but are unnecessary for this negative result.

**Global gluing/far-field failure:** still open. This cycle does not produce global `L^{3/2,∞}` vorticity, Biot–Savart tail control, or a global `L^3` backward sequence.

**Representation/normalization failure:** vorticity-direction zero-set/log-BMO production remains separate.

**State-space/source failure:** Pineau–Vicol's pre-singularity one-slice criteria are not ancient-solution Liouville theorems and require stronger source hypotheses.

## Outcome and residual
`PARTIAL_SUCCESS / STANDARD_ENSTROPHY_GRONWALL_TIME_TRACE_ROUTE_PRUNED`.

The root remains `OPEN_NO_SOLUTION_CERTIFICATE`. Type II is untouched.

Next: search for a scale-symmetry breaker in vortex-stretching/self-similar dynamics: a sign/coherence depletion estimate replacing `C0y^3` by an integrable coefficient times `y`, a finite-variation/monotone self-similar defect forcing a small late slice, or another exact consumer. Any candidate must be stress-tested for derivative loss, pressure/localization, far-field, and circular use of the desired critical smallness.

Novelty class of the solved route-pruning subproblem: `COMPOSITIONAL` (stored enstrophy identity + exact scaling + source-bound one-slice consumer; no mathematical novelty claim).
