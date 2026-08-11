# NS-B1a4 C001 R1 — the standard finite-I magnitude ledger does not itself orient local energy flow

**Cycle:** `NS-B1a4-SIGNED-NORECROSSING-20260811-R1`  
**Atom:** `NS-B1a4`  
**Frozen fibre:** `sha256:cf88fa50537b9dfc8df4cc2052c69710fe08963e27463fcb5692187e4fbd3205`  
**Prospective controller:** issue #173  
**Authority:** proposal/shadow route-pruning only; no Navier–Stokes root candidate; root #4 remains `OPEN_NO_SOLUTION_CERTIFICATE`.

## Exact discriminator

Issue #173 froze the narrow question before verification: can the registered finite-`I` magnitude ledger `A+C+D+E`, together with the standard suitable-solution local-energy inequality and pressure localization, **by itself** produce a one-sided signed temporal/no-recrossing law at nested scale, without introducing a new signed flux/correlation observable or stronger global/trajectory input?

The counterexample-first target was also frozen: use an exact smooth pressure-free shear only as a hostile local-energy-flux calibration. The hard DifferenceWitness is binding: such a calibration is not automatically a global finite-`I` mild bounded ancient solution and therefore cannot refute a theorem that genuinely uses that stronger source class.

## Primary source binding

Albritton–Barker, arXiv:1811.00502 (current arXiv rendering dated 22 March 2026), is used at the exact interfaces already registered in this lane:

- Theorem 1.1: Type-I singular suitable solutions are equivalent to nontrivial mild bounded ancient solutions with finite `I`;
- equations (1.1)–(1.5): the dimensionless magnitudes `A,C,D,E,I`;
- Definition 2.1 / equation (2.3): the suitable-solution local-energy inequality;
- Lemma 2.2: local compactness topology;
- equations (2.10)–(2.13): local Calderón–Zygmund plus harmonic pressure decomposition;
- Theorem 1.2: a separate global-`L^3` backward-sequence Liouville theorem.

No source is read as saying that finite `I` already supplies a sign law.

## Exact pressure-free recrossing calibration

Let `y=x_2` and, for all real `t`, define

```text
u(x,t) = (f(y,t),0,0),                    p(x,t)=0,
f(y,t) = 1 + (1/10)e^{-t} cos y - (1/20)e^{-4t} cos(2y).
```

This is an exact smooth Navier–Stokes solution. Indeed,

```text
div u = 0,
(u·∇)u = f ∂_{x_1}u = 0,
∂_t f = -(1/10)e^{-t}cos y + (1/5)e^{-4t}cos(2y)
      = ∂_{yy} f.
```

Hence `∂_t u-Δu+(u·∇)u+∇p=0` exactly. For `t>=0`,

```text
f(y,t) >= 1 - 1/10 - 1/20 = 17/20 > 0.
```

At the spatial point `y=0`,

```text
∂_t f(0,0) = -1/10 + 1/5 = 1/10 > 0,
∂_t f(0,1) = -(1/10)e^{-1} + (1/5)e^{-4} < 0
```

because `2<e^3`. By continuity there is `δ>0` such that on `|y|<δ`, `f(y,0)>1`, `∂_t f(y,0)>0`, and `∂_t f(y,1)<0` after shrinking `δ` if necessary.

Choose nonnegative nonzero smooth compactly supported factors `η_1(x_1),η_2(y),η_3(x_3)` with `supp η_2 subset (-δ,δ)` and set `η=η_1η_2η_3`. The localized kinetic observable

```text
K_η(t) = (1/2) ∫_{R^3} η(x)|u(x,t)|^2 dx
```

satisfies

```text
K_η'(t) = ∫ η f ∂_t f.
```

Thus `K_η'(0)>0` and `K_η'(1)<0`. Moreover `f(·,t)->1` uniformly as `t->+infinity`, while `f(y,0)>1` on the support of `η_2`, so

```text
K_η(+infinity) = (1/2)∫η < K_η(0).
```

Since `K_η'(0)>0`, there exists a small `t_1>0` with `K_η(t_1)>K_η(0)`. Any level `theta` strictly between those two values is crossed once upward in `(0,t_1)` and, because the eventual limit is below `K_η(0)<theta`, crossed again downward at a later time. This gives an exact **local recrossing** in a smooth pressure-free Navier–Stokes solution.

