# YM-S1a2j R22 — Wilson relevant-block conorm source audit

Authority: `PROPOSAL_SHADOW_ONLY`. Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.

## Atom / exact discriminator

Issue #335, signature `YM-S1a2j-WILSON-RELEVANT-BLOCK-CONORM-INVERSE-CONTRACTION-ADAPTED-NORM` asks whether the actual relevant block in Wilson §§30/38 has a uniform inverse/conorm margin in the graph norm, not merely a forward operator-norm or spectral-expansion statement.

The GitHub issue itself prospectively froze this discriminator before this detailed audit. The later R22 shadow fibre file was committed after an early indexed-source observation of Eq. (534); therefore the issue supplies the prospective atom boundary, while the literal R22 pre-action runtime binding is conservatively `CANNOT_CHECK/RETROSPECTIVE_ONLY` for that earliest observation. No prospective-discovery credit is backfilled.

## Primary-source bindings obtained

Primary author-uploaded/indexed manuscript surface: Jonathan J. Wilson, 2026, *Rigorous Construction of Four-Dimensional Yang–Mills Quantum Field Theory Via Gribov–Zwanziger Quantization and Renormalization Group Analysis: Measure-Theoretic Foundations, Spectral Properties, and the Mass Gap*.

### Section 30

The indexed primary text gives the finite-dimensional coupling linearization in the form

`(L_k c_k)_alpha = L^(d-Delta_alpha) c_{k,alpha} + sum_beta M^(k)_{alpha beta} c_{k,beta}`

with `M^(k)` described as finite-range covariance-contraction corrections and a uniform bound `C_M^(cov):=sup_k ||M^(k)||<infinity`. It then states, for a relevant/marginal/irrelevant splitting, constants `lambda_rel>1`, `lambda_irr<1` and Eq. (534)

`||L_k|_rel|| >= lambda_rel`, `||L_k|_irr|| <= lambda_irr`.

The same source subsequently says the spectral gap plus uniform Lipschitz nonlinear remainders yield a contracting graph transform.

### Section 38

The indexed primary text gives Eq. (580)

`lambda_{k+1}=A_k lambda_k + Phi_k(g_k,lambda_k)+Psi_k(K_k)`

with `||A_k||` only stated to be uniformly bounded on the acquired surface, while Theorem 38.5 says noncontracting finite-dimensional directions are controlled by tuning and the graph transform contracts.

A bounded post-freeze term search did not locate, on the acquired Wilson source surface, an explicit `A_k^{-1}`, `L_k^{-1}`, minimum-singular-value/conorm inequality, or exponential-dichotomy inverse estimate. This is a bounded non-exhaustive source statement, not an assertion that no such detail exists anywhere in the manuscript.

## Diagnosis: Eq. (534) is the wrong norm direction for a backward graph contraction

For an operator `A` on a normed finite-dimensional relevant space, `||A||>=lambda_rel>1` says only that **some** unit vector is expanded by at least `lambda_rel`. It does not imply injectivity and does not lower-bound expansion of every vector. The graph-transform requirement is instead a lower bound on the conorm

`m(A):=inf_{||v||=1} ||Av|| > 1`,

or equivalently, when invertible, `||A^{-1}|| < 1`.

Two exact hostile controls separate the claims:

1. `A=diag(2,0)`: `||A||=2>1`, but `A` is singular.
2. `A=diag(2,1/2)`: `||A||=2>1`, but `||A^{-1}||=2>1`; backward relevant evolution is not contractive in the same norm.

Thus the displayed Eq. (534), read literally as an ordinary operator norm, is insufficient to supply the inverse-relevant contraction invoked by a hyperbolic graph transform. This is a local hypothesis/type insufficiency, not a Yang–Mills counterexample and not a proof that the intended stable manifold cannot be repaired.

## Conditional local repair from the source's Eq. (532)

Eq. (532) exposes a useful repair coordinate. Suppose the relevant block is genuinely invariant and, in the same graph norm,

`L_k|_rel = D_rel + M_rel^(k)`, where `D_rel=diag(L^(d-Delta_alpha))` for relevant `alpha`.

Let `p_min=min_{alpha in A_rel}(d-Delta_alpha)>0`. Then the elementary conorm perturbation estimate gives

`m(L_k|_rel) >= m(D_rel) - ||M_rel^(k)|| >= L^p_min - C_M(L)`.

Consequently, if the source can bind a uniform margin

`L^p_min - C_M(L) >= 1+eta > 1`,

then every relevant block is invertible and

`||(L_k|_rel)^(-1)|| <= 1/(L^p_min-C_M(L)) <= 1/(1+eta) < 1`.

This would provide exactly the missing backward-relevant contraction coordinate at the linear level. It remains **conditional**: the acquired text states uniform boundedness of `M^(k)` but does not on the inspected surface give the required quantitative dependence of `C_M` on the block factor/norm, nor does it bind `L_k|_rel` to the Section-38 `A_k` in the exact graph metric. Those are the next source obligations.

## Analogue / disanalogy

Standard nonautonomous exponential-dichotomy definitions require the unstable restriction to be an isomorphism and control the inverse/backward evolution by a decaying bound. That is the correct structural analogue for the missing coordinate. It does not transfer automatically: Wilson's block is extracted from a gauge-fixed nonautonomous RG in scale-dependent regulator/polymer norms, and the relevant-subspace identity, nonlinear cross derivatives, shrinking `O(g^2)` domain, regulator uniformity, gauge/OS interfaces and physical continuum normalization remain separate obligations.

## Seven-role same-context expert cell

- rigorous lattice-gauge/RG: Eq. (532) gives a plausible diagonal-dominance repair shape, but relevant-block invariance and quantitative `C_M(L)` must be source-bound;
- nonautonomous invariant-manifold: a backward inverse/dichotomy factor is required on the expanding coordinate unless a different typed graph/Lyapunov–Perron object is supplied;
- Banach/operator theory: operator-norm lower bounds do not imply conorm bounds; the two diagonal controls are decisive;
- adversarial falsification: singular and weak-direction controls defeat the bare Eq. (534) inference;
- formal assurance/source binding: Section-30 `L_k|_rel` and Section-38 `A_k` are not treated as identical without an explicit source witness;
- OS/continuum gluing: any local UV graph repair has zero authority for gauge-invariant reflection positivity, OS reconstruction, continuum existence/nontriviality or physical mass gap;
- novelty/metrology: the conorm perturbation lemma is elementary (`RAKL_TRIVIAL`); retained value is source-scoped norm typing and path narrowing only.

All seven roles share the same evidence context and count `0/3` independent mathematical reviews.

## Verification / provenance boundary

Direct SSRN PDF delivery returned HTTP 403, and the source was not exposed as an `application/pdf` view to the screenshot backend. Mandatory PDF screenshot verification was attempted once and failed. Visual status: `CANNOT_CHECK`; the mathematical audit is bound only to indexed primary-author text. No missing formula is reconstructed from memory.

## Residual

`RES-YM-S1a2j-SOURCE-BIND-C_M_L-DOMINANCE-OR-DIRECT-CONORM-PLUS-L30-L38-BLOCK-IDENTITY-AND-ACTUAL-GRAPH-METRIC`

Even if that local residual closes, the previously open base-map inversion, next-radius invariance, cross-regulator slaving, gauge-invariant OS/reflection-positive transport, volume/lattice-spacing uniformity and continuum spectral identification remain separate.