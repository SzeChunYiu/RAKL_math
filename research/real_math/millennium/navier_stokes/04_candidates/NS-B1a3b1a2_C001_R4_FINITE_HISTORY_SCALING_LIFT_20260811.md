# NS-B1a3b1a2 R4 — finite-history scaling-lift obstruction

**Authority:** proposal/shadow route-pruning only. This note does not prove a Navier–Stokes singularity, exclude Type I or Type II blow-up, or change the Clay root state. Root remains `OPEN_NO_SOLUTION_CERTIFICATE`; independent mathematical review credit is `0/3`.

## Exact atom and frozen coordinate

Issue `#164 / NS-B1a3b1a2` asks whether adding a quantified backward-history window to the Albritton–Barker finite-`I` producer signature can repair the same-slab derivative-amplitude failure and force
\[
\|\omega(0)\|_{L^{3/2,\infty}(\mathbb R^3)}\le F(I,\text{history data}).
\]

Before candidate work this cycle froze the normalized finite history interval to `[-1,0]`, with the parabolic scaling law explicitly recorded. The result below is stronger than that single normalization: **no fixed finite history length `H>0` is a new coercive coordinate by itself.**

## Scoped result

### Proposition R4.1 (finite history can be manufactured from a temporal-edge separator)

Suppose there is a sequence of smooth exact whole-space Navier–Stokes solutions `(u^N,p^N)` on `R^3 x [0,\infty)` and times `tau_N>0` such that

1. their Albritton–Barker scale-invariant ledgers are uniformly bounded:
   \[
   \sup_N \mathbf I(\mathbb R^3\times (0,\infty);u^N,p^N)\le M<\infty,
   \]
   where `I` is the supremum over contained parabolic cylinders of `A+C+D+E`; and
2. their critical vorticity amplitudes diverge at `tau_N`:
   \[
   \|\omega^N(\tau_N)\|_{L^{3/2,\infty}}\to\infty.
   \]

Then, for every fixed finite `H>0`, there is a sequence of smooth exact solutions `(v^N,q^N)` on `R^3 x [-H,\infty)` with the same uniform `I` bound and
\[
\|\nabla\times v^N(0)\|_{L^{3/2,\infty}}\to\infty.
\]

Hence no universal implication of the form

`FINITE_I_ON_A_FIXED_FINITE_BACKWARD_WINDOW -> UNIFORM_GLOBAL_VORTICITY_L3_2_INFINITY_AT_THE_ENDPOINT`

can hold on exact smooth whole-space NSE solutions.

### Proof

Fix `H>0` and set
\[
\lambda_N=\sqrt{\tau_N/H}.
\]
Define, for `s\ge -H`,
\[
v^N(x,s)=\lambda_N u^N(\lambda_N x,\lambda_N^2(s+H)),
\qquad
q^N(x,s)=\lambda_N^2 p^N(\lambda_N x,\lambda_N^2(s+H)).
\]
This is exactly the Navier–Stokes scaling followed by a time translation, so `(v^N,q^N)` is an exact smooth NSE solution on the full finite history interval.

At the endpoint `s=0`, `lambda_N^2 H=tau_N`, and the vorticity is
\[
\Omega^N(x,0)=\lambda_N^2\omega^N(\lambda_N x,\tau_N).
\]
For `p=3/2`, the weak-Lorentz norm is critical:
\[
\|\lambda^2 f(\lambda\cdot)\|_{L^{3/2,\infty}}
=
\|f\|_{L^{3/2,\infty}}.
\]
Indeed the distribution function satisfies
\[
|\{x:|\lambda^2f(\lambda x)|>\alpha\}|
=
\lambda^{-3}|\{y:|f(y)|>\alpha/\lambda^2\}|,
\]
and the factor in
\[
\sup_{\alpha>0}\alpha\,|\{|g|>\alpha\}|^{2/3}
\]
is therefore `lambda^2 * (lambda^{-3})^(2/3)=1`. Thus
\[
\|\Omega^N(0)\|_{L^{3/2,\infty}}
=
\|\omega^N(\tau_N)\|_{L^{3/2,\infty}}\to\infty.
\]

