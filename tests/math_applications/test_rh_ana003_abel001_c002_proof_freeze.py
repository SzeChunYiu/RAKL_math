from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
RH = ROOT / "research/real_math/millennium/riemann_hypothesis"
FIXTURE = RH / "09_trace/rh_ana003_abel001_c002_proof_freeze_fixture.py"


def _module():
    spec = importlib.util.spec_from_file_location("rh_abel_c002_proof_freeze", FIXTURE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_freeze_documents_are_deterministic_and_checker_unexecuted() -> None:
    module = _module()
    expected = module.build_documents()
    for name, relative in module.PATHS.items():
        actual = json.loads((ROOT / relative).read_text(encoding="utf-8"))
        assert actual == expected[name]
    assert expected["manifest"]["status"] == "FROZEN_NOT_EXECUTED_UNTIL_PUBLIC_COMMIT"
    assert expected["chronology"]["proof_checker_executed_before_freeze"] is False
    assert expected["chronology"]["result_classified_before_freeze"] is False
    assert expected["receipt"]["mathematical_result_credit"] is False


def test_hand_certificate_covers_exact_o1_o7_and_boundaries() -> None:
    module = _module()
    certificate = module.build_documents()["certificate"]
    obligations = certificate["obligations"]
    assert [row["obligation_id"].split("-")[0] for row in obligations] == [f"O{i}" for i in range(1, 8)]
    assert all(row["status"] == "PROVED_IN_FROZEN_HAND_CERTIFICATE" for row in obligations)
    text = json.dumps(obligations, sort_keys=True)
    for required in ("nonintegral", "(-1)^n/(n-1)!", "Bellotti", "u=log", "improper-integral", "No term is permuted", "6k"):
        assert required in text
    assert certificate["authority"]["machine_formal"] is False
    assert certificate["authority"]["independent_review"] is False
    assert certificate["authority"]["riemann_hypothesis"] is False


def test_authorization_preserves_scoped_exclusions() -> None:
    module = _module()
    docs = module.build_documents()
    authorization = docs["authorization"]
    assert authorization["requires_public_freeze_commit"] is True
    assert authorization["proof_check_authorized"] is True
    assert set(authorization["forbidden"]) == {"n-uniformity", "reordering", "PR316 rate", "Li positivity", "RH", "global ledger update"}
    assert docs["certificate"]["proof_input_raw_sha256"] == module.PROOF_INPUT_RAW
    revalidation = docs["framework_revalidation"]
    assert revalidation["live_framework_origin_main_sha"] == module.FRAMEWORK_LIVE
    assert revalidation["protected_surfaces_byte_identical_between_pin_and_live"] is True
    assert revalidation["verdict"] == "CURRENT_NONBLOCKING_PROPOSAL_ONLY_ADDITIONS"
    assert revalidation["grants_mathematical_or_scientific_authority"] is False
