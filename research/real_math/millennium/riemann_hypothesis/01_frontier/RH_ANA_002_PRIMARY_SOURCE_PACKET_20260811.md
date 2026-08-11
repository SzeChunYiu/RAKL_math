# RH-ANA-002 primary-source packet — Li norm faithfulness / all-index bridge

**Atom:** `RH-ANA-002`  
**Root:** Riemann Hypothesis  
**Authority:** `SOURCE_BOUND_PRE_CANDIDATE_CONTEXT / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`  
**Framework authority inspected:** current `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`  
**Application base:** `SzeChunYiu/RAKL_math@d8ac4102285c4ed1ba0fbd5d8818dc4c4731a8cc`

## Why this child exists

`RH-ANA-001` proved a search-control negative result: a symmetric planted off-critical zero quartet can keep the first 626 Li transforms positive and turn negative only at index 627. That does not say anything negative about the actual zeta zeros; it says that **finite-index positivity is not the missing global mechanism**.

The next analytic question is therefore not “compute more Li coefficients.” It is:

> What exact zeta-specific theorem transports a manifestly positive analytic object, a prime-side formula, or a global growth constraint to the full all-index Li positivity condition without assuming an RH-equivalent statement?

The highest-information current representation is Masatoshi Suzuki's concrete norm formulation, because it cleanly separates an **unconditional positive object** from an **RH-equivalent identity**.

## Source 1 — Li's all-index criterion

Xian-Jin Li, *The Positivity of a Sequence of Numbers and the Riemann Hypothesis*, J. Number Theory 65 (1997), 325–333, DOI `10.1006/jnth.1997.2137`.

Li's criterion requires the complete sequence of coefficients, not a finite prefix. In the standard zero-sum convention,

`lambda_n = sum_rho [1 - (1 - 1/rho)^n]`

and RH is equivalent to the required nonnegativity for every positive integer `n`.

**Use here:** exact root-equivalent target coordinate.  
**Non-use:** no finite set of checked indices is promoted to RH evidence.

## Source 2 — Bombieri–Lagarias: Li / Weil / arithmetic formula

Enrico Bombieri and Jeffrey C. Lagarias, *Complements to Li's Criterion for the Riemann Hypothesis*, J. Number Theory 77 (1999), 274–287, DOI `10.1006/jnth.1999.2392`.

Two facts matter for this atom.

1. Li coefficients are tied to the Weil explicit-formula machinery on an explicit family `g_n`.
2. They admit an arithmetic formula with binomially weighted Laurent coefficients, archimedean terms, and zeta-values.

Suzuki reproduces the identities in a convenient source-readable form:

`2 lambda_n = W(g_n * conjugate[x^{-1} g_n(x^{-1})])`

and

`lambda_n = -sum_{j=1}^n binom(n,j) eta_{j-1}
            + 1 - (gamma_0 + log(4 pi)) n/2
            - sum_{j=2}^n binom(n,j)(-1)^{j-1}(1-2^{-j}) zeta(j)`.

The second formula is exact but not manifestly termwise positive. Its binomial/cancellation structure makes a naive “positive prime pieces dominate” inference unsafe without an all-`n` remainder theorem.

**Use here:** prime/archimedean source representation and explicit cancellation target.  
**Non-use:** termwise positivity is not assumed or inferred.

## Source 3 — Suzuki: unconditional `G_n`, RH-equivalent norm identity

Masatoshi Suzuki, *Li coefficients as norms of functions in a model space*, J. Number Theory 252 (2023), 177–194; arXiv `2301.05779`. The arXiv HTML consulted on 2026-08-11 displays a later source version while the bibliographic journal result remains 2023.

Suzuki defines `H_n(s)` from `xi`, `xi'/xi`, and the Laurent coefficients of `-zeta'/zeta`, then

`G_n(z) = H_n(1/2 - i z)`.

The paper separates two levels of authority:

### Unconditional layer

- Proposition 2.1 gives an exact identity linking `H_n` to a zero-sum meromorphic function through `xi/(xi+xi')`, derived using Weil's explicit formula.
- Proposition 2.2 states that the restriction of `G_n` to the real line is bounded, real-analytic, and belongs to `L^2(R)` for every positive integer `n`.

Thus the nonnegative quantity

`P_n := (1/(2 pi)) ||G_n||_2^2`

is a well-defined unconditional positive surrogate.

### Root-coupled layer

Theorem 1.1 states that RH is equivalent to

`lambda_n = P_n`

for **all** positive integers `n`.

Therefore the existence and positivity of `P_n` do not solve the Li positivity problem. The exact faithfulness equation is itself root-coupled.

For research control define, without claiming a theorem,

`D_n := P_n - lambda_n`.

