# NS-B2a1 result review — same-context only

**Result subject:** `39c6d299853550cdd2688c84c0cce246f4a783ca`  
**Pre-action freeze:** `dbf0805599843a5c96c0d3a5942a751c393cd023`  
**Independent-review credit:** none.

## Finding under review

The source-tail audit took predeclared branch B. Seregin's audited `F(a)=1` route supplies fixed-cylinder compactness and scale-critical upper bounds, but those analytic ingredients alone do not establish a `lim_{R→∞} limsup_k` annular-tail witness. A divergence-free critical-shell construction shows why local convergence plus the same critical scaling order cannot logically supply global tightness without additional structure. The construction is kinematic and is not an Euler or Navier–Stokes counterexample.

## Role-separated discussion

1. **Type-II/local-energy PDE lead — ACCEPT SCOPED.** The source quantifiers are represented faithfully: the convergence step is for each fixed `Q(a)`, while the target tail obligation is uniform at large radius. The review rejects any wording that says Seregin's full Euler dynamics cannot yield more.
2. **Concentration-compactness lead — ACCEPT SCOPED.** The critical-shell packet is a valid adversarial test of the compactness inference because it preserves order-one critical energy/gradient normalization while escaping every fixed compact set. It must remain explicitly non-PDE.
3. **Pressure/localization lead — ACCEPT WITH OPEN BRANCH.** No pressure-tail decay is inferred. Signed pressure/energy-flux cancellation remains an admissible successor and is not refuted by the kinematic packet.
4. **Euler-rigidity lead — ACCEPT CANDIDATE BLOCK.** The comparison to arXiv:2507.08733v2 correctly shows that the cited special Liouville routes add hypotheses. No generic ancient-Euler Liouville theorem is proposed.
5. **Vorticity/geometric lead — ACCEPT / DEFER.** Vorticity transport may provide a different global coordinate, but none is yet inherited by this source branch. Do not promote it from possibility to method authority.
6. **Formal-methods/assurance lead — ACCEPT CHRONOLOGY, NO FRAMEWORK CREDIT.** The pre-action bundle and receipt were committed before the source-audit result. This is an application-side chronology witness, not proof that RAKL #123 is implemented or that the search universe was complete.
7. **Novelty/research-value lead — ACCEPT AS RESIDUAL SHARPENING.** The useful contribution is not the generic statement that far fields are hard; it is the exact `fixed-a` versus `lim_R limsup_k` interface and the critical-shell falsifier tailored to the source scaling. Count this as scoped knowledge/obstruction/relation novelty only, not a new operator or theorem.

## Consensus verdict

`SCOPED_SOURCE_BOUND_INTERFACE_DIAGNOSTIC_ACCEPTED / CANDIDATE_GENERATION_BLOCKED / ROOT_AUTHORITY_NONE`.

## Next discriminator

Prefer a fresh `NS-B2a1a — PRELIMIT_ANNULAR_TIGHTNESS` atom unless primary-source structure exposes an exact signed flux identity first. The next packet must define the tail functional before evaluating it and must distinguish nonnegative tightness, signed flux, recentering/modulation, and symmetry-specific Euler rigidity.