Each of `A,C,D,E` is invariant under the same parabolic scaling and under spacetime translations. A parabolic cylinder contained in `R^3 x (-H,\infty)` maps to a parabolic cylinder contained in `R^3 x (0,\infty)`. Therefore
\[
\mathbf I(v^N,q^N;R^3\times(-H,\infty))
=
\mathbf I(u^N,p^N;R^3\times(0,\infty))
\le M.
\]
This proves the proposition.

## Exact antecedent re-verification

The antecedent is not assumed from authority of open PR `#165`; it is re-checked here as a shadow construction.

Choose `chi in C_c^\infty(R^3)` with `chi=1` on a fixed cube and
\[
A_N=(0,0,(a/N)\chi(x)\sin(Nx_1)),\qquad u_0^N=\nabla\times A_N.
\]
Then `div u_0^N=0` and `sup_N ||u_0^N||_3 <= C_chi a`. Kato's `L^m` theory, with `m=3`, gives global strong solutions when this critical norm is sufficiently small. On the cube where `chi=1`,
\[
\omega_0^N=(0,0,aN\sin(Nx_1)),
\]
so a fixed positive-measure subset has `|\omega_0^N|\gtrsim aN`. Smooth-data trace continuity allows a positive time `tau_N` (arbitrarily small for each fixed `N`) at which the same lower bound holds up to a fixed factor. The distribution-function formula then gives
\[
\|\omega^N(\tau_N)\|_{L^{3/2,\infty}}\gtrsim N.
\]

Uniform `L^\infty_tL^3_x` control from the small-data solution bounds `A` and `C`; the whole-space pressure formula `p=R_iR_j(u_i u_j)` and Calderón–Zygmund boundedness bound `D`; the local energy inequality with standard cutoffs bounds `E` without inserting an initial derivative norm. This is the same exact-NSE ledger audit that the R3 shadow episode used, but the current result needs only its verified properties, not its authority state.

**Source boundary:** Kato supplies the global small-critical-data dynamics, not the vorticity separator or the finite-history conclusion. The separator is an elementary smooth-data construction; Proposition R4.1 is the exact scaling transfer proved above.

## Why this is not a repeat of R3

R3 diagnosed **temporal-edge derivative blindness**: very short forward time does not repair the missing derivative coordinate.

R4 diagnoses a second, scale-covariant fact: a **fixed finite amount of backward time can always be generated from that short-time separator by parabolic rescaling**, while preserving both finite `I` and the critical weak-`L^{3/2}` output. The price is a compensating change of spatial scale. Therefore “history length = 1” is not by itself a scale-invariant anti-concentration hypothesis.

The pre-action separated-multiplicity construction was consequently rejected before promotion. Primary profile/stability literature supports spatially separated global solution mechanisms, but proving endpoint derivative lower bounds and a uniform `I` ledger for that route would add unnecessary interfaces. The exact scaling lift is strictly simpler and closes the frozen finite-history discriminator.

## Local mathematical failure versus gluing residual

### Local mathematical producer failure — CLOSED for fixed finite history

For every finite `H>0`,
\[
\mathbf I<\infty\text{ uniformly on }[-H,0]
\]
does **not** imply a uniform global `L^{3/2,\infty}` vorticity bound at `0`, even in smooth exact whole-space NSE.

This is a local mathematical failure of the proposed producer implication, not merely a retrieval or source gap.

### Separate local-to-global / source-class gluing residual — OPEN

The construction begins at a finite left endpoint `-H`. It is not a mild bounded ancient solution on all of `(-\infty,0)`. Parabolic scaling maps a finite interval to another finite interval; it does not create infinite backward history. Therefore this result does **not** refute a theorem that uses genuine ancientness, a backward sequence tending to `-\infty`, or another scale-relative global compactness/tightness condition.

Albritton–Barker's exact Type-I equivalence produces a nontrivial mild bounded ancient solution with `I<\infty`, and their separate Liouville theorem assumes bounded global `L^3` along a sequence of times tending to `-\infty`. Neither hypothesis is manufactured here.

Likewise, amplitude alone does not produce Grujić's critical-point morphology or log-BMO vorticity direction, and backward uniqueness remains downstream of terminal/global hypotheses.

## Limit-passage audit

