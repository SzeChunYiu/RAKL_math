# YM-S1a2i R20 — Wilson §38 graph-transform source audit

Authority: `PROPOSAL_SHADOW_ONLY / NO_THEOREM / NO_ROOT_AUTHORITY`.

## Frozen target

Issue #321 prospectively asks whether Wilson §38 actually supplies the missing base-coordinate inverse, backward relevant contraction, shrinking `O(g^2)` graph invariance, and regulator-matched stable-graph continuity. The R20 run-specific fibre was committed before the bounded repair search. Source spans seen earlier in the run are motivating/retrospective for strict discovery credit.

## Primary source

Jonathan J. Wilson, *Rigorous Construction of Four-Dimensional Yang–Mills Quantum Field Theory Via Gribov–Zwanziger Quantization and Renormalization Group Analysis: Measure-Theoretic Foundations, Spectral Properties, and the Mass Gap*, SSRN 6419219, written 15 March 2026, 197 pp.; author-uploaded ResearchGate full text of the same manuscript family was used for detailed indexed mathematical spans.

Selectors inspected prospectively after fibre freeze: §30.6–30.7, §38.1–38.3, Lemmas 38.3–38.4, Theorem 38.5 Steps 2–5, Lemmas 38.9–38.10, Theorem 38.11, and targeted searches for `inverse`, `Jacobian`, derivative/base-map monotonicity, `Delta lambda`, and stable-manifold/regulator continuity.

PDF visual verification was attempted on the SSRN delivery reference for pages around §38, but the web backend exposed it as non-`application/pdf`; four screenshot attempts therefore failed closed. Parsed/indexed primary-author text remains the evidentiary surface; visual PDF verification is `CANNOT_CHECK`.

## Source-bound displayed interface

The inspected text gives the one-step coordinates

- `g_{k+1}=g_k-b_0 g_k^3+r_k`, `|r_k|<=C_beta g_k^5`;
- `lambda_{k+1}=A_k lambda_k+Phi_k(g_k,lambda_k)+Psi_k(K_k)`, with `A_k` uniformly bounded, `Phi=O(g_k^2)+O(||lambda||^2)`, `Psi=O(||K||)`;
- `||K^F_k(u_k,K_k)|| <= rho ||K_k|| + C g_k^4`, `rho<1`, with local Lipschitz control.

Theorem 38.5 then defines a graph `h_k:g -> (lambda,K)`. Step 2 says the graph update is well posed as a function of `g'` because the irrelevant map contracts. Step 3 states `||lambda_{k+1}||<=c_lambda g_{k+1}^2` for small `g_*`. Step 4 states the graph transform is a sup-norm contraction because relevant directions are controlled by tuning and the remaining dependence contracts with `rho<1`.

Separately, §30.6 gives a nonempty relevant restriction with a uniform expansion factor `lambda_rel>1`, and §30.7 invokes a graph transform after a full-forward contraction argument. R19 already recorded the full-forward collision. R20 uses that prior source fact only to type the relevant sector; it does not mint a duplicate failure.

## Prospective discriminator A — base inversion is not supplied by a value remainder bound

To define `h_{k+1}(g')` from `h_k(g)`, the base map on the graph must be injective/monotone (or otherwise have a source-bound inverse/reparametrization). Contraction of the `K` coordinate does not imply this.

The displayed value estimate `|r(g)|<=C g^5` alone also does not imply injectivity. Exact smooth hostile family on `(0,g_*]`:

`F_N(g)=g-b g^3+epsilon g^5 sin(N g)`, with `0<epsilon<=C`.

It satisfies the same value remainder bound. For any fixed small `g_0>0`, choose `N` so `cos(N g_0)=-1` and `epsilon N g_0^5` dominates `1-3b g_0^2+5 epsilon g_0^4 sin(Ng_0)`. Then `F_N'(g_0)<0`, whereas `F_N'(g)->1>0` as `g->0`. A continuous injective map on an interval is monotone, so this smooth source-shaped family need not be injective. Therefore a derivative/Lipschitz-in-`g` estimate on `r_k` or an explicit inverse theorem is load-bearing.

The bounded primary-source repair search did not locate such a §38 base-map derivative/inverse estimate. A later §38.3 statement that *regulator matching equations* have Jacobian close to identity and are solvable by the inverse function theorem concerns microscopic counterterm matching at `k_m`; it is not the missing inverse of the RG base map `g -> g'` used in Theorem 38.5 Step 2.

Verdict: `DISPLAYED_HYPOTHESES_INSUFFICIENT_FOR_BASE_GRAPH_WELLDEFINEDNESS`; stronger unlocated source detail remains possible.

## Prospective discriminator B — irrelevant contraction does not contract a forward relevant graph

Exact source-shaped scalar control:

`g'=g-b g^3`, `lambda'=a lambda`, `K'=rho K`, with `a>1`, `0<rho<1`, and `Phi=Psi=0`.

This satisfies the displayed beta shape, a uniformly bounded relevant linear map, and strict irrelevant contraction. The base is monotone for sufficiently small `g`. But the forward graph transform on `lambda` graphs obeys

