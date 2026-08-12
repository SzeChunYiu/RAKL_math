# NS-B1a5 — ambient packet-train falsifier for ledger-only slice-tail inference

**Authority:** proposal/shadow scoped mathematics. This is an ambient-representation lemma, **not** a Navier–Stokes counterexample and not a root result.

## Frozen question

Does finiteness of the four numerical functionals A,C,D,E on every parabolic cylinder, by itself and without using the Navier–Stokes equation, force a finite global L3(R3) norm on each time slice?

## Construction

Fix a nonzero divergence-free phi in C_c^infty(B(0,a);R3). Choose L>4a, so translates phi_k(x)=phi(x-kLe1), k in Z, have pairwise disjoint supports. Define W(x)=sum_k phi_k(x). Choose eta in C_c^infty((-2,-1)), 0<=eta<=1, with eta(t*)=1 at t*=-3/2, and set u(x,t)=eta(t)W(x), p(x,t)=0 on R3 x R_-.

For F in {|W|^2, |W|^3, |grad W|^2}, boundedness gives integral_B F <= K r^3 for r<=1. For r>=1, a ball meets only O(1+r/L) packet supports, so integral_B F <= K'(1+r).

The temporal overlap of any cylinder with supp eta is <=min(r^2,1). Hence

- A(Q) <= K r^2 for r<=1 and K'(1+r)/r for r>=1;
- C(Q) <= K r^3 for r<=1 and K'(1+r)/r^2 for r>=1;
- E(Q) <= K r^4 for r<=1 and K'(1+r)/r for r>=1;
- D(Q)=0.

Therefore sup_Q(A+C+D+E)<infinity.

At t*, disjointness gives integral_R3 |u(x,t*)|^3 = sum_{k in Z} integral |phi|^3 = infinity, so u(.,t*) is not in global L3.

## Target-domain audit

The field is **not** an unforced Navier–Stokes solution for any compatible pressure: it vanishes for every t<=-2 but is nonzero at t*. A smooth unforced NSE solution with zero data at t=-2 is uniquely zero forward in time. Thus p=0 only fills the numerical D-slot; it does not supply the NSE pressure equation or suitability/local-energy inequality.

Apply current RAKL v3 DifferenceWitness typing:
- `realization_domain = AMBIENT_REPRESENTATION`;
- `assess_obligation_strength_claim -> REPRESENTATION_ONLY`;
- `may_certify_target_obligation_weakening = false`.

So the construction proves only: **the bare A+C+D+E values do not algebraically encode same-time global L3 tail control.** It does not prove that a mild bounded ancient Navier–Stokes solution with finite I can fail global L3 on a slice. That same-theory implication remains open.

## Routing consequence

Further ledger-only manipulation for this consumer is representation-saturated. A consequential next step must introduce a target-domain coordinate: mild NSE evolution, same-theory tail propagation/no-incoming, recurrence/compactness in an equation-sensitive norm, or another licensed same-time global-L3 producer.

## Provenance

Albritton–Barker arXiv:1811.00502 current snapshot 22 March 2026 supplies the exact ledger and Theorems 1.1–1.2. Pineau–Vicol arXiv:2607.09619v2 (6 August 2026), Theorem 1.9 and Remarks 1.10–1.11, is retained only as a same-theory analogue for equation-sensitive self-similar-speed information. No literature novelty claim is made for this packet-train construction.
