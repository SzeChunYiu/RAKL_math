# NS-B1a3b — same-context expert cell

**Authority:** `SAME_CONTEXT_ROLE_SEPARATED_REVIEW / PROPOSAL_SHADOW / NOT_INDEPENDENT_PEER_REVIEW / ROOT_AUTHORITY_NONE`  
**Frozen:** 2026-08-11T15:08:00Z  
**Bound fibre:** `sha256:91eb597a06cb3f8ee7ccd4d2e617a16d137b3b200bccfa4ca0d3fb2d3cd33e75`

The cell reviewed only the pre-candidate question: whether the already registered Type-I compactness output is strong enough to transport a vorticity-direction/coherence observable into the ancient limit. It did not review a proposed proof of regularity.

## Roles and delegated findings

### 1. PDE regularity / scaling lead
Background: suitable weak solutions, blow-up rescaling, epsilon regularity and ancient-solution compactness.  
Finding: under `u_r(x,t)=r u(x0+rx,t0+r^2t)`, vorticity scales as `omega_r=r^2 omega` while `xi=omega/|omega|` is amplitude-invariant where defined. The stored Type-I passage supplies local strong `L^3` velocity compactness, not a stated strong `curl u` convergence. A geometric observable using `xi` therefore sits one derivative beyond the reported strong topology. Scaling itself does not repair that mismatch.

### 2. Vorticity geometry / method-transfer lead
Background: Constantin–Fefferman geometric depletion, strain/vorticity criteria and Biot–Savart nonlocality.  
Finding: the registered Constantin–Fefferman route is conditional: it consumes a quantitative coherence property of vorticity direction for an actual solution. Parent failure `F-NS-R001B-LOCAL-GEOMETRY-SCOPE-GAP` already forbids replacing this nonlocal coherence object by pointwise alignment. The present transfer must therefore test the exact direction observable rather than another alignment proxy.

### 3. Harmonic-analysis / pressure lead
Background: Calderón–Zygmund pressure localization, Riesz transforms and derivative estimates.  
Finding: local pressure decomposition is not the first missing map here. The interface `u -> curl u -> curl u/|curl u|` has derivative loss followed by nonlinear normalization. Neither local weak pressure convergence nor bounded first-derivative energy supplies continuity of that map. Pressure/far-field compatibility remains a later obligation if the derivative-topology gate is ever closed.

### 4. Adversarial falsification lead
Background: compactness counterexamples, oscillatory sequences and hostile scale tests.  
Finding: the cheapest discriminator is a smooth compactly supported divergence-free high-frequency sequence generated as a curl of a small vector potential. It can converge strongly to zero in `L^3_loc` with uniformly bounded `L^2` first-derivative energy while its vorticity has order-one magnitude and rapidly rotating direction on a fixed core. If verified, this falsifies only the abstract inference from the stored convergence modes to direction compactness; it is not a Navier–Stokes counterexample.

### 5. Formal methods / verifier-trust lead
Background: statement binding, dependency scopes, falsifier contracts and non-escalation.  
Finding: candidate scope must be syntactic and narrow: `stored compactness modes => stable vorticity direction`. Verification obligations are divergence-free identity, support/smoothness, `L^3` decay rate, uniform gradient-energy bound and explicit rotating vorticity on the core. The falsifier must not be used to claim that exact Navier–Stokes dynamics cannot supply extra compactness.

### 6. Novelty / research-value lead
Background: prior-art risk, structural fingerprints and route-value assessment.  
Finding: the functional-analytic construction is elementary and no new theorem novelty should be claimed. Research value, if the falsifier succeeds, is route pruning and representation of a hidden derivative/quotient interface. The strongest defensible novelty class is to be determined only after verification; theorem-level novelty remains `UNRESOLVED`.

## Disagreements and strongest objection

The geometry lead initially favored immediately searching for a scale-critical coherence estimate inherited by Type-I rescaling. The adversarial and formal leads objected that inheritance cannot be assessed until continuity of the geometric observable in the available compactness topology is checked. The PDE lead agreed that this topological gate is strictly cheaper and logically prior.

Strongest objection to the chosen test: the calibration sequence will not solve Navier–Stokes. Resolution: scope the conclusion only to insufficiency of the **reported compactness modes by themselves**; exact PDE structure remains an open possible repair.

## Recommendation

`PROCEED_COUNTEREXAMPLE_FIRST_INTERFACE_TEST`.

Do not propose a new geometric regularity theorem. First test whether local strong velocity convergence plus bounded derivative energy can transport vorticity direction. If the test fails, normalize the result as a derivative/normalization gluing obstruction and reopen the path only through a source-valid strong-vorticity/nondegeneracy or direct geometry-stability estimate.
