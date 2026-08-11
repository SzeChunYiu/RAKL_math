# YM-S1c1a1 R9 — AF/IR vanishing and endpoint-preserving UV-alignment audit

**Authority:** `PRIMARY_SOURCE_AUDIT / PROPOSAL_SHADOW_ONLY / ROOT_AUTHORITY_NONE`  
**Root:** RAKL_math #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Active atom:** RAKL_math #171, `YM-S1c1a1-SECTION9-TELESCOPE-TERMINAL-ANCHOR-AFIR-SAME-THEORY-GLUING`  
**Successor control:** RAKL_math #177, `YM-S1c1a2-AFIR-ENDPOINT-PRESERVING-VANISHING-UV-ALIGNMENT`

## Primary source and exact provenance

Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026). Primary PDF: `https://arxiv.org/pdf/2606.19362`.

Load-bearing locations inspected directly in the primary PDF:

- Theorem 10.8, printed pp. 126–127, equations (10.77)–(10.81), especially the additive discrepancy recurrence and the paragraph immediately after (10.81).
- Appendix Lemma F.10, printed pp. 226–229, equations (F.68)–(F.80), especially the metric-distance/path-length inequality, the arbitrary-small-length claim, and the modified tail-only path.
- Appendix Theorem F.11, printed pp. 229–230+, equations (F.81)–(F.83), where Lemma F.10 is invoked as an endpoint-preserving arbitrarily short path.

Parsed-primary-PDF text was inspected for all of these locations. Visual PDF verification **succeeded** for Theorem 10.8 printed pp. 126–127 (screenshots of the theorem statement and the page containing (10.80)–(10.81)); repeated visual attempts on the Appendix F pages returned backend `Cache miss`, so Appendix-F visual verification is `CANNOT_CHECK`, not inferred passed.

## Finding A — Theorem 10.8 proves bounded discrepancy, not vanishing discrepancy

For fixed observables, define

`d_k = |S^AF_{m,k}(A_1,...,A_m) - S^IR_{m,k}(A_1,...,A_m)|`.

The displayed one-step estimate (10.80) is

`d_{k+1} <= d_k + C epsilon_k`,

and (10.81) gives

`d_K <= d_0 + C sum_{k=0}^{K-1} epsilon_k`,

with `sum epsilon_k < infinity`.

The source then notes that the right-hand side is bounded and tends to `d_0 + C sum epsilon_k`, says the initial difference can be absorbed by adjusting the starting scale or by finite Lipschitz distance of the initial data, and concludes that the AF and IR functionals converge to the same limiting value.

That conclusion does not follow from the displayed inequalities alone. Exact hostile control:

`d_k = 1` for every `k`, `epsilon_k = 0` for every `k`.

Then (10.80) and (10.81) hold with equality, the defects are summable, and the discrepancy never tends to zero. A finite Lipschitz/FRD distance is a boundedness datum, not a vanishing anchor.

**Scoped diagnosis:** the displayed proof of Theorem 10.8 is missing a vanishing comparison input. This does **not** establish that Theorem 10.8 is false; an unquoted endpoint/reference theorem, strict contraction, or actual-trajectory UV matching result could repair it if proved with the required same-theory scope.

A sufficient repair shape would be one of:

1. an actual-trajectory anchor `d_{k0} -> 0` when the common UV starting scale is moved appropriately;
2. a strict contraction `d_{k+1} <= q d_k + delta_k` with `q<1` and a tail forcing the right-hand side to zero;
3. a common reference/fixed-point theorem proving the AF and IR initial/slice states approach the same point in the relevant typed topology.

Any such repair must be volume/lattice-spacing/regulator uniform and must preserve the same gauge-invariant OS source algebra, quotient/Hilbert space, continuum subsequence, and physical-time normalization.

## Finding B — Lemma F.10's arbitrary-short-path claim conflicts with endpoint distance unless endpoints collapse

Lemma F.10 states for admissible regulators `Theta_0, Theta_1` that there is a `C^1` path with those endpoints and records the standard inequality

`d_adm(Theta_0,Theta_1) <= integral_0^1 ||partial_s Theta_s|| ds`.

The same lemma then claims that, by leaving all coarse scales below `k_*` fixed and interpolating only sufficiently fine scales, the path length can be made `< epsilon` for every `epsilon>0`.

For fixed endpoints with `d_adm(Theta_0,Theta_1)>0`, these two assertions cannot both hold: choose `epsilon < d_adm(Theta_0,Theta_1)`. Every endpoint-preserving path has length at least the endpoint distance.

