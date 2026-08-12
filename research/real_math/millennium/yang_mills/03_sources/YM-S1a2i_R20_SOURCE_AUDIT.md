# YM-S1a2i R20 — Section 38 shrinking-domain and graph-transform audit

Authority: **PROPOSAL/SHADOW ONLY**. Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`. This is a scoped audit of displayed UVR3 arguments in Jonathan J. Wilson's 2026 author-uploaded Yang–Mills manuscript; it is not a Yang–Mills counterexample, not a source-wide refutation, and not independent mathematical review.

## Prospective binding

The atom was frozen as issue #321 and the R20 fibre/pre-action receipt was committed before the consequential Section-38 equation audit. The predeclared discriminator required exact equations (578)–(580), base-map invertibility/reparametrization, a backward/inverse relevant contraction or quantitative graph-transform contraction, and invariance of the shrinking `O(g^2)` graph domain.

## Primary source boundary

Primary author-uploaded/indexed text inspected: Jonathan J. Wilson, *Rigorous Construction of Four-Dimensional Yang–Mills Quantum Field Theory Via Gribov–Zwanziger Quantization and Renormalization Group Analysis: Measure-Theoretic Foundations, Spectral Properties, and the Mass Gap* (2026), SSRN 6419219 / ResearchGate author-uploaded versions, especially Lemma 38.2 and Lemmas 38.3–38.4 / Theorem 38.5.

Direct SSRN PDF retrieval returned HTTP 403 and ResearchGate direct opening returned HTTP 429/failed fetch. No `application/pdf` view reference was acquired, so mandatory page screenshot verification is `CANNOT_CHECK`. The findings below are bounded to indexed primary-author text. No missing formula is reconstructed from memory.

## D1 — Lemma 38.2 uses the monotonicity of `g` in the wrong direction for a shrinking invariant ball

The source defines

`B_k = {0<g<=g_*, ||lambda||<=c_lambda g^2, ||K||_k<=c_K g^2}`

and proves `g_{k+1}<g_k`. In the irrelevant-coordinate step it derives only

`||K_{k+1}||_{k+1} <= c_K g_k^2`

and then says that `g_{k+1}<=g_k` yields

`||K_{k+1}||_{k+1} <= c_K g_{k+1}^2`.

That implication is reversed: the target radius decreases, since `c_K g_{k+1}^2 <= c_K g_k^2`. The same direction error occurs in the displayed relevant/marginal closure, where an old-radius bound `||lambda_{k+1}||<=c_lambda g_k^2` is promoted to the smaller target `c_lambda g_{k+1}^2` using only `g_{k+1}<=g_k`.

Exact scalar control: `g_k=1`, `g_{k+1}=1/2`, `c=1`, `x=3/4`. Then `x<=c g_k^2` but `x>c g_{k+1}^2`.

This is a local proof defect, not an impossibility result. For the **irrelevant** coordinate, equation (573) has genuine slack because `rho<1` and the forcing is `O(g_k^4)`. Combining the exact lower as well as upper control on `g_{k+1}` from (575) could plausibly repair the step after an explicit smallness inequality. Such a repair is not inferred as already proved by the displayed argument.

## D2 — the relevant/marginal old-radius estimate itself requires a missing strict linear margin

The displayed one-step bound is

`||lambda_{k+1}|| <= C_2 ||lambda_k|| + C_2 g_k^2 + C_2 ||K_k||_k`.

On `B_k` this gives

`||lambda_{k+1}|| <= [C_2 c_lambda + C_2(1+c_K)] g_k^2`.

To obtain even the **old** radius `c_lambda g_k^2`, one needs

`(1-C_2)c_lambda >= C_2(1+c_K)`.

Therefore a choice of `c_lambda` can close this estimate only if a strict margin such as `C_2<1` is available. The source at this point states only `C_2>0`; the displayed choice `c_lambda >= 4 C_2(1+c_K)` does not control the multiplicative term `C_2 c_lambda`. If `C_2>=1`, making `c_lambda` larger cannot repair the inequality.

This is the exact quantitative manifestation of the R19 type issue: a relevant/marginal forward block cannot be made contractive merely by enlarging the graph radius.

## D3 — Lemma 38.4 and Theorem 38.5 do not expose the missing hyperbolic inverse in the acquired text

Lemma 38.4 gives

`lambda_{k+1}=A_k lambda_k + Phi_k(g_k,lambda_k)+Psi_k(K_k)`

with only a **uniform bound** on `||A_k||`, plus `Phi_k=O(g_k^2)+O(||lambda_k||^2)` and `||Psi_k(K_k)||<=C||K_k||_k`.

Theorem 38.5 then says to choose `c_lambda` large compared with the operator bound on `A_k`, and Step 4 asserts that the graph transform contracts because finite-dimensional noncontracting directions are “controlled by tuning”. In the acquired primary text there is no displayed inverse/backward relevant block, exponential-dichotomy estimate, conorm lower bound, or contraction constant in which a relevant expansion enters as an inverse factor `<1`.

A correct stable-manifold theorem remains a live repair. The required source certificate is simply more specific now: identify the projected/graph/backward object and quantify its contraction rather than applying a full forward bound to an expanding coordinate.

## D4 — the one-step graph transform needs a typed base-map inverse/reparametrization

Theorem 38.5 Step 2 defines `h_{k+1}` by taking `(lambda,K)=h_k(g)`, applying the RG map to obtain `(g',lambda',K')`, and requiring `(lambda',K')=h_{k+1}(g')`. It says the irrelevant contraction makes the implicit definition of `K'` as a function of `g'` well posed.

Irrelevant contraction does not by itself show that the **base** map `g -> g'` is injective on the graph. Lemma 38.4 supplies the amplitude estimate

