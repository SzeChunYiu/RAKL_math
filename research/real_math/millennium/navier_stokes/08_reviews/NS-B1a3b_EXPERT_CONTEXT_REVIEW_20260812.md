# NS-B1a3b — seven-role expert context review

**Review class:** `SAME_CONTEXT_MULTIROLE / PRE_CANDIDATE / NO_INDEPENDENT_REVIEW_CREDIT`  
**Frozen fibre:** `sha256:4d62297d17027481b28283c707e69e79544c3866e82e66ff559eb8071af194b7`  
**Purpose:** adversarially select and constrain the next calculation before a result is written. Every role has access to the same frozen fibre, memory review, and primary-source audit; therefore this is deliberation, not an independent mathematical review.

## Expert cell and delegated responsibilities

1. **PDE / partial-regularity lead** — background in suitable weak solutions, local energy inequalities, epsilon regularity, and blow-up extraction. Delegated to bind the exact producer topology and identify what survives the Type-I limit passage.
2. **Vorticity geometry lead** — background in vortex stretching, direction coherence, flux methods, and geometric regularity criteria. Delegated to state the exact Lei–Ren–Tian consumer and distinguish range conditions from continuity conditions.
3. **Compactness / functional-analysis lead** — background in Sobolev compactness, weak convergence, concentration/oscillation, and Young-measure phenomena. Delegated to test continuity of `u -> curl(u)/|curl(u)|` under the registered convergence.
4. **Scaling / ancient-solution lead** — background in Navier–Stokes scaling, Type-I/II blow-up, self-similar/DSS/general ancient classes, and critical-element methods. Delegated to audit which symmetries and equation classes are actually relevant to this child.
5. **Adversarial-construction lead** — background in counterexample design for invalid functional inferences. Delegated to build the cheapest exact falsifier without presenting it as a Navier–Stokes solution.
6. **Proof-interface / formal-methods lead** — background in producer-consumer contracts, hypothesis ledgers, provenance, and proof DAGs. Delegated to keep episode, diagnosis, obstruction, and lesson distinct and to enforce root non-promotion.
7. **Frontier / novelty lead** — background in current regularity literature and source-lineage auditing. Delegated to search for recent geometric criteria and prevent source normalization or route pruning from being overstated as a new theorem.

## Round 1: role findings

### PDE / partial regularity

The registered blow-up machinery gives enough compactness to pass the velocity nonlinearity and suitable-weak structure locally. It does not state a strong convergence theorem for `nabla u_n` or `omega_n`. Local energy bounds supply an `L2` bound for gradients, which naturally gives weak subsequential information; that is a different output type from the pointwise/high-superlevel direction hypotheses consumed by geometric criteria.

**Requested blocker test:** require an explicit derivative-level passage before any geometry theorem is glued to the ancient limit.

### Vorticity geometry

Lei–Ren–Tian is unusually well matched to the *local* singularity setting: it avoids the global-tail defect exposed in B1a3. Its theorem does not say a Type-I solution automatically has a cone; instead, a cone restriction contradicts singularity. Corollary 1.5 sharpens the singular alternative: high-vorticity directions near a singularity must have a range meeting every great circle.

**Requested distinction:** a local geometric classifier is not yet an inherited ancient-state rigidity condition.

### Compactness / functional analysis

The composition `u -> curl u -> curl u/|curl u|` loses one derivative and then applies a discontinuous normalization at zero. Strong convergence of `u_n` in `L3_loc` alone cannot control it. Even weak `L2` convergence of gradients does not recover pointwise direction or stability of the moving sets `{|omega_n|>M}`. Oscillation can survive while velocity amplitude vanishes.

**Requested falsifier:** high-frequency divergence-free sequence with vanishing velocity norm and order-one oscillatory curl.

### Scaling / ancient solutions

This child is orthogonal to the previous global critical-element interface. Translation/dilation leakage remains relevant to a global minimal element, but a fixed-cylinder local geometry theorem can be tested before resolving global tail tightness. Exact backward self-similarity, DSS periodicity, and generic ancient time dependence are not interchangeable. No orbit class should be inferred from direction geometry.

