# NS-B2a1c1 R3 — generalized-F cutoff compatibility

**Candidate:** `C-NS-B2a1c1-POWERLAW-CUTOFF-WINDOW-R3`  
**Frozen:** `2026-08-12T04:52:45Z`, after the R3 MathContextFiber, dual-memory review, SEARCH review, and eight-event current-v3 pre-candidate trace.  
**Authority:** `PROPOSAL_SHADOW / SCOPED ALGEBRA ONLY`. Root `NS0` remains `OPEN_NO_SOLUTION_CERTIFICATE`; isolated mathematical reviews remain `0/3`.

Earlier C001/R2 writes in this branch are retained only as negative process history because they did not bind all current-v3 gate objects in executable form before their candidate identities. They do not receive strict-discovery credit.

Primary sources: Seregin `arXiv:2606.29468v1` and current Seregin `arXiv:2402.13229v3` (revised 2026-08-08).

The 2026 power-log example has `F(a)=a^(alpha-1)` and the nontrivial-possible branch `2alpha-3<=0`, so `alpha<=3/2`. Section 4 uses `3/s1+2/l1=4`, `l1<=s1`, and requires

`a^(2-3l1/2) / F(a)^((l1+1)/2) -> 0`.                 (4.4)

From `l1<=s1`, `1/s1<=1/l1`; therefore `4-2/l1=3/s1<=3/l1`, hence

`1<l1<=5/4`.

Substitution gives the exact cutoff exponent

`E(alpha,l1)=2-3l1/2-(alpha-1)(l1+1)/2`.

Thus (4.4) holds exactly when

`E<0  <=>  alpha > (5-2l1)/(l1+1)`.                    (A)

Equality fails because `E=0`. For every `l1>1`,

`3/2-(5-2l1)/(l1+1)=7(l1-1)/(2(l1+1))>0`,

so the source-compatible interval

`((5-2l1)/(l1+1), 3/2]`                                 (B)

is nonempty for every `1<l1<=5/4`.

Counterexample-first endpoint checks: `alpha=1`/F=1 fails, matching the predecessor; at `l1=5/4` the strict threshold is `10/9`; as `l1->1+` it tends to `3/2` from below; and `alpha=3/2` satisfies the strict cutoff condition for every `l1>1`.

Under the exact representation map `alpha=2-m`,

`E(2-m,l1)=[m(l1+1)+3-4l1]/2`,

so `E<0` is exactly

`m < (4l1-3)/(l1+1)`,

which is current `arXiv:2402.13229v3` equation (2.11). Also `alpha<=3/2` maps to `m>=1/2`, the lower side of its (1.10). This is the only transferred claim.

## Exact residual / gluing audit

The parameter-compatibility edge closes, but a different interface remains. Seregin 2026 Proposition 4.1 additionally assumes a finite time-slice vorticity functional `g(t0)<infinity`. Conservation does not make `g` zero. Current 2402.13229v3 Proposition 2.3 obtains the terminal-zero step only with an additional ancestor `ess sup_t L^q` hypothesis, `q=3/(2-m)=3/alpha`, which is not an output of the frozen 2026 generalized producer.

Therefore the remaining obstruction is `O-NS-B2a1c1-FINITE-G-TERMINAL-RIGIDITY-GLUE`, and the next atom is `NS-B2a1c1a — GENERALIZED_F_TERMINAL_TRACE_RIGIDITY`.

No Type-II exclusion is claimed. No Navier-Stokes backward-uniqueness theorem is imported after the equation changes to Euler. No numerical computation is treated as proof. Novelty class for this solved subproblem is defensibly `compositional` with secondary `representation`.