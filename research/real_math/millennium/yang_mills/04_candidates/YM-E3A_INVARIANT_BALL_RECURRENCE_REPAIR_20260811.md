# YM-E3a — invariant-ball repair of the Appendix A nonlinear recurrence

Status: `PROPOSAL / SHADOW VERIFIED LOCAL LEMMA / ROOT AUTHORITY NONE`

Active atom: `YM-E3a` (RAKL_math issue #93). Root: issue #5, `OPEN_NO_SOLUTION_CERTIFICATE`.

Frozen fibre: `../10_case_study/YM-E3A_FROZEN_FIBRE_20260811.json`, snapshot `sha256:97f8475b86180fb0e3eb747b519e385053863baffc5ce46bb19472609f24f24a`.

## Primary-source binding

Primary source actually inspected in this cycle: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026), Appendix A, especially Theorem A.9, the recurrence labelled (A.53), Lemma A.10, and the estimate labelled (A.59).

The source's Step 1 has the schematic local map

`Phi' = L Phi + Q(Phi,Phi)`, with `||L|| <= rho < 1` and `||Q(Phi,Phi)|| <= C ||Phi||^2` only while `||Phi|| <= r`.

Step 2 says the entry norm can be made arbitrarily small by moving sufficiently far into the weak-coupling regime / shrinking the compact bare-coupling interval. Step 3 then invokes the scalar recurrence

`x_{n+1} <= rho x_n + C x_n^2`.

The literal Lemma A.10 is printed without an invariant-ball/smallness condition. Its written induction attempts to close using a condition equivalent to `2 C r + C r^2 <= 0` for positive `C,r`, which cannot hold. This cycle does not infer any missing formula from memory: only the displayed source recurrence and source-stated local domain are used below.

Visual PDF screenshot verification was attempted for the relevant Appendix A pages, but the web PDF cache returned a transient cache miss. Parsed primary-source text was available; the screenshot failure is preserved as a verification-tooling limitation, not silently ignored.

## Counterexample-first falsification of the literal lemma

Take the equality recurrence with

`rho = 1/2`, `C = 1`, `r = 2`, `x_0 = 2`.

Then

- `x_1 = (1/2)2 + 2^2 = 5`,
- `x_2 = (1/2)5 + 5^2 = 27.5`.

The claimed A.10-type upper bound at `n=2` is

`rho^2 r + C r^2/(1-rho) = 0.5 + 8 = 8.5`.

Thus `27.5 > 8.5`. Therefore the scalar lemma is false as literally stated when no invariant-domain/smallness hypothesis is imposed. This is stronger than merely observing that the printed induction is invalid.

## Correct local lemma

**Proposition (invariant-ball nonlinear contraction).** Let `x_n >= 0`, `0 < rho < 1`, `C > 0`, and suppose

`x_{n+1} <= rho x_n + C x_n^2`.

Let `r_* > 0` satisfy `x_0 <= r_*` and

`q := rho + C r_* <= 1`.

Then the ball `[0,r_*]` is forward invariant. In particular,

`x_n <= rho^n r_* + C r_*^2 (1-rho^n)/(1-rho) <= rho^n r_* + C r_*^2/(1-rho)`.

If the inequality is strict, `q < 1`, then the stronger estimate holds:

`x_n <= q^n x_0`,

so `x_n -> 0` exponentially.

### Proof

Assume inductively `x_n <= r_*`. Then

`x_{n+1} <= (rho + C x_n)x_n <= (rho + C r_*)x_n = q x_n <= q r_* <= r_*`.

Since `x_0 <= r_*`, induction proves invariance. Unrolling the original recurrence gives

`x_n <= rho^n x_0 + C sum_{j=0}^{n-1} rho^{n-1-j} x_j^2`.

Invariance gives `x_j^2 <= r_*^2`, hence the geometric-series estimate above. Under `q<1`, the same one-step inequality gives `x_{n+1} <= q x_n`, and induction yields `x_n <= q^n x_0`. QED.

A convenient strict sufficient choice is

`r_* <= (1-rho)/(2C)`,

which yields `q <= (1+rho)/2 < 1`.

## Conditional source-internal repair path

This proposition repairs only the deterministic recurrence layer if all of the following source-side conditions are genuinely available:

