# NS-B2a1b same-context expert review — pre-action

**Status:** role-separated same-context AI review only. No independent-review credit and no mathematical authority.

**Framework source:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Current application main observed:** `SzeChunYiu/RAKL_math@6557b1b25fa839fe71aba8047c958d5da892edd8`  
**Stacked parent branch subject:** `SzeChunYiu/RAKL_math@b7aad40051409c2e6f47bf277cfda79a6da28c96` (PR #91; not canonical main)  
**Atom:** `NS-B2a1b — SIGNED_EULER_FLUX_ENERGY_DEFECT`  
**Frozen context:** `sha256:60800c31320de83fe7388a85e7ae647b6a190e287c59712a4738c633ffddbbb3`

## Shared exact obstruction

The parent Type-II route leaves open whether a signed local-energy-flux identity can replace nonnegative annular tightness. The present atom does not assume that the local energy inequality is an equality. The prospective discriminator is whether the exact inherited regularity of Seregin's ancient Euler limit satisfies a primary-source local energy equality criterion, or whether an explicit local energy defect remains and must itself be controlled at large radius.

The idea that a defect term may matter was recognized before this freeze and is therefore treated as **retrospective calibration/hypothesis only**. The evaluated outcome is the later source-and-exponent applicability audit.

## Role passes

### 1. Type-II / local-energy PDE lead
Background: suitable weak Navier–Stokes solutions, blow-up scaling, local energy inequalities.
- Evidence inspected: Seregin 2026 Theorem 3.1 as already source-bound in parent PR #91; current root issue #65.
- Strongest objection: the inherited statement explicitly supplies a local energy inequality. A signed telescoping argument cannot upgrade this to equality by notation.
- Cheapest discriminator: write the exact cutoff balance allowed by (3.7), then identify which term would be a defect if equality is unavailable.
- Vote: **ACCEPT DEFECT-CRITERION AUDIT / CANDIDATE BLOCKED**.

### 2. Euler energy / Onsager lead
Background: weak Euler solutions, commutator criteria, local versus global energy conservation.
- Evidence inspected: standard Constantin–E–Titi and Duchon–Robert routes as candidate source families, without assuming applicability.
- Strongest objection: energy equality criteria are exponent-, locality- and time-integrability-sensitive. The Seregin class must be matched coordinate by coordinate.
- Cheapest discriminator: audit one exact primary theorem against the inherited local regularity; if any hypothesis is missing, record `CANNOT_CHECK` rather than interpolate it into existence.
- Vote: **ACCEPT SOURCE-APPLICABILITY AUDIT**.

### 3. Pressure / localization lead
Background: local pressure integrability, local energy flux, cutoff identities.
- Evidence inspected: inherited pressure `L^{3/2}` scaling and parent pressure-tail warnings.
- Strongest objection: pressure transport is signed, while a local-energy defect has different sign semantics. Boundary cancellation cannot silently cancel an interior nonnegative defect.
- Cheapest discriminator: retain pressure flux and defect as separate terms in every cutoff identity and compare their scale normalization.
- Vote: **ACCEPT / KEEP TERMS SEPARATE**.

### 4. Concentration-compactness / tail lead
Background: noncompact symmetries, profile escape, local-to-global limits.
- Evidence inspected: parent `O-NS-B2a1-DOUBLE-LIMIT-TAIL-INHERITANCE`.
- Strongest objection: even if an exact local balance exists, a large-radius conclusion still needs uniform control of every surviving defect/boundary term.
- Cheapest discriminator: determine whether the normalized defect mass or its annular increment is forced to vanish, bounded only, or not source-controlled.
- Vote: **ACCEPT / GLOBAL QUANTIFIER STILL LOAD-BEARING**.

### 5. Adversarial weak-Euler lead
Background: dissipative weak Euler solutions and counterexample methodology.
- Evidence inspected: existence of rough Euler regimes where local energy inequality can be strict, used only as logical calibration.
- Strongest objection: citing rough dissipative Euler solutions does not show strict defect in Seregin's stronger inherited class.
- Cheapest discriminator: forbid counterexample language unless exact class membership is source-bound; use rough solutions only to refute a logical implication from 'weak Euler' alone.
- Vote: **ACCEPT WITH CLASS-SCOPE GUARD**.

### 6. Formal-methods / assurance lead
Background: chronology, artifact identity, fail-closed gates.
- Evidence inspected: current `RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466` AGENTS contract and method surfaces; parent PR #91 chronology.
- Strongest objection: the defect hypothesis was noticed before this atom was frozen. It must not be reported as a prospective discovery.
- Cheapest discriminator: preregister only the source-applicability outcome branches and commit this packet before the source audit.
- Vote: **ACCEPT ONLY AS PROSPECTIVE TEST OF A PRE-EXISTING HYPOTHESIS**.

### 7. Novelty / research-value lead
Background: prior-art boundary and information gain.
- Evidence inspected: parent double-limit obstruction and standard local-energy-defect literature families.
- Strongest objection: 'weak Euler may dissipate energy' is old. The only useful new route-local information would be the exact applicability map for the Seregin `F(a)=1` class and the resulting normalized defect obligation.
- Cheapest discriminator: if an established theorem immediately forces local energy equality from the inherited exponents, close this atom as compositional and move to flux telescoping; otherwise isolate the smallest missing exponent/globality coordinate.
- Vote: **ACCEPT HIGH-INFORMATION APPLICABILITY AUDIT**.

## Consensus and disagreement

Consensus: do not generate an Euler rigidity theorem or a signed-flux candidate. Freeze the packet, then test whether the inherited Seregin class forces local energy equality under a primary-source criterion. If not, keep an explicit defect term and quantify only what the inherited critical bounds support.

Residual disagreement: the Euler-energy lead considers equality plausible under additional local regularity, while the adversarial lead warns that no such implication may be asserted without an exact theorem match. The pressure/tail leads agree that even equality would not by itself solve the large-radius interface.

## Predeclared outcome branches

- **A — `INHERITED_REGULARITY_FORCES_LOCAL_ENERGY_EQUALITY`:** exact source theorem matches every inherited hypothesis; defect is zero in the required local sense.
- **B — `LOCAL_ENERGY_INEQUALITY_ONLY`:** audited source does not establish equality in the exact inherited class; retain an explicit nonnegative defect object.
- **C — `DEFECT_PRESENT_OR_UNRESOLVED_BUT_NORMALIZED_TAIL_CONTROL_INHERITED`:** equality is not obtained, but a source-backed defect/tail estimate is sufficient for the intended large-radius normalization.
- **D — `CANNOT_CHECK_ENERGY_EQUALITY_CRITERION`:** source access or exponent/locality mapping is insufficient.

## Recommended next action

After this review, freeze dual memory, trace and pre-action receipt, then execute `LOCAL_ENERGY_DEFECT_CRITERION_AUDIT`. No theorem candidate is admissible during this action.
