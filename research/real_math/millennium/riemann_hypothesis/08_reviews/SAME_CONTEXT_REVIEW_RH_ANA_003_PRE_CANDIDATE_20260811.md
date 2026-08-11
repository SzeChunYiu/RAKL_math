# RH-ANA-003 same-context expert review — pre-candidate

**Status:** `SAME_CONTEXT_ROLE_SEPARATED / NOT_INDEPENDENT_REVIEW / PRE_CANDIDATE`  
**Atom:** `RH-ANA-003`  
**Framework:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application base:** `SzeChunYiu/RAKL_math@8a608f340d47b4b6ae612275b0595faf6b804432`

This is one coordinated same-context expert cell. The roles are analytical lenses, not distinct external reviewers.

## Domain / Li-explicit-formula lead

**Background lens:** analytic number theory, zeta/L-functions, Li and Weil criteria.

**Finding.** The useful source cut is Lagarias' separation of the finite-place term from the archimedean term. Theorem 6.1 ties `S_f(n,pi)` to an incomplete Li coefficient at height about `sqrt(n)`, while the small incomplete-Li estimate is explicitly RH-conditional. The next action should therefore audit the *logical sufficiency* of proposed unconditional controls on this truncated power sum.

**Strongest objection.** Merely rephrasing the root as a uniform bound for the incomplete Li sum may have no localization value if the bound is itself equivalent to excluding all off-line zeros.

**Recommendation.** Run an inference-falsification audit before proposing a new bound.

## Prime / cancellation lead

**Background lens:** Euler products, logarithmic derivatives, regularized prime sums, binomial cancellation.

**Finding.** Bombieri–Lagarias/Lagarias arithmetic formulas are exact but signed and highly cancellative. A direct prime-side route remains viable in principle because cancellation can exploit arithmetic structure that a zero-density abstraction discards.

**Strongest objection.** Do not overgeneralize a failure of density-only control into a failure of explicit-formula or prime methods.

**Recommendation.** If density-only is pruned, preserve a separate direct-prime residual: identify the exact regularized remainder and prove a uniform estimate without termwise absolute-value destruction.

## Zero-density / zero-free lead

**Background lens:** zero counting, density estimates, zero-free regions, explicit zero detection.

**Finding.** Count/density and radial location are different coordinates for Li power sums. Palojärvi's results are a useful source-bound calibration because a finite interval of Li-type coefficients can detect/exclude zeros outside a radial region under explicit hypotheses.

**Strongest objection.** Strong density theorems sometimes encode horizontal location information, so the phrase “density is insufficient” must be scoped to premises that permit at least one fixed off-line radial outlier.

**Recommendation.** State the falsifier condition precisely: any proposed density/counting premise is rejected as sufficient if it remains compatible with one symmetry-respecting off-line quartet of fixed height/radius.

## Adversarial falsification lead

**Background lens:** counterexample construction, extremal cases, inference testing.

**Finding.** Use the exact radial identity `|1-1/rho|^2 = 1 + (1-2 Re(rho))/|rho|^2`. A single member with modulus `>1` yields power amplification. Pair it with the functional-equation and conjugation partners so that the hostile world preserves the same basic symmetry used in the previous Li-prefix calibration.

**Strongest objection.** Phase cancellation could hide the large modulus at selected indices.

**Recommendation.** The falsifier should claim only that aggregate count does not uniformly bound the power sum. For an outlier radius `R>1`, elementary power-sum/phase arguments or the existing exact quartet calibration provide indices with large contribution; no claim about every `n` is needed.

## Formal-methods / authority lead

**Background lens:** statement binding, chronology, verifier trust, authority separation.

**Finding.** `RH-ANA-003` is still `CONTEXT_REQUIRED`, so no new mathematical inequality can be proposed until the new context, memory and trace are frozen. Source facts must label RH-conditional inputs explicitly.

**Strongest objection.** A synthetic quartet can falsify an inference form but cannot be promoted to a zeta counterexample or to a theorem about all density methods.

**Recommendation.** Authority label the resulting audit `ROUTE_PRUNING_CALIBRATION_ONLY`; if it succeeds, open a narrower child rather than claiming progress on the root.

## Novelty / research-value lead

**Background lens:** prior-art distinction, explanatory value, information gain.

**Finding.** The radial mechanism itself is classical Li-criterion structure, so no mathematical novelty should be claimed. The research value lies in process localization: distinguishing population-count information from the root-critical radial/weighted coordinate, and making that distinction reusable in the RAKL method case study.

**Strongest objection.** A manuscript could overstate “new insight” when the mathematical content is a repackaging of known Li theory.

**Recommendation.** Classify any solved subproblem as `TRANSFER_NOVEL` or route-pruning calibration at most; retain `OPERATOR` novelty at zero.

## Cell synthesis

**Agreement.** Do not invent a new Li positivity inequality in this cycle. The highest-information action is a source-bound hostile audit of the implication

```text
aggregate zero count/density + standard explicit-formula bookkeeping
    =>
uniform incomplete-Li / finite-place control.
```

**Scoped discriminator.** Preserve the count/density premise while allowing one symmetry-compatible radial outlier. If the incomplete-Li power sum can then exceed the claimed `O(sqrt(n) log n)`-type envelope along some indices after the cutoff includes that outlier, the premise is insufficient by itself.

**Open disagreement.** Whether a realistic *weighted* zero-density theorem can be strictly weaker than RH yet strong enough for the finite-place term is unresolved. The prime-side route may also exploit cancellation invisible in a zero-space formulation.

**Recommendation:** `PROCEED_WITH_ROUTE_PRUNING_CALIBRATION / NO_NEW_RH_CANDIDATE_YET`.