- **Weak/strong convergence:** no blow-up-limit convergence is used in Proposition R4.1; it is an exact change of variables.
- **Pressure:** pressure scales exactly as `lambda^2`; the `D` ledger is invariant. No pressure localization/gluing is hidden in the transfer.
- **Far field:** the rescaling expands/contracts spatial structure and therefore exposes the real residual: a positive result must constrain scale-relative spatial organization/tail multiplicity, not merely elapsed time.
- **Noncompact symmetries:** dilation is the decisive noncompact symmetry. Translation is not needed for the proof.
- **Equation change:** none; every object solves the same viscous NSE. Type-II Euler-limit routes are untouched.
- **Backward uniqueness:** not invoked.
- **Self-similar/ancient interface:** a finite-window scaling lift is not an ancient solution and cannot be substituted into an ancient Liouville theorem.

## Episode -> diagnosis -> obstruction / lesson

**Episode `EP-NS-B1a3b1a2-R4-001`:** freeze `H=1`, retrieve the R3 temporal-edge failure as noncanonical experience, initially propose separated multiplicity, source-check profile/stability mechanisms, then test the exact NSE scaling operator against the frozen history coordinate.

**Diagnosis `DX-NS-B1a3b1a2-R4-001`:** finite history length by itself is a dimensional coordinate. Because the producer ledger and target Lorentz norm are both critical, scaling transports the temporal-edge hostile family to any prescribed finite history length without changing either side of the putative estimate.

**Obstruction `O-NS-B1a3b1a2-FINITE-HISTORY-SCALING-LIFT`:** any successful history-based producer must use information not removable by parabolic rescaling—genuine infinite ancientness/backward-sequence structure, or an additional scale-relative spatial/frequency/tightness coordinate.

**Reusable motif `M-NS-CRITICAL-FAILURE-SCALING-LIFT`:** when both a producer signature and consumer target are scaling invariant, test whether a proposed finite length/time regularizer can be normalized away while preserving a hostile family before investing in new estimates.

**Lesson status:** proposal/shadow. Experience may change route priority only.

## Novelty and saturation

Defensible RAKL novelty class for the solved scoped subproblem: **transfer**. The mathematical content is an exact operator transfer of a verified same-equation failure to a new finite-history signature.

Seven-axis status after verification:

- `KNOWLEDGE`: flat — no literature theorem was promoted as new mathematical content.
- `OPERATOR`: reopened — exact parabolic scaling becomes a reusable failure-transport operator.
- `EXPERIENCE_PATTERN`: reopened — temporal-edge failure and finite-history failure are now linked by a critical-scaling motif.
- `OBSTRUCTION`: reopened — fixed finite backward history is pruned as a standalone producer coordinate.
- `RELATION`: reopened — R3 same-slab failure implies every finite-H failure.
- `PATH`: reopened — route moves to genuinely ancient/backward-sequence or scale-relative tightness information.
- `META_METHOD`: flat — no framework-authority rule changed.

## Next action

Do not spend another cycle proving a fixed-window smoothing estimate from finite `I` alone. The next high-information discriminator is:

> In the actual mild bounded ancient finite-`I` source class, is there a scale-relative compactness/tail/frequency certificate (or a backward-sequence critical norm) that produces global vorticity amplitude and survives the Type-I blow-up passage?

This must keep the two questions separate: `(i)` local derivative smoothing on interior cylinders and `(ii)` global Lorentz tail/profile multiplicity. A local operator lemma does not glue to the global ancient source without an explicit same-theory interface.

## Primary-source provenance

1. Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502, current arXiv HTML revision dated 2026-03-22 and checked 2026-08-11. Used for the exact `A,C,D,E,I` definitions, the Type-I <-> nontrivial mild bounded ancient finite-`I` equivalence, compactness topology, and the separate backward-sequence global-`L^3` Liouville hypothesis.
2. Tosio Kato, *Strong L^p-solutions of the Navier-Stokes equation in R^m, with applications to weak solutions*, Math. Z. 187 (1984), 471-480, DOI `10.1007/BF01174182`; primary journal scan checked 2026-08-11. Used only for local strong `L^m` solutions and global existence for sufficiently small critical `L^m` data, specialized to `m=3`.
3. Jean-Yves Chemin and Isabelle Gallagher, *Wellposedness and stability results for the Navier-Stokes equations in R^3*, arXiv:math/0611044v2. Primary PDF checked 2026-08-11, especially Proposition 4.1 and the cross-profile perturbation argument. Retrieved to test the separated-profile alternative; **rejected as load-bearing evidence** because the scaling-lift proof makes that additional nonlinear-decoupling interface unnecessary.

No numerical computation is used as proof.
