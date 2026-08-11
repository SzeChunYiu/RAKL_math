# NS-B1a3b1b-C001 — current-v3 and source revalidation

**Authority:** PROPOSAL/SHADOW POST-RESULT VERIFICATION ONLY. No root, proof, lesson, tool, or independent-review authority.

## Current framework subject
Before completing this cycle, current `SzeChunYiu/RAKL` `main` was re-read at `b724b75c71f37956b6188584ce32e3c554ea2d6d`. `RAKL_VERSION.json` still declares method version `3.0.0`, software package `0.1.0`, constitution epoch `v3-authority-hardening-20260811`. The current `src/rakl/method_specs.py`, `src/rakl/experience_substrate.py`, `src/rakl/episode_admission.py`, `schemas/task-episode.schema.json`, and `schemas/episode-admission-receipt-v1.schema.json` were inspected directly.

The framework moved after the prospective pre-action freeze (`812e9cf18345ef430f0a4cc3ff78f93d7f18ed22`). The current TaskEpisode contract now requires content-bound `storage_admission`, and current v3 provides an explicit episode-admission receipt separating immediate proposal/shadow retention from canonical inventory admission. Operational adaptation was therefore limited to authority-safe bookkeeping: the episode was rebound to the current exact hash contract with `storage_admission=PROPOSAL_SHADOW_STORED`, and `EAR-NS-B1a3b1b-C001-R1-20260811` was added with `storage_status=PROPOSAL_SHADOW_STORED`. No canonical inventory, promotion, lesson/tool, proof, or root gate is satisfied by that receipt.

## Primary-source mathematical recheck
The local mathematical result was rechecked against primary sources, not inferred from the pending application branch.

- Evan Miller, `arXiv:1710.05569`, records the whole-space 3D NSE vorticity/enstrophy evolution and the standard cubic differential estimate `d/dt ||omega||_2^2 <= C ||omega||_2^6` (equivalently `y'<=C y^3` for `y=||omega||_2^2`) together with the standard energy/dissipation setting. This independently matches the derivation in the candidate audit.
- Ben Pineau and Vlad Vicol, `arXiv:2607.09619v2` (revised 2026-08-06), Theorem 1.9 and Proposition 9.5, provide a genuinely local Type-I one-slice regularity consumer. Proposition 9.5 requires a sufficiently small rescaled local enstrophy on one late slice under a local pointwise Type-I velocity bound and annular pressure control. It is a consumer, not a producer from finite dissipation alone.

For the registered hostile scalar profile `y_a(t)=a(T-t)^(-1/2)`, `y_a'=(a/2)(T-t)^(-3/2)` and `y_a^3=a^3(T-t)^(-3/2)`, so `y_a'<=C y_a^3` whenever `a^2>=1/(2C)`. Meanwhile `integral_{T-epsilon}^T y_a=2a sqrt(epsilon)<infinity`, `sup y_a=infinity`, and `(T-t)^(1/2)y_a=a`. Thus the standard scalar consequences of finite dissipation plus the cubic enstrophy inequality do not force a bounded trace or a small late scale-critical slice. This remains a proof-architecture falsifier only; the scalar profile is not asserted to solve NSE.

## Same-context expert cell revalidation
1. **PDE/vorticity analyst** — checked the vorticity identity, scaling, interpolation exponents, Young absorption, and the cubic endpoint. Verdict: local scalar derivation is sound in the stated smooth whole-space favorable model.
2. **Blow-up/compactness specialist** — checked the Type-I scaling exponent and warned that global finite energy dissipation is not identical to Albritton–Barker's local scale-normalized Type-I functional `E`. Verdict: the negative result is valid only for the standard scalar bootstrap architecture and cannot be promoted to Type-I exclusion.
3. **Harmonic-analysis/geometric-depletion specialist** — checked that an `L^2_x` enstrophy trace is not the Grujic global critical `L^{3/2,infinity}` vorticity amplitude nor log-BMO direction input. Verdict: global Lorentz/far-field and phase normalization remain separate.
4. **Adversarial falsification specialist** — checked amplitude threshold and integrability/unboundedness simultaneously. Verdict: discriminator passes and is constant-robust for every finite positive cubic constant.
5. **Provenance/authority auditor** — checked current-v3 schema drift, shadow storage separation, pending PR #131 authority, local-vs-gluing separation, and root gates. Verdict: retain only proposal/shadow route-pruning evidence; independent review remains `0/3`.

## Failure separation and residual
Primary failure is **LOCAL_MATHEMATICAL / PROOF-ARCHITECTURE ENDPOINT**: absolute vortex-stretching compression to `y'<=Cy^3` loses exactly the information needed to force a uniform/small critical time trace. This is not a new localization/gluing failure. Pressure/cutoff localization, global Lorentz/far-field production, vorticity-direction normalization, pre-singularity-to-ancient state-space matching, downstream backward-uniqueness/unique-continuation hypotheses, and Type II remain separate open residuals.

The next admissible route should change the stretching closure before scalar cubic compression — for example via sign/coherence depletion, finite-variation/monotonicity in self-similar variables, or a frequency-local mechanism — or rotate to another exact source-valid consumer. Root state remains `OPEN_NO_SOLUTION_CERTIFICATE`.