1. Step 1 supplies fixed/uniform `rho in (0,1)`, `C>0`, and an admissible local radius `r_0>0` for the actual polymer norm and RG map.
2. Step 2 reaches an entry state with `||Phi_K|| <= r_*` without using the desired contraction circularly.
3. Choose `r_* <= min(r_0,(1-rho)/(2C))`.

Then the Step-1 quadratic estimate remains applicable at every subsequent iterate, and the scalar norm satisfies a genuine geometric decay bound with factor at most `(1+rho)/2`.

This is a **conditional local repair**, not a verification of source conditions 1–2. Exact source-level construction of the non-Abelian RG map, the provenance and scale-uniformity of its constants, and the bare-coupling entry argument remain open obligations under issue #93.

## Important distinction: boundedness versus decay

The A.59-form estimate

`rho^n r_* + C r_*^2/(1-rho)`

has a positive `n -> infinity` floor when `C,r_*>0`. Therefore that estimate alone does not prove convergence to zero. The strict invariant-ball inequality `q<1` supplies the missing direct geometric estimate `x_n <= q^n x_0`. Any downstream argument requiring actual norm decay must use a bound of this latter type (or another valid zero-floor estimate), not infer decay from the positive-floor bound alone.

## Transfer assumptions and disanalogies

The scalar proposition transfers to the source RG step only under a norm inequality with the exact same `rho,C` and an iterate that remains inside the local domain. It does **not** transfer merely from an abelian block-spin model, a perturbative beta-function computation, a fixed-cutoff contraction, or a finite-volume estimate. In particular:

- scalar contraction is not gauge fixing or gauge invariance;
- small-polymer-norm contraction is not construction of a nontrivial continuum Euclidean measure;
- a local weak-coupling recurrence is not a thermodynamic/continuum limit;
- Euclidean decay is not by itself the physical Hamiltonian mass gap without reflection positivity, OS reconstruction, and spectral identification in the same limiting theory;
- perturbative asymptotic freedom is not a substitute for the source's nonperturbative existence/universality bridge.

## Expert-cell audit (same context; no independent-review credit)

- **Nonlinear dynamics:** proposition and hostile counterexample are algebraically correct; `q<1` is sufficient for invariant-domain geometric decay.
- **Constructive RG/polymer:** propagation is noncircular only after source-binding the local domain and entry norm. That binding is still open.
- **Constructive QFT/OS:** no claim here establishes Euclidean-measure existence, reflection positivity, OS reconstruction, continuum nontriviality, or a physical spectral gap.
- **Asymptotic freedom:** the recurrence repair does not establish the perturbative beta-function identification or universality claim.
- **Adversarial audit:** literal A.10 is falsified by the explicit equality recurrence; candidate survives the same attack because the counterexample violates `q<=1`.
- **Formal assurance:** deterministic arithmetic and invariant-ball cases are covered by the accompanying executable test.
- **Source/novelty audit:** primary-source provenance is explicit; result is classified, at most, as `COMPOSITIONAL` relative to issue #93's already-stored repair direction. No theorem/root novelty is claimed.

## Local versus gluing residuals

**Local mathematical residuals:** exact source binding of `rho,C,r_0`; proof that Step 2 reaches `r_*` without circular use of contraction; propagation through the exact source Theorem A.9 and any claimed AF/universality identification.

**Local-to-global/gluing residuals (separate):** construction and nontriviality of the continuum Euclidean measure; gauge-invariance/gauge-fixing compatibility; reflection positivity in the limiting measure; finite/infinite-volume and continuum-limit uniformity/interchange; OS reconstruction; correlation-decay-to-Hamiltonian-spectrum identification; positive physical mass gap in that same theory; extension to every compact simple gauge group under the official root contract.

## Success-contract status for issue #93

1. Correct recurrence lemma with explicit invariant-ball hypotheses: **LOCALLY VERIFIED / PROPOSAL**.
2. Independent algebraic proof and recurrence-domain propagation: **LOCALLY VERIFIED / PROPOSAL**.
3. Exact FRD/polymer source binding of constants/radius: **OPEN**.
4. Noncircular bare-coupling entry into invariant domain: **OPEN**.
5. Propagation through Theorem A.9 and AF/universality identification: **OPEN**.
6. Perturbative beta function kept separate from nonperturbative existence: **ENFORCED AS SCOPE BOUNDARY; source derivation remains OPEN**.

Root promotion is prohibited. No full Yang–Mills existence theorem, mass-gap theorem, or solution certificate is produced by this atom.
