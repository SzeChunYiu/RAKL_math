# NS-B2a1c1 R2 — generalized-F axial cutoff window

**Candidate:** `C-NS-B2a1c1-POWERLAW-CUTOFF-WINDOW-R2`  
**Frozen after corrected Gate-D trace:** `2026-08-12T04:43:17Z`  
**Authority:** `PROPOSAL_SHADOW / SOURCE_BOUND_SCOPED_ALGEBRA / NO_ROOT_AUTHORITY`  
**Root:** `NS0 = OPEN_NO_SOLUTION_CERTIFICATE`, independent mathematical reviews `0/3`.

The earlier same-cycle `C001` write is retained as a **process-invalid precursor** because its first trace artifact did not satisfy current `ResearchTraceEntry` minimum fields. It may be used only as negative process history/truth-check provenance. This R2 candidate is the first candidate identity bound after the corrected RAKL-v3 Gate-D trace.

## Exact source state

Seregin 2026 (`arXiv:2606.29468v1`) gives the generalized example

`f(lambda)=lambda^(alpha-1)/log^gamma(e/lambda)`, `1<alpha<2`,

with `F(a)=a^(alpha-1)`, and the nontrivial-possible branch `2 alpha-3<=0`, so `alpha<=3/2`. Section 4 assumes

`3/s1 + 2/l1 = 4`, `l1<=s1`,

and condition (4.4)

`a^(2-3l1/2) / F(a)^((l1+1)/2) -> 0`.

The current comparison source is Seregin `arXiv:2402.13229v3` (revised 2026-08-08), especially (1.4), (1.10), (2.11), Proposition 2.2 and Proposition 2.3.

## Result 1 — admissible l1 range

From `l1<=s1`, `1/s1<=1/l1`. Hence

`4-2/l1 = 3/s1 <= 3/l1`,

so `1<l1<=5/4`.

## Result 2 — exact cutoff window

With `F(a)=a^(alpha-1)`, the exponent in (4.4) is

`E(alpha,l1)=2-3l1/2-(alpha-1)(l1+1)/2`.

Condition (4.4) holds exactly when `E<0`, equivalently

`alpha > (5-2l1)/(l1+1)`.                                      (A)

The inequality is strict. Equality makes the cutoff factor order one rather than decaying.

For every `l1>1`,

`3/2-(5-2l1)/(l1+1)=7(l1-1)/(2(l1+1))>0`.

Therefore the 2026 nontrivial-possible branch contains the nonempty compatible interval

`((5-2l1)/(l1+1), 3/2]`, for every `1<l1<=5/4`.                  (B)

Adversarial endpoint checks:

- `alpha=1` (the limiting `F=1` case) fails, consistent with `NS-B2a1c`.
- equality in (A) fails because `E=0`.
- at `l1=5/4`, the threshold is `alpha>10/9`.
- as `l1->1+`, the threshold tends to `3/2` from below.
- `alpha=3/2` satisfies (4.4) for every `l1>1`.

## Result 3 — exact representation relation to current v3 source

Set `alpha=2-m`. Then

`E(2-m,l1)=[m(l1+1)+3-4l1]/2`.

Thus `E<0` is exactly

`m < (4l1-3)/(l1+1)`,

which is equation (2.11) of the current `arXiv:2402.13229v3`. Also `alpha<=3/2` is `m>=1/2`, matching the lower side of (1.10).

This verifies an exact **representation/compositional bridge** for the cutoff exponent only. It does not transfer the older terminal-time theorem.

## Rigidity-interface audit

The local algebraic obstruction from the parent F=1 branch is therefore parameter-specific rather than a global blacklist of the cutoff-conservation operator. But the Type-II route remains open for two separate reasons.

First, Seregin 2026 Proposition 4.1 assumes there exists `t0<=0` with

`g(t0)=(2/l1) int_R3 (|omega_theta(u)(x,t0)|/r)^(l1/2) dx < infinity`.

The currently bound 2026 Theorem-3.1/Section-4 producer does not state this as an automatic output.

Second, even conservation of `g` does not imply `g=0`. Current `arXiv:2402.13229v3` Proposition 2.3 reaches a terminal zero state only after an additional ancestor condition

`ess sup_{-1<t<0} int_C |v(x,t)|^q dx < infinity`, with `q=3/(2-m)=3/alpha`.

That extra time-slice hypothesis is not part of the generalized 2026 producer frozen for this atom. Importing Proposition 2.3 wholesale would therefore violate the DifferenceWitness and the same-theory gluing contract.

## Scoped outcome

`NS-B2a1c1` closes only this edge:

`GENERALIZED_F_PRODUCER -> SECTION4_4_4_PARAMETER_COMPATIBILITY`.

The next atom is `NS-B2a1c1a — GENERALIZED_F_TERMINAL_TRACE_RIGIDITY`: derive, from the exact 2026 power-log source assumptions, both a source-valid finite-`g` time and a terminal-time/other rigidity trigger, or prove that the interface is unavailable in that source class.

Failure separation:

- **local mathematics:** verified compatible window; F=1/equality are falsified subcases.
- **retrieval/representation:** old Proposition 2.3 is rejected as a wholesale transfer because its ancestor `L^q` premise is unmatched.
- **local-to-global/gluing:** finite `g(t0)` plus terminal/rigidity output remain unproved from the generalized producer.
- **root:** no Type-II exclusion, no Type-I closure, no closed Clay proof DAG, no promotion.

Primary provenance: `https://arxiv.org/abs/2606.29468` (v1) and `https://arxiv.org/abs/2402.13229` (current v3).