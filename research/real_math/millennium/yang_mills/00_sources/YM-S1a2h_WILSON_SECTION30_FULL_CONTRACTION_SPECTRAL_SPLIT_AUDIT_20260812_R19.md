# YM-S1a2h R19 — Wilson Section 30 full-contraction / relevant-splitting audit

**Authority:** proposal/shadow source-audit evidence only. This is not a Yang–Mills theorem, not a theorem-nonexistence result, not independent review, and not root authority.

**Atom:** `YM-S1a2h` / issue #301  
**Signature:** `YM-S1a2h-WILSON-FULL-RG-CONTRACTION-VS-RELEVANT-SPECTRAL-SPLITTING-STABLE-GRAPH-CLOSURE`  
**Frozen application base:** `3871283cfe5040801b174e25b045e05ee0228cc2`  
**Current RAKL source of truth used before the detailed source test:** `1b866dc5aafc7e952f4de5acaa75bd3f7b71048e`, method `3.0.0`, package `0.1.0`.

## Primary source and verification boundary

Primary source inspected: Jonathan J. Wilson, author-uploaded manuscript, *Rigorous Measure-Theoretic Construction of Yang-Mills Quantum Field Theory via Gribov-Zwanziger Quantization, Polymer Expansion, and Renormalization Group Analysis: Spectral Properties, Exponential Clustering, and Mass Gap in Four Dimensions*, ResearchGate publication `399279692`, DOI `10.13140/RG.2.2.22056.43527`. The indexed full text identifies the content as uploaded by Jonathan Jared Wilson on 2026-03-05.

The bounded source audit used the author-uploaded indexed primary text for §§30.4–30.7, including equations (524)–(535), Theorem 30.6, and its graph-transform proof steps. The web retrieval surface labels the item as a PDF, but screenshot calls fail because the returned ResearchGate search object is not exposed to the screenshot backend as `application/pdf`. Visual PDF verification is therefore `CANNOT_CHECK` in this run; this is a tooling/verification limitation, not mathematical evidence. The parsed author-uploaded text independently exposed the load-bearing formulas and theorem text on repeated searches.

## Exact source-bound interface

Section 30.4 defines the scale state as a pair `(c_k,K_k)`, with `c_k` the relevant/marginal coupling coordinates and `K_k` the irrelevant polymer activity, in a norm of the form

`||(c_k,K_k)||_{X_k}=|c_k|+||K_k||`.

Section 30.5 then forms the full sequence state and, from the one-step difference estimates, states equation (528) in the form

`delta_{k+1} <= Lip_k delta_k`,

`Lip_k = max{ ||L_k|| + 2 C_k r, kappa_k + 2 A_k r }`,

where the first `L_k` is the linearized coupling map. The source then requires parameters such that `sup_k Lip_k <= L < 1`, and uses that to call the induced full sequence map a Banach contraction.

Section 30.6/30.7 classifies the same coupling-space linearization by relevant/marginal/irrelevant sectors. Equation (534) states a uniform relevant expansion and irrelevant contraction,

`||L_k|_rel|| >= lambda_rel > 1`, `||L_k|_irr|| <= lambda_irr < 1`,

and Theorem 30.6 assumes both this spectral splitting and the equation-(528) condition `sup_k Lip_k < 1`. Its proof Step 1 again invokes a strict contraction on a sequence norm containing the full `(c_k,K_k)` state; Step 2 only afterward introduces a graph transform to eliminate expanding relevant directions.

The same manuscript elsewhere makes the relevant sector non-vacuous on the displayed surface: its operator basis lists a quadratic mass coordinate as relevant, and later the RG supplement says the only relevant quadratic operator is the mass term while the kinetic term is marginal. Theorem 30.6 itself is stated as a codimension-`|A_rel|` stable manifold and explicitly performs an expanding-direction elimination step.

## Counterexample-first / direct compatibility check

This check does not need an imported stable-manifold theorem. It uses the source's own equations.

If `A_rel` is nonempty and the restriction in (534) is the restriction of the same linearized coupling map occurring in (528), then for every scale `k`, in the same norm,

`||L_k|| >= ||L_k|_rel|| >= lambda_rel > 1`.

Because the remaining radius correction in the first branch of (528) is nonnegative,

`Lip_k >= ||L_k|| >= lambda_rel > 1`.

Therefore the simultaneous theorem hypotheses

`||L_k|_rel|| >= lambda_rel > 1`

and

`sup_k Lip_k < 1`

cannot both hold for the same unchanged full forward coupling coordinate. No choice of a smaller positive radius `r` or smallness parameter can reverse this inequality. A weighting of the sequence norm also does not make an expanding one-step coupling block into a forward contraction unless the expanding coordinate is first removed, solved backward, or represented on an invariant graph with a different map.

This is stronger and more local than R18's generic “bounded relevant block is not enough” control: the source's own displayed definitions make the full-forward Banach-contraction premise incompatible with its relevant spectral-splitting premise when the relevant sector is present.

## Does the later graph-transform paragraph repair it?

