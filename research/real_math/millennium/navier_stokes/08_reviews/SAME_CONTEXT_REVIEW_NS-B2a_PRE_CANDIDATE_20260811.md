# Same-context expert review — NS-B2a pre-candidate gate

Frozen context packet: `sha256:a480d04f46ad09b5db95a45fb85d35edfcfc2e8afa22e3fc41fa73ee4ed191f9`  
Framework authority: `SzeChunYiu/RAKL@a151d5612709ea0f95c3ea232630f246f722739a`  
Application base: `SzeChunYiu/RAKL_math@7548c3c9a30c63e18956aefb68674d523acfe937`

## Shared statement

The cell reviews only the following question: in Seregin arXiv:2606.29468v1, Theorem 3.1, F=1 Type-II branch, does the source-supported ancient **Euler** blow-up profile carry enough inherited far-field information for a rigorous rigidity contradiction, and what exact atom is missing?

No member may import Navier–Stokes backward uniqueness, global finite energy, global L3, self-similarity, almost-periodicity, or spatial decay unless it is separately source-bound.

## Role-separated review

### 1. Type-II/local-energy PDE analyst

Background: suitable weak Navier–Stokes solutions, local energy inequalities, singularity blow-up scaling.

Finding: the rescaled viscosity coefficient tends to zero, so the limiting PDE class is Euler. The source route is valid as a classification/extraction mechanism in its stated branch. `(3.5)` and `(3.8)` must remain attached to the exact source hypotheses.

Atomic objection: the classification alone is not a rigidity theorem; the source does not hand us the global tail control needed to close the blow-up contradiction.

Verdict: `PASS_SOURCE_CLASSIFICATION / RIGIDITY_OPEN`.

### 2. Concentration-compactness / critical-element analyst

Background: profile decompositions, noncompact symmetries, minimal counterexamples.

Finding: the extraction is local and therefore compatible with translation/dilation escape. Nothing in the frozen packet supplies a global critical norm, minimal blow-up threshold, stability theorem, or almost-periodicity modulo symmetries.

Atomic objection: a critical-element argument would be circular if its compactness conclusion were used to create the far-field tightness that the argument itself requires.

Verdict: `PROFILE_LEAKAGE_UNCONTROLLED / MINIMAL_ELEMENT_TRANSFER_NOT_YET_LICENSED`.

### 3. Pressure/localization analyst

Background: Calderón–Zygmund pressure recovery, local pressure decompositions, localized energy flux.

Finding: local normalized pressure convergence is sufficient for the source's local limit passage, but does not determine the behavior of the harmonic/far-field pressure contribution on expanding balls.

Atomic objection: an incoming-energy estimate must include pressure flux. A velocity-only shell estimate cannot simply discard the nonlocal pressure term.

Verdict: `LOCAL_PRESSURE_PASS / FAR_FIELD_PRESSURE_OPEN`.

### 4. Rigidity / unique-continuation analyst

Background: parabolic backward uniqueness, Liouville theorems, Euler rigidity.

Finding: generic Navier–Stokes backward uniqueness is inapplicable after the viscosity coefficient vanishes. The retrospective backward-smallness calculation only gives local decay along selected times tending to minus infinity.

Atomic objection: no theorem has been bound that propagates this local ancient-Euler smallness forward to all times under only `(3.5)` and local energy.

Verdict: `NS_BACKWARD_UNIQUENESS_VETOED / EULER_NATIVE_RIGIDITY_REQUIRED`.

### 5. Vorticity/geometric-depletion analyst

Background: Euler vorticity transport/stretching, direction coherence, geometric depletion.

Finding: the Euler limit offers a natural vorticity formulation, but no inherited direction-coherence, depletion, enstrophy, or global vorticity-integrability hypothesis is present in the source packet.

Atomic objection: local depletion cannot be promoted to global control without a quantitative transport/flux statement compatible with the far field.

Verdict: `VORTICITY_ROUTE_PROPOSAL_ONLY / NO_INHERITED_DEPLETION_ASSUMPTION`.

### 6. Adversarial / formal-assurance analyst

Background: counterexample construction, proof-state chronology, public trace assurance.

Finding: a compactly supported steady Euler field is a tempting falsifier but violates the F=1 gradient spacetime growth bound, so it does not refute the exact class. The backward-smallness consequence was derived before the new context was frozen and therefore receives zero strict preregistration credit.

Atomic objection: do not relabel retrospective insight as a candidate or use an inapplicable Euler construction as a refutation.

Verdict: `GAVRILOV_DIRECT_FALSIFIER_REJECTED / CHRONOLOGY_ENFORCED`.

## Cell discussion and consensus

The six reviews agree on the same bottleneck. Seregin's fresh route changes the limiting equation class and thereby invalidates a common Type-I closure reflex. The most informative next atom is not another local regularity estimate; it is a pressure-aware far-field inheritance problem across the singular scaling.

Consensus:

`SOURCE_ROUTE_VALID_AS_CLASSIFICATION / LIMIT_IS_EULER / GENERIC_NS_BACKWARD_UNIQUENESS_INAPPLICABLE / FAR_FIELD_INCOMING_FLUX_UNCONTROLLED / RETROSPECTIVE_CALIBRATION_ONLY / ROOT_AUTHORITY_NONE`.

## Chosen next step

Bind the weakest no-incoming-energy/far-field-tightness statement that can be proved on the **rescaled Navier–Stokes sequence before passage to the limit**, including pressure flux, and test whether it is stable as `f(λ)->0`.

Alternatives rejected for the next step:

- invoke Navier–Stokes backward uniqueness — wrong PDE class;
- assume global finite energy or L3 — not inherited;
- force a minimal critical element — no frozen minimality/stability theorem;
- assume self-similar/periodic orbit — source branch is more general;
- infer rigidity from the retrospective local backward-smallness lemma alone — far field remains open.

No theorem candidate is generated in this packet.
