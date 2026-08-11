# NS-R001d1 source packet — heat baseline versus nonlinear depletion

**Atom:** `NS-R001d1`  
**Root:** `RAKL_math#4`  
**Framework authority read for this packet:** `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`  
**Authority:** strict pre-candidate context only; no new Navier–Stokes lemma or root claim.

## Exact obstruction

The merged `NS-R001/A1` screen showed that Leray-energy size plus generic divergence-free/Calderón–Zygmund structure cannot by itself control a scale-critical regularity quantity. The merged `NS-R001b` screen showed that adding local strain/vorticity alignment still does not isolate the Clay-relevant class unless exact trajectory dynamics, finite energy/global localization and nonlocal structure are used jointly.

The next representation therefore separates three objects before any new candidate:

1. the **linear heat/Stokes baseline** generated automatically from finite-energy data;
2. the exact **nonlinear Duhamel feedback** containing advection and Leray-projected pressure coupling;
3. a genuinely **critical target coordinate** whose improvement cannot already be explained by the linear baseline.

Pending PR #33 reports a separate static projected-remainder calibration and proposes a positive-time child. Its exact-head application CI is unresolved at packet freeze, so that result is treated as provisional route evidence and is not imported into the frozen failure-lattice authority.

## Primary-source matrix

### Miller — projected strain/vorticity remainder

Primary source: Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691.

The paper derives the strain-space projection identity and regularity criteria involving

`P_st((u·∇)S + S^2 + (3/4) ω⊗ω)`

relative to viscous strain diffusion. The source is useful because it explicitly asks when advection depletes the nonlinearity. It does **not** derive the required remainder control from arbitrary finite kinetic energy. Therefore it supplies a target coordinate and a conditional bridge, not the missing global estimate.

### Barker–Prange — localized critical smoothing

Primary source: Tobias Barker and Christophe Prange, arXiv:1812.09115.

Their localized smoothing starts from local scale-critical `L^3` control (and variants) and propagates it into quantified short-time regularity. The singularity-side concentration statement is a downstream contrapositive. The method is near-solved context for this atom, but its load-bearing critical input is assumed rather than generated from the global energy class.

### Cheskidov–Eguchi — finite energy plus frequency-local critical smallness

Primary source: Alexey Cheskidov and Taichi Eguchi, arXiv:2503.11642.

The paper constructs global smooth solutions for finite-energy data under smallness of a high-frequency `BMO^{-1}` component and weaker critical low-frequency control. This is especially relevant because it combines finite energy with a critical frequency decomposition. The broken assumption is precisely the active one: arbitrary Clay data need not provide the registered small critical components.

### Coiculescu–Palasek — hostile large-critical-data calibration

Primary source: Matei P. Coiculescu and Stan Palasek, arXiv:2503.14699.

The paper constructs critical `BMO^{-1}` data with two distinct global solutions smooth for positive time, establishing sharpness phenomena beyond the small-data Koch–Tataru regime. This source is used only as a warning against treating large critical-space membership as if it were the small perturbative regime. It is not a finite-energy singularity result and supplies no negative evidence against the Clay conjecture.

### Koch–Tataru critical theory

Source: H. Koch and D. Tataru, *Well-posedness for the Navier–Stokes equations*, Adv. Math. 157 (2001), DOI `10.1006/aima.2000.1937`.

The successful mechanism is not “heat smoothing alone”; it is closure of the exact mild equation in a critical function-space geometry under smallness. The transfer obligation for `NS-R001d1` is therefore to identify whether arbitrary finite-energy evolution can dynamically create an equivalent smallness/coherence property without assuming it.

## Baseline calculation to freeze before the next candidate

For the heat semigroup in three dimensions, standard scaling gives

`||e^{νtΔ} f||_3 <= C (νt)^(-1/4) ||f||_2`.

Thus positive-time `L^3` smoothing from an `L^2` datum has a nontrivial **linear** explanation. A future nonlinear-depletion claim must compare against that baseline rather than treating any positive-time smoothing as equation-specific progress.

For the Duhamel term, the standard gradient heat mapping has the dimensional form

`||∇e^{ν(t-s)Δ} F||_3 <= C (ν(t-s))^(-3/4) ||F||_2`.

Together with `||u⊗u||_2 <= ||u||_3 ||u||_6` and the energy-class `u in L_t^2 L_x^6`, this exposes a near-diagonal temporal endpoint that must be audited before a crude `L_t^∞L_x^3` bootstrap is trusted. **This packet does not execute or claim the outcome of that audit.**

The predeclared hostile control for the next post-gate cycle is a unit-`L^2` temporal pulse concentrating near `s=t`. It is intended only to test the scalar convolution architecture induced by these standard estimates. Failure would be a proof-architecture no-go, not a Navier–Stokes counterexample.

## Representation and scope ledger

- `L_x^3` is critical under the exact Navier–Stokes solution scaling.
- `L_t^∞L_x^2 ∩ L_t^2 dot H_x^1` is supercritical.
- heat `L^2 -> L^3` smoothing is a baseline, not a root bridge.
- any Duhamel estimate must record the kernel exponent, spatial exponents, time-integrability exponent, viscosity dependence and restart interval.
- pressure/nonlocality remains inside the Leray projection; replacing the exact projected nonlinearity by an unsigned scalar bound can only prune that proof architecture.
- a negative endpoint audit cannot exclude frequency-local cancellation, tent-space closure, local-energy flux, projected-strain depletion or another exact trajectory mechanism.

## Provisional-parent boundary

`RAKL_math#33` is open and mergeable but its pinned application workflow is queued at this packet freeze. `NS-R001d1` is therefore frozen as a **pre-candidate** context that is independently motivated by the two merged failures. No PR #33 result is promoted into the local success/failure memory snapshot.

## Next discriminator

Only after the context, memory and trace machine gates pass:

1. freeze one exact semigroup/energy endpoint-closure candidate;
2. bind the standard heat exponents and all constants/scopes;
3. run the predeclared near-diagonal temporal-concentration hostile control;
4. classify any failure as `PROOF_ARCHITECTURE_ENDPOINT_GAP`, not theorem impossibility;
5. if the crude route fails, reopen the representation toward cancellation-aware tent/frequency/local-energy/projected-strain coordinates rather than retrying the same Hölder estimate.
