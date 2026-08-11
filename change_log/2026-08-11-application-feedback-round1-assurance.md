# 2026-08-11: harden application-feedback round-one reconstruction

- Verify producer commit `590b962` remains reachable from the current merged
  history before reconstructing its bundle.
- Validate result/trace/context identities and require every strict-UTC
  observation timestamp to precede the producer commit.
- Authenticate a clean framework source before importing framework code, then
  import only from a detached checkout at historical framework commit
  `15f1c3a`.
- Decouple the historical receipt from future changes to the current
  application framework gitlink/config pin.
- Preserve the existing bundle, receipt, producer identity and proposal-only
  authority boundary unchanged.

No application lesson was promoted and no mathematical claim changed.
