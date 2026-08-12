# NS-B2a1c1 — generalized-F axial cutoff window

**Authority:** `PROPOSAL_SHADOW / SOURCE_BOUND_SCOPED_ALGEBRA / NO_ROOT_AUTHORITY`  
**Root:** `NS0 = OPEN_NO_SOLUTION_CERTIFICATE`, independent mathematical reviews `0/3`.

## Frozen atom

The parent `NS-B2a1c` proved that the specialized `F(a)=1` branch cannot satisfy Seregin's Section-4 cutoff condition (4.4). This child asks whether the *generalized power-log* example in the same 2026 paper reopens that conservation operator, and if so what exact interface remains before any Type-II exclusion.

Primary source anchors:

- Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468v1 (28 June 2026), equations (3.9)–(3.11), Section 4 equations (4.1)–(4.6): https://arxiv.org/abs/2606.29468
- Gregory Seregin, *A note on potential Type II blowups of axisymmetric solutions to the Navier-Stokes equations*, arXiv:2402.13229v3 (current revision 8 August 2026), equations (1.4), (1.10), (2.11), Proposition 2.2, Proposition 2.3, Corollary 2.4: https://arxiv.org/abs/2402.13229

The 2026 source gives, for

`f(lambda)=lambda^(alpha-1)/log^gamma(e/lambda)`, `1<alpha<2`,

the asymptotic ratio

`F(a)=a^(alpha-1)`

and on the nontrivial-possible branch requires

`2 alpha - 3 <= 0`, hence `alpha <= 3/2`.

Section 4 additionally assumes

`3/s1 + 2/l1 = 4`, `l1 <= s1`,

and its cutoff consumer is

`a^(2-3l1/2) / F(a)^((l1+1)/2) -> 0` as `a -> infinity`.  

## Verification block 1 — admissible l1 range

Because `l1 <= s1`, one has `1/s1 <= 1/l1`. Using `3/s1 + 2/l1 = 4`,

`4 - 2/l1 = 3/s1 <= 3/l1`,

so `4 <= 5/l1`, therefore

`1 < l1 <= 5/4`.

This reproduces the exponent region used in the parent F=1 incompatibility check.

## Verification block 2 — exact generalized-F cutoff condition

Substitute `F(a)=a^(alpha-1)` into (4.4). The cutoff quantity is

`a^E`, with

`E(alpha,l1) = 2 - 3l1/2 - (alpha-1)(l1+1)/2`.

Since a pure power tends to zero at infinity exactly when its exponent is negative,

`E(alpha,l1)<0`

is equivalent to

`4 - 3l1 - (alpha-1)(l1+1) < 0`,

hence

`alpha > (5-2l1)/(l1+1)`.                                    (A)

This inequality is strict. At equality the exponent is exactly zero and the cutoff quantity is identically order one, so (4.4) fails.

## Verification block 3 — the window is nonempty inside the 2026 nontrivial branch

For `l1>1`,

`3/2 - (5-2l1)/(l1+1) = 7(l1-1)/(2(l1+1)) > 0`.

Therefore, for every admissible `1<l1<=5/4`, the interval

`( (5-2l1)/(l1+1), 3/2 ]`                                  (B)

is nonempty and lies inside `1<alpha<=3/2`.

Endpoint/adversarial checks:

- `F=1` corresponds to the limiting exponent `alpha=1`; it fails because `(5-2l1)/(l1+1) >= 10/9 > 1` on `l1<=5/4`, agreeing with `NS-B2a1c`.
- At `l1=5/4`, threshold `(A)` is `alpha>10/9`.
- As `l1 -> 1+`, the threshold tends to `3/2` from below, so the window becomes narrow but remains nonempty for every permitted `l1>1`.
- At `alpha=3/2`, (4.4) holds for every `l1>1`; this is exactly the endpoint of the 2026 nontrivial-possible range.

## Verification block 4 — exact relation to the current 2024-v3 condition

Set the old pure-power parameterization

`alpha = 2 - m`.

Then

`E(2-m,l1) = [m(l1+1) + 3 - 4l1]/2`.

Thus `E<0` is exactly

`m < (4l1-3)/(l1+1)`,

which is equation (2.11) of the *current* arXiv:2402.13229v3. Also `alpha<=3/2` is `m>=1/2`, matching the lower side of (1.10). The 2026 generalized `F` cutoff condition is therefore an exact representation of the older power-law boundary-exponent condition on this coordinate.

## What is actually closed

`NS-B2a1c1` closes only the local producer/consumer **parameter compatibility** question:

> Unlike `F=1`, the power-log family `F(a)=a^(alpha-1)` has a nonempty source-compatible region in which Section-4 condition (4.4) can hold, and its strict exponent condition is exactly the current 2024-v3 condition (2.11) after `alpha=2-m`.

This is a scoped compositional/representation result. It neither proves Proposition 4.1's additional hypotheses from the generalized producer nor excludes a Type-II singularity.

## Gluing audit — still open and separate

The local algebra is **not** the remaining obstruction. Seregin 2026 Proposition 4.1 assumes, in addition to the Section-4 conditions, that for some `t0<=0`,

`g(t0)=(2/l1) int_R3 (|omega_theta(u)(x,t0)|/r)^(l1/2) dx < infinity`.

The audited Theorem-3.1/Section-4 producer does not state this as an automatic output. Even if this finite-time integrability is established and conservation follows, conservation alone does not force `g=0`. A terminal-time vanishing or another exact rigidity trigger is still needed.

The older v3 Proposition 2.3 supplies such a route only after adding the ancestor condition

`ess sup_{-1<t<0} int_C |v(x,t)|^q dx < infinity`, `q=3/(2-m)=3/alpha`,

which is used to obtain `u(.,0)=0`. That ancestor time-slice hypothesis is not part of the 2026 generalized producer as currently bound here, so importing Proposition 2.3 would be an invalid theorem transfer without a separate inheritance proof.

Accordingly the next child is:

`NS-B2a1c1a — GENERALIZED_F_TERMINAL_TRACE_RIGIDITY`

> Can the exact 2026 power-log source assumptions yield (i) a finite `g(t0)` at some time and (ii) a same-theory terminal-time zero/rigidity trigger, or an alternative source-valid Liouville closure, without importing the old pure-power `L^q` hypothesis or losing control at spatial infinity?

Failure classes are kept separate:

- **local mathematical failure:** none in the verified parameter window; endpoint equality and F=1 are explicitly falsified subcases.
- **source/representation failure:** old Proposition 2.3 cannot be transferred wholesale from pure-power to power-log scaling.
- **local-to-global/gluing failure:** finite `g(t0)` plus a terminal-time/rigidity trigger are not yet produced by the generalized source packet.
- **root failure:** Type-II as a whole remains open; Type-I work is separate; the Clay root proof DAG is not closed.

No numerics are used as proof.