This is not merely an abstract objection to the proof's presentation. The modified path used to obtain the small tail bound sets the low-scale components to the `Theta_0` value for all `s`, while only high-scale components are interpolated. If `Theta_0` and `Theta_1` differ at any frozen low scale, the `s=1` point of the modified path is not `Theta_1`. The proof also optionally replaces the slice projector by a tail/truncated projector, which likewise requires an endpoint-binding argument. The source does not derive that arbitrary admissible endpoints have identical frozen low-scale data or zero `d_adm` distance.

Exact metric hostile control: take any metric-space pair `x,y` with `d(x,y)=1`. No path connecting `x` to `y` can have length `<1/2`. Freezing the coordinate on which they differ can produce a short path only by changing an endpoint.

**Scoped diagnosis:** the tail-localization maneuver as displayed mutates or fails to bind the original endpoint data unless additional equality/quotient hypotheses are proved. This is a representation/quantifier problem as well as a local proof problem.

## Finding C — Theorem F.11 inherits the endpoint-binding obligation

Theorem F.11 invokes Lemma F.10 to obtain, for arbitrary admissible `Theta_0,Theta_1`, a path whose endpoints are the original schemes, whose support lies only on sufficiently fine FRD scales, and whose length is `< epsilon`; it then lets `epsilon -> 0` in a Lipschitz bound to conclude equality of continuum Schwinger functions.

Because the key arbitrarily-short endpoint-preserving path is not established by the displayed F.10 proof for fixed endpoints at positive `d_adm` distance, F.11 does not yet repair Finding A. A valid repair must either:

- prove the actual original endpoints have `d_adm=0` in a typed quotient/equivalence relation and show that quotient preserves the relevant OS/gauge observables; or
- produce an endpoint-preserving path with a genuinely vanishing bound derived from additional UV matching, rather than by deleting nonzero coarse endpoint differences.

## Local failure vs local-to-global/gluing failure

**Local/source-proof failures:** (10.80)–(10.81) do not imply `d_k -> 0`; F.10's arbitrary-short endpoint-preserving path is incompatible with positive endpoint metric distance, and its tail-only construction generally changes an endpoint.

**Local-to-global/gluing residual:** even a corrected vanishing estimate must identify the same AF/IR continuum state on the same gauge-invariant generating algebra, same RP/OS quotient, same physical time normalization, and same continuum subsequence. Finite distance, continuity, or two separate compactness subsequences are insufficient for this identification.

## Same-context expert cell

1. **Constructive QFT / OS reconstruction:** equality must be obtained on a generating gauge-invariant cylinder algebra before OS reconstruction can identify one continuum state; bounded distance does not provide this.
2. **Rigorous RG / renormalization:** moving the starting scale is useful only if an actual AF/IR trajectory theorem proves the comparison tends to zero, uniformly in the continuum/volume parameters.
3. **Functional analysis / metric geometry:** an additive recurrence with summable positive defects need not contract; every rectifiable path has length at least endpoint metric distance.
4. **Gauge theory / physical state:** a repair may not freeze, truncate, or quotient projector/blocking data unless the operation preserves gauge invariance, RP positivity, physical-time normalization and the physical-state identification.
5. **Formal proof / quantifier audit:** F.10 quantifies over fixed arbitrary endpoints and arbitrary epsilon; the tail-only construction must retain both endpoints for those quantifiers to be satisfied.
6. **Adversarial source + RAKL v3 assurance:** primary-source text supports the scoped diagnoses; no impossibility theorem, protected lesson, or independent-review credit is warranted.

## DifferenceWitness / disanalogies

- `finite distance` vs `distance -> 0`;
- `summable additive error` vs `contractive error recursion`;
- `tail-only interpolation` vs `path with the original endpoints`;
- `continuity of regulator dependence` vs `exact regulator independence`;
- `same-context OS formalism` vs `proved identity of the same reconstructed state`.

## Outcome and residual

**Outcome:** `PARTIAL_SUCCESS__DIRECT_AFIR_EQUALITY_PROOF_REQUIRES_VANISHING_NOT_BOUNDEDNESS__APPENDIX_UV_ALIGNMENT_PATH_FAILS_ENDPOINT_BINDING_AS_DISPLAYED`

**Residual:** `RES-YM-S1c1a2-ENDPOINT-PRESERVING-VANISHING-AFIR-ANCHOR-OR-STRICT-CONTRACTION-SAME-OS-THEORY`

No Yang–Mills theorem, continuum-existence proof, positive mass-gap proof, or root certificate is claimed.