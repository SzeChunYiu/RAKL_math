# NS-B2a1d — exact Hill-vortex hostile witness for the F=1 Euler-side rigidity interface

**Atom:** `NS-B2a1d` / issue #213  
**Parent:** `NS-B2a1` / issue #198, root #4  
**Framework frozen before consequential verification:** `SzeChunYiu/RAKL@43897d3afaf0038385102d5acc64793c05ec40f0`, method 3.0.0  
**Application pre-action commit:** `f8d0a0d5b311d0ffb3655542b25655c9fb9f7166`  
**Pre-action receipt:** `sha256:f0ea46e1b4b119248e09d9293bb81194ae3df7a4305ec70df9a11955e993b182`  
**Authority:** `SOURCE_BOUND_SCOPED_RIGIDITY_FALSIFIER / PROPOSAL_SHADOW / ROOT_AUTHORITY_NONE`

## Frozen question

Does an explicit translating Hill spherical vortex give a nonzero ancient Euler pair satisfying the displayed `F(a)=1` Euler-side state in Seregin, arXiv:2606.29468v1, Theorem 3.1 — namely (3.5), the distributional Euler equations (3.6), and the local-energy inequality (3.7) — while centered backward observation windows become small because the coherent core translates to the far field?

A positive answer falsifies only the implication

```text
(3.5)-(3.7) + nonzero state + centered backward local smallness
    ==> global Euler triviality
```

when no additional no-incoming-flux/tightness/recentering/ancestry condition is supplied. It does **not** construct a Navier–Stokes blowup and does not show that Hill's vortex lies in the image of Seregin's Navier–Stokes extraction.

## Primary-source binding

1. **Seregin 2026, arXiv:2606.29468v1, Theorem 3.1.** The limit state is an ancient Euler pair on `R^3 x (-infinity,0)` with the scale-weighted kinetic, pressure and gradient bound (3.5), distributional Euler equation (3.6), local-energy inequality (3.7), and source nontriviality (3.8). In the logarithmic example immediately following the theorem, `F(a)=1`.
2. **Choi, arXiv:2011.06808v2, §§1.1, 2.3, 2.4.** Hill's spherical vortex is an exact three-dimensional Euler traveling wave. Its unit-ball vortex core translates forever at constant speed, the physical velocity vanishes at spatial infinity, and the explicit stream function is

```text
psi_H(r,z) = (W/2) r^2 (5/2 - (3/2)(r^2+z^2)),     rho <= 1,
           = (W/2) r^2 rho^(-3),                    rho > 1,
W = 2/15,
rho = sqrt(r^2+z^2).
```

The corresponding physical velocity is `V_r=-(partial_z psi_H)/r`, `V_z=(partial_r psi_H)/r`. Choi also records the two-parameter Hill scaling and nonzero travel speed `W_H(lambda,a)=(2/15) lambda a^2`.
3. **Abe, arXiv:2008.09345, §§1, 2.2.** The traveling-wave representation is source-bound independently, and Hill's spherical vortex appears as the explicit limiting Hicks–Moffatt case. This is corroborating primary evidence; the load-bearing velocity calculation below uses Choi's explicit physical stream function.

## Exact velocity and regularity calculation

Differentiate Choi's stream function. For the unit Hill profile,

```text
rho <= 1:
V_r = (3W/2) r z,
V_z = (W/2) (5 - 6 r^2 - 3 z^2).

rho > 1:
V_r = (3W/2) r z rho^(-5),
V_z = (W/2) (2 z^2 - r^2) rho^(-5).
```

In Cartesian coordinates the radial component is

```text
(V_1,V_2) = (3W/2) z (x_1,x_2)                         for rho <= 1,
(V_1,V_2) = (3W/2) z (x_1,x_2) rho^(-5)                for rho > 1,
```

so there is no axis singularity. On `rho=1`, both radial formulas coincide, and

```text
V_z^inside = (W/2)(2-3r^2) = V_z^outside.
```

Thus `V` is continuous, piecewise `C^1`, with bounded first derivatives on each side of the sphere. Continuity removes any surface measure from the weak first derivative, hence `V in W^{1,infinity}_loc(R^3)`. Outside the unit ball,

```text
|V(x)| <= C rho^(-3),
|grad V(x)| <= C rho^(-4).
```

Consequently

```text
V in L^p(R^3) for every p > 1,
grad V in L^2(R^3),
V in L^2(R^3) intersect L^3(R^3).
```

These are direct consequences of the explicit primary-source formula, not numerical evidence.

## Pressure class

Let `c=W e_3` with the sign chosen to match the physical translation and set

```text
U(x,tau) = V(x-c tau),   tau < 0.
```

Choi's traveling-wave statement gives a global weak Euler solution. Normalize pressure by the standard whole-space representation

```text
P = R_i R_j (U_i U_j)
```

up to the harmless time-dependent pressure gauge. Since `U in L^3(R^3)` uniformly in time, `U_i U_j in L^(3/2)` and Calderon–Zygmund boundedness yields a translation-invariant finite bound

```text
||P(tau)||_(L^(3/2)(R^3)) <= C ||V||_3^2.
```

The explicit exterior irrotational region gives the consistent asymptotic check

```text
P = c dot V - |V|^2/2 + constant,
```

hence `P=O(rho^(-3))` after normalization at infinity. The Riesz-transform argument, rather than this asymptotic alone, is the global `L^(3/2)` certificate.

## Verification of Seregin (3.5) with F(a)=1

Write `Q(a)=B(a) x (-a^2,0)`.

### Kinetic term

For every `a>0` and every `tau`, translation does not change the global `L^2` norm:

```text
(1/a) integral_{B(a)} |U(x,tau)|^2 dx
    <= ||V||_2^2/a,                   a >= 1.
```

