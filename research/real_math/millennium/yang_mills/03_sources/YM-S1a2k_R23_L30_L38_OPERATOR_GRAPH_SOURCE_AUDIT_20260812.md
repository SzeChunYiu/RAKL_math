# YM-S1a2k R23 — Section-30/Section-38 operator and graph-parameterization source audit

Authority: **PROPOSAL/SHADOW ONLY**. Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`. This audit concerns a local source-typing interface in Jonathan J. Wilson's 2026 author manuscript; it is not a Yang–Mills counterexample, not a source-wide refutation, and not an independent mathematical review.

## Prospective boundary and live-work collision

Issue #356 prospectively froze this child after live-work review found draft PR #351 already exercising the distinct `YM-S1a2j` operator-norm-versus-conorm discriminator. PR #351 is open/draft and therefore guides routing only. R23 does not repeat that conorm calculation. Its discriminator is whether any Section-30 inverse/conorm information is actually typed to the Section-38 stable-graph operator and norm.

The branch serialization of this audit occurs after the public issue freeze and after source acquisition. Prospective credit, to the extent chronology can be checked, rests only on issue #356; no post-hoc branch file is treated as a pre-action receipt.

## Primary source and verification boundary

Primary author manuscript: Jonathan J. Wilson, *Rigorous Construction of Four-Dimensional Yang–Mills Quantum Field Theory Via Gribov–Zwanziger Quantization and Renormalization Group Analysis: Measure-Theoretic Foundations, Spectral Properties, and the Mass Gap* (2026), SSRN 6419219 / OSF `bgu6a_v4`, with author-uploaded indexed full text also exposed by ResearchGate.

Bounded source queries targeted Sections 30.4–30.7 and 38.2–38.3, especially equations (524)–(535), (576)–(580), Theorems 30.6 and 38.5, and the regulator-matching paragraph preceding Lemma 38.9.

Direct SSRN delivery returned HTTP 403 when opened. Three screenshot attempts on the SSRN delivery search reference (nominal manuscript pages 96, 115 and 118; zero-index request pages 95, 114 and 117) were rejected because the backend did not expose the object as `application/pdf`. Visual verification is therefore `CANNOT_CHECK`; claims below are bounded to indexed primary-author text. No missing formula is reconstructed from memory.

## S1 — common extraction genealogy is source-bound

Section 30.4 defines a Banach state `(c_k,K_k)`, with finite-dimensional relevant/marginal coupling vector `c_k` in a chosen local-operator basis and polymer activity `K_k`. Equations (524)–(527) define the one-step coupling linearization `L_k`, explicitly saying it is induced by `Loc_k` and block rescaling. Section 30.6 gives the component formula

`(L_k c_k)_alpha = L^(d-Delta_alpha) c_{k,alpha} + sum_beta M^(k)_{alpha beta} c_{k,beta}`,

with finite-range covariance-contraction correction `M^(k)`.

Section 38.2 uses the same polymer norm/RG closure, defines `u_k=(g_k,lambda_k)` as the relevant/marginal coordinate vector with the additional GZ-compatible local couplings selected by `Loc_k`, and states that the `lambda` coordinates are finite-dimensional Taylor coefficients of the extracted local part. Thus the two sections are not unrelated theories: a common extraction/coordinate genealogy is positively source-bound.

## D1 — the source does not bind `A_k` to the Section-30 relevant block in the norm needed by the graph transform

Section 38.4 writes

`lambda_{k+1}=A_k lambda_k + Phi_k(g_k,lambda_k)+Psi_k(K_k)`

and on the acquired surface states only that `||A_k||` is uniformly bounded, with the linear term described as the isolated linear counterterm transport. The bounded exact-term search did not locate a formula identifying `A_k` with a stated restriction/projection of the Section-30 `L_k`, nor an explicit change-of-coordinates map carrying one to the other, nor a quantitative equivalence between the Section-30 regulator-weighted coupling norm and the Section-38 graph sup/product norm.

This matters to the pending `YM-S1a2j` repair. Even if a primary estimate eventually establishes `||(L_k|rel)^-1|| <= q < 1` in one coordinate norm, it cannot be applied to `A_k` merely because both operators arise from extracted relevant/marginal Taylor coefficients.

Exact similarity control: let

`L = diag(2,3)`, `J = [[1,M],[0,1]]`, `A=J L J^-1`.

In the infinity norm, `||L^-1||_inf=1/2`, whereas

`A^-1 = [[1/2,-M/6],[0,1/3]]`

and `||A^-1||_inf = 1/2 + |M|/6`. At `M=4`, the transported inverse norm is `7/6>1`. Thus a strict backward contraction is not invariant under an unquantified coordinate change; a uniform condition-number/intertwiner bound is load-bearing.

This is a source-typing insufficiency, not an assertion that the intended operators are different. A primary equality `A_k=P L_k P` in the same norm, or uniformly conditioned intertwiners with a strict transported margin, withdraws this diagnosis.

## D2 — Section 30 and Section 38 use mathematically different graph parameterizations

Theorem 30.6 states a codimension-`|A_rel|` stable manifold in the scale-0 Banach state and says: for every admissible initial irrelevant activity `K_0`, there is a unique tuned relevant/marginal coupling vector `c_0=c_0(K_0)`. Its proof describes a graph transform `Gamma: Pi_irr X_0 -> Pi_rel X_0`.

Theorem 38.5 instead defines a graph space of maps

`h_k:(0,g_*) -> R^(m-1) x K_k`, `g -> (lambda,K)`,

and asserts that for every sufficiently small initial gauge coupling there is a unique `lambda_{k0}` **and a unique irrelevant activity** `K_{k0}` producing the controlled UV orbit.

Those are not the same graph statement. A stable manifold that tunes relevant coordinates as functions of freely chosen stable/irrelevant data does not by itself make the irrelevant datum unique as a function of one marginal coordinate.

Elementary control: in the state `(g,lambda,K)`, the set `M={(g,0,K): g in I, K in B}` is a perfectly valid codimension-one graph with `lambda` slaved to `(g,K)`, but for any fixed `g` it contains every `K in B`; it does not define a one-dimensional graph `g -> (lambda,K)`. To obtain the Section-38 parameterization from such a stable manifold requires an additional microscopic initialization/selector curve `K=K_init(g)` (plus a uniqueness/transversality statement), or a direct graph-transform proof on the `g`-parameterized graph space.

The acquired Section-38 proof attempts the latter, but its base-map inversion, shrinking-radius and relevant backward-contraction obligations are already separately frozen by R20/R22. The bounded R23 search did not locate a theorem deriving the Section-38 one-dimensional graph from Theorem 30.6 through a microscopic initialization map.

## D3 — regulator basis freedom makes conditioning part of the universality obligation

Section 38.3 states that admissible regulators produce the recursion on the same finite relevant space `R^m`, possibly after a fixed invertible linear change of basis in the extracted polynomial space, and Lemma 38.9 invokes an invertible linear reparameterization at a mesoscopic matching scale.

That is useful positive typing, but it does not on the acquired surface supply uniform bounds for the reparameterization and its inverse over the regulator family. Any graph-contraction or inverse-relevant margin transported across those coordinates therefore needs its condition-number loss included explicitly. Pointwise finite-dimensional invertibility is not enough for the requested regulator-uniform continuum bridge.

## Episode -> diagnosis -> obstruction/lesson separation

Episode `EP-YM-S1a2k-R23-20260812` records the actions and observations above.

Diagnosis `DG-YM-S1a2k-R23-L30-L38-REPRESENTATION-GLUE-SHADOW` classifies the observed relation as: common extraction genealogy is present, but exact operator/norm and graph-parameterization transport are not source-bound.

Scoped failures:
- `FS-YM-S1a2k-L30-L38-OPERATOR-NORM-IDENTITY-UNBOUND-R23-SHADOW`
- `FS-YM-S1a2k-STABLE-GRAPH-PARAMETERIZATION-SELECTOR-UNBOUND-R23-SHADOW`
- `FS-YM-S1a2k-REGULATOR-BASIS-CONDITIONING-UNBOUND-R23-SHADOW`

Remaining obstruction:
- `O-YM-S1a2k-RELEVANT-BLOCK-INTERTWINER-AND-STABLE-GRAPH-SELECTOR-R23-SHADOW`

No lesson, tool or motif is minted. The elementary similarity and graph-dimension controls are verification aids, not mathematical novelty.

## Result / residual

Outcome: `PARTIAL_SUCCESS_NEW_OPERATOR_GRAPH_GLUING_OBSTRUCTION`.

Residual before:
`RES-YM-S1a2j-SOURCE-BIND-C_M_L-DOMINANCE-OR-DIRECT-CONORM-PLUS-L30-L38-BLOCK-IDENTITY-AND-ACTUAL-GRAPH-METRIC`.

Residual after:
`RES-YM-S1a2k-SOURCE-BIND-L30-L38-OPERATOR-INTERTWINER-UNIFORM-NORM-PLUS-MICROSCOPIC-GRAPH-SELECTOR-THEN-CONORM-AND-DIRECT-GRAPH-CONTRACTION`.

Even a local closure leaves the R20 shrinking-radius/base-inverse obligations, regulator-stable-graph slaving, gauge-invariant reflection positivity/OS reconstruction, finite/infinite-volume and cutoff uniformity, continuum nontriviality, physical spectral identification, and every root-promotion gate separate.