Not as displayed. Theorem 30.6 proof Step 1 obtains “for each choice of the finite-dimensional relevant/marginal initial data” a unique full trajectory by applying Banach contraction to the full sequence state. Step 2 then says the graph-transform operator on `Gamma: Pi_irr X_0 -> Pi_rel X_0` is contractive because of the nonlinear Lipschitz bounds and the spectral gap. That is the correct *shape* of a repair, but the displayed proof does not replace the impossible Step-1 full-forward contraction with a mixed-direction Lyapunov–Perron/graph-space map, nor does it expose a graph-transform contraction constant built from the inverse relevant expansion and the stable contraction.

A source-complete repair would need, at minimum, to define the actual mixed-direction operator before using Banach's theorem: evolve stable/irrelevant coordinates forward; solve the relevant coordinates backward (or through an equivalent invariant-graph equation using the inverse relevant block); prove the graph transform maps the stated shrinking domain into itself; and bind quantitative derivative constants yielding a contraction on graph space. The relevant inverse must enter with a factor below one, e.g. a bound controlled by `lambda_rel^{-1}`, rather than treating `||L_k||` of the full forward map as below one.

This repair shape is not promoted as a theorem transfer. Prior rigorous RG/stable-manifold work is only a structural analogue because its field content, norms, gauge/GZ constraints, nonautonomous trajectory, reflection-positive/OS source structure, and physical spectral obligations are not already matched.

## RAKL-current DifferenceWitness realization-domain guard

Current RAKL `failure_lattice.py` requires realization-domain typing before a DifferenceWitness can support consequential obligation-strength routing. Accordingly, the generic finite-dimensional hostile statement “an unchanged forward block with spectral radius/eigenvalue above one cannot be a strict contraction in an equivalent norm” is recorded only as `AMBIENT_REPRESENTATION` when used abstractly. It is **not** used to weaken a Yang–Mills root obligation.

The scoped source diagnosis above instead comes from the target atom's exact displayed source formulas (528) and (534). It says the *written Section-30 proof interface* is internally incompatible unless the full forward map is retyped. It does not say no correct Yang–Mills stable manifold exists.

## Local failure versus gluing failure

**Local mathematical/source-proof failure:** the displayed full-forward contraction premise and displayed relevant expansion premise cannot coexist for the same nonempty relevant coordinate.

**Representation inconsistency (secondary):** Section 30.2 says pure Yang–Mills has no relevant operators except possible Gribov effects, while the operator basis / later supplement explicitly carries a relevant quadratic mass coordinate. This is not used as the main contradiction because the source may intend a GZ-specific mass coordinate; it must nevertheless be typed consistently in any repair.

**Local-to-global / gluing residual (separate):** even a repaired regulator-by-regulator stable manifold does not supply the R18-missing regulator-matched decay/slaving estimate for all relevant coordinates in the Section-38 universality comparison. It also does not establish the same-theory OS source algebra, transfer Hamiltonian, volume/lattice-spacing uniform physical mass normalization, or continuum spectral identification required by root #5.

## Expert-cell synthesis

1. **Rigorous lattice-gauge RG:** equations (528) and (534) cannot both have the stated strict inequalities on the same full coupling map with a nonempty relevant block.
2. **Nonautonomous stable-manifold dynamics:** a valid construction should contract a graph/Lyapunov–Perron operator, not the unchanged full forward state containing expanding coordinates; the source's Step 2 has the right label but not the quantitative replacement on the inspected surface.
3. **Banach/functional analysis:** restriction norm lower bounds force the full operator norm lower bound; decreasing the nonlinear radius cannot make the linear expanding block contractive.
4. **Gauge/GZ representation:** whether the mass coordinate is an allowed GZ relevant coordinate must be typed explicitly; changing the coordinate set changes the theorem being proved.
5. **OS/continuum spectral gluing:** this local repair cannot be promoted through the separate Section-38/OS/continuum interfaces without new same-theory estimates.
6. **Adversarial verification:** cheapest exact falsifier passed against the displayed source equations; no target-theory counterexample is claimed.
7. **RAKL-v3 provenance/metrology:** the generic analogue stays representation-only under the new realization-domain gate; episode, diagnosis, proposed obstruction, and any future lesson remain distinct; same-context review earns `0/3` independent-review credit.

## Outcome and next discriminator

**Outcome:** `PARTIAL_SUCCESS / SOURCE_DISPLAYED_PROOF_INCOMPATIBILITY_VERIFIED / REPAIR_NOT_SOURCE_BOUND`.

**Residual after:** `RES-YM-S1a2h-MIXED-DIRECTION-LYAPUNOV-PERRON-OR-GRAPH-TRANSFORM-WITH-QUANTITATIVE-CONSTANTS-PLUS-SECTION38-DELTA-LAMBDA-SAME-THEORY-GLUING`.

The next high-information source test is not another generic contraction argument. It is to locate or supply, before any root-facing composition, an exact mixed forward/backward graph-transform operator with its norm, derivative constants, `lambda_rel^{-1}`-type gain, shrinking-domain invariance along the asymptotically-free trajectory, and a regulator-matched Lipschitz/slaving theorem for the relevant coordinates used by Section 38.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.