## Local-energy identity and pressure ablation

For this smooth solution the local-energy inequality is an equality. With stationary product cutoff `η`,

```text
K_η'(t) + ∫η|∇u|^2
 = (1/2)∫|u|^2 Δη + ∫((1/2)|u|^2+p)u·∇η.
```

Here `p=0`, and the integrated convective cutoff term vanishes exactly:

```text
∫ (1/2)f^3 ∂_{x_1}η
 = (1/2)(∫η_1') (∫ f^3 η_2 η_3) = 0.
```

Therefore the observed local rise/fall and recrossing do not require pressure and do not require net convective transport through this cutoff. Signed diffusive/cutoff exchange is sufficient. In particular, pressure magnitude or pressure localization cannot be the **universal** source of local one-sidedness.

## Magnitude-ledger audit

On every fixed bounded parabolic cylinder in this smooth solution, `A,C,E` are finite and `D=0`; the local suitable-solution ledger is therefore finite. Nothing in mere local finiteness of these nonnegative magnitudes fixes the sign of `K_η'` or prevents the explicit recrossing above.

This is not promoted to a global finite-`I` counterexample. The constant background makes, for large balls, `A(B_R)` grow like `R^2` (and the corresponding large-cylinder `C` also diverges), so the whole-space supremum `I` is not finite. The formula is smooth for all negative times but the exponential modes grow backward, so it is not a mild **bounded** ancient solution. These are hard DifferenceWitnesses, not repairable omissions.

## What is and is not pruned

**Supported scoped outcome:** `EXISTING_LEDGER_SIGN_INSUFFICIENT_ROUTE_PRUNING`.

The result prunes the proof move

```text
standard local suitable-solution identity
+ finite nonnegative A/C/D/E magnitude bookkeeping
+ pressure localization/magnitude information alone
=> intrinsic one-sided local energy/no-recrossing orientation.
```

Any positive Type-I theorem in the actual finite-`I` ancient class must therefore obtain orientation from information not present in that local unsigned representation: for example a genuinely signed flux/correlation observable, a trajectory/global compactness or minimality input, a no-return mechanism using ancient history, or a different rigidity quantity. This is a representation/sign-information diagnosis.

The result **does not** refute:

- a theorem using the full global finite-`I` ancient source class in an essential way;
- pressure–velocity coherence coupled to additional global or temporal information;
- compactness/minimality/rigidity, epsilon-regularity plus an independent decay mechanism, or a new dimensionless monotone defect;
- the Type-I singularity scenario itself;
- the separate Type-II lane;
- any Clay root outcome.

## Scaling, endpoint and circularity audit

`A,C,D,E` retain their usual parabolic scale invariance in the source theory. The hostile calculation introduces no endpoint estimate, derivative loss or bootstrap: it is an exact heat-shear solution and an exact smooth local-energy identity. The use of `t=0` is not an initial-data singular endpoint because the displayed solution is defined smoothly for all real `t`; the backward growth is used only to witness failure of the ancient-bounded source condition.

## Episode -> diagnosis -> obstruction boundary

- **Episode:** execute the exact pressure-free shear falsifier and verify local recrossing.
- **Diagnosis:** unsigned local `A+C+D+E` bookkeeping and pressure localization do not themselves encode temporal orientation.
- **Obstruction shadow:** a root-facing no-recrossing route needs a separately typed signed/global/trajectory coordinate before it can glue to the finite-`I` ancient source class.
- **Candidate lesson:** none is promoted; this episode may guide search only.

Scoped novelty class: `representation` (route-diagnostic only, not a literature-novelty certificate).

## Next atom

Do not estimate the same unsigned ledger again. Prospectively freeze one specific additional coordinate and falsify it before proof search: either (i) a signed local-energy/pressure correlation with a scale-normalized threshold, or (ii) a genuinely ancient/global no-return observable whose definition survives the Albritton–Barker blow-up/compactness interface. The first test must include a same-theory DifferenceWitness showing why the new coordinate is not removable by translation, dilation or the pressure-free shear calibration above.
