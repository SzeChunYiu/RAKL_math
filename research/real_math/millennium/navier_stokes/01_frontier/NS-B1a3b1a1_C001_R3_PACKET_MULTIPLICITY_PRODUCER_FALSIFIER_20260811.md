# NS-B1a3b1a1-C001 R3 — packet-multiplicity falsifier for same-slab finite-I -> global critical-vorticity amplitude

**Authority:** `SOURCE_BOUND_SCOPED_ROUTE_PRUNING / EXACT_ANALYTIC_COUNTEREXAMPLE_FAMILY_TO_UNIVERSAL_PRODUCER_IMPLICATION / PROPOSAL_SHADOW / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`; independent mathematical review credit remains `0/3`.

## 1. Exact scoped proposition

Let the weak-Lorentz quasi-norm be
\[
 \|f\|_{L^{3/2,\infty}}^*=\sup_{\lambda>0}\lambda\,|\{|f|>\lambda\}|^{2/3}.
\]
There exists a sequence of exact global smooth whole-space 3D incompressible Navier–Stokes solutions `u^(N)` on `R^3 x [0,infinity)` such that:

1. `sup_N sup_{t>=0} ||u^(N)(t)||_{L^3(R^3)} < infinity`;
2. on the normalized same-slab interior `R^3 x (0,1)`, the Albritton–Barker scale-invariant local quantities `A+C+D+E`, and hence the corresponding finite-`I` ledger, admit a bound independent of `N`;
3. there are positive times `t_N -> 0` after passing to a subsequence if desired such that
\[
 \|\operatorname{curl}u^{(N)}(t_N)\|_{L^{3/2,\infty}}^*\to\infty.
\]

Consequently, the universal same-slab implication

`uniform critical L^3 velocity control + uniform finite-I ledger => uniform global L^{3/2,infinity} vorticity amplitude`

is false without additional history, frequency/tightness, derivative, profile, or singularity-persistence hypotheses.

This is **not** a counterexample to Navier–Stokes regularity, to Albritton–Barker, or to Grujic. The constructed solutions are deliberately smooth small-data solutions and therefore carry a decisive DifferenceWitness against first-singular-time / ancient-limit transfer.

## 2. Exact divergence-free packet family

Choose `psi in C_c^infinity(R^3)`, nonzero, so that
\[
 \phi=(\partial_2\psi,-\partial_1\psi,0)
\]
has nonzero curl. Then `div phi=0`, `phi` is smooth and compactly supported, and for some `theta>0`
\[
 E_\theta=\{x:|\operatorname{curl}\phi(x)|>2\theta\}
\]
has positive measure `m>0`.

Choose translations `x_1,...,x_N` so that the translated supports of `phi` are pairwise disjoint and set
\[
 u_0^{(N)}(x)=\varepsilon N^{-1/3}\sum_{j=1}^N\phi(x-x_j).
\]
The construction is exactly divergence-free. Disjoint support gives the exact critical-norm identity
\[
 \|u_0^{(N)}\|_3^3
 =\varepsilon^3N^{-1}\sum_{j=1}^N\|\phi\|_3^3
 =\varepsilon^3\|\phi\|_3^3,
\]
so
\[
 \|u_0^{(N)}\|_3=\varepsilon\|\phi\|_3
\]
for every `N`.

Choose `epsilon` below the small-`L^3` threshold in Kato's whole-space theory. Kato's 1984 primary paper gives global strong solutions for sufficiently small `L^3` data in dimension three. Applied separately to each datum `u_0^(N)`, this produces an **exact nonlinear Navier–Stokes solution** `u^(N)` with a common critical `L_t^infinity L_x^3` bound depending only on the common small initial `L^3` norm.

No evolved solution is ever represented as a sum of evolved packets. The packet sum is only an initial datum; nonlinear evolution is supplied by the exact small-data theorem.

## 3. Uniform same-slab finite-I verification