For `0<a<=1`, boundedness of `V` gives

```text
(1/a) integral_{B(a)} |U|^2 <= C a^2.
```

Therefore the first `F=1` term is uniformly finite.

### Pressure term

For every `a>0`,

```text
(1/a^2) integral_{-a^2}^0 integral_{B(a)} |P|^(3/2) dx d tau
 <= ||P(0)||_(3/2)^(3/2),
```

because the pressure profile merely translates. Hence the second term is uniformly finite.

### Gradient term: the moving-core occupancy lemma

For any nonnegative `h in L^1(R^3)` and nonzero constant velocity `c`, Fubini gives

```text
integral_{-a^2}^0 integral_{B(a)} h(x-c tau) dx d tau
  = integral h(y) * |{tau in [-a^2,0]: |y+c tau|<a}| dy
  <= (2a/|c|) ||h||_1.
```

The time set is the intersection of `[-a^2,0]` with a line crossing a radius-`a` ball at speed `|c|`, so its length is at most `2a/|c|`. Taking `h=|grad V|^2` gives

```text
(1/a) integral_{Q(a)} |grad U|^2
  <= 2 |c|^(-1) ||grad V||_2^2
```

for every `a>0`. This proves the third `F=1` term.

Thus the exact Hill traveling solution has a finite constant in Seregin's displayed bound (3.5) with `F(a)=1`.

## Euler equation and local-energy interface

The pair is an exact traveling Euler solution, so (3.6) holds distributionally. The explicit velocity is globally locally Lipschitz as above; the weak Euler equation can therefore be multiplied by `U` and the product rule is valid. With compactly supported test functions in space-time this gives the local kinetic-energy **equality**

```text
integral |U(tau_0)|^2 phi(tau_0)
 = integral_{-infinity}^{tau_0} integral
   ( |U|^2 partial_tau phi + U dot grad phi (|U|^2+2P) ),
```

and hence Seregin's inequality (3.7) for nonnegative `phi`.

## Nontriviality and the source-threshold boundary

`V` is nonzero on the unit ball, so for every finite admissible mixed-norm exponent pair used in the source, the corresponding unit-cylinder quantity is strictly positive. Therefore this explicit state satisfies a nontriviality inequality of the same form as (3.8) for **some** positive threshold chosen below its own mixed norm.

This does not identify that threshold with Seregin's ancestry-specific `epsilon_0` inherited from a hypothetical Navier–Stokes singularity. No such identification is needed for the hostile rigidity test, and none is claimed.

## Centered backward escape

At backward time `tau=-A^2`, the vortex core is a distance `|c|A^2` from the origin while the centered observation ball `B(A)` has radius only `A`. For sufficiently large `A` and every `x in B(A)`,

```text
|x+c A^2| >= |c|A^2-A >= (|c|/2) A^2.
```

The exterior formula therefore gives

```text
sup_{x in B(A)} |U(x,-A^2)| <= C A^(-6).
```

Hence, for every finite `p>=1`,

```text
||U(.,-A^2)||_{L^p(B(A))} <= C A^(3/p-6) -> 0.
```

In particular centered backward `L^3` and `L^6` norms vanish even though the global Euler state is a permanently nonzero traveling vortex. The mechanism is noncompact translation, not dissipation.

## Falsifier verdict

`HILL_ADVERSARY_MATCHES_EULER_SIDE_INTERFACE`.

The conditional moving-core calibration in XM005/PR #71 can be upgraded, for the Euler-side interface only, to an **exact source-bound adversary**: a translating Hill spherical vortex satisfies the displayed `F=1` scale budget (3.5), the Euler equation (3.6), the local-energy inequality (3.7), and nontriviality of the same form, while centered backward local observation decays to zero.

Therefore a rigidity proof that consumes only those Euler-side properties plus centered backward local smallness is false. Any viable Seregin-ancestry closure must use an additional producer-specific coordinate that excludes the translating incoming-core world — e.g. a genuinely inherited no-incoming-flux/tightness/recentering condition or another global invariant with an exact source-to-limit proof.

## DifferenceWitness and exact residual

This is **not** a counterexample to Seregin Theorem 3.1 and **not** a Navier–Stokes singularity. The theorem says that a hypothetical source sequence produces a member of an Euler class; it does not say every Euler member of that displayed class is source-realizable. The Hill pair has not been shown to be in the image of that extraction.

Accordingly the local mathematical failure and the local-to-global/gluing failure remain separate:

- **Euler-side local rigidity failure:** `F-NS-B2a1d-F1-CENTERED-LOCAL-RIGIDITY-NONCOMPACT-TRANSLATION` — centered local smallness plus the displayed Euler-side state is insufficient.
- **Producer-to-limit gluing residual:** `O-NS-B2a1-DOUBLE-LIMIT-TAIL-INHERITANCE` — prove a source-inherited tail/no-incoming coordinate with the correct `lim_R limsup_k` quantifiers.
- **New sharpened producer obstruction:** `O-NS-B2a1d-PRODUCER-MUST-EXCLUDE-TRANSLATING-INCOMING-CORE` — the inherited coordinate must specifically charge or exclude moving-core escape.

The next high-information move is therefore back to `NS-B2a1a` (prelimit annular/tail tightness) or, orthogonally, `NS-B2a1b` only if a signed flux/telescoping law can be shown to detect a translating incoming coherent core. Generic Euler Liouville search based only on centered local decay is pruned.

## Root boundary

Root status remains `OPEN_NO_SOLUTION_CERTIFICATE`, root authority `NONE`, independent mathematical reviews `0/3`. No exact Clay alternative, closed proof DAG, verifier/dependency/axiom closure, isolated recheck, bounded root novelty search or three isolated reviews has been supplied.