`D_n` is merely a bookkeeping defect. The next source audit asks whether the unconditional identities already expose a useful exact representation or sub-obligation for `D_n` that is strictly weaker than forcing `D_n=0` for all `n`.

**Use here:** strongest current localization of “positive object vs exact target identity.”  
**Hard warning:** importing model-space membership or the all-`n` norm equality as unconditional would be circular.

## Source 4 — Lagarias: Li / Weil and unconditional-vs-RH asymptotics

Jeffrey C. Lagarias, *Li Coefficients for Automorphic L-Functions*, Ann. Inst. Fourier 57 (2007), 1689–1740; arXiv `math/0404394`.

Lagarias relates generalized Li coefficients to Weil's quadratic functional, gives an RH positivity criterion, and studies asymptotics both unconditionally and under RH.

**Transfer:** instead of proving every sign separately, one may try to exclude the off-line growth regime globally.  
**Risk:** an unconditional bound strong enough to do this may itself be near-root strength. It must be classified before candidate generation.

## Source 5 — Voros: asymptotic dichotomy

André Voros, *Sharpenings of Li's criterion for the Riemann Hypothesis*, Math. Phys. Anal. Geom. 9 (2006), 53–63; arXiv `math/0506326`.

Voros gives a sharp qualitative dichotomy: under RH the Li coefficients have the familiar tempered `n(A log n + B)` behavior, whereas failure of RH produces a non-tempered oscillatory contribution.

**Transfer:** all-index positivity may be attacked through a global growth-class exclusion instead of indexwise inequalities.  
**Risk:** the source does not itself supply the unconditional global bound required to exclude the off-line regime.

## Current-frontier scan — 2026 material

A current search on 2026-08-11 also found recent numerical/operator and working-paper positivity proposals. The most directly checkable primary example used here only as a **boundary control** is:

Taebong Kim et al., *A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its Universality, and an Operator Form of Weil's Positivity Criterion*, arXiv `2607.24830` (2026).

Its abstract explicitly frames the work as numerical/Archimedean and says it does **not** prove RH.

Recent unreviewed papers and repository preprints that claim RH or propose new positivity equivalences are not used as premises here. They may become adversarial-review targets only after their proof-critical bridge is isolated. “Recent” is not an authority level.

## Four-route faithfulness matrix

| Route | Unconditional object/identity already available | Root-critical missing coordinate | Cheapest next audit |
|---|---|---|---|
| Suzuki norm | `G_n in L2`, hence `P_n >= 0` | exact `lambda_n = P_n` all `n` | classify each proof ingredient as unconditional / RH-conditional / RH-equivalent; seek exact `D_n` subidentity |
| Bombieri–Lagarias arithmetic | exact arithmetic formula for `lambda_n` | uniform control of cancellations/remainder for all `n` | identify first term family whose available bounds lose sign or grow with `n` |
| Lagarias–Voros growth | exact asymptotic dichotomy / unconditional information | unconditional bound excluding non-tempered off-line regime | map strongest known unconditional bound vs minimum exclusion threshold |
| Weil positivity | exact explicit formula | positivity on full admissible class without RH | test any proposed positive core for density/continuity and hidden root-strength |

## Cross-Millennium DifferenceWitness

The selected reusable tool is `T-XM-ROOT-BRIDGE-STABILITY-AUDIT`.

**Source lesson:** in the Yang–Mills calibration, a positive finite-scale dimensionless gap did not guarantee a positive continuum physical gap after the required normalization.

**Shared abstraction:** a locally valid positive surrogate is not enough if the root conclusion requires another preservation/faithfulness bridge.

**Material difference:** RH-ANA-002 is not a cutoff/continuum problem. It is an exact analytic identity/faithfulness problem. The Yang–Mills adversarial sequence has no RH authority.

**Target-specific applicability witness:** Suzuki gives `P_n >= 0` unconditionally while the all-`n` equality `P_n=lambda_n` is RH-equivalent. That is enough to justify reusing the *audit procedure*, not the source counterexample.

## Pre-candidate conclusion

The current atom is not “prove `D_n=0`.” That would simply restate a root-equivalent identity.

The registered next action is a **Li-norm faithfulness matrix**:

1. reconstruct Suzuki's proof dependencies around Theorem 1.1 and Propositions 2.1–2.2;
2. label every bridge `UNCONDITIONAL`, `RH_CONDITIONAL`, `RH_EQUIVALENT`, or `UNKNOWN`;
3. keep `D_n` only as bookkeeping;
4. ask whether the unconditional explicit-formula identities yield any exact subidentity, sign, orthogonality defect, or source term for `D_n`;
5. if no strictly weaker sub-obligation appears, record `NO_STRICTLY_WEAKER_BRIDGE_FOUND` and rotate representation rather than inventing another norm positivity story.

No mathematical candidate is generated in this packet.
