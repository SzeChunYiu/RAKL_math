# YM-S1a2g R18 — Wilson UVR3 invariant/stable-manifold and universality audit

Authority: **PROPOSAL/SHADOW ONLY**. This is source evidence, falsification of specific displayed inference forms, and routing diagnosis. It is not a Yang–Mills counterexample, not a refutation of Balaban, not a proof that the Wilson construction cannot be repaired, not independent review, and not a root certificate.

## Exact atom and root contract

- Root: RAKL_math issue #5, state `OPEN_NO_SOLUTION_CERTIFICATE`.
- Atom: `YM-S1a2g`.
- Issue: #295.
- Signature: `YM-S1a2g-WILSON-UVR3-INVARIANT-STABLE-MANIFOLD-AND-UNIVERSALITY-CLOSURE`.
- Frozen fibre: `10_case_study/YM-S1a2g_PRE_CANDIDATE_FIBRE_MEMORY_20260812_R18.json`.
- Parent: #283 / draft R17 PR #290.
- Active question: whether the displayed Section-38 UVR3/UVR4 hypotheses actually imply the shrinking invariant region, tuned stable manifold, and full regulator-difference decay required by the asserted continuum universality.
- Non-target coordinates held open: exact same-theory OS/transfer observable transport, physical mass normalization, lattice-spacing uniformity, continuum nontriviality, and the Clay root.

## Current RAKL v3 use

This cycle re-read current `SzeChunYiu/RAKL` main before the mathematical audit: SHA `43897d3afaf0038385102d5acc64793c05ec40f0`, method `3.0.0`, package `0.1.0`. The v3 architecture separates object/facet/context/fibre coordinates; `rakl.v3` exposes `TaskEpisode`, problem-fibre/gluing, novelty, saturation, and protected-authority surfaces; `method_specs.py` makes decomposition/routing/search proposal-only and requires explicit context/evidence for gluing. The present packet therefore freezes the fibre, records experience-conditioned routing, uses hostile controls before accepting a theorem label, separates local mathematical failure from same-theory gluing failure, and creates no protected authority.

Canonical process surfaces actually invoked: `decomposition`, `routing`, `search_query_generation`, `source_selection_reliability`, `claim_extraction`, `ontology_terminology_normalization`, `mathematical_context_translation`, `equivalence_similarity`, `contextual_theory_gluing`, `contradiction_diagnosis`, `gap_discovery`, `experiment_query_selection`, `memory`, `review`, `saturation_stopping`, `prompting_context_policy`, and `synthesis`.

## Primary source and retrieval boundary

Primary claim-family inspected:

Jonathan J. Wilson, *Rigorous Construction of Four-Dimensional Yang–Mills Quantum Field Theory Via Gribov–Zwanziger Quantization and Renormalization Group Analysis: Measure-Theoretic Foundations, Spectral Properties, and the Mass Gap*, author-uploaded 2026 manuscript. ResearchGate record DOI `10.13140/RG.2.2.10405.77282`, author content uploaded March 5, 2026.

The runtime could not obtain the full PDF through the direct SSRN/OSF/ResearchGate download surfaces (403/429 behavior in bounded attempts). The search index exposes author-uploaded full-text spans including Sections 37–38 and the equations/theorem text used below. Therefore every conclusion here is limited to those exposed primary-source spans. A page-by-page PDF verifier audit remains `BLOCKED_SOURCE_RETRIEVAL`, not silently assumed.

Structural analogues, not theorem transfers:
- David C. Brydges and Gordon Slade, *A renormalisation group method. IV. Stability analysis*, arXiv:1403.7255.
- David C. Brydges and Gordon Slade, *A renormalisation group method. V. A single renormalisation group step*, arXiv:1403.7256.

Their relevance is methodological: rigorous RG stability requires explicit contraction/error hypotheses, including for a nonperturbative coordinate. Their model is not Yang–Mills/GZ, and they provide no target gauge/OS/spectral transport certificate.

## Source-coverage correction to R17

R17 correctly rejected the semantic collision “large field” = “strong coupling.” It also used Wilson Section 37 as evidence that the manuscript itself still left UVR2–UVR4 as future work.

That source diagnosis was incomplete. The same author-uploaded manuscript immediately follows Section 37 with Section 38, whose opening states that it replaces the roadmap with a theorem/proof treatment of UVR2–UVR4. The safe correction is:

