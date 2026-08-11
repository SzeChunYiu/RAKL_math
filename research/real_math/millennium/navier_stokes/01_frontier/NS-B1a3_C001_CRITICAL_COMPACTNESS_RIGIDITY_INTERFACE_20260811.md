# NS-B1a3-C001 — Critical compactness / rigidity interface audit

**Date:** 2026-08-11  
**Authority:** `SOURCE_BOUND_INTERFACE_ROUTE_PRUNING / LOCAL_COMPACTNESS_ACCEPTED / GLOBAL_GLUE_BLOCKED / COMPUTATION_NOT_USED / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`

## Executive finding

The local Type-I blow-up compactness package and the selected global rigidity packages meet at a **missing global critical-tightness interface**.

Albritton–Barker's registered Type-I quantity `I` is a supremum of local scale-invariant cylinder quantities `A+C+D+E`. Their Theorem 1.1 supplies the correct global ancient object: a nontrivial mild bounded ancient solution with `I<infinity`. Their local compactness lemma supplies strong `L^3_loc` convergence for velocity and weak `L^{3/2}_loc` convergence for pressure, while persistence of singularities preserves the selected singular core.

But the rigidity trigger in their Theorem 1.2 is different: it requires a backward sequence `t_k -> -infinity` with a **uniform global** `L^3(R^3)` bound. Likewise the Gallagher–Koch–Planchon critical-element/profile-decomposition route starts from boundedness in an explicitly specified **global critical** Lebesgue/Besov topology and resolves translation/dilation loss of compactness inside that topology.

Therefore the following implication is **not licensed by the cited sources**:

`finite I + local suitable compactness + persistence of one core  =>  global critical precompactness or backward global-L3 sequence`.

This is a gluing/interface failure, not a failure of the local compactness mathematics.

## Exact limit-passage interface

