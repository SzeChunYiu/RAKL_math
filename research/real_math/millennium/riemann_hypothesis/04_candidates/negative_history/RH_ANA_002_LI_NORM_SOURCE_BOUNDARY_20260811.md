# RH-ANA-002 negative history — Suzuki norm-faithfulness source boundary

**Failure id:** `F-RH-ANA-002-SUZUKI-NORM-FAITHFULNESS-SOURCE-BOUNDARY`  
**Episode:** `EP-RH-ANA-002-LI-NORM-AUDIT-20260811`  
**Context:** `sha256:300b787769442af040d944e0b52db106881844a9238c021e8804c7f382660742`  
**Diagnosis authority:** `OBSERVED_ONLY`  
**Root authority:** `NONE`

## Observed route result

The preregistered Li-norm faithfulness audit was executed without proposing a theorem. Suzuki's 2023 construction gives `G_n in L^2(R)` unconditionally and therefore a manifestly nonnegative quantity `P_n=(2*pi)^(-1)||G_n||_2^2`. But the paper's route identifying this norm with `lambda_n` uses model-space structure tied to RH: Proposition 3.1 makes the Hermite–Biehler/inner-function condition equivalent to RH and Proposition 3.2 explicitly assumes RH. Theorem 1.1 states the **all-index** equality itself as equivalent to RH.

The registered source audit found no exact unconditional `D_n=P_n-lambda_n` identity, sign theorem, orthogonality relation, or source term that is demonstrably weaker than that all-index equality. This is a source-bound search result, not an impossibility theorem.

## Competing diagnoses preserved

1. The norm representation may be intrinsically root-coupled, so every exact all-index faithfulness closure is root-strength.
2. A useful unconditional `D_n` decomposition may exist but be absent from the inspected source boundary.
3. The missing coordinate may be better exposed by a different representation, especially a localized Weil/prime-side quadratic form or a global-growth route.

No diagnosis is selected. Under current RAKL v3, the episode records what happened; the failure record remains `OBSERVED_ONLY` until new evidence discriminates among these explanations.

## Relation to RH-ANA-001

`F-RH-ANA-001-FINITE-LI-PREFIX` and this failure share the residual “all-index control is missing,” but they are not the same failure family. RH-ANA-001 loses the infinite tail through finite projection. RH-ANA-002 keeps an all-index positive surrogate but loses **faithfulness to the target Li sign**. That DifferenceWitness is why the norm audit was a legitimate new discriminator rather than a relabeled finite-prefix retry.

## Cross-Millennium transfer boundary

The previously selected `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` contributed only an audit pattern: check whether a positive surrogate preserves the root-critical coordinate. Its Yang–Mills evidence does not transfer to RH. The RH-specific DifferenceWitness remains exact-identity faithfulness versus continuum normalization. No cross-problem counterexample or theorem is imported.

## Repair policy

Do not retry the same norm-faithfulness family merely by defining a new defect or positive quantity. A retry requires new unconditional structure and an explicit DifferenceWitness. Otherwise rotate representation under a fresh strict pre-candidate gate. Suzuki's 2026 screw-function/Weil-form work is retained only as a current primary-source pointer for that next context.