- Section 37 cannot, by itself, be used as a current-manuscript admission that UVR2–UVR4 remain unattempted.
- The scientific question must move to whether Section 38's displayed hypotheses and proofs actually close those coordinates.
- This is a **source-coverage/decomposition process failure in R17**, not a scientific failure of Yang–Mills and not protected learning.

Shadow process-failure ID: `F-YM-S1a2g-R18-R17-SECTION38-MISSED-SOURCE-COVERAGE`.

## Section-38 displayed system

The exposed UVR3 text gives an irrelevant-coordinate estimate of the form

\[
\|K_{k+1}\|_{k+1}\le \rho\|K_k\|_k+C_1g_k^4,\qquad 0<\rho<1,
\]

a relevant/marginal estimate

\[
\|\lambda_{k+1}\|\le C_2\|\lambda_k\|+C_2g_k^2+C_2\|K_k\|_k,
\]

and the coupling recursion

\[
g_{k+1}=g_k-b_0g_k^3+r_k,\qquad |r_k|\le C_3g_k^5.
\]

The proposed shrinking region has
\[
\|K_k\|_k\le c_Kg_k^2,\qquad \|\lambda_k\|\le c_\lambda g_k^2.
\]

Later Lemma 38.4 presents
\[
\lambda_{k+1}=A_k\lambda_k+\Phi_k(g_k,\lambda_k)+\Psi_k(K_k),
\]
with only a uniform bound on `||A_k||` in the exposed statement, plus quadratic/nonlinear remainder bounds. Theorem 38.5 then invokes tuning/stable-manifold language.

For regulator comparison, the exposed Lemma 38.10 gives
\[
\|\Delta K_{k+1}\|\le \rho\|\Delta K_k\|+Cg_k^2\|\Delta u_k\|+Cg_k^6
\]
and
\[
\|\Delta u_{k+1}\|\le (1+Cg_k^2)\|\Delta u_k\|+C\|\Delta K_k\|+Cg_k^6,
\]
where `u=(g,lambda)`. Theorem 38.11's exposed proof then reasons through a `(Delta g, Delta K)` contraction and says the remaining `lambda` coordinates are slaved by the stable manifold.

## D1 — local `K` invariant-ball proof contains an inequality-direction error, but it has a plausible repair

The exposed Lemma-38.2 argument first obtains a strict-margin estimate at the old coupling scale, schematically
\[
\|K_{k+1}\|\le \frac{1+\rho}{2}c_Kg_k^2.
\]
It then uses `g_{k+1} <= g_k` to infer the stronger target
\[
\|K_{k+1}\|\le c_Kg_{k+1}^2.
\]

That inference direction is invalid: `g_{k+1}^2 <= g_k^2` makes the target right-hand side smaller, not larger.

This is a local proof gap, not a fatal obstruction. The preceding strict factor `(1+rho)/2<1` can plausibly repair it if one proves, uniformly in the allowed regime,
\[
\frac{g_{k+1}^2}{g_k^2}\ge \frac{1+\rho}{2}.
\]
The coupling recursion gives `g_{k+1}/g_k = 1-b_0g_k^2+O(g_k^4)`, so sufficiently small `g_*` should make such a margin available if all constants/signs are source-bound. The missing step is to state and verify that quantitative comparison rather than appeal to monotonicity in the wrong direction.

**Local mathematical status:** `PARTIALLY_IDENTIFIED_REPAIRABLE_GAP`.

Cheapest falsifier/repair certificate: retain the strict `rho` margin and prove
`rho*cK*g_k^2 + C1*g_k^4 <= cK*g_{k+1}^2`
with explicit uniform constants.

## D2 — the displayed `lambda` hypotheses do not certify the claimed shrinking invariant region

The relevant-coordinate issue is more load-bearing. Insert the region hypotheses into the displayed coarse estimate:
\[
\|\lambda_{k+1}\|
 \le C_2(c_\lambda+1+c_K)g_k^2.
\]
To infer the target
\[
\|\lambda_{k+1}\|\le c_\lambda g_{k+1}^2
\]
one needs
\[
C_2(c_\lambda+1+c_K)
\le c_\lambda\,\frac{g_{k+1}^2}{g_k^2}.
\]

Uniform boundedness of `A_k` (or a positive finite `C2`) alone does not give this. In particular, if the admissible bound permits an expanding scalar linear part, increasing `c_lambda` does not create contraction.