Normalize viscosity to `1` and a candidate singular point to `(0,0)`. Under parabolic rescaling,

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`,  
`p_lambda(x,t)=lambda^2 p(lambda x,lambda^2 t)`.

For suitable weak solutions with uniform local `L^3` velocity and `L^{3/2}` pressure bounds, Albritton–Barker Lemma 2.2 gives, after passing to a subsequence on every fixed smaller cylinder,

`u^(n) -> v strongly in L^3_loc`,  
`p^(n) ⇀ q weakly in L^{3/2}_loc`.

This strength is enough to pass the local nonlinear term and local energy inequality, and Proposition 2.3 supplies persistence of singularities under the stated blow-up hypothesis. Thus **local core extraction is accepted**.

What is not obtained by this statement is any of:

- strong convergence in global `L^3(R^3)`;
- tightness of `|u^(n)|^3 dx` at spatial infinity;
- a uniform global critical norm of the ancient limit along backward times;
- uniqueness of the global profile after quotienting translation/dilation symmetries;
- global pressure identification from the local weak pressure limit.

The limit passage is therefore local-to-local. A later global rigidity theorem needs a separate local-to-global certificate.

## Pressure localization audit

In the persistence argument, pressure is decomposed schematically as

`p^(n) = p_loc^(n) + h^(n)`,

where `p_loc^(n)` is the localized Calderón–Zygmund transform of a cutoff of `u^(n) tensor u^(n)` and `h^(n)` is harmonic on a smaller ball. Local `L^3` convergence controls the localized singular-integral part, and harmonic interior estimates control `h^(n)` on still smaller cylinders.

That mechanism is exactly sufficient for local epsilon-regularity/persistence. It does **not** identify the global harmonic/far-field pressure component or prove velocity-tail tightness. Replacing this local harmonic-remainder control by a global pressure formula would change the proof interface and requires additional decay/integrability hypotheses.

## Noncompact symmetry / profile leakage audit

The critical symmetries are spatial translation and parabolic dilation (with time translation fixed by normalization of the singular time). Two adversarial calibrations show why local compactness does not certify global critical compactness:

1. **Translation escape.** For any fixed nonzero `phi in L^3(R^3)`, the translates `phi(x-x_n)` with `|x_n|->infinity` converge to zero strongly in `L^3(K)` on every compact `K` while preserving the global `L^3` norm.
2. **Orthogonal profiles.** A bounded critical-space sequence can decompose into profiles whose translation/dilation parameters become asymptotically orthogonal. Selecting the singular core does not show that the remaining profiles carry zero global critical mass.

These are not Navier–Stokes counterexamples. They are exact falsifiers of the **topological inference** from local convergence to global critical tightness.

The Gallagher–Koch–Planchon machinery is therefore a valid analogue only after the target lane has first constructed a bounded global critical sequence/state space. It cannot be used to manufacture that prerequisite from finite `I` by circularity.

## Rigidity interface audit

### Albritton–Barker Theorem 1.2

Valid trigger: a mild ancient solution with `sup_k ||v(t_k)||_L3(R3)<infinity` for some `t_k -> -infinity` is zero.

Missing target interface: finite `I` does not, in the registered source package, imply that global backward-sequence bound. The current cycle does not prove that such an implication is false for Navier–Stokes; it records that the implication is a separate open obligation.

### Backward uniqueness / unique continuation

The Escauriaza–Seregin–Šverák route is not a generic black box. A valid invocation must bind the precise critical/terminal setting and verify the hypotheses of the parabolic unique-continuation theorem for the vorticity equation, including the domain, regularity/coefficient bounds, exterior/global control and terminal-time information used in the proof.

Finite `I` plus local suitable convergence does not by itself certify those hypotheses. Hence `APPLY_BACKWARD_UNIQUENESS` is blocked until a theorem-specific hypothesis ledger is discharged.

### Exact self-similar rigidity

For a backward self-similar ansatz, changing to similarity variables introduces drift/dilation terms and yields the stationary Leray profile equation. Nečas–Růžička–Šverák and Tsai-type theorems address that transformed profile class under their source hypotheses.

A general Type-I ancient limit instead remains a time-dependent solution of the original Navier–Stokes equation. Applying a stationary Leray-profile theorem to that class would be an equation/interface mismatch.

## Type-I versus Type-II

This audit is entirely conditional on the Albritton–Barker Type-I class `I<infinity`. It neither classifies nor excludes Type-II blow-up. If a singular sequence has no uniform Type-I bound, the compact ancient class used here may be unavailable and the normalization/rigidity program must be rebuilt under a different concentration mechanism.

## Minimal critical-element verdict

A minimal-counterexample/critical-element construction is **deferred, not refuted**.

Before invoking it in `NS-B1a3`, the lane must supply all of the following:

1. an explicitly named global critical topology `X` for the relevant ancient or pre-blow-up states;
2. a proof that the Type-I blow-up sequence is uniformly bounded in `X`, or an alternate source-valid compactness input;
3. a profile decomposition/stability theorem in `X` compatible with Navier–Stokes evolution;
4. normalization of translation/dilation parameters and a proof that escaped profiles do not carry the rigidity-critical information;
5. pressure/far-field compatibility sufficient for the target rigidity theorem;
6. a rigidity theorem whose hypotheses match the resulting global ancient class exactly.

Without item 2, “take a minimal critical element” assumes the missing bridge rather than proving it.

## Geometry route disposition

The failure is specific to the **global critical compactness glue**. It does not touch equation-specific vorticity/geometric depletion. Because B1a1 already pruned scale-neutral shell accounting and B1a2 pruned finite-energy critical-core counting, the next orthogonal high-information child should test a precise vorticity-direction/coherence condition that is inherited by the finite-`I` ancient class and has a matching rigidity/regularity theorem. That child must start from a fresh fibre and exact source hypotheses; no coherence property is assumed here.

## Scoped failure normalization

- `F-NS-B1a3-PROFILE-LEAKAGE` — local strong convergence leaves noncompact translation/dilation profiles uncontrolled globally.
- `F-NS-B1a3-UNCONTROLLED-FAR-FIELD` — local pressure/velocity compactness does not certify the global tail needed by a global critical rigidity theorem.
- `F-NS-B1a3-LOCAL-GLOBAL-INTERFACE-MISMATCH` — the output type of the compactness stage is weaker than the input type of the selected rigidity stage.
- `F-NS-B1a3-UNIQUE-CONTINUATION-HYPOTHESIS-GAP` — backward uniqueness is blocked until its theorem-specific terminal/exterior/regularity hypotheses are proved for the exact ancient limit.
- `F-NS-B1a3-EQUATION-CHANGE-MISMATCH` — stationary Leray-profile rigidity cannot be transferred to arbitrary time-dependent ancient solutions.

These failures are scoped experience. None is a theorem that no alternative dynamics-specific bridge exists.

## Outcome and residual

**Outcome:** `PARTIAL_SUCCESS / SOURCE_BOUND_INTERFACE_ROUTE_PRUNING`.

**Residual before:** a broad suggestion to try critical-element compactness, geometry, pressure-time coherence or another Liouville trigger after energy-based routes failed.

**Residual after:** the critical-element route has one explicit prerequisite atom: construct or derive a **global critical tightness/state-space certificate** from the Type-I dynamics without reusing the pruned energy/shell arguments. In parallel, vorticity/geometric depletion is reopened as the most orthogonal live family.

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`.

No Type-I exclusion, Type-II classification, global regularity proof, novelty certificate, formal proof certificate, or independent mathematical review is created by this audit.

## Primary-source provenance

- Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502: Theorems 1.1–1.2, Lemma 2.2, Proposition 2.3, and the local pressure decomposition used in persistence of singularities.
- Isabelle Gallagher, Gabriel S. Koch, Fabrice Planchon, *A profile decomposition approach to the L^infinity_t(L^3_x) Navier-Stokes regularity criterion*, arXiv:1012.0145, Math. Ann. 355 (2013), 1527–1559.
- L. Escauriaza, G. A. Seregin, V. Šverák, *L_{3,infinity}-solutions of the Navier–Stokes equations and backward uniqueness*, Russian Math. Surveys 58 (2003), 211–250.
- J. Nečas, M. Růžička, V. Šverák, *On Leray's self-similar solutions of the Navier-Stokes equations*, Acta Math. 176 (1996), 283–294.
- Tai-Peng Tsai, *On Leray's self-similar solutions of the Navier-Stokes equations satisfying local energy estimates*, Arch. Ration. Mech. Anal. 143 (1998), 29–51.
