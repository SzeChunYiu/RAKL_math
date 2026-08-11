# RH-SPEC-002a same-context pre-candidate expert review

Date: 2026-08-11. Review authority: `SAME_CONTEXT_ROLE_SEPARATED / NOT_INDEPENDENT / PRE_CANDIDATE_ONLY / ROOT_AUTHORITY_NONE`.

Active atom: `RH-SPEC-002a` — determine the weakest source-defined ground-state/prolate-proxy approximation that can transport the already-proved proxy transform limit to the actual semilocal Weil-form ground-state transform on every root-relevant closed substrip of `|Im z|<1/2`, while preserving the separate simple/even and finite-`N` obligations.

The cell reviewed `RH_SPEC_002A_CONTEXT_FIBER_20260811.json`, the source packet, the post-calibration dual memory, and the parent `RH-SPEC-002` calibration. These are analytical roles sharing the same evidence context; none counts as independent peer review.

## 1. Analytic number theory / Weil-form lead

**Background/role.** Explicit formulas, completed zeta/Xi normalizations, Weil quadratic forms, prime-power and archimedean terms. Owns the exact root mapping and source-side normalization.

**Evidence inspected.** CCM Theorem 1.1, Lemma 7.3, Sections 7–8; the exact RH root contract; parent spectral-limit calibration.

**Finding.** The child atom is materially sharper than the parent. The source itself places the relevant spectral variable at `Xi(z)=xi(1/2+i z)` and states that suitable convergence on closed substrips of `|Im z|<1/2` would entail RH. Requiring full-plane local-uniform convergence would therefore add theorem debt not demanded by this route. The source also proves the proxy-side transform convergence; the missing arithmetic bridge is the actual `xi_lambda` versus `c_lambda k_lambda` relation.

**Strongest objection.** A source-defined scalar `c_lambda` is load-bearing. A scalar selected by matching known zeta zeros or minimizing discrepancy against Xi would make the bridge circular even if the subsequent complex analysis were correct.

**Attempted falsifier.** Check whether the atom accidentally merges `N->infinity` and `lambda->infinity`. It does not: fixed-lambda finite-`N` determinant/eigenvector transport remains an explicit sibling obligation.

**Residual uncertainty.** It is not yet known whether the QW/prolate source identities yield any norm strong enough for transform convergence.

**Vote.** `ACCEPT_CONTEXT / PROCEED_ONLY_TO_NORM_AND_GAP_CALIBRATION`.

## 2. Functional analysis / spectral-operator lead

**Background/role.** Self-adjoint operators, quadratic forms, spectral perturbation, eigenspace stability and approximation theory. Owns simplicity/separation and state-vector transport.

**Evidence inspected.** CCM semilocal Weil operator setup and Section 8 missing steps; parent strong-resolvent and pollution calibrations; Kato-style eigenspace stability principle only at generic method-transfer level.

**Finding.** Qualitative simplicity and quantitative eigenspace stability must not be conflated. If the route tries to derive `xi_lambda ~ c_lambda k_lambda` from a small residual or a small operator discrepancy, the estimate must expose the separation of the lowest eigenvalue from the rest of the QW spectrum, or provide another source-specific rigidity mechanism. A nearly degenerate self-adjoint calibration can otherwise rotate the ground state by order one while scalar diagnostics look small.

**Strongest objection.** The source does not currently provide a generic operator-norm comparison `QW_lambda - PW_lambda` to which an off-the-shelf perturbation theorem can simply be applied. The relation is subtler and trace/form based; importing a perturbation theorem without constructing its exact hypotheses would be a false transfer.

**Attempted falsifier.** Reserve a two-by-two nearly degenerate family as the cheapest known-answer regression against any future residual-to-vector claim.

**Residual uncertainty.** The true QW ground-state gap may stay uniformly useful, shrink, or require a different rigidity coordinate; this cycle establishes no behavior of that gap.

**Vote.** `ACCEPT_CONTEXT / REQUIRE_SEPARATION_OR_ALTERNATE_RIGIDITY_WITNESS`.

## 3. Complex analysis lead

**Background/role.** Holomorphic convergence, normal families, Hurwitz/Rouché zero transport, Fourier/Laplace transforms in complex strips. Owns the target topology.

**Evidence inspected.** Parent `T-RH-SPEC-HURWITZ-DOMAIN-ZERO-TRANSPORT`, finite-zero-prefix failure, CCM strip convergence statement and proxy limit.

**Finding.** The target-side implication should be formulated domain-locally: for every `delta>0`, compact-uniform transform convergence on closed subsets of `|Im z|<=1/2-delta` is the natural root-relevant objective. An exact triangle-inequality bound from a substrip-weighted `L1` error is a useful positive calibration. Ordinary `L2` convergence on a growing logarithmic support is not automatically an adequate substitute because converting `L2` to `L1` can acquire a growing support/weight factor.

**Strongest objection.** A proposed function norm is not progress unless its continuity estimate is written against the exact Fourier/Mellin convention and lambda-dependent support. Saying “the vectors are close” without a transform-controlling norm leaves the critical coordinate unspecified.

