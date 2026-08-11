from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research/real_math/millennium/yang_mills"


def test_g3_reclassification_is_scoped_to_strong_coupling_covariance() -> None:
    matrix = (
        BASE / "01_frontier/YM-S1_GAP_TRANSPORT_OBLIGATION_MATRIX_20260811.md"
    ).read_text(encoding="utf-8")
    audit = (
        BASE / "03_sources/YM-S1B_THERMODYNAMIC_UNIFORMITY_AUDIT_20260811.md"
    ).read_text(encoding="utf-8")

    assert "SUPPORTED_INFINITE_VOLUME_STRONG_COUPLING_COVARIANCE" in matrix
    assert "SUPPORT_FAMILY_UNIFORMITY_OPEN" in matrix
    assert "source/support-dependent constants" in matrix
    assert "does **not** promote the global `G3` obligation" in audit
    assert "YM-S1b1 — source-family/support uniformity" in audit


def test_volume_audit_preserves_spectral_and_continuum_obligations() -> None:
    audit = (
        BASE / "03_sources/YM-S1B_THERMODYNAMIC_UNIFORMITY_AUDIT_20260811.md"
    ).read_text(encoding="utf-8")
    review = (
        BASE / "08_reviews/YM-S1B_THERMODYNAMIC_UNIFORMITY_REVIEW_20260811.md"
    ).read_text(encoding="utf-8")

    for obligation in (
        "Source/OS binding (`G4`)",
        "RG transport (`G5`)",
        "Physical-unit scaling (`G6`)",
        "Continuum spectral identification (`G7`)",
    ):
        assert obligation in audit

    assert "NO_MATHEMATICAL_CANDIDATE" in audit
    assert "ROOT_AUTHORITY_NONE" in audit
    assert "NO_INDEPENDENT_REVIEW" in review
    assert "do not count as independent mathematical reviewers" in review


def test_audit_records_the_load_bearing_primary_sources() -> None:
    audit = (
        BASE / "03_sources/YM-S1B_THERMODYNAMIC_UNIFORMITY_AUDIT_20260811.md"
    ).read_text(encoding="utf-8")

    assert "arXiv:2204.12737" in audit
    assert "10.1007/s00220-022-04609-1" in audit
    assert "10.1016/0003-4916(78)90039-8" in audit
    assert "independent of `L`" in audit
