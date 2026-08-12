# NS-B2a1c — F=1 compatibility audit for Seregin condition (4.4)

**Authority:** proposal/shadow source-bound route diagnostic only. No Navier–Stokes theorem, no Euler Liouville theorem, no Clay/root authority, and no independent-review credit.

## Frozen question

For the child atom frozen in RAKL_math #203, determine whether the large-radius condition (4.4) used in Section 4 of Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468v1 (submitted 2026-06-28), can hold in the paper's logarithmic `F(a)=1` regime under the exact Section-4 exponent constraints.

The possible exponent mismatch was noticed during source scoping before the current v3 packet was frozen. This audit therefore claims **verification credit only**, not strict RAKL hypothesis-generation/preregistration credit.

## Primary-source bindings

The audited arXiv source states:

1. Theorem 3.1 produces a nontrivial ancient **Euler** limit and the weighted bound (3.5), local energy inequality (3.7), and nontriviality (3.8).
2. Immediately after Theorem 3.1, for the logarithmic example originating from (2.10), the paper states exactly `F(a)=1`.
3. Section 4 assumes `1 < l1,s1 < infinity` and

   `3/s1 + 2/l1 = 4`.

4. Later in the same section it additionally assumes `l1 <= s1`, together with axisymmetry/swirl-free structure and a pointwise bound; the stronger derivative quantity appears in (4.1)/(4.2).
5. From (4.3), the paper says a conservation law can be derived under the additional large-radius condition

   `a^(2 - (3/2) l1) / F(a)^((l1+1)/2) -> 0` as `a -> infinity`  `(4.4)`.

The notation `F` is overloaded in the surrounding prose: (4.3) also writes `F(f)=Phi(|f|)`, but (4.4) has argument `a` and is the scaling function `F(a)` inherited from (2.2)/(4.2). The screenshot/PDF formula was checked directly to avoid confusing these two uses.

## Exact algebraic discriminator

Assume the Section-4 exponent restrictions and `F(a)=1`.

Because `l1 <= s1` and both are positive,

`1/s1 <= 1/l1`.

Therefore

`4 = 3/s1 + 2/l1 <= 3/l1 + 2/l1 = 5/l1`,

so

`l1 <= 5/4`.

The power of `a` in (4.4) is

`beta = 2 - (3/2) l1`.

Hence every admissible Section-4 pair satisfies

`beta >= 2 - (3/2)(5/4) = 1/8 > 0`.

With `F(a)=1`, the left side of (4.4) is exactly `a^beta`, and for `a >= 1` it is at least `a^(1/8)`. Thus it diverges to `+infinity`; it cannot converge to zero.

### Endpoint/adversarial check

The most favorable allowed endpoint for making `beta` small is `l1=5/4`, where `beta=1/8`, still strictly positive. To make `beta<0` one would need `l1>4/3`, but the Section-4 constraints force `l1<=5/4<4/3`. There is no equality or logarithmic endpoint rescue in the exact `F(a)=1` regime.

A symbolic inequality check was used only as an algebra calibration; the displayed argument above is the proof.

## Outcome

`F1_AXIAL_44_INCOMPATIBLE_SCOPED_ROUTE_PRUNING`.

**Verified scoped fact:** within the exact Section-4 exponent regime, the paper's additional condition (4.4) is incompatible with the logarithmic `F(a)=1` scaling example. Consequently the particular Section-4 cutoff-to-conservation-law mechanism cannot simply be imported as a closure for the general `F(a)=1` Type-II ancient-Euler branch.

This does **not** show that the general F=1 ancient Euler limit is non-existent or trivial. It does **not** exclude another tail/no-incoming-flux quantity, signed cancellation/telescoping, a prelimit Navier–Stokes annular estimate, recentering/minimality, a different Euler invariant, or a different symmetry-specific Liouville theorem.

## DifferenceWitness / source-family boundary

The Section-4 consumer already has a stricter producer state than general Theorem 3.1: axisymmetry, swirl-free limit, the derivative coordinate in (4.1)/(4.2), `l1<=s1`, a pointwise bound, and then (4.4). The present incompatibility is therefore a **consumer/source-interface failure** for one specialized positive analogue, not a local failure of Theorem 3.1 and not a general Euler rigidity failure.

The previously recorded gluing obstruction remains separately open:

- `F-NS-B2a1-DOUBLE-LIMIT-TAIL-INHERITANCE`: fixed-cylinder convergence and critical bounds do not by themselves provide `lim_R limsup_k` tail tightness.

The earlier local/absolute route failure also remains separate:

- `F-NS-B2a-F1-ABSOLUTE-CUTOFF-FLUX-NONDECAY`: absolute F=1 cutoff estimates remain scale-critical and nondecaying after normalization.

This cycle adds the orthogonal specialized-consumer failure:

- `F-NS-B2a1c-F1-AXIAL-44-EXPONENT-INCOMPATIBLE`.

## Limit-passage and rigidity interface audit

- **Weak/strong convergence:** not strengthened here; Theorem 3.1's fixed-cylinder compactness is not upgraded to a global tail statement.
- **Pressure localization/far field:** no new pressure decay is asserted. The prior far-field/double-limit residual is retained.
- **Noncompact symmetries:** no translation/dilation compactness is gained.
- **Equation change:** the extracted equation is Euler; Navier–Stokes backward uniqueness is inadmissible unless a future route returns to an exact Navier–Stokes producer with matching hypotheses.
- **Physical/source identification:** the specialized Section-4 vorticity conservation consumer is not source-complete for the general F=1 branch, independently of the exponent contradiction.
- **Numerics/computation:** none is used as proof.

## Next action

Rotate away from the specialized Section-4 `(4.4)` reuse in the F=1 branch. Reopen `NS-B2a1a — PRELIMIT_ANNULAR_TIGHTNESS` or `NS-B2a1b — SIGNED_EULER_FLUX_TELESCOPING`, with a fresh current-v3 packet, rather than searching a generic Euler Liouville theorem before its global producer signature is available.

Root remains `OPEN_NO_SOLUTION_CERTIFICATE`; root authority `NONE`; independent mathematical review `0/3`; Type-I and all other Type-II scenarios remain open.