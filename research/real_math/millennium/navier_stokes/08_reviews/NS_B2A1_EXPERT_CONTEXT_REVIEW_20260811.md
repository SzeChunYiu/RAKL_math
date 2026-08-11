# NS-B2a1 same-context expert pre-candidate review

**Atom:** `NS-B2a1 — EULER_TAIL_TIGHTNESS_OR_SIGNED_FLUX`  
**Context hash:** `sha256:46107a3521175794ea4dadece4101723a57bf6af8dc9e8680a3c47d31c70902e`  
**Memory review:** `sha256:baa4a039e9a51b50463cc9a0dc83cdbc5b7a1346f1ae7313face94226034f25c`  
**Framework:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application base:** `SzeChunYiu/RAKL_math@50c703f3f0c518bba1b48fb17e51b03d53ed02c3`  
**Authority:** role-separated same-context review only. It is **not independent peer review** and creates no theorem/root authority.

## Common evidence inspected

- exact Clay/Fefferman Navier–Stokes root contract mirrored in the repository;
- Gregory Seregin, `arXiv:2606.29468v1`, especially the fixed-cylinder convergence used in the extraction and Theorem 3.1 equations (3.5)–(3.8);
- issue #65 and its two current comments;
- pending PR #72 exact head `33b01df7ca7dd2d3a23ddf7cb92813efeeddeb87`, proposal-only F=1 absolute-cutoff calibration;
- pending PR #71 exact head `260f971b72a1caa9d186fa00e29b0878b5b6a01c`, proposal-only XM005 moving-core calibration;
- canonical `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` at blob `12a77d4e9cf3b5704432ec4d9b6c84c5ad7fd967`;
- frozen `NS-B2a1` context and memory review.

## 1. Type-II / local-energy PDE lead

**Finding.** The source extraction controls convergence on each fixed `Q(a)`. Theorem 3.1 then gives a nontrivial ancient Euler limit with scale-weighted local energy, pressure and gradient control. None of these statements is, by itself, a uniform prelimit tail estimate outside growing balls.

**Strongest counter-hypothesis.** Perhaps the centered singular scaling and source nontriviality already pin the only relevant concentration core, making additional escaping packets irrelevant to the rigidity argument.

**Required falsifier.** Use a calibration with a fixed nonzero local core **plus** a second translated divergence-free packet. If local convergence retains the core while the second packet carries non-vanishing global tail mass, then source nontriviality does not repair the topology gap by itself.

**Residual if falsifier passes.** Derive a source-specific estimate that excludes additional profile leakage for the actual rescaled suitable-weak sequence.

**Vote:** `ACCEPT_NEXT_DISCRIMINATOR / NO_EULER_RIGIDITY_CANDIDATE_YET`.

## 2. Concentration-compactness / quantifier-order lead

**Finding.** The bridge contains two limits with different scopes: `k -> infinity` at fixed radius and `R -> infinity` for a tail. The implication needed by a global rigidity argument requires a uniformity statement such as

`lim_{R->infinity} sup_k Tail_k(R)=0`,

or a recentered/modulo-symmetry equivalent. Fixed-radius convergence alone cannot exchange these quantifiers.

**Strongest counter-hypothesis.** The scale-critical `sup_a` bounds on the *limit* could indirectly imply enough tightness, even if the convergence theorem is local.

**Required falsifier.** Separate the statements. Construct a locally convergent nontrivial two-packet sequence with uniformly bounded local norms but a tail packet at `|x_k| -> infinity`; this shows local topology plus boundedness does not contain the missing uniform-tail quantifier. It does not decide whether the PDE supplies an extra estimate.

**Residual.** `PRELIMIT_UNIFORM_TAIL_MODULUS_OR_RECENTERING`.

**Vote:** `ACCEPT_NEXT_DISCRIMINATOR`.

## 3. Pressure / far-field localization lead

**Finding.** Velocity-tail nontransfer is already enough to block a naive global handoff. Pressure is harder because local pressure compactness permits local normalizations while a global `|p|^{3/2}` tail depends on one consistent normalization/decomposition and on nonlocal harmonic pieces.

**Strongest counter-hypothesis.** A Calderón–Zygmund representation tied to the actual velocity sequence might supply the missing pressure tail once velocity tightness is known.

**Required falsifier.** Do **not** use an arbitrary pressure bump as a PDE counterexample. First settle velocity tightness. If a velocity modulus survives, separately audit whether the source pressure normalization is globally compatible and whether the far-field harmonic remainder is uniform in `k`.

