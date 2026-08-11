# Same-context expert review — RH-ANA-002 prime-side strength audit

**Context hash:** `sha256:e18ec3c2a81fb33d9b3d12c927da9778f899e64fef8edaa067224904df60e796`  
**Review class:** same-context multidisciplinary cell; **not** independent mathematical review.  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`.

## Team and delegated roles

### 1. Analytic number theorist — Li/xi semantics lead
**Background:** zeta/L-functions, Li and Weil criteria, explicit formulas.  
**Evidence inspected:** Lagarias 2007 arithmetic decomposition; Bombieri–Lagarias criterion; RH-ANA-001 calibration.  
**Finding:** the useful object is not “more positive Li coefficients” but the implication-strength of a zeta-specific bound on the finite-place residual.  
**Strongest objection:** the arithmetic split can simply relocate the root difficulty.  
**Delegated check:** classify any proposed residual estimate as partial, root-strength, or circular before proof search.  
**Vote:** `ACCEPT_PRE_CANDIDATE_REFRAME`.

### 2. Explicit-formula / prime-sum specialist — regularization lead
**Background:** von Mangoldt sums, logarithmic derivatives, Guinand–Weil formula, Tauberian/cutoff analysis.  
**Evidence inspected:** Lagarias equations for `S_f`, the regularized zeta coefficients, and the Li-test-function cutoff discussion.  
**Finding:** termwise sign or absolute-value domination is structurally suspect because the finite-prime expression is defined through cancellation with a subtraction/cutoff term.  
**Strongest objection:** a pretty prime formula may be invalid after changing summation order or discarding the renormalizing subtraction.  
**Delegated check:** every future candidate must state cutoff, subtraction, order of limits, and uniformity in `n`.  
**Vote:** `ACCEPT_WITH_REGULARIZATION_GUARD`.

### 3. Zero-free-region specialist — graded-progress lead
**Background:** classical zero-free regions, Li-type zero-exclusion criteria.  
**Evidence inspected:** Brown 2005 abstract-level finite-prefix/region relation; Freitas 2005 parameterized criterion; Bellotti–Trudgian–Yang 2026 explicit region.  
**Finding:** finite Li information has a legitimate partial output: a quantified zero-free region. This supplies a graded target coordinate between finite computation and RH.  
**Strongest objection:** Brown's detailed internal constants should not be imported without a correction audit.  
**Delegated check:** freeze an exact partial zero-free target and compare it to current source bounds before candidate generation.  
**Vote:** `ACCEPT_PARTIAL_REGION_COORDINATE`.

### 4. Adversarial asymptotic analyst — root-equivalence/falsification lead
**Background:** asymptotic analysis, oscillatory sums, adversarial counterexamples.  
**Evidence inspected:** Lagarias incomplete-Li formula and RH-failure exponential alternative; `T-XM-ROOT-BRIDGE-STABILITY-AUDIT`; RH-ANA-001 quartet.  
**Finding:** a uniform polynomial bound on exact `S_f(n)` is already root-strength. Treating it as a “prime-side lemma” would be false decomposition of difficulty.  
**Strongest objection:** the route-strength corollary is source-derived and should not be advertised as a new theorem.  
**Delegated check:** apply the root-bridge audit to every proposed global residual bound and the quartet calibration to every finite-prefix surrogate.  
**Vote:** `REJECT_GLOBAL_POLYNOMIAL_SF_AS_CHILD_TARGET`.

### 5. Formal methods / assurance specialist — gate and identity lead
**Background:** RAKL mathematical assurance, context/memory/trace audits, exact statement binding.  
**Evidence inspected:** current RAKL `55d4cb0a83f271d3263fbe48f99b173119c732d2`, current mathematical-research workflow, current RAKL_math agent contract.  
**Finding:** this cycle can freeze source-bound route classification, but no candidate may appear before context, dual-memory review and trace pass current gates. The repository submodule pin is reproducibility metadata and is older than current RAKL main, so exact-head research CI must also check current RAKL main.  
**Strongest objection:** passing the pinned application suite alone would not certify compliance with a newer framework head.  
**Delegated check:** add a strict packet regression and require PR CI/status before merge.  
**Vote:** `ACCEPT_PRE_CANDIDATE_ONLY`.

### 6. Novelty / research-value reviewer — redundancy and frontier lead
**Background:** literature mapping, equivalence detection, research-program prioritization.  
**Evidence inspected:** Lagarias, Brown, Freitas, current zero-free-region source, prior RH workspace.  
**Finding:** the formulas and implication relationships are source-bound known mathematics. The research value is route pruning: it prevents spending cycles on an RH-equivalent prime-growth target disguised as a smaller lemma.  
**Strongest objection:** another equivalent criterion without a cheaper independently provable obligation has near-zero frontier value.  
**Delegated check:** candidate search may resume only at a target demonstrably between current partial zero-free results and root-strength all-index control.  
**Vote:** `ACCEPT_ROUTE_PRUNING / NO_NOVELTY_CLAIM`.

## Cell synthesis

Unanimous on the control decision:

1. Preserve `RH-ANA-001` as the exact finite-prefix falsifier.
2. Reuse `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` only through the recorded DifferenceWitness.
3. Reject “prove `S_f(n)=O(n^A)` for all `n`” as a supposedly cheap child atom; Lagarias' source results make that endpoint root-strength.
4. Re-represent the frontier as a **graded zero-exclusion problem**.
5. Next candidate, if exact-head gates pass, must target one explicit partial zero-free region stronger than a registered baseline yet strictly weaker than RH.

## Breakthrough-learning disposition

- `REFLECTIVE_RESTRUCTURE`: yes — replace binary finite-prefix/root framing by an implication-strength ladder.
- `CONTRASTIVE_DISCRIMINATION`: yes — Brown/Freitas partial regions versus Lagarias root-strength all-`n` growth.
- `FIXATION_RESET`: bounded — stop treating “prime-side formula” as automatically simpler.
- `EFFECTUAL_PROBE`: yes — select a partial zero-free target whose success/failure changes the information state.
- `EXPLORATORY_RECOMBINATION`: not yet — no distant mechanism is allowed until the partial target and cutoff contract are frozen.

These are search-policy recommendations only.

**Authority:** `STRICT_PRE_CANDIDATE_SAME_CONTEXT_REVIEW / SOURCE_BOUND_ROUTE_PRUNING / NO_CANDIDATE / NO_NOVELTY / ROOT_AUTHORITY_NONE`.