**Requested scope:** Type-II remains open; backward uniqueness and stationary Leray-profile theorems are not needed for this local interface test.

### Adversarial construction

Take `u_n=(0,n^{-1}sin(n x_1),0)`. It is smooth and divergence free. `u_n -> 0` strongly in every local `L3`, but `curl u_n=(0,0,cos(n x_1))`; where nonzero, the normalized direction flips between `+e3` and `-e3`. This exactly falsifies the bare topology inference while making no PDE claim.

**Requested guardrail:** label this `FUNCTIONAL_TOPOLOGY_CALIBRATION_ONLY` and never call it a Navier–Stokes counterexample.

### Proof interface / formal methods

The consequential observation should be frozen as an episode first: the selected producer topology does not decide the selected consumer observable. Only then may a diagnosis be proposed: derivative loss plus singular normalization / moving-superlevel instability. The generalized obstruction must remain scoped and falsifiable by an equation-specific compactness theorem. A reusable lesson cannot be promoted from this same-context episode alone.

**Requested root status:** `OPEN_NO_SOLUTION_CERTIFICATE`, root authority `NONE`.

### Frontier / novelty

Lei–Ren–Tian (arXiv:2501.08976) supplies the strongest load-bearing local range criterion located for this cycle. Giga–Miura confirms the Type-I direction-continuity family but requires extra geometry. Grujic (arXiv:2607.08866, July 2026) is a recent logarithmic-depletion route with additional vorticity-concentration and weighted-BMO hypotheses. None licenses generic inheritance from finite-I.

**Requested novelty discipline:** count a new source-bound relation/path only if it is semantically absent from the current Navier–Stokes repository; do not count paper discovery or prose volume as learning.

## Round 2: cross-role objections and resolutions

**Geometry -> compactness:** Could the PDE itself upgrade the derivative convergence enough to save direction transport?  
**Resolution:** possibly; the functional falsifier does not exclude an equation-specific upgrade. The obstruction is therefore “missing registered transport certificate,” not “impossible transport.” Its falsifier is any valid PDE compactness theorem meeting the exact consumer.

**PDE -> geometry:** Does Lei–Ren–Tian require transporting the cone condition to the ancient limit at all?  
**Resolution:** no. Their proof can start from the pre-limit suitable weak solution with a geometric assumption and then uses a flux mechanism. Therefore an orthogonal live route is to search for a *pre-limit* reason the singularity would violate the great-circle requirement or to derive a stable flux observable directly. This bypasses the transport obstruction.

**Scaling -> PDE:** Does the local geometry route secretly depend on global pressure control?  
**Resolution:** not at theorem input. Lei–Ren–Tian is formulated for local suitable weak solutions with local pressure integrability. The prior far-field obstruction is retained as memory but rejected as the primary diagnosis here.

**Formal -> all roles:** Is weak derivative convergence actually needed for the topological falsifier?  
**Resolution:** no. The falsifier attacks the even stronger unsupported shortcut from velocity `L3_loc` convergence alone. The result artifact must carefully say that the local-energy sequence may also have bounded gradients, but no source in the active packet has been bound that upgrades those gradients to the strong/directional convergence required by the consumer.

**Frontier -> geometry:** Does the 2026 logarithmic-depletion result solve the inheritance issue?  
**Resolution:** no. It begins from additional concentration and weighted-BMO hypotheses. Treat it as a candidate family whose own input bridge would need proof.

## Pre-candidate consensus

The highest-information action is **not** to invent a vorticity-coherence property of the ancient limit. It is to audit the producer-consumer interface first.

Registered decision:

1. verify the exact Lei–Ren–Tian local consumer and its singular great-circle contrapositive;
2. retain the Albritton–Barker/local-energy compactness output at its actual strength;
3. run the high-frequency divergence-free topology falsifier;
4. diagnose derivative/direction transport separately from far-field, profile leakage, backward uniqueness, and equation-change failures;
5. if blocked, open two explicit descendants: `(a)` an equation-specific vorticity-direction/flux transport certificate, and `(b)` a direct pre-limit flux/range route that does not require transporting `xi` through the ancient limit.

No role grants theorem, novelty, or root authority. This review earns **zero independent-review credit**.
