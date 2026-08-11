# XM005 — Moving-core hostile calibration for Type-II Euler-limit rigidity

**Atom:** `XM-MOVING-CORE-RIGIDITY-005`  
**Target:** Navier–Stokes issue #65, `NS-B2a`  
**Framework source of truth inspected first:** `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`  
**Application base:** `SzeChunYiu/RAKL_math@5d6bdc6f566921f51a375fdc2e8035123cf4830c`  
**Authority:** `SOURCE_BOUND_HOSTILE_CALIBRATION / TRANSFER_RESEARCH_CONTROL_ONLY / NO_NS_CANDIDATE / NO_ROOT_AUTHORITY`

## Question

The fresh `NS-B2a` route isolates an ancient Euler limit from Seregin's Type-II Navier–Stokes scaling and asks for a far-field/no-incoming-energy inheritance theorem plus Euler rigidity. A retrospective calculation in that issue also observes backward times at which centered expanding balls see small local velocity.

This cycle asks the cheapest adversarial question before any rigidity theorem is invented:

> Can centered backward local smallness coexist with a nontrivial coherent Euler structure simply because the structure translates through space faster than the observation window expands?

A positive hostile calibration does not refute Seregin's source class. It shows that a proposed rigidity interface must control moving-center escape/incoming flux rather than infer global triviality from centered local decay alone.

## Primary-source anchors

1. Gregory Seregin, *On potential Type II blowups for the Navier–Stokes equations*, arXiv:2606.29468v1 (28 June 2026), Theorem 3.1. The source produces a nontrivial ancient Euler pair `(u,p)` on `R^3 x (-infinity,0)`, with the scale-weighted energy/pressure/gradient bound (3.5) and local energy inequality (3.7).
2. Ken Abe, *Existence of vortex rings in Beltrami flows*, arXiv:2008.09345, current manuscript dated 22 March 2026. The source constructs classical axisymmetric traveling-wave Euler solutions. Its traveling frame is `v(x,t)=u(x+u_infinity t)-u_infinity`; `v` vanishes at spatial infinity, and Theorem 1.1 gives compactly supported vorticity for a family of vortex rings.
3. Daomin Cao, Guolin Qin, Weilin Yu, Weicheng Zhan and Changjun Zou, *Existence, uniqueness and stability of steady vortex rings of small cross-section*, arXiv:2201.08232v4. The source treats steady vortex rings as global traveling-wave solutions and uses kinetic energy/impulse variational structure. It is a calibration source, not an assertion that every such ring lies in Seregin's exact class.

No secondary source is used for the load-bearing traveling-wave or Type-II statements.

## Exact kinematic lemma

Let `c in R^3`, `c != 0`, and let `h >= 0` be integrable on `R^3`. For every `a>0`,

```text
I(a) = integral_{-a^2}^0 integral_{B(a)} h(x+c*tau) dx d tau
     <= (2a/|c|) ||h||_{L1(R^3)}.
```

Proof: set `y=x+c*tau` and use Fubini. For fixed `y`, the set of times satisfying `|y-c*tau|<a` is the intersection of `[-a^2,0]` with the preimage of a radius-`a` ball under a line of speed `|c|`. Its one-dimensional length is at most `2a/|c|`. Integrating this occupancy time against `h(y)` gives the bound.

This lemma is elementary but load-bearing: a coherent packet can cross a centered cylinder for only `O(a)` time even though the cylinder has parabolic duration `a^2`.

## Conditional Seregin-budget calibration

Consider a traveling ancient Euler pair

```text
U_c(x,tau) = W(x+c*tau),
P_c(x,tau) = P(x+c*tau),
```

with `c != 0`. Assume, only for this calibration, the exact integrability needed below:

```text
W in L2(R^3),
grad W in L2(R^3),
P in L^(3/2)(R^3),
```

and enough local boundedness/regularity to control the `a -> 0` regime.

Then the moving-core occupancy lemma gives, for large `a`,

```text
(1/a) integral_{Q(a)} |grad U_c|^2 <= 2|c|^{-1} ||grad W||_2^2,
(1/a^2) integral_{Q(a)} |P_c|^(3/2) <= 2(|c| a)^{-1} ||P||_(3/2)^(3/2),
(1/a) sup_{-a^2<tau<0} integral_{B(a)} |U_c|^2 <= a^{-1} ||W||_2^2.
```

For small `a`, local boundedness gives the required boundedness after the same scale factors. Thus the three displayed `F(a)=1` pieces of Seregin's (3.5) are **kinematically compatible** with a translating finite-energy profile.

This is deliberately conditional. The present cycle did not locate a primary-source statement proving that Abe's specific Beltrami rings satisfy every exact global `L2/H1/L^(3/2)` requirement above, so the ring is not claimed as a literal counterexample inside Seregin's Theorem-3.1 class. The conditional world is sufficient as a hostile interface test; a future exact counterexample claim would require source-binding those integrability and local-energy hypotheses.

