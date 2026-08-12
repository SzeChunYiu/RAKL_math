# Same-context expert review — NS-B1b1 Pineau–Vicol v2 transfer

**Status:** `SAME_CONTEXT_REVIEW_ONLY / NOT_INDEPENDENT / NO_ROOT_REVIEW_CREDIT`  
**Atom:** `NS-B1b1`  
**Frozen context:** `sha256:2d62451fec625e6ee71e9ae9f300c5da1f82597b26933ce60e267030313d4f22`

Each role reviewed the same exact atom and source packet. Role separation is used to expose atomic gaps; it is not represented as independent mathematical review.

## Role 1 — ancient-solution / Type-I PDE

**Task.** Audit the Albritton–Barker blow-up object and what survives the limit.

**Finding.** The source-bound limit is a nontrivial mild bounded ancient solution with finite local scale-invariant `I`, obtained through strong `L^3_loc` velocity compactness, weak `L^(3/2)_loc` pressure compactness and persistence of singularity. This does not supply exact RSS/RDSS structure, a global `L^3` trace, or one-slice self-similar-generator smallness.

**Hostile check.** Do not apply Pineau–Vicol Theorem 1.9 to the bounded ancient limit and mistake endpoint regularity for a Liouville theorem: the target is `v=0`, not merely local regularity of an already bounded ancient solution.

## Role 2 — self-similar / RSS / RDSS

**Task.** Bind the 2026 v2 theorem statements and residual parameter regimes.

**Finding.** Theorem 1.4 eliminates exact global RSS only for sufficiently small or sufficiently large `|alpha|` under global pointwise Type-I decay; `alpha~1` remains open. Theorem 1.7 eliminates exact RDSS only for extreme rotation and sufficiently short self-similar period, with the large-rotation lambda window shrinking like the stated `1/(1+alpha^2)` exponent.

**Hostile check.** Exact symmetry is a hypothesis, not a compactness consequence. Moderate rotation, longer-period RDSS, and genuinely nonperiodic renormalized trajectories remain outside the theorem.

## Role 3 — concentration-compactness / critical elements

**Task.** Test whether global critical-element logic can manufacture the missing almost-periodic finite-`I` orbit.

**Finding.** Gallagher–Koch–Planchon/Kenig–Koch rely on global critical spaces with profile decompositions and decoupling. The finite-`I` quantity is local-supremum based and lacks a source-bound profile orthogonality/Palais–Smale theorem.

**Hostile check.** Separated or moving concentration packets can evade fixed compact sets while preserving local critical bounds at the level of functional logic. No PDE counterexample is asserted; the burden is a new tightness/decoupling theorem.

## Role 4 — pressure / local-energy

**Task.** Compare the pressure topology in the blow-up passage with Pineau–Vicol Theorem 1.9.

**Finding.** `D` is critical `L^(3/2)` oscillation control modulo means. Pineau–Vicol assumes a fixed-annulus `L^infinity` pressure bound. Weak `L^(3/2)_loc` convergence cannot pass or create that stronger bound. Near-field Calderón–Zygmund and harmonic far-field pieces must be separately controlled.

**Hostile check.** Prior pressure-tail failure `F-NS-B1a-C001-PRESSURE-SUMMABILITY` forbids reconstructing a missing far-field bound by an unjustified unsummed shell series; it does not forbid a separately proved local annular estimate.

## Role 5 — vorticity / geometric depletion

**Task.** Assess the weighted-enstrophy mechanism as a transferable rigidity coordinate.

**Finding.** Pineau–Vicol provides a real local depletion mechanism: one-slice near-stationarity produces small local enstrophy, propagates it, and activates CKN regularity. This is orthogonal to absolute scale-shell accounting and is therefore a promising *method-transfer target*.

**Hostile check.** The adjoint weight and pressure/derivative estimates use stronger source assumptions. Replacing them by finite `A,C,D,E` must be proved, not inferred.

## Role 6 — adversarial constructions

**Task.** Stress the proposed “compactness gives a near-stationary slice” shortcut.

**Finding.** Periodic/RDSS or rotating renormalized trajectories can be compact while their time derivative never becomes small in the required norm. Translation/dilation drift and multiple profiles additionally create moving-center/far-field leakage.

**Hostile check.** Any Stage-B extraction theorem must carry a signed/monotone/integrable derivative budget or another anti-recurrence mechanism. Boundedness alone fails as logic.

## Role 7 — formal assurance / novelty boundary

**Task.** Enforce current RAKL gates and source-version correctness.

**Finding.** Current RAKL `main` at `60a38728d0ebace2fa2312bcad81d1d3f9df757c` was read first. Its post-pin change is CI path behavior, not a change to math-context/memory/trace/assurance semantics. Pineau–Vicol **v2 dated 2026-08-06** must be bound explicitly because Theorem 1.9 is an added result. No candidate is present in the trace.

**Hostile check.** Source novelty is not theorem novelty. Same-context role separation is not isolated review. Root promotion is unavailable.

## Consensus

`TRANSFER_BLOCKED_SCOPED / NEW_PRIMARY_LITERATURE_MILESTONE / NO_METHOD_TRANSFER_YET / ROOT_AUTHORITY_NONE`

The strongest next question is not “are Type-I singularities self-similar?” It is the narrower pre-candidate atom:

`NS-B1b1a`: determine whether Pineau–Vicol's local weighted-enstrophy/epsilon-regularity argument can be reformulated under the exact finite `A,C,D,E` and suitable-weak pressure controls preserved by the Albritton–Barker blow-up passage.

Even a successful `NS-B1b1a` would leave a second independent gap: extraction of one late self-similar time with small weighted generator. No candidate is authorized until that child freezes its own context, memory review, expert review and trace.
