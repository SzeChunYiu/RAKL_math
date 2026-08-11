# YM-S1c1a2a — irrelevant-coordinate forcing / normal-form consistency audit (R10)

**Authority:** `PROPOSAL_SHADOW_ONLY / SOURCE-PROOF-AND-REPRESENTATION-AUDIT / ROOT_AUTHORITY_NONE`  
**Root:** #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Parent atom:** #177 / `YM-S1c1a2-AFIR-ENDPOINT-PRESERVING-VANISHING-UV-ALIGNMENT`  
**Cycle subatom:** `YM-S1c1a2a-IRRELEVANT-COORDINATE-FORCING-NORMAL-FORM-CONSISTENCY`  
**Primary target:** Mir Faizal and Arshid Shabir, arXiv:2606.19362v1 (9 June 2026), Sections 10.1–10.2.  
**Near-solved transfer analogue:** Bauerschmidt–Brydges–Slade, arXiv:1211.2477; Brydges–Slade, arXiv:1403.7256.

This record audits only the displayed RG argument and the coordinate obligations needed by the AF/IR identification route. It is not a proof or disproof of the Yang–Mills Millennium problem, and it does not grant theorem, lesson, obstruction, review-independence, or framework authority.

## 1. Exact local mismatch

Theorem 10.4 defines the effective action with the irrelevant polymer activity `K_k` normalized to have zero projection onto the marginal `tr F^2` functional. The displayed one-step estimate is

`||K_{k+1}|| <= theta ||K_k|| + c1 g_k^2`

and the proof explicitly says that integrating the marginal sector generates a **strictly irrelevant `g_k^2` piece**, yielding the additive forcing term; see (10.34), (10.39). The same theorem bounds the marginal remainder by

`|R_k| <= c2 |g_k|^5 + c3 |g_k| ||K_k|| + c3 ||K_k||^2`.

Later, Theorem 10.7 says, again for `(g_k,K_k)` in the same polydisc, that the starting point is

`g_{k+1}=g_k-beta0(log b) g_k^3 + R_g(g_k,K_k)`,
`K_{k+1}=b^{-omega} K_k + R_K(g_k,K_k)`

with

`||R_K(g,K)|| <= C (g^2+||K||) ||K||`,

i.e. no additive `O(g^2)` forcing. From this homogeneous-looking recurrence the proof derives exponential decay of `K_k`.

No coordinate change, stable-graph subtraction, or new definition of `K_k` is stated between these displays in the inspected source. A search for “stable manifold” and “coordinate change” returns no matching Section-10 transition. Therefore the later exponential-decay step is **not derived from the earlier raw-`K` estimate as written**. This is a local source/representation obligation; it is not yet a theorem-level contradiction because a missing coordinate theorem could repair it.

## 2. Counterexample-first inference test

The additive-forcing estimate cannot itself imply exponential raw-`K` decay. In the scalar model

`K_{k+1}=q K_k + c g_k^2`, `0<q<1`,

with `g_k^2 ~ 1/k`, the stable response is `K_k ~ c/(1-q) g_k^2`, hence polynomial rather than exponential. More importantly, combine this with an allowed source-shaped marginal mixed term

`g_{k+1}=g_k-beta g_k^3 + a g_k K_k`.

On the leading slaved graph `K=A g^2`, invariance at order `g^2` forces

`A = c/(1-q)`,

and substitution gives

`g_{k+1}=g_k-[beta-a c/(1-q)] g_k^3 + O(g_k^5)`.

Thus the **norm bounds alone** permit an `O(gK)=O(g^3)` contribution from the slaved irrelevant sector that shifts the leading cubic coefficient. They therefore do not certify both (i) an additive `O(g^2)` raw-`K` forcing and (ii) an unchanged universal one-loop marginal coefficient without an additional cancellation/projection/normal-form lemma.

This hostile control attacks only the inference from the displayed estimates. The actual gauge-theory map may possess a cancellation not encoded by those bounds.

## 3. Smallest repair surface

A sufficient repair would be a typed slaving/normal-form theorem. One admissible shape is an analytic or sufficiently regular map `Psi(g)=O(g^2)` and a transformed coordinate

`Ktilde = K - Psi(g)`

such that, on the exact Yang–Mills RG map and uniformly in all required regulators/scales,

