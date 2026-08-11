from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AUDIT = (
    ROOT
    / "research/real_math/millennium/navier_stokes/03_source_audits/"
    / "NS-B1a1_SRC001_SHAHMUROV_2606_07875_20260811.md"
)
REVIEW = (
    ROOT
    / "research/real_math/millennium/navier_stokes/08_reviews/"
    / "NS-B1a1_SRC001_SOURCE_AUDIT_EXPERT_CELL_20260811.md"
)


def test_source_audit_preserves_nonpromotion_boundary() -> None:
    audit = AUDIT.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")

    assert "SOURCE_ARGUMENT_BLOCKED_AS_WRITTEN" in audit
    assert "NO_METHOD_TRANSFER" in audit
    assert "NO_THEOREM_REFUTATION" in audit
    assert "OPEN_NO_SOLUTION_CERTIFICATE" in audit
    assert "minimal dyadic scale" in audit
    assert "2^{-n}" in audit
    assert "finite-scale truncation" in audit
    assert "BLOCK_PROOF_PROMOTION" in review
    assert "NO_METHOD_TRANSFER_PENDING_REPAIR_WITNESS" in review
    assert "NO_THEOREM_AUTHORITY" in review
    assert "ROOT_AUTHORITY_NONE" in review


def test_source_audit_binds_current_repository_boundary() -> None:
    audit = AUDIT.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")

    framework_sha = "15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3"
    application_sha = "d8ac4102285c4ed1ba0fbd5d8818dc4c4731a8cc"

    assert framework_sha in audit
    assert framework_sha in review
    assert application_sha in audit
    assert "issue #25" in audit
    assert "issue #4" in review
