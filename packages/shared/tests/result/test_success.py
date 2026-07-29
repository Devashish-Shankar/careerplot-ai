"""
==========================================================
CareerPilot AI

Shared Package Tests

Success Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from careerpilot_shared.result import Success


def test_success_value() -> None:
    result = Success("CareerPilot")

    assert result.value == "CareerPilot"


def test_success_has_no_error() -> None:
    result = Success(42)

    assert result.error is None


def test_success_boolean_properties() -> None:
    result = Success(True)

    assert result.is_success
    assert not result.is_failure
