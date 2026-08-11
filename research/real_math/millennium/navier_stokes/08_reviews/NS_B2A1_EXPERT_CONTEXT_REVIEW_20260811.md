# NS-B2a1 same-context expert review — pre-action

**Status:** role-separated same-context review only. This is not independent peer review and grants no mathematical authority.

**Framework source:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application base:** `SzeChunYiu/RAKL_math@4838969ecc18a091da79a059b58b8568634289b7`  
**Atom:** `NS-B2a1 — EULER_TAIL_TIGHTNESS_OR_SIGNED_FLUX`  
**Frozen context:** `sha256:98be9901f6e091516242ed427b7d1d95f660c8e2650c506fe7ab6ed89ac22e21`

## Shared exact obstruction

Seregin's 2026 Theorem 3.1 produces a nontrivial ancient Euler limit under scale-weighted bounds and convergence on every fixed parabolic cylinder. In the logarithmic example `F(a)=1`, those bounds are scale critical. Before any Euler Liouville candidate, determine whether the original Navier–Stokes blow-up sequence carries a source-defined annular/tail or signed-flux quantity that is uniform in the sequence and survives the large-radius limit. Fixed-radius compactness alone is not accepted as a tail theorem.

## Role passes

### 1. Type-II / local-energy PDE analyst
Background: suitable weak Navier–Stokes solutions, blow-up scaling, local energy inequalities.
- Evidence inspected: Seregin arXiv:2606.29468v1 Theorem 3.1/proof; prior B1/B1a application state.
- Strongest objection: the source gives estimates for every fixed radius, but the desired no-incoming-energy statement is a uniform large-radius assertion; the two quantifiers must not be conflated.
- Cheapest falsifier: search the source proof for an annular estimate uniform in the blow-up index whose normalized tail vanishes as radius grows.
- Vote: **ACCEPT NEXT ACTION / CANDIDATE BLOCKED**.

### 2. Concentration-compactness analyst
Background: critical PDE compactness, profile decompositions, noncompact symmetries.
- Evidence inspected: fixed-cylinder convergence in Theorem 3.1; noncanonical moving-core calibration in PR #71.
- Strongest objection: local strong convergence is compatible with translated mass escaping every centered expanding observation region unless a tightness/recentering condition is added.
- Cheapest falsifier: require an explicit `lim_R limsup_k` tail quantity, or a source-derived center/modulation rule controlling escape.
- Vote: **ACCEPT NEXT ACTION / TAIL WITNESS REQUIRED**.

### 3. Pressure/localization analyst
Background: pressure decomposition, local energy flux, Calderón–Zygmund/nonlocal tails.
- Evidence inspected: Theorem 3.1 pressure bound and local energy inequality; canonical Type-I pressure-summability failure.
- Strongest objection: pressure transport is signed and nonlocal; absolute shell bounds can be critical without proving either decay or cancellation.
- Cheapest falsifier: derive a source-level signed boundary-flux identity with controlled pressure normalization, or demonstrate that only absolute boundedness is available.
- Vote: **ACCEPT NEXT ACTION / NO PRESSURE TAIL ASSUMED**.

### 4. Euler rigidity analyst
Background: ancient Euler flows, Liouville theorems, unique-continuation scope.
- Evidence inspected: Seregin arXiv:2507.08733v2 Sections 3–4 and arXiv:2304.04045.
- Strongest objection: known same-author Liouville closures add self-similar, axisymmetric, derivative or vorticity hypotheses. None is yet inherited by the general F=1 branch.
- Cheapest falsifier: table every extra hypothesis of the candidate Liouville theorem against exact source inheritance before theorem search.
- Vote: **BLOCK EULER-LIOUVILLE CANDIDATE / ACCEPT INHERITANCE AUDIT**.

### 5. Vorticity/geometric analyst
Background: Euler vorticity transport, geometric depletion, conserved/transported structures.
- Evidence inspected: extracted Euler equation and the axisymmetric/vorticity special cases in Seregin's prior note.
- Strongest objection: vorticity invariants may offer a different closure, but importing them without source-level regularity/tail conditions risks moving the missing global control into a new variable.
- Cheapest falsifier: test whether any vorticity quantity required by a known rigidity result is uniformly inherited from the source sequence.
- Vote: **DEFER VORTICITY ROUTE UNTIL TAIL AUDIT**.

### 6. Formal-methods / assurance analyst
Background: statement binding, chronology, evidence lineage, fail-closed gates.
- Evidence inspected: current RAKL AGENTS.md, method contracts, authority-hardening changelog, RAKL #123.
- Strongest objection: prior B2a discriminator was retrospective. A new action must be frozen before execution, even though the framework does not yet implement the proposed pre-action receipt automatically.
- Cheapest falsifier: require a content-bound pre-action bundle and receipt committed before any result artifact.
- Vote: **ACCEPT ONLY WITH PRE-ACTION FREEZE**.

### 7. Novelty / research-value analyst
Background: prior-art boundary and information-gain assessment.
- Evidence inspected: Seregin 2023/2025/2026 route sequence and current application issue/PR state.
- Strongest objection: merely saying "far field is uncontrolled" would add little. The useful atomic advance must identify the exact quantifier/interface defect and the minimal measurable tail functional or signed-flux alternative.
- Cheapest falsifier: if the source already states the required `lim_R limsup_k` estimate (or an equivalent), this atom is redundant and should immediately route to the inherited Euler rigidity theorem.
- Vote: **ACCEPT HIGH-INFORMATION SOURCE AUDIT**.

## Consensus and disagreement

Consensus: execute `SOURCE_TAIL_INHERITANCE_AUDIT` first; do not generate an Euler theorem candidate. The decisive question is whether source-level estimates commute with the large-radius limit strongly enough to exclude escape. No role grants independent-review credit.

Residual disagreement: the pressure and vorticity leads leave open the possibility that signed cancellation or a transported invariant closes the route even if nonnegative annular tightness fails. Those are predeclared successor branches, not assumptions.

## Recommended next action

Freeze the exact fibre/receipt, then inspect the source derivation for a quantity `T_k(R)` or signed flux `Φ_k(R)` with one of:

1. `lim_{R→∞} limsup_{k→∞} T_k(R)=0`; or
2. an exact signed cancellation/telescoping identity stable through the Euler limit.

If neither exists, record the missing double-limit/tail inheritance as the next gluing obstruction and keep candidate generation blocked.