Albritton–Barker define the scale-invariant quantities on a parabolic cylinder `Q(z_0,r)` by, schematically,
\[
 A=r^{-1}\operatorname*{ess\,sup}_t\int_{B_r}|u|^2,
\quad
 C=r^{-2}\int_Q|u|^3,
\]
\[
 D=r^{-2}\int_Q|p-[p]_{B_r}(t)|^{3/2},
\quad
 E=r^{-1}\int_Q|\nabla u|^2,
\]
and their finite-`I` ledger is the supremum of `A+C+D+E` over subcylinders. Their Lemma 2.5 states that weak-Serrin control `u in L_t^{q,infinity}L_x^{p,infinity}`, `3/p+2/q=1`, implies finite `I`; the endpoint `(p,q)=(3,infinity)` is admissible.

For this family the common strong `L_t^infinity L_x^3` bound also makes the uniformity in `N` explicit. Write
\[
 U=\sup_N\sup_{t\ge0}\|u^{(N)}(t)\|_3<\infty.
\]
For every backward cylinder `Q(z_0,r)` compactly contained in `R^3 x (0,1)`, with `r<=1`, Hölder gives
\[
 A\lesssim U^2,
\qquad
 C\le U^3.
\]
Using the canonical whole-space pressure normalization
\[
 p=R_iR_j(u_i u_j),
\]
Calderón–Zygmund boundedness gives `||p(t)||_{3/2} <= C U^2`, hence after subtracting the ball mean,
\[
 D\lesssim U^3.
\]
Finally the local energy inequality with a cutoff adapted to `Q(z_0,r)` yields
\[
 E\lesssim U^2+U^3.
\]
Indeed the cutoff-Laplacian term scales as `r^{-1}(r^{-2})(r^2)(r U^2)=O(U^2)` after the `E` normalization, while the convection and pressure-work terms scale as `r^{-1}(r^{-1})(r^2)O(U^3)=O(U^3)`. All constants are dimensional/cutoff constants, independent of packet number and cylinder center. Thus
\[
 \sup_N I(\mathbb R^3\times(0,1);u^{(N)},p^{(N)})<\infty
\]
in the same normalized interior-slab sense used by the active producer test.

This is also consistent with the source-bound Albritton–Barker weak-Serrin-to-Type-I lemma; no equivalence between unrelated Type-I formulations is assumed.

## 4. Global weak-Lorentz vorticity lower bound

At the temporal edge,
\[
 \omega_0^{(N)}=\operatorname{curl}u_0^{(N)}
 =\varepsilon N^{-1/3}\sum_{j=1}^N
  \operatorname{curl}\phi(x-x_j).
\]
On each translated copy `E_theta+x_j`,
\[
 |\omega_0^{(N)}|>2\varepsilon\theta N^{-1/3}.
\]
The copies are disjoint and have total measure `Nm`. Therefore at level
\[
 \lambda_N=2\varepsilon\theta N^{-1/3}
\]
we obtain
\[
 \|\omega_0^{(N)}\|_{L^{3/2,\infty}}^*
 \ge
 2\varepsilon\theta N^{-1/3}(Nm)^{2/3}
 =2\varepsilon\theta m^{2/3}N^{1/3}.
\]
Thus the critical vorticity amplitude diverges like `N^{1/3}` although the critical velocity norm is exactly fixed.

The exponent mismatch is structural: the `L^3` velocity budget of `N` disjoint packets is cubic, so amplitudes may be scaled by `N^{-1/3}`; the weak-`L^{3/2}` distribution function sees total superlevel measure `N`, contributing `N^{2/3}` and leaving the net factor `N^{1/3}` after one derivative.

## 5. Positive-time persistence: not a boundary-only artifact

For each fixed `N`, `u_0^(N)` is smooth and compactly supported. The Kato small-data solution agrees with the classical smooth solution and the mild formula is continuous to `t=0` in `C^1` for this fixed smooth datum. Equivalently, the heat-semigroup term converges to `u_0^(N)` in `C^1`, and the Duhamel term tends to zero in `C^1` on a sufficiently short, `N`-dependent interval.