1. `Ktilde_{k+1}=L_b Ktilde_k + O(g_k^4) + O(g_k^2 ||Ktilde_k||) + O(||Ktilde_k||^2)` with `||L_b||<1` (or a stronger invariant-graph form);
2. after substituting `K=Psi(g)+Ktilde`, the marginal equation has **no new `O(g^3)` term**, so its remainder is genuinely higher order than the universal cubic beta term;
3. the map `(g,K) <-> (g,Ktilde)` is defined on the same admissible trajectory range and preserves/controls the one-slice transfer kernel and its Lipschitz constants;
4. the transformed chart is uniform in volume, lattice spacing, regulator/FRD data and RG scale at the strength required by #177;
5. the chart change preserves the same gauge-invariant source algebra, reflection-positive OS quotient/Hilbert space, continuum subsequence and fixed-physical-time normalization.

A mere formal subtraction in a Banach norm is insufficient: the same-theory gluing and kernel-observable map must be transported.

## 4. Solved/near-solved analogue and DifferenceWitness

Bauerschmidt–Brydges–Slade (arXiv:1211.2477) give a rigorous structural-stability theorem for an infinite-dimensional RG dynamical system near a **non-hyperbolic** fixed point. Their state is split into a nonperturbative Banach-space coordinate `K` and marginal/relevant finite-dimensional coordinates. Under explicit derivative, contraction, and boundary-condition assumptions, they construct a unique global flow close to a triangular quadratic reference flow. In their notation the marginal reference variable behaves as `bar g_j ~ 1/j`; the controlled nonperturbative coordinate is of order `bar g_j^3`, and the marginal correction is bounded at higher order with logarithmic factors. Brydges–Slade (arXiv:1403.7256) separately build the single-step nonperturbative coordinate and its contraction conditions.

**Transfer mapping:** compare their marginal `bar g_j` with `u_k=g_k^2` for the Yang–Mills flow, since `u_k` is also order `1/k`; compare their contractive `K` with a *properly normalized/slaved* Yang–Mills irrelevant coordinate.

**DifferenceWitness / broken assumptions:** the source Yang–Mills raw estimate presently permits additive forcing of order `g_k^2 = u_k`, not order `u_k^3`; the gauge model, polymer norm, source algebra, reflection positivity, regulator uniformity, and marginal-projection cancellation hypotheses are different and are not supplied by the analogue. The analogue therefore **guides the repair architecture only**; it does not transfer a theorem.

## 5. Consequences for the AF/IR vanishing route

This audit reopens the representation coordinate underneath the R7/R8/R9 AF/IR failures. It explains why simply replacing the R7 harmonic `O(g^2)` coupling-difference estimate by “strict contraction in `K`” is not licensed: the source has two incompatible displayed `K` recursion shapes unless a transition certificate is supplied.

It also separates two failure layers:

- **local mathematical/source-representation failure:** the raw-to-homogeneous `K` transition and the leading-beta cancellation are not derived by the inspected estimates;
- **local-to-global gluing failure:** even a repaired coordinate theorem must still transport to the same one-slice kernels, OS sources/quotient and continuum state required by #177.

No finite computation, fitted trajectory, or numerical RG run can close either proof obligation.

## 6. Counterfactuals / falsifiers that would overturn this diagnosis

The diagnosis is withdrawn if a source-bound argument establishes any of the following on the exact Section-10 objects:

- the `K_k` in (10.65) is explicitly a different coordinate from the `K_k` in (10.34)/(10.39), with a typed invertible transition and propagated kernel/source bounds;
- the generated `c1 g^2` term in (10.39) has an exact cancellation that makes the actual `K` update homogeneous at the required order;
- an invariant/stable graph `Psi(g)` is constructed and the marginal projection of its slaved piece is proved not to shift the cubic beta coefficient;
- a different direct AF/IR comparison bypasses the `K` coordinate while still satisfying all same-theory and vanishing requirements of #177.

## 7. Outcome and residual

**Outcome:** `PARTIAL_SUCCESS__RAW_K_ADDITIVE_FORCING_AND_LATER_HOMOGENEOUS_K_RECURRENCE_REQUIRE_AN_EXPLICIT_COORDINATE_OR_CANCELLATION_CERTIFICATE`

**Residual after R10:**  
`RES-YM-S1c1a2b-SLAVING-NORMAL-FORM-PLUS-MARGINAL-CANCELLATION-AND-SAME-OS-KERNEL-TRANSPORT`

**Scoped novelty classification:** `representation` (proposal/shadow only): the high-information advance is a coordinate-identity obstruction and a precise normal-form repair surface, not a new Yang–Mills theorem. The scalar hostile-control algebra is elementary and should not be counted as protected mathematical novelty.
