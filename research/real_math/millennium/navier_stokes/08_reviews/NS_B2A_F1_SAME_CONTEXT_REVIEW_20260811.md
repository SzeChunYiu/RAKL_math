# Same-context expert review — NS-B2a F=1 absolute cutoff-flux calibration

**Review type:** role-separated same-context technical review; not independent mathematical review.  
**Root authority:** none.

## Delegated expert cell

### 1. Type-II / Euler-scaling PDE lead

**Background:** blow-up rescaling, suitable weak Navier-Stokes solutions, ancient Euler limits.

**Evidence inspected:** Seregin arXiv:2606.29468v1, especially Theorem 3.1 and the `F(a)=1` logarithmic example.

**Finding:** the limit equation is Euler. The `F=1` branch carries critical local `A/E/D`-type bounds, not a global tail condition.

**Strongest objection:** the source theorem may contain an implicit compactness consequence stronger than the displayed bounds.

**Attempted falsifier:** searched the theorem statement and immediate example for an exterior/tail or translation-tightness clause. None is part of the displayed theorem interface.

**Vote:** `ACCEPT_SCOPED_SOURCE_INTERFACE`.

### 2. Local-energy / flux analyst

**Background:** local energy inequalities, Caffarelli-Kohn-Nirenberg scaling, cutoff estimates.

**Evidence inspected:** equation (3.7) plus the `F=1` bounds in (3.5).

**Finding:** time-cutoff, cubic transport, and pressure transport terms are each `O(R)` on a parabolic window of scale `R`; after normalizing by local kinetic energy scale `R`, all are `O(1)`.

**Strongest objection:** a signed boundary term can be much smaller than its absolute bound.

**Attempted falsifier:** retained signs instead of absolute values. No sign is controlled by (3.5) alone, so the calculation cannot rule out cancellation and must stay scoped to absolute estimates.

**Vote:** `ACCEPT_NEGATIVE_ABSOLUTE_FLUX_DISCRIMINATOR`.

### 3. Pressure / localization analyst

**Background:** pressure representations, Calderón-Zygmund localization, pressure normalization.

**Evidence inspected:** `D_p(R)` in Seregin (3.5) and merged RAKL_math pressure-tail failure `F-NS-B1a-C001-PRESSURE-SUMMABILITY`.

**Finding:** Hölder with `L^{3/2}` pressure and local `L^3` velocity is exactly scale critical. The merged Type-I pressure result is a warning against reintroducing raw pressure divergence as the missing global mechanism.

**Strongest objection:** harmonic/exterior pressure pieces may encode extra tail information.

**Attempted falsifier:** asked whether the present estimate identifies a global pressure representation. It does not. Harmonic/exterior structure remains an open child coordinate.

**Vote:** `ACCEPT_WITH_PRESSURE_SCOPE_BOUNDARY`.

### 4. Concentration-compactness / far-field analyst

**Background:** profile decompositions, moving centers, tightness, loss of mass at infinity.

**Evidence inspected:** origin-centered scale bounds and issue #65's far-field residual.

**Finding:** local weak convergence can preserve every compact-set estimate while losing annular/tail information through translations or separated profiles. A no-incoming-flux theorem must therefore bind the prelimit tails or produce an equivalent compactness mechanism.

**Strongest objection:** nontriviality is registered near the origin, possibly anchoring the profile enough to suppress escape.

**Attempted falsifier:** separate anchoring of one nontrivial profile from exclusion of additional far-field incoming energy. The former does not imply the latter.

**Vote:** `ACCEPT_TAIL_TIGHTNESS_AS_SEPARATE_GLUE`.

### 5. Euler rigidity / Liouville analyst

**Background:** ancient Euler Liouville problems and rigidity assumptions.

**Evidence inspected:** Seregin 2025/2026 Euler-scaling programme and the exact current theorem interface.

**Finding:** available rigidity statements in this programme use additional structural hypotheses; no general `critical local energy + local energy inequality -> u=0` theorem is licensed by the inspected source.

**Strongest objection:** a broader Liouville theorem may exist outside the bounded search.

**Attempted falsifier:** bounded primary-source search for a theorem with exactly the present hypotheses. No such theorem was identified; this is not a literature-wide nonexistence claim.

**Vote:** `OPEN_RIGIDITY_THEOREM`.

### 6. Adversarial-construction analyst

**Background:** hostile scaling worlds, scale recurrence, stationary/compactly supported Euler examples.

**Evidence inspected:** critical homogeneity and the previously discussed compactly supported steady-Euler near miss.

**Finding:** the easiest adversary is not an asserted Euler solution satisfying the full source class; it is the scaling fact itself: an `O(1)` normalized upper bound cannot certify decay.

**Strongest objection:** using a hostile non-solution would overstate the negative result.

**Attempted falsifier:** removed all non-solution examples from the proof. The route-pruning conclusion still follows from homogeneity alone.

**Vote:** `ACCEPT_WITHOUT_COUNTEREXAMPLE_CLAIM`.

### 7. Formal assurance / v3 telemetry analyst

**Background:** RAKL chronology, immutable episodes, failure diagnosis, promotion boundaries.

**Evidence inspected:** current RAKL v3 `TaskEpisode`, problem-fibre and saturation contracts; current RAKL_math chronology.

**Finding:** this discriminator was recognized before a fresh strict `NS-B2a` context was frozen. It must be stored as retrospective experience, not prospective candidate evidence. Failure cause remains `OBSERVED_ONLY`.

**Strongest objection:** retroactively creating a polished context could make the result look preregistered.

**Attempted falsifier:** require an explicit chronology field and tests that prohibit any `CANDIDATE_PROPOSED`/theorem-authority marker.

**Vote:** `ACCEPT_RETROSPECTIVE_ONLY`.

## Consensus

`ABSOLUTE_F1_CUTOFF_DECAY_NOT_OBTAINED / TAIL_GLUE_OPEN / EULER_RIGIDITY_OPEN / OBSERVED_ONLY_FAILURE / NO_CANDIDATE / ROOT_AUTHORITY_NONE`

The next mathematical work must begin with a fresh context for `NS-B2a1`, not with a theorem drafted from this retrospective calibration.