Hence for every fixed `N` there exists `t_N>0` such that
\[
 \|\omega^{(N)}(t_N)-\omega_0^{(N)}\|_\infty
 <\varepsilon\theta N^{-1/3}.
\]
On the union of the translated `E_theta` sets we then have
\[
 |\omega^{(N)}(t_N)|>\varepsilon\theta N^{-1/3},
\]
so
\[
 \|\omega^{(N)}(t_N)\|_{L^{3/2,\infty}}^*
 \ge \varepsilon\theta m^{2/3}N^{1/3}\to\infty.
\]
No uniform lower bound on `t_N` is asserted or needed. The active discriminator explicitly asks about behavior near a temporal edge, and this check ensures the falsifier is realized at strictly positive times rather than only by an initial trace.

## 6. Scaling, endpoints, pressure, nonlocality, derivative loss and circularity audit

- **Scaling/units.** `||u||_3` and `||omega||_{3/2,infinity}` are both invariant under Navier–Stokes parabolic scaling; the counterexample is not created by comparing quantities of different physical homogeneity.
- **Endpoint.** The failure is at a derivative endpoint: a critical velocity norm does not control a critical norm of one spatial derivative. Packet multiplicity makes this failure quantitative.
- **Pressure.** Pressure is nonlocal, but it is not the active obstruction. It is controlled for finite-I verification by the whole-space Riesz-transform formula and the common `L^3` velocity bound.
- **Vorticity equation.** Curl eliminates pressure exactly from the local vorticity equation, but it does not manufacture a derivative estimate; the strain remains nonlocal through Biot–Savart/Riesz transforms.
- **No circular bootstrap.** The construction never assumes a vorticity bound in order to prove finite-I. Finite-I is certified from velocity/pressure/local-energy information, and the vorticity lower bound is obtained independently from the exact initial packet geometry plus trace continuity.
- **Constants.** Every producer-side bound depends only on the fixed packet `phi`, the chosen small `epsilon`, dimensional Calderón–Zygmund/cutoff constants and the source small-data bound; none depends on `N`.

## 7. DifferenceWitness and failure separation

### Local mathematical / representation-interface failure

The universal local producer edge under test fails:

`same-slab finite-I + critical velocity control -/-> global critical-vorticity amplitude control`.

Normalize this as

`F-NS-B1a3b1a1-SAMESLAB-FINITEI-TO-WL32`.

Diagnosis: the producer controls the velocity at critical scaling but contains no mechanism that suppresses arbitrarily many small, separated derivative packets. The obstruction is

`OBS-NS-PACKET-MULTIPLICITY-L3-TO-WL32`.

### Local-to-global / gluing residual — separate, not merged into the local failure

This falsifier does **not** settle whether first-singular-time history, singularity persistence, an ancient compactness limit, global tightness, a frequency envelope, or a profile condition can rule out packet multiplicity and thereby produce the Grujic amplitude input. Those are different source-to-target edges. The earlier

`F-NS-B1a3-UNCONTROLLED-FAR-FIELD`

and

`F-NS-B1a3-LOCAL-GLOBAL-INTERFACE-MISMATCH`

remain separately open gluing warnings.

### DifferenceWitness against over-transfer

The constructed family is smooth and small-data; it has no first singular time. It has no prescribed one-sided pre-singularity history, no ancient singularity-persistence certificate, no frequency tightness, and no Grujic critical-profile/phase hypothesis. Therefore it cannot be transferred as a counterexample to a theorem whose hypotheses add any of those structures.

The reusable lesson candidate is

`L-NS-B1a3b1a1-HISTORY-OR-FREQUENCY-NEEDED`:

> A same-slab critical velocity/finite-I ledger cannot by itself pay for global critical vorticity amplitude; any positive producer must add a mechanism that suppresses packet multiplicity, such as source-valid one-sided history, derivative/frequency tightness, global concentration control, or a profile/persistence constraint.

Experience affects search priority only; this lesson has proposal/shadow authority.

## 8. Same-context expert cell and cross-review

All four roles reviewed every load-bearing step; no role grants independent-review credit.