`g'=g-b_0 g^3+r_k`, `|r_k|<=C_beta g^5`,

but the acquired text does not expose a derivative/Lipschitz bound on `r_k` with respect to the graph data sufficient to prove fixed-step monotonicity/invertibility. Step 5 proves only that `g_{k+1}<g_k` along a selected orbit; that is a time-direction inequality, not injectivity of the map from one graph parameter to the next.

A source-bound derivative estimate or an alternative parametrization can repair this. Until then the graph-transform definition is typed only schematically.

## Analogue / DifferenceWitness

Standard hyperbolic/nonautonomous invariant-manifold constructions use an explicit stable/unstable splitting (often an exponential dichotomy) and solve the expanding block backward or use a graph transform whose contraction constant contains the inverse unstable expansion. That structural analogue supports the **shape** of the repair, not its Yang–Mills applicability. Differences left open here are the nonautonomous asymptotically-free base, regulator-weighted polymer Banach spaces, GZ counterterm coordinates, scale-dependent norms, gauge constraints, and the downstream OS/continuum interfaces.

## Same-context expert cell

1. **Rigorous lattice-gauge RG:** D1 is a shrinking-target error. The `rho<1` slack in (573) makes a K-coordinate repair plausible, but the relevant block needs a different mechanism.
2. **Nonautonomous invariant-manifold theory:** Step 2 needs a base inverse/reparametrization; expanding relevant directions normally enter through backward/inverse dynamics or a dichotomy, not a full forward contraction.
3. **Banach-space functional analysis:** the algebraic closure condition for the displayed lambda estimate requires `C_2<1`; increasing `c_lambda` cannot absorb `C_2 c_lambda` when `C_2>=1`.
4. **Asymptotic-freedom scaling:** `g_{k+1}^2=g_k^2-O(g_k^4)`, so the target ball shrinks by `O(g_k^4)`. A valid invariant-region proof must spend an explicit contraction margin against that shrinkage.
5. **GZ/gauge representation:** any tuning/projection repair must retain all required GZ-compatible relevant counterterms and cannot silently replace the gauge-fixed theory.
6. **OS/continuum gluing:** even a repaired UV stable graph supplies no automatic gauge-invariant OS quotient, reflection positivity, continuum nontriviality, or physical mass-gap transport.
7. **Adversarial provenance/metrology:** D1–D4 are source-scoped. Same-context agreement earns `0/3` independent-review credit; PDF visual verification remains `CANNOT_CHECK`.

## Outcome and residual

Outcome: `PARTIAL_SUCCESS_NEW_PROSPECTIVE_SHRINKING_DOMAIN_FAILURE_AND_SHARPER_HYPERBOLIC_GRAPH_CONTRACT`.

Residual before: `RES-YM-S1a2h-PROJECTED_OR_BACKWARD-RELEVANT-GRAPH-CONTRACTION-PLUS-REGULATOR-MATCHED-LAMBDA-SLAVING-AND-SAME-OS-SPECTRAL-TRANSPORT-UNBOUND`.

Residual after: `RES-YM-S1a2i-NEXT-RADIUS-INVARIANCE-PLUS-BASE-INVERSE-PLUS-RELEVANT-BACKWARD-GRAPH-CONTRACTION-AND-REGULATOR-SLAVING-UNBOUND`.

No lesson, research tool, protected obstruction, protected novelty, or root authority is minted by this audit.
