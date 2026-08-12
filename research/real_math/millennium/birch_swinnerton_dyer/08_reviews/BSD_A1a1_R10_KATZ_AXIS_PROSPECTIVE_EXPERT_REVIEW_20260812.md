# BSD A1a1 R10 prospective same-context expert cell

**Authority:** proposal/shadow same-context review only; independent mathematical-review credit **0/3**.  
**Framework:** RAKL `3.0.0` at `43897d3afaf0038385102d5acc64793c05ec40f0`.  
**Application freeze:** `597b7d98b514af33808d5f32be2cd5c906cfe036` / tree `c4b4fd034a0a9856bb78338e784ad42f67aa7a64`.  
**Fibre:** `sha256:5913e3f7f24fe72170ced53f6cd110e0f7c6c2be84299d1d0df37ec0602950e2`.  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`.

The cell was constituted before accepting the R10 route conclusion. Each role received the same frozen fibre and was asked to challenge a distinct possible hidden inference.

1. **Complex analytic L-function specialist** — verifies that the root datum is the exact complex order at the fixed curve's Hasse–Weil L-function and refuses to replace `=2` by merely positive even order. Finding: Castella's CM setup is compatible with positive even order, but no displayed theorem in the audited pages identifies the complex derivative coordinate with a Katz p-adic derivative coordinate.

2. **CM/Katz p-adic L-function specialist** — audits character types and interpolation. Finding: the displayed Katz interpolation theorem covers infinity types `(k+j,-j)`, `k>=1`, `j>=0`; the elliptic Hecke character `psi_E`, obtained from a `(-1,0)` character times finite-order characters, is not itself in that displayed critical region. Therefore critical-value interpolation is not, by itself, an order/derivative transport theorem.

3. **Iwasawa/main-conjecture specialist** — audits Theorem C's proof dependencies. Finding: in the stated CM cell, `ord L_p=2` first yields `r<=2` through Rubin/Perrin-Riou and `r>=2` through Coates–Wiles plus p-parity, hence `r=2`. The displayed dimension step does not use finite p-primary Sha or `ord L_p^*=1`.

4. **Selmer/localization specialist** — isolates the transverse direction. Finding: after dimension two is obtained, the proof invokes Rubin's derived elliptic unit and the additional `ord L_p^*=1` plus finite p-primary Sha hypotheses to force nonzero localization. This is a different target conjunct from dimension.

5. **Heights/regulator specialist** — checks whether Remark 1.3.1 closes the reverse direction. Finding: the equality statements are tied to p-adic-height nondegeneracy and additional finiteness/nonvanishing conditions. Those cannot be imported from exact complex rank two without a new theorem.

6. **BSD local/global accountant** — tracks what remains after the local CM cell. Finding: even a successful p-primary Selmer/localization bridge would leave Mordell–Weil identification, all-prime Sha/finiteness, Néron–Tate regulator, Tamagawa factors, torsion, real period, and the exact complex leading coefficient as separate gluing obligations.

7. **Adversarial verifier / DifferenceWitness role** — tests the tempting statement “same interpolating family means same vanishing order.” The formal germ `F_m(X,Y)=X^2+Y^m` gives order 2 on one coordinate axis and arbitrary order `m` on the other. This is deliberately **not** an arithmetic model; it only proves the structural inference requires an explicit order-preserving transition witness.

## Cell synthesis

Local source verification passes in its special CM scope. The R9 bundled cell can be sharpened into a **dimension gate** and a **transverse-localization gate**. The naive route “Katz interpolation ⇒ complex/p-adic vanishing orders agree” is rejected as a representation/coordinate-faithfulness shortcut. No expert role found a source-backed exact complex-rank-two-to-Katz-order theorem in the bounded search, but literature completeness is not claimed. Root authority remains none.

The prior R7/R8/R9 failure family changed routing: it blocked another carrier rotation and forced a theorem-proof decomposition plus coordinate-axis audit. R9's shadow episode was retrieved but rejected as technical authority and independently reverified in the primary PDF. XM018 was retrieved but rejected as a strict transfer because it addresses intersection-only nonexpansion rather than differential coordinate faithfulness.

Framework hypothesis, proposal only: extend `StructuralMappingWitness` / mathematical-context-translation telemetry with an optional `differential_invariants_to_preserve` field (e.g. vanishing order, derivative order, regulator rank) so that interpolation/value-preservation cannot be mistaken for derivative/order preservation. Current v3 was sufficient to catch the issue; this is a benchmarkable enhancement, not a gate defect.