- `EX-NS-R3-A` (critical PDE/local energy): accepted the small-`L^3` exact-solution producer and the normalized `A,C,D,E` estimates; flagged that global `L^2` energy is not uniform in `N`, so the claim is deliberately restricted to the active critical-velocity / finite-I producer contract.
- `EX-NS-R3-B` (harmonic analysis/Lorentz): verified the distribution-function lower bound `N^{-1/3} N^{2/3}=N^{1/3}` and the `L^{3/2}` pressure control; rejected any claim that curl makes all nonlocality disappear.
- `EX-NS-R3-C` (adversarial construction): verified divergence-free disjoint packet data and required the explicit guard that only initial data are superposed; nonlinear evolved solutions are not.
- `EX-NS-R3-D` (verification/gluing): required the strictly positive `t_N` trace argument and the explicit DifferenceWitness separating this smooth temporal-edge family from first-singular-time / ancient contexts.

Cross-review consensus: the scoped falsifier is valid as a route-pruning result; it has no root theorem authority.

## 9. Episode -> diagnosis -> obstruction/lesson

**Episode:** `TE-NS-B1a3b1a1-R3-C001` — execute the prospectively frozen packet-multiplicity stress test on the exact same-slab amplitude producer edge.

**Diagnosis:** `DX-NS-B1a3b1a1-R3-PACKET-MULTIPLICITY` — finite-I and critical velocity control are compatible with arbitrarily large global weak-`L^{3/2}` vorticity because neither producer object controls multiplicity of separated derivative packets.

**Reusable obstruction:** `OBS-NS-PACKET-MULTIPLICITY-L3-TO-WL32` — critical velocity size and critical derivative amplitude have different packet-count accumulation laws.

**Reusable lesson candidate:** `L-NS-B1a3b1a1-HISTORY-OR-FREQUENCY-NEEDED` — search next for an additional source-valid anti-multiplicity mechanism, not a sharper repetition of the same-slab estimate.

These four records are logically distinct and remain proposal/shadow.

## 10. Outcome, novelty class, saturation and next action

**Outcome:** `SCOPED_FALSIFIER_VERIFIED / UNIVERSAL_SAME_SLAB_PRODUCER_PRUNED / HISTORY_SENSITIVE_PRODUCER_OPEN / ROOT_OPEN`.

The solved bounded subproblem is classified `compositional` in the RAKL novelty taxonomy, structural rank `0`: the result composes classical small-data existence, scale-invariant local estimates and an elementary Lorentz packet count. No mathematical novelty claim is made.

Saturation transition:
- reopened and then resolved/flattened for this exact child: `motif`, `failure`;
- reopened for the next route: `path`;
- flattened without new semantic learning: `operator`, `context`, `retrieval`, `method_basis`.

**Next atom:** `NS-B1a3b1a2 — HISTORY/FREQUENCY ANTI-MULTIPLICITY PRODUCER TEST`.

Ask for the weakest source-valid additional hypothesis naturally inherited from a first-singular-time Type-I sequence — one-sided history, frequency envelope/tightness, nonrecurrence, concentration compactness, or profile persistence — that excludes the packet-multiplicity family and can genuinely produce a uniform global `L^{3/2,infinity}` vorticity amplitude. If no such hypothesis survives the exact source interface, rotate to an orthogonal unsaturated critical-rigidity child rather than repeating same-slab derivative estimates.

## 11. Primary-source provenance

1. Tosio Kato, *Strong Lp-solutions of the Navier-Stokes equation in R^m, with applications to weak solutions*, Math. Z. **187** (1984), 471–480, DOI `10.1007/BF01174182`. Exact use: global strong solution for sufficiently small critical `L^m` initial data, here `m=3`; the construction uses the source's small-data whole-space solution theory only.
2. Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, J. Math. Fluid Mech. **21** (2019), 43, DOI `10.1007/s00021-019-0448-z`, arXiv:1811.00502. Exact use: definitions of `A,C,D,E,I` and Lemma 2.5 (`weak Serrin implies Type I`) including `(p,q)=(3,infinity)`.
3. Zoran Grujic, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866v2 (13 July 2026). Exact use: target consumer's global `L_t^infinity L_x^{3/2,infinity}` vorticity-amplitude input; no Grujic theorem is invoked on the constructed solutions.

Framework source of truth for this cycle: RAKL `main` SHA `bf94d16847971069912501e9a63f0e97a1e3e159`, `RAKL Verified Discovery Method` v`3.0.0`, `method_specs.py` version `2026-08-07.3`.
