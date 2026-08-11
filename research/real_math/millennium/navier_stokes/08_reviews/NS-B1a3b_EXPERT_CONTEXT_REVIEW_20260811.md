# NS-B1a3b same-context expert cell — vorticity/geometric-depletion interface

**Authority:** `SAME_CONTEXT_ROLE_SEPARATED_REVIEW_ONLY / NOT_INDEPENDENT_REVIEW / ROOT_AUTHORITY_NONE`

**Frozen atom:** `NS-B1a3b`  
**Context packet:** `sha256:6dd7969ddde37ed9384dc40064927cdda8b1ba78a536791b21aa06298dbf0900`  
**Review time:** `2026-08-11T15:08:30Z`

## Cell composition and delegated remit

1. **PDE blow-up analyst** — background in suitable weak solutions, parabolic scaling, ancient limits, Type-I/II classifications. Remit: bind the exact producer state space and scaling laws.
2. **Vorticity-geometry analyst** — background in vortex stretching, vorticity-direction coherence and two-dimensional rigidity. Remit: audit Giga–Miura and geometric-depletion hypotheses.
3. **Compactness/interface auditor** — background in weak/strong convergence, pressure localization and nonlinear observable closure. Remit: test whether normalized vorticity survives the actual extraction topology.
4. **Adversarial construction analyst** — background in oscillation/concentration counterexamples and noncompact symmetries. Remit: build the cheapest topology-level falsifier for invalid passage claims.
5. **Rigidity/unique-continuation analyst** — background in ancient-solution Liouville arguments and backward uniqueness. Remit: prevent theorem-interface leakage and equation-class substitution.
6. **Proof/authority reviewer** — background in formal statement alignment, source provenance and novelty boundaries. Remit: enforce the Clay root contract, distinguish source theorem from inference, and downgrade recent/preprint evidence appropriately.

## Deliberation ledger

### Finding A — “Type I” is not one state space

The PDE analyst bound Albritton–Barker's Type-I notion to finite local `I=sup(A+C+D+E)`. The vorticity analyst bound Giga–Miura's “type I mild” hypothesis to the pointwise self-similar rate `||u||_∞(t) <= C0(-t)^(-1/2)`. The source text in Albritton–Barker lists this `c_∞` quantity among stronger Type-I controls from which their weak finite-`I` condition follows, while warning that boundedness of one common Type-I quantity is not generally known to imply the others. The proof/authority reviewer therefore rejected treating the two labels as interchangeable.

**Cell decision:** direct transfer `AB finite-I -> Giga–Miura theorem` is blocked unless an additional state-space implication is proved. This is a theorem-signature mismatch, not evidence against the Giga–Miura theorem.

### Finding B — the geometric observable is not closed under the AB compactness statement

The compactness auditor noted that AB's source-level suitable-weak compactness gives strong `L^3_loc` convergence of velocity and weak `L^{3/2}_loc` convergence of pressure, together with the usual weak derivative control. Giga–Miura's blow-up argument instead obtains locally uniform derivative/vorticity convergence from bounded mild-solution parabolic estimates before passing `ζ=ω/|ω|` on compact subsets where the limiting vorticity is nonzero.

The adversarial analyst supplied a topology calibration: on a fixed compact set, `w_n(x)=(0,n^{-1} sin(n x_1),0)` is divergence free and tends strongly to zero in every local `L^3`, while `curl w_n=(0,0,cos(n x_1))` stays order one and its normalized direction alternates between `+e_3` and `-e_3` away from zeros. Its local `H^1` seminorm remains bounded. This is **not** claimed to be a Navier–Stokes solution; it is a functional-analytic falsifier showing that the convergence/boundedness topology alone cannot justify continuity of `u -> curl(u)/|curl(u)|`.

**Cell decision:** any finite-`I` geometry route needs a separate vorticity-direction compactness/defect certificate, or a stronger regularity theorem that upgrades the extraction topology. Silent passage of normalized vorticity is rejected.

### Finding C — Giga–Miura remains an exact solved subclass analogue

The vorticity analyst and rigidity analyst jointly checked the positive side. Under Giga–Miura's stronger Type-I mild hypothesis, maximum-velocity rescaling gives uniform derivative bounds and locally uniform convergence. Their alignment hypothesis on high-vorticity sets scales so that, on compact subsets where the limiting vorticity is nonzero, the direction oscillation collapses and the limiting vorticity has a spatially constant direction. The subsequent two-dimensional bounded-ancient Liouville step is therefore theorem-matched inside that state space.

**Cell decision:** retain `GM-TYPEI-GEOMETRY` and `GM-2D-LIOUVILLE` as solved analogue/method-transfer evidence; do not blacklist them because the broader AB finite-`I` interface fails.

### Finding D — recent logarithmic-depletion work is narrower, not a bridge

The proof/authority reviewer classified Grujic arXiv:2607.08866 as a recent primary preprint source. Its stated mechanism assumes a critical-point singularity/concentration setting and critical Lorentz-scale vorticity control together with a logarithmic BMO-type condition on vorticity direction. The compactness auditor found no source-bound derivation of those hypotheses from AB finite `I` in this cycle.

**Cell decision:** retain as a near-solved geometry analogue and vocabulary expansion only. It cannot close the finite-`I` inheritance interface in this cycle.

### Finding E — pressure, far field, unique continuation, and equation changes stay separated

The rigidity analyst kept the prior `NS-B1a3` safeguards active. A geometry criterion local to high-vorticity regions does not itself repair the independent global critical-tail/pressure issue in `NS-B1a3a`. Backward uniqueness is not invoked because no exact terminal/exterior hypotheses are produced here. Stationary Leray-profile theorems are not substituted for general time-dependent ancient solutions. Type-II is untouched.

**Cell decision:** scoped prior failures guide routing only; none is promoted to a global method blacklist.

## Alternatives considered

The cell considered: (i) directly importing Giga–Miura as a finite-`I` theorem; (ii) attempting to infer the `L^∞` self-similar rate from finite `I`; (iii) passing vorticity directions through AB compactness without an upgrade; (iv) using the recent logarithmic-depletion preprint as a bridge; and (v) keeping the geometry lane open but replacing the target with an exact closure/state-space prerequisite. Alternatives (i), (iii), and (iv) fail exact interface checks; (ii) is a major unresolved bridge, not something this cycle may assume. The cell unanimously selected (v).

## Recommended discriminator before candidate generation

Freeze a candidate that makes only this bounded claim: **the currently registered finite-`I` extraction package does not itself satisfy the input/closure hypotheses of the selected vorticity-direction rigidity theorems.** Falsify it by exhibiting either (a) a primary-source theorem deriving the Giga–Miura `L^∞` Type-I rate from AB finite `I`, or (b) a source-valid closure theorem for an exact geometric observable under the AB compactness topology sufficient for rigidity.

The next constructive child, if this candidate survives, should search for a scale-critical geometric defect functional that is both dynamically controlled/inherited in the finite-`I` class and sequentially closed under its actual compactness topology.
