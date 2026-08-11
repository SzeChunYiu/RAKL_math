# NS-B2a1-C001 — local convergence does not transfer uniform tail tightness

**Atom:** `NS-B2a1`  
**Candidate:** `NS-B2a1-C001`  
**Authority:** `PROSPECTIVE_COMPACTNESS_CALIBRATION / ROUTE_PRUNING_ONLY / NOT_EULER_COUNTEREXAMPLE / NOT_NAVIER_STOKES_COUNTEREXAMPLE / ROOT_AUTHORITY_NONE`  
**Frozen context:** `sha256:46107a3521175794ea4dadece4101723a57bf6af8dc9e8680a3c47d31c70902e`  
**Frozen memory review:** `sha256:baa4a039e9a51b50463cc9a0dc83cdbc5b7a1346f1ae7313face94226034f25c`  
**Frozen pre-candidate trace:** `sha256:495974a4586a0f0539b8380573e84e3b9d6590cdc048fa9971d6062ec6846a86`  
**Framework:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application base:** `SzeChunYiu/RAKL_math@50c703f3f0c518bba1b48fb17e51b03d53ed02c3`

## Source-side interface being audited

Seregin `arXiv:2606.29468v1` obtains subsequences of the Euler-scaled Navier–Stokes fields that converge on **every fixed** parabolic cylinder `Q(a)`: strongly in local `L_{3ν}` for `1 <= ν < 10/9`, weak-* in local `L_{2,∞}`, and weakly for the gradient in local `L_2`. Theorem 3.1 then produces a nontrivial ancient **Euler** limit satisfying scale-weighted local energy, pressure and gradient bounds plus the Euler local-energy inequality.

The open rigidity bridge is global. A no-incoming-energy/tail condition requires information at radii `R -> infinity`, or an equivalent recentered/signed-flux handoff. The question is therefore whether the source's fixed-cylinder compactness can by itself justify that global passage.

## Proposition — two-packet escape calibration

Let `η in C_c^∞((-1,0))` be nonzero. Choose nonzero `ψ_0,ψ_1 in C_c^∞(R^3)` and define smooth compactly supported divergence-free fields

`w_j = (∂_2 ψ_j, -∂_1 ψ_j, 0)`, `j=0,1`.

Choose translations `x_k in R^3` with `|x_k| -> infinity`, and define

`W_k(x,t) = η(t) [w_0(x) + w_1(x-x_k)]`,

`W(x,t) = η(t) w_0(x)`.

Then:

1. `div W_k = div W = 0`;
2. `W_k -> W` in `C^∞_loc(R^3 x (-∞,0))`, hence strongly in every local `L^p`, while the local limit `W` is nonzero;
3. for every `1 <= p < infinity`, the sequence is **not uniformly L^p-tail tight**:

   `lim_{R->infinity} sup_k ∫_{-1}^0 ∫_{|x|>R} |W_k(x,t)|^p dx dt >= ||η||_{L^p(-1,0)}^p ||w_1||_{L^p(R^3)}^p > 0`;

4. analogous non-tightness holds for any derivative norm for which `w_1` has nonzero derivative, including the spatial-gradient `L^2` tail;
5. despite this escape, centered scale-normalized local quantities of the same dimensional type as energy, cubic mass and gradient energy can be uniformly bounded in `k` for this compactly supported calibration family.

### Proof

Divergence-freeness follows from the curl-form construction. Let `K` be any fixed compact subset of spacetime. Because `w_1` has compact support and `|x_k| -> infinity`, for all sufficiently large `k` the translated support `supp w_1 + x_k` is disjoint from the spatial projection of `K`. Therefore `W_k = W` identically on `K` for all sufficiently large `k`, proving `C^∞_loc` convergence and preserving the nonzero fixed core.

Now fix a sufficiently large radius `R` containing `supp w_0`. For every such `R`, choose `k` so large that `supp w_1 + x_k` lies outside `B(R)`. The two packets are then disjoint and the tail integral contains the full translated packet, giving

`∫_{-1}^0 ∫_{|x|>R} |W_k|^p >= ||η||_p^p ||w_1||_p^p`.

Taking `sup_k` and then `R -> infinity` gives the stated positive lower bound. Translation preserves derivative norms, so the same argument applies to nonzero derivative tails.

