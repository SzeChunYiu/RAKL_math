# RH-SPEC-002a same-context expert review

**Review authority:** role-separated same-context research review only. These roles are not independent peer reviewers and do not satisfy any root-review requirement.

**Atom:** `RH-SPEC-002a` — source-side ground-state identification / determinant compactness.

## Expert cell

### 1. Analytic number theory / entire-function lead

**Background:** explicit formulas, Xi entire function, Fourier/Mellin transforms, zero transport.

**Evidence inspected:** CCM Theorem 5.10 and Sections 7–8; the merged RH-SPEC-002 retrospective calibration; the conditionally reusable Hurwitz/Rouche tool.

**Finding:** the target-side analytic implication is already comparatively clean. If the actual normalized source determinant converges locally uniformly to nonzero Xi on a root-relevant domain and the finite-stage zeros are real, zero transport follows. The hard step is upstream: replace the prolate proxy by the true Weil ground state with a weighted estimate strong enough for compact-uniform transform convergence.

**Strongest objection:** an `L2` or pointwise comparison on expanding intervals can be too weak off the real axis because the Fourier/Mellin weight grows exponentially in the imaginary direction.

**Vote:** `ACCEPT_REPRESENTATION / BLOCK_THEOREM_CANDIDATE`.

### 2. Spectral/operator perturbation lead

**Background:** self-adjoint forms, isolated eigenspaces, Kato/Davis–Kahan style perturbation, Rayleigh–Ritz.

**Evidence inspected:** lower-bounded `QW_lambda`, finite restrictions `QW_lambda^N`, simple/even hypothesis in CCM, current failure memory on resolvent incompleteness and spectral pollution.

**Finding:** the missing proxy-to-ground-state step should be treated as a **conditioned eigenspace-identification** problem. A small energy, small lowest eigenvalue, or small approximate-eigenvector residual is meaningful only relative to the separation between the lowest relevant eigenspace and competitors. The next source-side discriminator must expose that denominator rather than hide it.

**Strongest objection:** a gap-based theorem cannot assume a uniform positive gap; simplicity/evenness and quantitative gap behavior are themselves unresolved source obligations.

**Vote:** `ACCEPT_GAP_RESIDUAL_DISCRIMINATOR / BLOCK_UNIFORM_GAP_ASSUMPTION`.

### 3. Weil-form / prolate-transfer lead

**Background:** Weil quadratic form, prolate time-frequency concentration, source-specific operator geometry.

**Evidence inspected:** CCM prolate proxy `k_lambda`, Lemma 7.3, Section 8 missing steps, the source discussion comparing tiny Weil eigenvalues with prolate concentration defects.

**Finding:** the source gives a real transfer target rather than a superficial analogy: the prolate proxy has the desired analytic limit, while the Weil ground state generates the real-zero determinant. But neither similar small eigenvalues nor numerical profile proximity proves the vectors coincide. A valid transfer must derive a quantitative comparison from the trace-formula relation or another source identity.

**Strongest objection:** there may be no operator-norm perturbation `QW_lambda - PW_lambda` small enough for a direct Davis–Kahan application. The residual should therefore be defined source-first; form-theoretic or compactness/uniqueness alternatives must remain open.

**Vote:** `REVISE_TO_SOURCE_COMPUTABLE_RESIDUAL`.

### 4. Adversarial functional-analysis lead

**Background:** spectral instability, near degeneracy, counterexample design.

**Evidence inspected:** RH-SPEC-002 failures for strong-resolvent incompleteness, Galerkin pollution, joint-limit ambiguity and finite-zero-prefix overreach.

**Finding:** the cheapest new hostile control is a two-mode self-adjoint family with a collapsing ground-state gap. It should demonstrate that absolute residual or Rayleigh excess can tend to zero while the approximate vector stays a fixed angle from the true ground state if the residual is not small relative to the gap.

**Strongest objection:** bottom-of-spectrum approximation is less exposed to classic interior spectral pollution, so reusing the old pollution example alone would be low-information. The new calibration must specifically attack **ground-state conditioning**.

**Vote:** `ACCEPT_NEW_HOSTILE_CONTROL / REJECT_REPEAT_OF_OLD_POLLUTION_ONLY`.

### 5. Formal methods / assurance lead

**Background:** statement binding, chronology, proof obligations, verifier trust.

**Evidence inspected:** current RAKL `AGENTS.md`, `skills/rakl-core/workflows/mathematical-research.md`, the PR15 chronology failure now retained in RH memory, and the new context/memory packet.

**Finding:** this cycle must stop before candidate generation. The next exact calibration/evaluator identity must be frozen in repository state before any evaluated source result. The packet must bind the current RH tool/failure snapshots exactly and preserve the distinction between a standard perturbation theorem, its source-specific applicability proof, and any new mathematical claim.

**Strongest objection:** a later-written trace timestamp cannot repair candidate/evaluator chronology; exact committed identity is required.

**Vote:** `PASS_PRE_CANDIDATE_ONLY / BLOCK_RESULT_ACCESS_BEFORE_EVALUATOR_FREEZE`.

### 6. Novelty / research-value lead

**Background:** source comparison, rediscovery risk, research portfolio control.

**Evidence inspected:** CCM 2025, Connes–van Suijlekom 2025, current RH issue #3 and recent RH application history.

**Finding:** residual-over-gap perturbation theory is standard mathematics, not a novelty claim. The research value lies in **re-representing the CCM missing step into falsifiable atomic obligations** and determining whether the actual arithmetic source supplies the numerator and denominator required by a known stability theorem. A future source-specific estimate could be interesting, but novelty must be searched only after truth assurance.

**Strongest objection:** presenting the conditioning reframing as a new RH theorem would overclaim. It is currently search-control structure.

**Vote:** `ACCEPT_RESEARCH_CONTROL_GAIN / NO_NOVELTY_AUTHORITY`.

## Joint discussion and delegation result

The cell considered four next moves:

1. immediately conjecture `xi_lambda ≈ c_lambda k_lambda`;
2. assume the lowest Weil eigenvalue is enough to control the eigendirection;
3. jump to a de Branges/canonical-system positivity formulation;
4. freeze a **ground-state gap/residual calibration** that first distinguishes well-conditioned from nearly-degenerate proxy identification.

Moves 1–3 are rejected before candidate generation. Move 4 has the highest expected epistemic contraction because it can split the route cleanly:

- if the actual source lacks usable spectral separation or the proxy residual is not asymptotically smaller than that separation, a broad class of perturbative identification routes is pruned;
- if the needed rate relation survives, standard isolated-eigenspace machinery becomes legitimately applicable and exposes a narrower source theorem to prove;
- if operator residuals are unavailable, the failure itself motivates a compactness-plus-uniqueness or form-theoretic child instead of another unconstrained guess.

## Frozen recommendation

After machine audit of the strict packet, freeze an exact `RH-SPEC-002A-GAP-RESIDUAL-CALIBRATION` evaluator **before** inspecting evaluated source quantities. It must include:

- a two-mode near-degeneracy planted negative control;
- explicit definitions for the relevant parity-sector ground gap and proxy residual/Rayleigh excess;
- fixed-`lambda`, `N -> infinity` versus outer `lambda -> infinity` order;
- a weighted source norm sufficient for compact-uniform transform convergence on a frozen substrip;
- positive, negative and `CANNOT_CHECK` branches.

No candidate theorem has been generated by this review.

**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`.
