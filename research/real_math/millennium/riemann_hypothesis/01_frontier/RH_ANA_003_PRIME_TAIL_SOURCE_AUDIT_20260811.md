# RH-ANA-003 — Bombieri–Lagarias prime/tail source audit

**Authority:** source-bound discriminator / same-context expert synthesis / no RH theorem / no mathematical candidate / root authority none.

## Exact atom

In the exact Bombieri–Lagarias arithmetic representation of the Li coefficients, localize the first place where fixed-parameter prime-side control fails to supply an all-`n` sign theorem. Test whether modern zero-density input repairs that loss without silently strengthening to zero exclusion.

The frozen fibre is `RH_ANA_003_CONTEXT_FIBER_20260811.json`, hash `sha256:1708d7be2a9a8403c727ee4e5c1723fe5ff44e46fed3843290e804b3c84b4dc1`.

## Primary-source reconstruction

Primary source: Enrico Bombieri and Jeffrey C. Lagarias, *Complements to Li's Criterion for the Riemann Hypothesis*, J. Number Theory 77 (1999), 274–287, DOI `10.1006/jnth.1999.2392`; author-hosted preprint `https://websites.umich.edu/~lagarias/doc/bombieri.pdf`, accessed 2026-08-11.

Bombieri–Lagarias first state a Guinand–Weil explicit formula for a Mellin-transform test function. Their Lemma 2 identifies the inverse Mellin transform of `1-(1-1/s)^n` with a polynomial `P_n(log x)` on `0<x<1`. Their Theorem 2 then gives, for every fixed positive integer `n`, an arithmetic formula of the form

`lambda_n = - sum_{j=1}^n (-1)^(j-1) binom(n,j) C_j/(j-1)! + A_n`,

where

`C_j = lim_{x->infinity} [ sum_{m<=x} Lambda(m)(log m)^(j-1)/m - (log x)^j/j ]`

and `A_n` is the explicit archimedean term

`1 - (log(4*pi)+gamma)n/2 - sum_{j=2}^n (-1)^(j-1) binom(n,j)(1-2^(-j)) zeta(j)`.

The regularization is part of the theorem and must not be replaced by a finite prime truncation. In the proof of their equation (3.8), the cutoff error contains the degree-`n` polynomial `P_n(log epsilon)` and an error with `(log(1/epsilon))^(n-2)` dependence. The paper proves the cutoff limit for each fixed `n`; this proof segment does **not** state a uniform-in-`n` cutoff modulus suitable for passing from finite/fixed-index arithmetic control to all-index Li positivity.

This is the first exact coordinate localized in this cycle:

> **fixed-`n` renormalized prime formula -> all-`n` sign control is a separate uniform triangular-cancellation obligation.**

It is not a flaw in Bombieri–Lagarias. Their theorem is exact for every fixed `n`; the missing item is what a new proof strategy would need if it tried to infer all-index positivity from controlled prime truncations or fixed-`j` Laurent/prime constants.

A second primary reference, Jeffrey C. Lagarias, *Li Coefficients for Automorphic L-Functions*, arXiv:`math/0404394v4` / Ann. Inst. Fourier 57 (2007), explicitly distinguishes unconditional and RH-conditional asymptotic information for Li coefficients. It is used here as a guard against treating an asymptotic coordinate as automatically sign-determining for every index.

## Current zero-density input and falsifier

Current primary input checked: Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, arXiv:`2405.20552` (2024), Theorem 1.2 / displayed consequence `N(sigma,T) <= T^{30(1-sigma)/13+o(1)}`. This is a strong density theorem, but its logical type is a count upper bound, not a zero-exclusion theorem.

For an off-critical zero `rho=beta+i gamma` with `beta<1/2`, define `q=1-1/rho`. Then exactly

`|q|^2 = 1 + (1-2 beta)/|rho|^2 > 1`.

The functional-equation/reflection partner on the other side has reciprocal modulus. Thus an abstract symmetric off-line quartet has a Li contribution with an exponentially growing envelope `|q|^n` along suitable indices. The amplification scale is quantified by

`log |q| = (1/2) log(1 + (1-2 beta)/|rho|^2)`,

so for a high zero with small horizontal displacement the index needed for order-one amplification is on the scale `n ~ |rho|^2/(1-2 beta)`.

This does **not** construct a zeta zero. It is an inference-form falsifier: a density inequality that permits even one off-line zero cannot by itself imply the all-index Li sign condition. Sparse exceptional zeros are exactly the case that the root forbids and that a nonzero density upper bound does not exclude.

## Expert-cell discussion

The analytic-number-theory lead accepted the Bombieri–Lagarias fixed-`n` formula and flagged the cutoff proof's explicit `n`-dependence as the first quantifier-order boundary. The Li/Weil specialist rejected any move that rebrands `lambda_n>=0` or a full Weil positivity condition as the missing lemma; the residual must be strictly weaker and independently falsifiable. The mollifier/resonance specialist rejected current average/density control as sufficient because it does not rule out a sparse exceptional zero and therefore cannot close every Li index. The adversarial proof auditor separated two failures: the **local mathematical** issue is absence of a source-proved uniform triangular cancellation estimate; the **local-to-global/gluing** issue is the invalid inference from density/finite-cutoff control to the all-index sign family. The RAKL v3 provenance lead kept both observations at shadow/proposal authority and prohibited novelty or root promotion.

## Route decision and residual

`RH-ANA-003` records a bounded partial success: the previously vague “prime/archimedean cancellation or all-n tail” residual is narrowed to a concrete quantifier-sensitive object. Any continuation of this route must control the full triangular family

`{C_j/(j-1)! : 1<=j<=n}`

together with the archimedean alternating binomial transform, with an error/sign estimate uniform enough in `n` to imply the desired coefficient sign. A fixed `j`, fixed `n`, finite-prime, or density-average bound does not satisfy that contract.

Next residual (not a theorem candidate): `RH-ANA-003a — TRIANGULAR_RENORMALIZATION_UNIFORMITY`. The cheapest next action is to source-bind known unconditional growth bounds for the normalized `C_j`/equivalent Laurent coefficients and propagate them through the exact binomial transform, counterexample-first. If the propagated envelope is comparable to or larger than the main archimedean scale, retire this prime-side subroute rather than optimizing finite truncations.

## Source provenance

- Bombieri, E.; Lagarias, J. C. (1999), DOI `10.1006/jnth.1999.2392`, author preprint above, especially explicit formula and Theorem 2, pp. 6–10 of the preprint.
- Lagarias, J. C., arXiv:`math/0404394v4`, journal reference Annales Institut Fourier 57 (2007), 1689–1740.
- Guth, L.; Maynard, J., arXiv:`2405.20552`, especially Theorem 1.2 / zero-density consequence.

No computation is used as proof. No source is treated as independent review of this cycle.
