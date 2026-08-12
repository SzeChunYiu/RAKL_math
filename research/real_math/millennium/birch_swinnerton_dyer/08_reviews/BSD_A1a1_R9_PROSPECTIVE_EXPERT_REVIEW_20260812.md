# BSD A1a1 R9 prospective same-context expert review

**Cycle:** `BSD-A1a1-ZHANG-LOWER-BOUND-20260812-R9`  
**Atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**Nested obstruction:** `BSD-A1a2-LOCALIZATION-POSITIVE-RANK-BRIDGE`  
**Frozen fibre:** `sha256:1169325f3cc17acc2094488809bc13ebba796a54aa51bcbc132690c98e1987c9`  
**Review authority:** same-context adversarial review only; **independent mathematical review credit = 0**.

## Role-separated cell

1. **Complex analytic / automorphic specialist** — protects the exact source coordinate `ord_{s=1}L(E,s)=2`, the functional-equation sign, and same-curve scope. Verdict: exact order two has even parity, hence root number `+1`; Wei Zhang Theorem 1.4(ii) may therefore be specialized to the `+1` branch, but not beyond its stated prime hypotheses.
2. **Gross–Zagier / Heegner specialist** — checks the auxiliary quadratic-field construction and whether the return to `E/Q` is explicit. Verdict: Zhang's proof chooses an auxiliary `K`, uses the twist derivative and Gross–Zagier to make the base Heegner point torsion, and the stated theorem returns the consequence to `Sel_{p^∞}(E/Q)`; no unwitnessed base-change promotion is needed for the lower bound.
3. **Euler/Kolyvagin-system specialist** — distinguishes nonvanishing from vanishing order. Verdict: Theorem 1.1 gives a nonzero Kolyvagin system; Theorem 1.2 identifies its vanishing order with a Selmer-eigenspace maximum minus one. The rank-two proof gives only `nu_infinity >= 1`; it does **not** prove `nu_infinity = 1`.
4. **Selmer / localization specialist** — checks the target arithmetic coordinate. Verdict: Theorem 1.4(ii) proves only `corank_Zp Sel_{p^∞}(E/Q) >= 2` in the rank-two `+1` cell. It does not prove exact corank two and does not produce the R7 transverse nonzero localization at `p`. The `p^∞`-Selmer coordinate must not be silently identified with the `V_pE` Selmer dimension when exactness is claimed.
5. **BSD leading-term / local-factor adversary** — tracks Sha, regulator, Tamagawa, torsion, and exceptional/trivial-zero issues. Verdict: none of Mordell–Weil rank two, finiteness of `Sha[p^∞]`, regulator nondegeneracy, all-prime Sha, Tamagawa/torsion bookkeeping, or the complex leading Taylor coefficient is closed. The rank-one refined formula later in Zhang's paper is not transferable to rank two.
6. **Source/provenance and counterexample-first auditor** — checks theorem direction and current frontier. Verdict: the 2014 author-hosted primary paper was absent from the bounded R8 four-source family, so R8 was not false but was incomplete by its own bounded-only scope. Current Kim–Pollack work gives exact Selmer structure in a discrete Kurihara-number coordinate under its Iwasawa input; it does not furnish the missing complex-order-two identity. Any candidate assuming exact Selmer rank, nonzero localization, p-adic BSD/main-conjecture strength, or a root-strength regulator is rejected.
7. **RAKL v3 / metrology auditor** — checks episode/diagnosis/failure separation, process surfaces, saturation, and authority. Verdict: record the Zhang theorem as a **stored/compositional partial transfer**, not new mathematics; record the R8-to-R9 source-coverage miss as a source/retrieval process failure, not a mathematical obstruction; keep `BSD-A1a2` active but split its residual. No lesson/tool/motif or protected obstruction is promoted.

## Consensus

**PASS for a scoped partial theorem-path; FAIL for root or A1a2 closure.** The accepted chain is

`ord_{s=1}L(E,s)=2`  
`=> root number +1`  
`=> (Wei Zhang Theorem 1.4 hypotheses at p) corank_Zp Sel_{p^∞}(E/Q) >= 2`.

The sharp residual is no longer a completely missing complex-to-arithmetic entry. It is now the conjunction of an **upper/exactness problem** (`>=2` to exactly `2` in a root-faithful arithmetic coordinate), a **transverse p-local localization problem**, explicit `p^∞`/`V_p` coordinate binding where required, and the separate full BSD leading-term gluing problem.

## Falsifiers retained

Reject any proposed continuation that (a) reads Zhang's lower bound as equality, (b) treats nonzero Kolyvagin system as vanishing order exactly one, (c) uses the rank-one refined BSD theorem as a rank-two theorem, (d) assumes the desired localization/nonvanishing witness, (e) substitutes a discrete/p-adic order for complex Taylor order without a comparison theorem, or (f) suppresses local/Tamagawa/torsion/Sha/regulator hypotheses.

**Root state:** `OPEN_NO_SOLUTION_CERTIFICATE`.