### Hostile scalar control

Take a one-dimensional admissible model under only the displayed Lemma-38.4 type hypotheses:
\[
\lambda_{k+1}=2\lambda_k,\qquad \Phi_k=0,\qquad \Psi_k=0,
\]
with `A_k=2`, which is uniformly bounded. For any nonzero `lambda_k` of order `g_k^2`, the image expands while the target radius `c_lambda*g_{k+1}^2` shrinks. The stated boundedness hypothesis therefore cannot imply forward invariance of the whole displayed `lambda` ball.

This does **not** rule out a tuned stable graph. A stable-manifold theorem can select special relevant initial data even when the ambient relevant map has expanding directions. But then the proof must exhibit the missing structure: a stable/unstable splitting, backward/forward graph transform, invertibility/transversality, and quantitative contraction/Lipschitz constants for the tuned graph. The exposed statement “`A_k` uniformly bounded” is not that certificate.

Shadow obstruction: `OBS-YM-S1a2g-R18-RELEVANT-STABLE-SPLITTING-UNBOUND`.

**Local mathematical status:** displayed hypotheses are insufficient for the asserted invariant-ball conclusion; a stronger unexposed lemma could repair it.

## D3 — the exposed regulator-difference recursion does not by itself imply full `Delta u -> 0`

The second regulator estimate has multiplier `1+Cg_k^2`, which is greater than one. It is a stability/Gronwall-shaped upper bound, not a contraction statement for the full relevant vector `Delta u=(Delta g,Delta lambda)`.

### Hostile recurrence

Let `x_k=||Delta K_k||=0`. At the matching scale take `y_{k_m}=||Delta u_{k_m}||=0`. Set
\[
y_{k_m+1}=\frac C2 g_{k_m}^6>0
\]
and thereafter `y_{k+1}=y_k`. This sequence satisfies the displayed one-sided inequality
\[
y_{k+1}\le (1+Cg_k^2)y_k+Cg_k^6
\]
but does not converge to zero. Therefore Lemma 38.10's displayed inequalities alone cannot certify `||Delta u_k|| -> 0`.

The exposed Theorem-38.11 proof then narrows to `Delta g` and `Delta K`, while treating `Delta lambda` as slaved by Theorem 38.5. That handoff needs an explicit **regulator-matched stable-manifold comparison**:
\[
\|\Delta\lambda_k\|\le L_g|\Delta g_k|+L_K\|\Delta K_k\|+\eta_k,
\qquad \eta_k\to0,
\]
or an equivalent direct same-theory observable estimate. A stable manifold constructed separately for each regulator does not automatically provide this cross-regulator Lipschitz/intertwining relation.

Shadow obstruction: `OBS-YM-S1a2g-R18-DELTA-U-TO-DELTA-G-SUBSTITUTION-UNBOUND`.

**Gluing status:** `LOCAL_TO_GLOBAL/SAME_THEORY_UNIVERSALITY_GLUE_OPEN`.

## Expert-cell synthesis

1. **Rigorous lattice-gauge RG specialist.** Section 38 must replace the R17 roadmap shortcut as the active source. The `K` monotonicity step is directionally wrong but appears locally repairable by retaining the strict contraction margin. The `lambda` coordinate needs a genuinely quantitative tuned-manifold argument.
2. **Dynamical-systems/stable-manifold analyst.** A uniformly bounded linear part is not a stable splitting. Relevant directions are exactly where tuning is expected; the theorem must identify which coordinates are solved backward/implicitly and give the contraction/transversality constants for the graph transform.
3. **OS/transfer-Hamiltonian spectral specialist.** Even a repaired UVR3/UVR4 construction would not by itself close the mass-gap root. It still must bind the resulting continuum theory to the same gauge-invariant OS source algebra/transfer Hamiltonian and physical-time gap.
4. **Asymptotic-freedom/coupling-normalization specialist.** `Delta g -> 0` cannot silently stand in for `Delta u -> 0`; coupling asymptotics and counterterm/relevant-coordinate universality are distinct typed coordinates.
5. **Adversarial mathematical physicist.** The scalar controls satisfy the exposed inequality classes while violating the target conclusions, so they falsify the inference from the displayed hypotheses. They do not falsify Yang–Mills or any stronger unexposed theorem.
6. **Primary-source/provenance auditor.** R17 missed a directly adjacent Section 38 and must be corrected. Direct PDF retrieval remains blocked, so exact page-by-page verification is outstanding.
7. **RAKL v3 metrology/authority auditor.** Same-context role separation earns `0/3` independent-review credit. Episode, diagnosis, process failure, and shadow obstruction remain distinct; no protected lesson or obstruction is admitted.