**Residual.** `PRESSURE_TAIL_NORMALIZATION_AFTER_VELOCITY_TIGHTNESS`.

**Vote:** `ACCEPT_VELOCITY_FIRST / PRESSURE_DEFERRED`.

## 4. Euler rigidity / unique-continuation lead

**Finding.** The limiting equation is Euler. Parabolic Navier–Stokes backward uniqueness is not inherited. A candidate Euler Liouville theorem should not be invented until its global/tail hypotheses are demonstrably available from the source class.

**Strongest counter-hypothesis.** The local-energy inequality plus source nontriviality and backward expanding-ball smallness might already imply an Euler rigidity statement without a full tail modulus.

**Required falsifier.** Pending XM005 already warns that centered local smallness can be compatible with translation escape. The new two-packet test should check the stronger case in which nontrivial local mass remains while additional global content escapes.

**Residual.** Only after tail/recentering is source-bound should the lane search the exact Euler Liouville theorem.

**Vote:** `BLOCK_RIGIDITY_CANDIDATE_PENDING_HANDOFF`.

## 5. Vorticity / geometric-depletion lead

**Finding.** Vorticity transport and geometric-depletion coordinates are translation covariant. Centered vorticity smallness can therefore fail to distinguish actual dissipation/depletion from a core moving out of the observation region.

**Strongest counter-hypothesis.** A scale-invariant vorticity quantity could be recentered naturally by a concentration center and avoid velocity-tail bookkeeping.

**Required falsifier.** Any such recentering must preserve the source nontriviality witness and make center motion explicit. A post-hoc center chosen after seeing the limit would be a new, unbound symmetry quotient.

**Residual.** `CONTENT_BOUND_CONCENTRATION_CENTER_OR_TAIL_MODULUS`.

**Vote:** `NO_VORTICITY_SHORTCUT_YET`.

## 6. Adversarial construction lead

**Finding.** A pure translating packet is an insufficient hostile control because it converges locally to zero, whereas Seregin (3.8) forces a nontrivial limit. The correct hostile calibration is

`W_k(x,t) = eta(t) [w_0(x) + w_1(x-x_k)]`, with `|x_k| -> infinity`,

where `eta` is a smooth compactly supported time cutoff and `w_0,w_1` are nonzero smooth compactly supported divergence-free fields with separated supports. Then `W_k -> eta w_0` strongly in every local `L^p`, while the global/tail norm of the translated second packet does not disappear uniformly in `k`.

**Strongest objection.** `W_k` is not an Euler or Navier–Stokes solution.

**Answer / scope discipline.** Correct. It is a counterexample only to the **topological inference** from local convergence to global tail inheritance. The target PDE must separately prove why its sequence cannot realize this escape mode.

**Vote:** `RUN_THIS_FALSIFIER`.

## 7. Formal assurance / novelty lead

**Finding.** The discriminator is admissible only as a scoped compactness/gluing calibration. It cannot be presented as a Navier–Stokes counterexample, Euler counterexample, new rigidity theorem or root progress. Pending PR #71/#72 are warning inputs only because neither is canonical main authority.

**Strongest process objection.** The action might duplicate XM005.

**Resolution.** XM005 targets centered backward local smallness versus a moving core. `NS-B2a1` instead tests the **prelimit-to-limit quantifier exchange** and strengthens the hostile control to a fixed nontrivial local core plus an escaping second packet. The discriminated implication and residual are different.

**Novelty posture.** No external novelty claim. The useful output is a source-specific research-control obstruction and exact next proof obligation.

**Vote:** `PROCESS_CLEAN_IF_TRACE_FROZEN_BEFORE_RESULT`.

## Cell synthesis

Consensus next action:

> Freeze the required seven-event pre-candidate trace, then prove the two-packet local-convergence/tail-nontransfer calibration. If the calibration succeeds, register the scoped obstruction `LOCAL_CONVERGENCE_ALONE_DOES_NOT_TRANSFER_TAIL_TIGHTNESS`, and open the source-specific residual `PRELIMIT_UNIFORM_TAIL_MODULUS_OR_RECENTERING`. Do not propose an Euler rigidity theorem in this cycle.

Strongest unresolved objection after that expected result: the actual Seregin blow-up sequence may possess additional PDE structure that excludes the calibration. That is exactly the next atom and must be proved from the source hypotheses rather than assumed.

**Overall vote:** `PROCEED_TO_FROZEN_COUNTEREXAMPLE_FIRST_CALIBRATION / ROOT_AUTHORITY_NONE`.