**Attempted falsifier.** Reserve a growing-support family with vanishing unweighted `L2` norm but non-vanishing integral/transform at a fixed point to reject weak norm claims.

**Residual uncertainty.** The exact source convention and endpoint behavior under the map `E` may make a different weighted norm preferable.

**Vote.** `ACCEPT_CONTEXT / CALIBRATE_TRANSFORM_CONTINUITY_BEFORE_THEOREM_SEARCH`.

## 4. Prolate / harmonic-analysis lead

**Background/role.** Prolate spheroidal wave functions, concentration operators, Fourier eigenfunctions and asymptotic mode comparison. Owns the proxy chain `PW_lambda -> h_lambda -> k_lambda`.

**Evidence inspected.** CCM Lemmas 7.2–7.3 and Section 8 numerical/proxy discussion.

**Finding.** The proxy side is substantially solved at the authority needed for planning: `k_lambda` has a source-defined construction and its transform tends to Xi uniformly on the relevant closed substrips. Re-deriving that limit has lower information value than attacking the source-identified `k_lambda` versus ground-state relation.

**Strongest objection.** Prolate spectral stability does not automatically transfer to the semilocal Weil operator. The two objects share a deep relation in the source, but the exact state-comparison inequality is precisely what is missing.

**Attempted falsifier.** Reject any candidate whose only evidence is numerical overlap or matching low eigenvalues; demand a source-side residual/form identity plus the exact norm conversion.

**Residual uncertainty.** It is not known which prolate estimates survive the arithmetic `E` transform with constants strong enough as `lambda` grows.

**Vote.** `ACCEPT_CONTEXT / DO_NOT_RESEARCH_PROXY_LIMIT_AGAIN`.

## 5. Adversarial falsification lead

**Background/role.** Counterexample-first functional analysis and approximation pathology. Owns repeat-failure tests and representation mismatch detection.

**Evidence inspected.** Four `RH-SPEC-002` failure experiences, the proposed weighted transform bridge and the proposed eigenspace-stability transfer.

**Finding.** Two orthogonal calibrations have high partition power before any RH-specific theorem candidate:

1. a nearly degenerate `2x2` self-adjoint family where a perturbation/residual vanishes in absolute size while the lowest eigenvector rotates by order one unless normalized by the spectral gap;
2. a growing-domain error family where unweighted `L2 -> 0` but a relevant transform functional remains order one, exposing the missing support/weight factor.

These tests discriminate whether a future argument controls the load-bearing coordinate rather than merely producing another small scalar diagnostic.

**Strongest objection.** Generic counterexamples are warnings, not evidence that the actual CCM route fails. Any negative transfer must include a DifferenceWitness showing that the target candidate relies on the same insufficient implication.

**Attempted falsifier.** The two calibrations above are frozen as the next cheap regressions; no target-specific negative conclusion is drawn yet.

**Residual uncertainty.** A source-specific trace identity may provide a stronger coordinate that bypasses both generic failure modes.

**Vote.** `ACCEPT_CONTEXT / EXECUTE_CALIBRATIONS_FIRST`.

## 6. Formal methods / novelty and research-value lead

**Background/role.** Exact statement binding, artifact chronology, dependency DAGs, source equivalence and novelty boundaries. Owns the authority ceiling.

**Evidence inspected.** Current RAKL mathematical-research workflow, child context/memory hashes, source wording of the missing CCM steps, RH root issue.

**Finding.** `RH-SPEC-002a` is a legitimate decomposition of a source-stated missing step, not a new theorem. The route improvement is methodological: reduce the target topology to the minimal source-supported root domain, expose the state-vector norm and spectral-separation coordinates, then calibrate them before candidate generation.

**Strongest objection.** A future “lemma” that merely restates “if `xi_lambda` converges to `k_lambda`, then the transforms converge” has little research value unless it identifies a source-verifiable sufficient norm or derives the norm from QW/prolate structure.

**Attempted falsifier.** Compare every proposed statement to CCM Section 8 and reject paraphrased open obligations as novelty.

**Residual uncertainty.** No bounded novelty search for a future target theorem has been opened because no theorem candidate exists yet.

**Vote.** `ACCEPT_CONTEXT / NO_NOVELTY_AUTHORITY / NO_CANDIDATE_YET`.

## Cell synthesis

Unanimous disposition:

`STRICT_CONTEXT_ACCEPTED / SAME_CONTEXT_REVIEW_ONLY / PROCEED_TO_NORM_AND_GAP_CALIBRATION / NO_MATHEMATICAL_CANDIDATE_YET / ROOT_AUTHORITY_NONE`.

The selected next action is deliberately **not** to propose an RH lemma. First formalize and test the two load-bearing implication channels:

- exact substrip-weighted function error -> compact-uniform complex transform error;
- exact source residual/operator comparison + quantitative separation/rigidity -> normalized ground-state alignment.

If either implication is stated more weakly, the corresponding hostile calibration should reject it before target-specific proof search.
