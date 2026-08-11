# Same-context expert cell — RH-SPEC-003 pre-candidate review

Atom: `RH-SPEC-003`  
Context packet: `sha256:90a186d8e391a32b0aaa061f3c9cd42ad009633caa0232f190562e894769d529`  
Decision: **PASS TO FROZEN NEXT-STEP ONLY; NO RH CANDIDATE OR ROOT AUTHORITY**

This is a role-separated same-context review of the frozen trace-class-threshold atom. The cell reviews the same assumptions and evaluator; it does not vote on a hidden proof.

## Delegation and findings

### 1. Operator theorist — domain, self-adjointness, compact resolvent, Schatten class

Background: unbounded self-adjoint operators, compact resolvent, functional calculus, Schatten ideals.

Assigned checks: make the operator hypotheses exact; verify that the proposed singular-value calculation is legitimate; identify the cheapest family-level contradiction.

Finding: the atom is well-posed only conditionally. For self-adjoint `H`, functional calculus makes `(I+H^2)^(-alpha/2)` positive and bounded. Under compact resolvent/discrete finite-multiplicity spectrum, its singular values are the stated spectral weights. The proposed endpoint falsifier is legitimate only after exact completeness/multiplicity gives the target counting law. A formal differential expression, symmetric operator, or numerically Hermitian matrix is insufficient.

Residual warning: a noncompact/continuous-spectrum realization is outside this filter.

### 2. Analytic number theorist — zero counting, multiplicity, RH binding

Background: zeta zeros, argument principle, Riemann–von Mangoldt counting, explicit formula.

Assigned checks: ensure the counting input is unconditional; prevent simple-zero or RH assumptions; audit one- versus two-sided counting conventions.

Finding: von Mangoldt's zero-counting law counts nontrivial zeros with multiplicity and is unconditional. The asymptotic `N(T) ~ (T/(2*pi)) log T` is enough for the threshold. A ± spectral duplication changes only a constant factor; a finite exceptional set changes finitely many summands. Neither affects convergence. No assumption that zeros are simple is permitted.

Residual warning: the counting law alone does not identify a Hilbert-space spectrum with the zeros.

### 3. Trace-formula / dynamical specialist — ordinary trace versus distributional trace and prime matching

Background: Selberg-style trace formulas, spectral distributions, periodic-orbit analogies, regularized traces.

Assigned checks: decide exactly what the no-go excludes; stop a Schatten calculation from being overread as a trace formula.

Finding: failure of `S_1` at first-order resolvent scale excludes an **ordinary** trace-class formula at that scale for an exact compact-resolvent HP spectrum. It does not exclude heat traces, stronger powers, relative traces, weak/Dixmier traces, zeta regularization, or distributional trace formulas. Each alternative requires its own definition and convergence/interchange proof. Zero counting supplies no prime weights or test-function identity.

Residual warning: “prime = periodic orbit” analogies have no authority until exact prime-power amplitudes and multiplicities are derived.

### 4. de Branges / canonical-systems specialist — representation and positivity circularity

Background: Hermite–Biehler/de Branges spaces, canonical systems, self-adjoint extensions.

Assigned checks: test whether the atom improperly assumes a de Branges positivity or representation equivalent to RH.

Finding: the atom does not require de Branges positivity. If a concrete canonical system is proposed later, its coefficients, Hilbert space, boundary conditions, self-adjoint extension, completeness and Xi identification must be established independently. A positivity criterion equivalent to RH cannot serve as an independent premise.

Residual warning: discrete real spectra inside an abstract canonical system do not provide the arithmetic identification.

### 5. de Bruijn–Newman / random-matrix specialist — flow and statistical calibration

Background: heat-flow deformation of Xi, zero statistics, random-matrix models.

Assigned checks: assess whether flow or GUE phenomena strengthen the threshold.

Finding: they do not. The threshold follows from the deterministic global count. Newman-flow or GUE observations may suggest operator models, but finite-zero location/correlation agreement cannot prove domain, self-adjointness, completeness, multiplicity, or trace legitimacy.

Residual warning: no numerical experiment should be accepted as evidence for the endpoint theorem.

### 6. Adversarial verifier — cheapest counterexamples and scope escapes

Background: proof auditing, counterexample design, limit/interchange failure modes.

Assigned checks: try to break the intended implication with convention changes or alternate trace notions.

Finding: finite eigenvalue modifications and ± duplication fail to repair endpoint divergence. The cheapest valid escapes are structural, not numerical: use stronger smoothing (`alpha*p>1`), rigorously regularize/distribute the trace, or leave the compact-resolvent class. These escapes must be typed rather than treated as contradictions to the no-go.

Residual warning: do not infer `(H-i)^(-1)` trace-class failure without self-adjointness, because the singular-value identity used at that step is part of the self-adjoint functional calculus.

## Cell synthesis

The six roles agree that the frozen atom is a useful **necessary-condition filter** and is materially orthogonal to the existing limit-stability work. It does not produce a Hilbert–Pólya operator, positivity theorem, prime trace formula, Xi representation, de Bruijn–Newman bound, or RH proof.

Candidate generation is acceptable only after the context packet, dual memory review and hash-chained pre-candidate trace pass the pinned framework audits. The first candidate must be the exact threshold statement registered in the precontext contract, with the endpoint divergence and exemptions explicit.
