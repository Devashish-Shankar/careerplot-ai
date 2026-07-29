"""
==========================================================
CareerPilot AI

Shared Package Tests

Failure Tests

Author: Devashish Shankar
==========================================================
"""

from __future__ import annotations

from careerpilot_shared.result import Failure


def test_failure_contains_exception() -> None:
    error = RuntimeError("Failure")

    result = Failure(error)

    assert result.error is error


def test_failure_has_no_value() -> None:
    error = RuntimeError()

    result = Failure(error)

    assert result.value is None


def test_failure_boolean_properties() -> None:
    result = Failure(ValueError())

    assert result.is_failure
    assert not result.is_success
