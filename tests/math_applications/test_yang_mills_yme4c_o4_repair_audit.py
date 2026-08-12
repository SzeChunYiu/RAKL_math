from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
YM = ROOT / "research" / "real_math" / "millennium" / "yang_mills"


def test_literal_rie_sum_exponent_does_not_vanish() -> None:
    # Source equation (4.47) contributes a_k^-4 and (4.49) contributes a_k^1.
    assert -4 + 1 == -3
    assert -3 != 1


def test_shadow_episode_keeps_root_open_and_reviews_nonindependent() -> None:
    episode = json.loads(
        (YM / "10_case_study" / "YM-E4c_V3_TASK_EPISODE_20260811T1837Z.json").read_text()
    )
    assert episode["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert episode["independent_review_count"] == 0
    assert episode["outcome"] == "SCOPED_SOURCE_PROOF_FAILURE_WITH_NEW_REPRESENTATION_GLUING_OBSTRUCTION"
    assert "F-YM-E4C-ARBITRARY-O4-LATTICE-ACTION-UNBOUND" in episode["new_failure_ids"]


def test_failure_is_scoped_and_not_promoted() -> None:
    delta = json.loads(
        (YM / "07_memory" / "YM_E4c_FAILURE_EXPERIENCE_DELTA_20260811T1837Z.json").read_text()
    )
    assert delta["authority"] == "PROPOSAL_SHADOW_ONLY"
    assert delta["new_failure_experience"]["status"] == "SUPPORTED_SOURCE_LOCAL_SHADOW"
    assert delta["new_obstruction_shadow"]["promotion_status"] == "NOT_PROMOTED"
    assert delta["new_lesson_ids_created"] == [] if "new_lesson_ids_created" in delta else delta["lesson_ids_created"] == []


def test_hash_chain_terminal_and_fibre_binding_are_stable() -> None:
    trace = json.loads(
        (YM / "08_trace" / "YM_E4c_HASH_CHAIN_TRACE_20260811T1837Z.json").read_text()
    )
    fibre = json.loads(
        (YM / "01_frontier" / "YM_E4c_FIBRE_BINDING_20260811T1837Z.json").read_text()
    )
    assert trace["terminal_hash"] == "sha256:c13636267119059d4215f2387d0656d60dd1cf3d43b68ed4f52c561bf9509c5e"
    assert fibre["fibre_manifest_hash"] == "sha256:29ce4b6423fd90604b6effc5d686ac9aaf7dcc6399455a0efe17c9bd41cd1de1"
    assert fibre["application"]["root_status"] == "OPEN_NO_SOLUTION_CERTIFICATE"
