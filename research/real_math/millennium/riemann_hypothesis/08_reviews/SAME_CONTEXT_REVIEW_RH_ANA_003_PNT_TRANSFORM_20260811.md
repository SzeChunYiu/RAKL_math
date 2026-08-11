# RH-ANA-003 same-context expert review

**Authority:** role-separated same-context AI review. This is not independent peer review and grants no theorem or root authority.

## Shared packet

- Root contract: `00_problem_contract/success_contract.yaml`
- Active atom: `02_problem_dag/RH_ANA_003.yaml`
- Frozen context: `01_frontier/RH_ANA_003_CONTEXT_FIBER_20260811.json`
- Source reconstruction: `01_frontier/RH_ANA_003_PNT_ERROR_TRANSFORM_20260811.md`
- Dual memory: `07_memory/RH_ANA_003_RESEARCH_MEMORY_REVIEW_20260811.json`

## Expert cell

### Domain/theory lead

**Background/role:** analytic number theory, explicit formulae, Li criterion, prime-number-theorem error terms.  
**Finding:** the useful new coordinate is not another positive surrogate but the exact signed transform of `E(x)=psi(x)-x` obtained after preserving Lagarias' regularization. The algebraic collapse to `K_n(t)=L_{n-1}^{(1)}(-t)` is source-derived and should be treated as localization, not novelty.  
**Strongest objection:** fixed-`n` integration by parts does not by itself give any uniform-in-`n` estimate.  
**Vote:** ACCEPT the context localization; BLOCK any theorem candidate.

### Analogy/method-transfer lead

**Background/role:** harmonic analysis, transforms, asymptotics, structural transfer.  
**Finding:** the high-order-filter analogy is useful only to distinguish magnitude information from signed/correlation information. It suggests a discriminator: audit the induced family majorant before spending effort on sharper pointwise PNT constants.  
**Strongest objection:** the arithmetic error is not arbitrary bounded noise, so adversarial alignment cannot be transferred as an arithmetic counterexample.  
**Vote:** ACCEPT as proposal-routing evidence only.

### Adversarial falsification lead

**Background/role:** counterexample design and proof-strategy stress testing.  
**Finding:** any argument that extracts a one-sided Li conclusion from a symmetric pointwise envelope without an additional signed/correlation input should be challenged by the hostile envelope-alignment control `epsilon_host(t)=B(t) sgn W_n(t)`. This tests the inference rule, not zeta.  
**Strongest objection:** a sufficiently small absolute majorant could still imply the desired inequality, so the hostile-sign observation alone does not falsify all pointwise-bound routes. A quantitative family comparison is required.  
**Vote:** REVISE the broad no-go claim to the narrower quantitative discriminator.

### Formal-methods lead

**Background/role:** exact statement binding, indexing/sign audits, proof obligations.  
**Finding:** the key identities are internally consistent with Lagarias' equations (4.11)-(4.13): the two alternating signs cancel in `S_f`, and the continuous counterterm is the antiderivative of the associated-Laguerre kernel. Small-`n` checks `K_1=1`, `K_2=t+2`, `K_3=t^2/2+3t+3` are consistent.  
**Strongest objection:** the lower endpoint and Stieltjes convention must remain explicit, and no `n->infinity`/regularization interchange has been proved.  
**Vote:** ACCEPT the fixed-`n` transform identity; BLOCK uniform asymptotics.

### Novelty/research-value lead

**Background/role:** prior-art boundaries, explanatory value, search information gain.  
**Finding:** the transform is an algebraic re-expression of known arithmetic Li formulas and is not claimed as new mathematics. Its research value is operational: it converts the vague `prime/archimedean cancellation` residual into a precise one-sided family-transform obligation and separates what current PNT magnitude theorems do and do not provide.  
**Strongest objection:** before any publication-level novelty language, search specifically for prior analyses of the same associated-Laguerre/PNT-error transform.  
**Vote:** ACCEPT as internal problem decomposition; NOVELTY UNASSESSED.

## Synthesis and next action

All five lenses agree that candidate generation should remain blocked. The cheapest next discriminator is **not** a new RH inequality. It is a quantitative, source-bound audit of

`M_n(B) = integral B(t) |W_n(t)| dt`

against the exact threshold `S_infty(n)-n+1`, using a current primary-source PNT envelope and explicitly separating finite calibration from an all-`n` proof. If that sign-blind majorant is not competitive, open the residual `which weakest zeta-specific signed/correlation statistic of E changes the transform bound?` and audit whether that statistic is strictly weaker than RH.

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`.