## Episode -> diagnosis -> obstruction/lesson boundary

- **Episode:** `EP-YM-S1a2g-R18-20260812` audited the current manuscript's Section 38 after correcting the R17 source-coverage miss.
- **Diagnosis:** `DG-YM-S1a2g-R18-UVR3-INVARIANCE-AND-UNIVERSALITY-NOT-CLOSED-BY-DISPLAYED-BOUNDS`.
- **Process/source failure:** `F-YM-S1a2g-R18-R17-SECTION38-MISSED-SOURCE-COVERAGE`.
- **Shadow mathematical obstructions:** `OBS-YM-S1a2g-R18-RELEVANT-STABLE-SPLITTING-UNBOUND` and `OBS-YM-S1a2g-R18-DELTA-U-TO-DELTA-G-SUBSTITUTION-UNBOUND`.
- **Reusable lesson:** proposal only — keep irrelevant contraction, relevant tuning, coupling asymptotics, regulator comparison, and OS/spectral transport as distinct typed coordinates. A theorem label such as “stable manifold” does not license a cross-regulator or spectral pushforward without its quantitative interface.
- **Authority:** no protected memory admission or scientific-authority transition requested.

## Prior experience that changed routing

- `YM-S1a2f-R17-PR290` was selected as immediate negative/source history but corrected because Section 38 was missed.
- `YM-R10-STABLE-COORDINATE-PR193` changed verification: it forced separate typing of raw `K`, relevant `lambda`, and marginal/coupling flow and prompted scalar hostile controls instead of accepting “stable manifold” as an operator certificate.
- PR #256/#258 were retrieved but rejected from the active move because they are live fixed-cutoff OS/transfer work and do not answer this UVR3 coordinate.
- Brydges–Slade IV/V were retrieved as solved rigorous-RG structural analogues, then rejected for theorem transfer because of explicit model/gauge/OS/spectral DifferenceWitnesses.
- No cross-Millennium theorem was transferred.

## Failure classification

- **Local mathematical failure:** present, narrowly, for the exposed `g_{k+1}<=g_k` inference used to strengthen a `K` bound to the smaller `g_{k+1}^2` radius.
- **Local proof/source insufficiency:** present for the `lambda` invariant/stable-manifold step under only the displayed bounded-`A_k` hypotheses.
- **Retrieval/decomposition/source failure:** present in R17 because Section 38 was missed.
- **Representation/type failure:** present if bounded relevant transport is treated as contraction, or if `Delta g` is treated as the full `Delta u`.
- **Local-to-global / same-theory gluing failure:** present in the regulator-universality handoff unless a regulator-matched stable-graph/intertwining estimate is source-bound.
- **Verification/tooling limitation:** full PDF verifier audit blocked by source retrieval.
- **No Yang–Mills counterexample and no theorem-nonexistence result.**

## Saturation / novelty / next discriminator

Reopened proposal/shadow axes: `KNOWLEDGE`, `OBSTRUCTION`, `RELATION`, `PATH`, because Section 38 changes the source state and exposes narrower interfaces. The fixed-cutoff `OPERATOR` lane is flattened for this cycle due live PR #256/#258. Protected retained novelty is zero on all seven axes.

The solved subproblem “do the exposed inequalities, by themselves, imply the claimed shrinking invariant ball/full difference decay?” is **compositional / RAKL_TRIVIAL**: it is resolved by elementary inequality checking and hostile scalar controls, not by a new Yang–Mills theorem.

Next discriminator, in order:
1. source-bind the missing quantitative `K` ratio margin and decide whether D1 is fully repaired;
2. locate or derive the exact stable/unstable splitting and graph-transform constants for `lambda`, including how tuning is performed;
3. prove a regulator-matched estimate carrying `Delta lambda` from `(Delta g,Delta K)` to zero;
4. only after UVR3/UVR4 are source-certified, return to the same-theory OS/transfer observable and regulator-uniform physical mass normalization.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.
