# NS-B1a2 same-context expert review — compactness-to-drift bridge

**Authority:** SAME_CONTEXT_ROLE_SEPARATED_REVIEW / NOT_INDEPENDENT / NO_THEOREM_AUTHORITY  
**Framework inspected:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**RAKL_math base:** `8a608f340d47b4b6ae612275b0595faf6b804432`  
**Frozen context:** `sha256:93f1d63d36fe43910713623d0c385e799506530fbb02790706ca8c824a076fe5`  
**Frozen memory review:** `sha256:55846db2ed577a688dc7786b22c11f2a9aa73b5c6c738cf33ba7b0198718a2cf`

## Exact review question

For a non-trivial mild bounded ancient 3D Navier–Stokes solution in the Albritton–Barker finite-`I` Type-I class, can local critical control plus compactness/minimality of the renormalized orbit force one sufficiently late self-similar time at which the scaling-generator drift is small enough to activate a source-valid near-self-similarity regularity theorem?

This review authorizes only the cheapest hostile discriminator. It does not authorize a new PDE theorem candidate.

## Role 1 — Type-I / ancient-solution PDE lead

**Background:** suitable weak solutions, ancient-solution extraction, critical regularity and Liouville theorems.  
**Source facts checked:** Albritton–Barker `1811.00502`; the existing `NS-B1` implication matrix.

The finite-`I` class is not interchangeable with a pointwise Type-I bound or a global `L^3` bound. The useful source-valid Liouville trigger remains a backward sequence with bounded global `L^3`, while Pineau–Vicol's new local criterion requires different, stronger hypotheses. The proposed bridge is therefore legitimate only if each required hypothesis is inherited explicitly.

**Strongest objection:** a compactness argument can silently import global tail control or pointwise Type-I decay not contained in finite `I`.  
**Vote:** ACCEPT the hostile audit; BLOCK any theorem candidate.

## Role 2 — Renormalized dynamics / concentration-compactness lead

**Background:** critical-element methods, orbit compactness modulo symmetries, recurrent dynamics.

Precompactness of an orbit is a topological statement, not a dissipation statement. A compact recurrent orbit can move forever with speed bounded away from zero. Translation/dilation modulation can further hide motion in quotient coordinates.

**Strongest falsifier:** `z(s)=(cos s,sin s)` is compact but `|z'(s)|=1` for every `s`.  
**Required repair if the route is to survive:** finite total variation, a coercive Lyapunov defect, asymptotic regularity, or a source-valid no-recurrence theorem.  
**Vote:** ACCEPT the hostile audit; expect `COMPACTNESS_ONLY_INSUFFICIENT`.

## Role 3 — Local-energy / pressure lead

**Background:** local energy inequality, pressure localization, harmonic pressure and scale-invariant estimates.

The previous `NS-B1a1` cycle already removed standard absolute shell bookkeeping as a finite scale currency. Pineau–Vicol Theorem 1.9 also carries a fixed-annulus pressure `L^∞` hypothesis that finite `D` does not automatically supply.

**Strongest objection:** even if a small-drift slice were obtained, the theorem interface could still fail at the pointwise velocity or annular-pressure coordinates.  
**Vote:** ACCEPT the audit; keep interface obligations separate.

## Role 4 — Vorticity / weighted-energy lead

**Background:** vorticity stretching, enstrophy, Gaussian-weighted estimates.

Pineau–Vicol convert one-slice small self-similar-time derivative into local enstrophy smallness and then propagate it. That direction does not invert automatically. A generic Gaussian-weighted energy for the unrestricted self-similar-time equation has nonlinear convection and pressure contributions with no evident fixed sign.

**Strongest objection:** do not infer a Lyapunov functional by analogy with gradient flows; derive its sign under the exact target class or reject it.  
**Vote:** ACCEPT a formal/localized sign audit as calibration only.

## Role 5 — Adversarial dynamical-systems lead

**Background:** recurrent/periodic dynamics, counterexamples to compactness-to-stationarity implications.

Pineau–Vicol themselves treat DSS/RDSS profiles as periodic in self-similar time and describe them as breather-like scenarios. Their special RDSS theorem only gets exclusion under restricted parameter regimes, including small self-similar period in the relevant cases. This is direct source evidence that periodic orbit is a distinct scenario, not automatic approximate stationarity.

Long-time vector averaging is also unsafe:
`T^{-1}∫_S^(S+T) ∂_s U ds = (U(S+T)-U(S))/T`.
A bounded orbit makes the vector average small, but cancellation does not imply small `T^{-1}∫||∂_s U||` or a single time with small norm. The circle control has zero average derivative over a full period while its speed is identically one.

**Vote:** ACCEPT; this is the cheapest decisive logical falsifier.

## Role 6 — Formal-methods / assurance lead

**Background:** statement binding, chronology, content identity and trust boundaries.

Current RAKL main has hardened v3 authority transitions: caller IDs/booleans cannot mint authority without protected content attestations. This application cycle has no protected authority context for theorem/tool/framework promotion, so all TaskEpisode/failure/novelty records remain proposal/shadow telemetry.

**Chronology requirement:** context, method-transfer review, expert review, memory review and seven-event trace must be frozen before the hostile audit result.  
**Vote:** ACCEPT only under proposal/shadow authority.

## Role 7 — Novelty / research-value lead

**Background:** frontier calibration and rediscovery risk.

The useful new object is not another self-similar Liouville theorem. It is a route discriminator separating:
1. compact/precompact renormalized dynamics,
2. small instantaneous scaling-generator drift,
3. exact source prerequisites for a regularity theorem.

The logical counterexamples are elementary and should not be claimed as mathematical novelty. Research value comes from preventing an invalid compactness-to-rigidity bridge and exposing the exact next missing coordinate.

**Vote:** ACCEPT as route-pruning / method-transfer calibration; no novelty claim.

## Consensus and delegated action

All seven roles agree on the following pre-candidate decision:

`RUN_COMPACTNESS_TO_DRIFT_HOSTILE_AUDIT / NO_THEOREM_CANDIDATE`.

The audit must test three claims separately:

1. `precompact orbit => liminf ||∂_s U|| = 0`;
2. `small long-time vector increment => one-time small ||∂_s U||`;
3. `time-averaged Navier–Stokes profile => stationary Leray profile`.

A negative result prunes only compactness/averaging **without an additional sign-controlled or finite-variation coordinate**. It does not rule out concentration-compactness plus a genuine rigidity mechanism, nor does it alter the Navier–Stokes root status.
