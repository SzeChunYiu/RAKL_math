# NS-B1a2-C001 — finite kinetic energy does not quantize L3-critical cores

**Atom:** `NS-B1a2`  
**Candidate/result ID:** `NS-B1a2-C001-CRITICAL-BLOB-PACKING`  
**Authority:** `SCOPED_ANALYTIC_ROUTE_PRUNING / FUNCTIONAL_CALIBRATION / NO_NAVIER_STOKES_COUNTEREXAMPLE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

## Question

The previous child `NS-B1a1` showed that the standard finite-`I` local-energy ledger is scale-neutral after normalization and therefore does not by itself supply a well-founded dyadic charge. A natural next possibility is to use the finite kinetic energy of the physical smooth solution as a positive currency: if every critical concentration core consumed a scale-independent amount of kinetic energy, finite energy could bound the number of cores and might support a global-tail or compactness argument.

This audit tests that inference before any new compactness theorem is proposed.

We deliberately give the route a favorable extra hypothesis that is stronger than finite Albritton–Barker `I`: at the physical parabolic scale

`lambda = sqrt(T-t)`, assume

`||u(t)||_infinity <= M/lambda`.

The result below does **not** claim that this pointwise bound follows from finite `I`. It asks whether finite energy would quantize critical cores even if this stronger amplitude control were supplied.

## Proposition — energy-based core count has the wrong scale

Fix a time `t<T` and write `lambda=sqrt(T-t)`. Suppose

1. `u(t) in L^2(R^3)` with `||u(t)||_2^2 <= E0`;
2. `||u(t)||_infinity <= M/lambda`;
3. `B_1,...,B_N` are pairwise disjoint spatial balls; and
4. every ball is `L^3`-critical in the sense

   `||u(t)||_{L^3(B_j)} >= gamma > 0`.

Then

`N <= (M E0)/(gamma^3 lambda)`.

In particular, finite kinetic energy and the favorable pointwise Type-I amplitude bound do not yield a scale-independent `O(1)` bound on the number of disjoint critical cores as `lambda -> 0`.

### Proof

For every `j`,

`gamma^3 <= integral_{B_j} |u|^3`.

Using the pointwise bound,

`integral_{B_j}|u|^3 <= ||u(t)||_infinity integral_{B_j}|u|^2 <= (M/lambda) integral_{B_j}|u|^2`.

Therefore

`integral_{B_j}|u|^2 >= gamma^3 lambda/M`.

The balls are disjoint, hence

`N gamma^3 lambda/M <= sum_j integral_{B_j}|u|^2 <= ||u(t)||_2^2 <= E0`.

Rearranging gives the stated estimate.

`QED`.

## Scaling interpretation

The obstruction is not a bad constant. It is the critical scaling.

An `L^3`-critical velocity profile at spatial scale `lambda` has characteristic amplitude `lambda^-1`. Its scale contributions are

- `L^3` mass cubed: `lambda^-3 * lambda^3 = O(1)`;
- kinetic energy squared: `lambda^-2 * lambda^3 = O(lambda)`.

Thus kinetic energy is **supercritical relative to the L3 concentration scale**: the energy cost of one critical core vanishes linearly as the core shrinks. A finite `L^2` budget can therefore pay for a number of such cores diverging like `lambda^-1`.

This is structurally different from an energy-critical bubbling problem in which every critical bubble carries a fixed positive amount of the conserved energy and finite energy can bound bubble count.

## Counterexample-first functional calibration — the exponent is attainable

This construction is an instantaneous smooth divergence-free field. It is **not** asserted to solve Navier–Stokes and is not a counterexample to any dynamics-specific theorem.

Choose a nonzero divergence-free `phi in C_c^infinity(B(0,1);R^3)`. For small `lambda>0`, choose pairwise separated centers `x_1,...,x_N` in a fixed bounded region so the supports below are disjoint, with

`N(lambda)=floor(c/lambda)`

for a fixed sufficiently small `c>0`. Define

`u_lambda(x) = sum_{j=1}^{N(lambda)} lambda^-1 phi((x-x_j)/lambda)`.

Because the supports are disjoint and each summand is divergence-free, `u_lambda` is smooth and divergence-free. Direct scaling gives

`||lambda^-1 phi((.-x_j)/lambda)||_infinity = lambda^-1 ||phi||_infinity`,

`||lambda^-1 phi((.-x_j)/lambda)||_2^2 = lambda ||phi||_2^2`,

and

`||lambda^-1 phi((.-x_j)/lambda)||_3^3 = ||phi||_3^3`.

Consequently,

`||u_lambda||_2^2 = N(lambda) lambda ||phi||_2^2 = O(1)`,

while

`||u_lambda||_3^3 = N(lambda) ||phi||_3^3 ~= c ||phi||_3^3/lambda`,

so

`||u_lambda||_3 ~= C lambda^-1/3 -> infinity`.

There is no geometric packing obstruction: `N(lambda)=O(lambda^-1)` balls of radius `O(lambda)` occupy only `O(lambda^2)` total volume, far below the `O(lambda^-3)` packing capacity of a fixed three-dimensional region.

The family therefore saturates the relevant scaling: finite kinetic energy plus the scale-correct amplitude bound is compatible, at the level of instantaneous divergence-free fields, with a diverging number of disjoint `L^3`-critical cores and an unbounded global `L^3` norm.

## Relation to source-backed concentration results

Barker–Prange-type critical-norm concentration results support the existence of a nontrivial critical concentration near a singular point at parabolic scale. They do not supply the missing scale-independent multiplicity bound or global tail tightness. The present audit does not weaken those concentration theorems. It only shows that **finite kinetic energy is not by itself the missing quantization currency** that upgrades local critical concentration to a bounded global profile inventory.

Likewise, Albritton–Barker's source-valid Liouville trigger remains intact: a mild ancient solution with a backward sequence uniformly bounded in global `L^3` is zero. This audit explains why physical finite energy plus instantaneous scale-correct concentration/amplitude estimates do not automatically manufacture that global `L^3` sequence.

There is an additional scaling warning for the ancient-limit formulation. Under the usual Navier–Stokes blow-up rescaling, a fixed global physical `L^2` budget does not remain a uniform global `L^2` bound on the rescaled ancient sequence; its global `L^2` norm has supercritical scaling. Thus the physical-energy route is weaker still when transported to the ancient-limit chart.

## What is pruned

The following inference is retired as a standalone proof family:

`finite kinetic energy + favorable Type-I amplitude + local critical L3 concentration`

`=> scale-independent finite critical-core count`

`=> global L3 tail tightness / Liouville-ready compactness`.

The first implication already fails at the scale-bookkeeping level: the best direct energy count is `O(lambda^-1)`, and the packed divergence-free calibration realizes the same scaling without violating the instantaneous assumptions.

## What remains live

This result does **not** rule out:

- a dynamics-specific no-recrossing or persistence theorem;
- interaction between nearby cores that makes the functional packing dynamically impossible;
- vorticity-direction coherence or geometric depletion;
- pressure-aware temporal cancellation;
- a minimal/critical-element construction in a genuinely critical global topology;
- compactness modulo translation/dilation obtained from an additional invariant;
- another source-valid Liouville trigger weaker than a global `L^3` sequence.

These mechanisms contain information absent from kinetic energy alone.

## Expert-cell disposition

The seven-role same-context review agreed that the packing audit is the correct cheap discriminator. The concentration-compactness lead ranks a minimal-critical-element route highest after this negative result; the vorticity/geometry lead ranks coherence/depletion highest. The disagreement is preserved. Neither route is promoted by this audit.

## Residual opened

`NS-B1a3` should ask for a **dynamics-specific critical compactness/coherence coordinate**: what property inherited by every relevant Type-I ancient limit prevents the `O(lambda^-1)` multi-core/tail-escape pattern that finite energy permits, and either yields a backward global-`L^3` sequence or activates another source-valid Liouville theorem?

A fresh context, dual-memory review, expert review and hash-chained trace are required before any `NS-B1a3` candidate.