Finally, the compact supports and smoothness imply that for very small centered radii each local integral scales by volume, while for radii larger than the packet sizes the numerators are bounded by fixed global packet norms and the scale-normalizing denominators grow. When a translated packet first enters a centered ball, the relevant radius is comparable to `|x_k|`, so the normalization is no worse. Thus uniform boundedness of the local scale-normalized calibration quantities is compatible with failure of uniform tail tightness.

## Exact logical consequence

The calibration proves the implication

`fixed-cylinder local convergence + bounded local/scale-critical norms -> uniform global tail tightness`

is false **as a statement of topology and boundedness alone**, even when:

- every field is smooth and divergence-free;
- the local limit is nonzero;
- convergence is stronger than the local convergence used in the source extraction;
- a fixed amount of global norm survives in an escaping profile.

Equivalently, the quantifiers

`for every fixed R: W_k -> W on B(R)`

and

`lim_{R->infinity} sup_k Tail_k(R)=0`

cannot be interchanged without a separate uniformity theorem.

## Scope boundary

This is **not** a counterexample to Seregin Theorem 3.1. The fields `W_k` are not asserted to solve Navier–Stokes or Euler, satisfy the exact suitable-weak local-energy inequality, or arise from the source blow-up scaling. The proposition falsifies only a proposed compactness inference. Its scientific use is to localize what the PDE must supply in addition to local convergence.

It is also stronger than the pending XM005 moving-core calibration in one specific respect: the local limit here remains nontrivial because the fixed core `w_0` stays in view while a second packet escapes. Therefore source nontriviality at unit scale does not, by itself, repair the abstract local-to-global topology gap.

## Source-specific conclusion

Seregin's fixed-`Q(a)` convergence can pass local equations, local inequalities and fixed-radius observables. It cannot **by that convergence topology alone** establish a no-incoming-energy/far-field statement whose content is uniform as `R -> infinity`.

A valid Type-II rigidity route must therefore produce at least one additional source-bound handoff, for example:

1. a uniform prelimit tail modulus
   `lim_{R->infinity} sup_k Tail(v^{lambda_k},q^{lambda_k};R)=0`;
2. a content-bound concentration center and compactness modulo translation, with nontriviality and all rigidity hypotheses preserved after recentering;
3. a signed/telescoping boundary-flux relation that avoids absolute tail tightness but has a justified order of limits;
4. a different Euler Liouville theorem whose hypotheses are genuinely local and already supplied by Theorem 3.1.

The first three are bridge obligations. The fourth remains a separate source search, not something this calibration rules out.

## Pressure warning

The calibration already blocks a velocity-only tail inference. Pressure requires an additional audit. Local pressure convergence/estimates do not automatically define one globally compatible `|p|^{3/2}` tail because pressure has nonlocal structure and local normalizations must be reconciled. No pressure-tail theorem is claimed here.

## New scoped obstruction

`O-NS-B2a1-UNIFORM-TAIL-OR-RECENTERING`

> Fixed-cylinder compactness plus local scale-critical control does not transfer a global tail/no-incoming-energy condition. The Seregin Type-II route requires a separately proved **uniform tail modulus, content-bound recentering/profile-compactness certificate, equivalent signed-flux handoff, or genuinely local Euler rigidity theorem**.

The corresponding route-level failure is

`F-NS-B2a1-LOCAL-CONVERGENCE-TAIL-NONTRANSFER`.

This failure is scoped to the inference from local compactness/boundedness alone. It does not blacklist the Seregin route, concentration-compactness, signed flux, or Euler rigidity.

## Next atom

`NS-B2a2 — PRELIMIT_UNIFORM_ANNULAR_TIGHTNESS_OR_RECENTERING`

Exact next question:

> From the original suitable-weak Navier–Stokes hypotheses used in Seregin's F=1 Type-II scaling, can one derive a uniform-in-k annular/tail modulus, or a content-bound recentering/profile-compactness statement, strong enough to prevent loss of velocity/energy/flux at spatial infinity and compatible with the source nontriviality witness?

First hostile checks:

- a fixed local core plus one or more escaping packets;
- translation speeds/centers not controlled by the centered blow-up normalization;
- pressure normalization and harmonic far-field pieces;
- failure of `lim_R sup_k` even when every fixed-radius `k -> infinity` limit is clean;
- whether any proposed tail bound secretly assumes a global critical norm or almost periodicity not present in the source.

**Root status remains:** `OPEN_NO_SOLUTION_CERTIFICATE`.