## Backward expanding-ball escape

Let `tau -> -infinity` and take any observation radius `R(tau)=O(sqrt(|tau|))`. A traveling core centered at `-c*tau` has distance `|c||tau|` from the fixed origin, which dominates `R(tau)`. If `W in L^p(R^3)` for the local norm under consideration, then

```text
||W(·+c*tau)||_{L^p(B(R(tau)))} -> 0
```

because the translated observation set escapes to the spatial tail of `W`.

Therefore the conjunction

```text
centered backward expanding-ball smallness
+ scale-weighted local/spacetime budget
```

is not, by itself, a logically faithful surrogate for

```text
global triviality of the ancient Euler state.
```

The missing interface is exactly what `NS-B2a` already suspected: a source-inherited no-incoming-energy/far-field-tightness or moving-center control that prevents a coherent packet from entering/leaving the observation region without being charged.

## Structural transfer and DifferenceWitness

**Transferred operation:** `T-XM-ROOT-BRIDGE-STABILITY-AUDIT`, at no more than its currently canonical application authority. No literal P-vs-NP, BSD, Hodge, RH or Yang–Mills mathematics is transferred.

| Coordinate | Prior cross-problem pattern | NS-B2a target |
|---|---|---|
| attractive local/surrogate observable | closure size, positive norm, discrete order, detector output, local spectral lemma | centered backward local smallness + local scale budget |
| root-critical quantity | actual cover cost / Li sign / complex order / algebraic source / physical continuum gap | global Euler triviality in exact Seregin limit class |
| missing bridge | faithfulness / correction / assembly / target binding | no-incoming-energy, tightness, recentering or equivalent global control |
| hostile world | surrogate excellent while target bad | nontrivial translating coherent core that escapes centered windows |
| literal source mathematics transferred | none | none |

**DifferenceWitness:** unlike P-vs-NP's free closure mass or RH's conditional norm identity, the NS failure mechanism is geometric transport through a noncompact translation symmetry. The common abstraction is only that a locally favorable observable can fail to preserve the root-critical coordinate across an unproved interface.

**Cheapest target falsifier:** before any Euler Liouville theorem uses backward centered smallness, test the claimed implication on a translating finite-energy profile satisfying the exact proposed source norms. If the proof does not explicitly exclude moving-core escape, the implication is incomplete.

## Seven-role same-context expert cell

1. **Type-II / suitable-weak Navier–Stokes analyst** — bound Seregin Theorem 3.1 and kept the target limited to the ancient Euler limit class.
2. **Euler vortex-ring analyst** — bound the existence of translating coherent Euler structures and refused to infer unlocated global integrability properties.
3. **Local-energy / scaling analyst** — derived the world-tube occupancy estimate and checked the scale factors.
4. **Concentration-compactness analyst** — identified noncompact translation as the mechanism by which centered local decay can coexist with nontriviality.
5. **Adversarial falsification / assurance analyst** — blocked the stronger claim that a cited vortex ring is already an exact Seregin-class counterexample.
6. **Cross-domain transfer analyst** — transferred only the root-coordinate preservation audit operation and recorded the disanalogies.
7. **RAKL meta-method analyst** — classified the episode as a bridge/gluing diagnostic and proposed a framework-level preservation receipt rather than a new mathematical operator.

This is one same-context role-separated review, not independent mathematical peer review.

## Outcome and residual

**Outcome:** `PARTIAL_SUCCESS / INTERFACE_NECESSITY_SHARPENED`.

The cycle supplies a rigorous occupancy lemma and a conditional hostile world showing why centered backward smallness is not a faithful global-triviality coordinate under translation escape. It strengthens the case that `NS-B2a` must explicitly bind a no-incoming-energy/tightness/recentering theorem before using local decay as a rigidity trigger.

**Residual:** source-bind an exact nontrivial ancient Euler traveling profile satisfying all components of the intended `F=1` Theorem-3.1 budget and local-energy class, or prove directly from the Navier–Stokes blow-up ancestry a tightness/no-incoming-flux property that excludes every moving-core calibration.

**Failure category:** `BRIDGE_GLUING + NONCOMPACT_REPRESENTATION`, not a theorem failure.

**v3 saturation effect:** the local `KNOWLEDGE` coordinate is not the bottleneck; the episode reopens `RELATION` and `PATH` (the interface from local decay to global rigidity) and sharpens `OBSTRUCTION` (moving-center escape). No new primitive operator is justified.

**v3 novelty metrology:** `UNRESOLVED` for mathematical-solution ancestry. At research-control level this is a cross-domain transfer of an existing audit operation, not a novelty claim.