`lambda_new(g')=a lambda(g(g'))`,

so sup-norm differences in the relevant graph coordinate are multiplied by `a>1`, not contracted. Reparametrizing by an invertible base does not create the missing inverse-relevant factor. This mirrors the manuscript's own §30 relevant expansion classification.

The same control also falsifies the Step-3 inference from a bound at `g^2` to the smaller target radius at `g'^2`: at the boundary `lambda=c_lambda g^2`, `lambda'=a c_lambda g^2>c_lambda g'^2`. Making `c_lambda` larger does not repair a multiplicative coefficient `a>1`; an explicit backward solve, inverse-relevant gain, transversality/graph-space construction, or equivalent cancellation is required.

The bounded source search did not locate a quantitative §38 inverse-relevant factor, Lyapunov–Perron operator, or full graph-space derivative/contraction constant. Theorem 38.5 Step 4 states the conclusion qualitatively.

Verdict: `DISPLAYED_HYPOTHESES_INSUFFICIENT_FOR_FULL_GRAPH_CONTRACTION_AND_SHRINKING_RELEVANT_INVARIANCE`.

## Prospective discriminator C — regulator matching is not stable-graph continuity

§38.3 does contain a useful distinct local fact: after matching finite-dimensional relevant coordinates at a scale `k_m`, the manuscript says the microscopic-counterterm matching equations have Jacobian close to identity and invokes the inverse function theorem. That can support *same-scale matching* if its constants are accepted.

Theorem 38.11 then needs the relevant-coordinate difference to vanish along the two regulator flows and says the remaining `lambda` coordinates are slaved by the stable manifold. The inspected source surface did not provide a quantitative cross-regulator estimate for the stable graphs themselves (for example `||h_k^R-h_k^{R~}||` controlled by the regulator mismatch with a vanishing tail) or an intertwining theorem that turns per-regulator graph existence into `Delta lambda_k ->0`.

Verdict: `LOCAL_REGULATOR_MATCHING_DISTINCT_FROM_CROSS_REGULATOR_STABLE_GRAPH_CONTINUITY`; the latter remains a gluing residual.

## Expert-cell synthesis

1. **Rigorous lattice-gauge RG:** §38 provides value and local-Lipschitz bounds, but the graph base needs a typed inverse on the actual tuned graph.
2. **Invariant-manifold dynamics:** forward expansion in the relevant coordinate requires a backward/inverse-relevant mechanism or a differently oriented graph transform; irrelevant contraction alone is insufficient.
3. **Banach analysis:** the source-shaped scalar model is an exact inference-form falsifier for the claimed sup-norm contraction under the displayed assumptions.
4. **AF scaling:** `g'<g` shrinks the `c g^2` radius, so one-step invariance requires a strict quantitative margin, not merely an `O(g^2)` estimate.
5. **Gauge/GZ representation:** no conclusion here changes the target theory; this is a proof-interface audit, not a gauge-equivalence or physical-state result.
6. **OS/continuum spectral gluing:** even a repaired stable graph does not close same-theory OS source algebra, physical transfer/Hamiltonian identification, lattice-spacing normalization, or continuum spectral identification.
7. **Adversarial provenance/RAKL:** source absence is bounded, not universal; same-context review earns `0/3` independent review credit.

## Episode -> diagnosis -> obstruction / lesson

- **Episode:** execute the frozen §38 source-repair search and hostile controls.
- **Diagnosis:** the displayed §38 graph-transform proof omits two typed quantitative interfaces: base inversion and inverse-relevant/full-graph contraction; the later regulator matching does not supply cross-regulator graph continuity.
- **Shadow failures:** local representation/proof-interface failure for graph well-definedness/contraction; separate local-to-global gluing failure for regulator-stable-graph transport.
- **Shadow obstruction:** `O-YM-S1a2i-SECTION38-GRAPH-TRANSFORM-TYPING-R20-SHADOW`, scoped only to what follows from the displayed hypotheses.
- **Lesson:** none promoted. The needed pattern was already anticipated by issue #321 and R19; raw confirmation is not a new reusable lesson.

## Outcome and residual

Outcome: `PARTIAL_SUCCESS__SECTION38_DISPLAYED_GRAPH_TRANSFORM_HYPOTHESES_FORMALLY_INSUFFICIENT__LOCAL_MATCHING_IFT_DOES_NOT_CLOSE_BASE_INVERSE_OR_CROSS_REGULATOR_GRAPH_CONTINUITY`.

Residual after:

`RES-YM-S1a2i-SOURCE-BOUND-C1-BASE-INVERSE-PLUS-INVERSE-RELEVANT-GRAPH-CONTRACTION-SHRINKING-RADIUS-MARGIN-AND-REGULATOR-STABLE-GRAPH-CONTINUITY`.

No Yang–Mills counterexample is claimed. No theorem in the manuscript is declared impossible to repair. Numerics are irrelevant to this proof-interface discriminator. Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.
